"""YouTube, Instagram ve TikTok'taki son içerikleri çeker, data/content.json'a yazar.

Kapak görselleri data/media/ altına indirilir; site ziyaretçisinin tarayıcısı bu
platformlara hiç bağlanmaz. Bir platform hata verirse o platformun son başarılı
verisi korunur ve hata raporlanır; site boş kalmaz.

Ortam değişkenleri (GitHub Actions secret'ları):
  IG_TOKEN                 Instagram uzun ömürlü erişim anahtarı
  TIKTOK_CLIENT_KEY        TikTok uygulama anahtarı
  TIKTOK_CLIENT_SECRET     TikTok uygulama sırrı
  TIKTOK_REFRESH_TOKEN     TikTok yenileme anahtarı
  NEW_SECRETS_FILE         Yenilenen anahtarların yazılacağı geçici dosya
  FETCH_REPORT             Çalışma raporunun yazılacağı dosya
"""
from __future__ import annotations

import io
import json
import os
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

from PIL import Image, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402

NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015",
      "media": "http://search.yahoo.com/mrss/"}
SIZE_WIDE = (640, 360)
SIZE_TALL = (360, 640)


# ---------- kapak görselleri ----------

def _safe_id(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]", "", str(value))[:64]


def store_thumb(platform: str, item_id: str, candidates: list[str], size: tuple[int, int],
                allowed_hosts: list[str]) -> str | None:
    """İlk çalışan aday görseli indirir, kırpar, yeniden kodlar. Dosya adını döndürür."""
    name = f"{platform}-{_safe_id(item_id)}.jpg"
    path = C.MEDIA_DIR / name
    if path.exists():
        return name
    for url in candidates:
        if not url or not C.host_allowed(url, allowed_hosts):
            continue
        try:
            raw = C.http_request(url, max_bytes=C.MAX_IMAGE_BYTES)
            with Image.open(io.BytesIO(raw)) as probe:
                probe.verify()
            with Image.open(io.BytesIO(raw)) as img:
                img = ImageOps.exif_transpose(img).convert("RGB")
                img = ImageOps.fit(img, size, method=Image.Resampling.LANCZOS)
                C.MEDIA_DIR.mkdir(parents=True, exist_ok=True)
                img.save(path, "JPEG", quality=82, optimize=True, progressive=True)
            return name
        except C.FetchError:
            continue
        except Exception:  # bozuk ya da desteklenmeyen görsel
            continue
    return None


# ---------- YouTube ----------

def parse_youtube_feed(xml_bytes: bytes) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    items = []
    for e in root.findall("a:entry", NS):
        vid = (e.findtext("yt:videoId", default="", namespaces=NS) or "").strip()
        link_el = e.find("a:link[@rel='alternate']", NS)
        url = link_el.get("href") if link_el is not None else f"https://www.youtube.com/watch?v={vid}"
        desc = e.findtext("media:group/media:description", default="", namespaces=NS)
        if not vid:
            continue
        items.append({
            "platform": "youtube",
            "id": vid,
            "kind": "short" if "/shorts/" in url else "video",
            "title": (e.findtext("a:title", default="", namespaces=NS) or "").strip(),
            "url": url,
            "published": C.parse_time(e.findtext("a:published", namespaces=NS)).isoformat(),
            "ad": C.is_ad(desc),
            "guides": C.guide_slugs_in(desc),
        })
    return items


def fetch_youtube(cfg: dict) -> list[dict]:
    cid = cfg["platforms"]["youtube"]["channel_id"]
    url = "https://www.youtube.com/feeds/videos.xml?channel_id=" + urllib.parse.quote(cid)
    try:
        items = parse_youtube_feed(C.http_request(url))
    except ET.ParseError:
        raise C.FetchError("YouTube akışı okunamadı.") from None
    for it in items:
        vid = urllib.parse.quote(it["id"])
        if it["kind"] == "short":
            it["_thumb_src"] = [f"https://i.ytimg.com/vi/{vid}/oardefault.jpg",
                                f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"]
            it["_thumb_size"] = SIZE_TALL
        else:
            it["_thumb_src"] = [f"https://i.ytimg.com/vi/{vid}/maxresdefault.jpg",
                                f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"]
            it["_thumb_size"] = SIZE_WIDE
    return items


# ---------- Instagram ----------

IG_FIELDS = "id,caption,media_type,media_product_type,media_url,thumbnail_url,permalink,timestamp"


def refresh_instagram_token(token: str) -> tuple[str, int | None]:
    url = ("https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token="
           + urllib.parse.quote(token))
    data = C.http_json(url)
    new = data.get("access_token")
    if not new:
        raise C.FetchError("Instagram anahtarı yenilenemedi.")
    return new, data.get("expires_in")


def normalize_instagram(data: dict) -> list[dict]:
    items = []
    for m in data.get("data", []):
        if not m.get("permalink") or not m.get("id"):
            continue  # telif nedeniyle bağlantısı gizlenen gönderiler atlanır
        caption = m.get("caption") or ""
        is_video = m.get("media_type") == "VIDEO"
        items.append({
            "platform": "instagram",
            "id": str(m["id"]),
            "kind": "reel" if m.get("media_product_type") == "REELS" or is_video else "post",
            "title": C.title_from_caption(caption),
            "url": m["permalink"],
            "published": C.parse_time(m["timestamp"]).isoformat(),
            "ad": C.is_ad(caption),
            "guides": C.guide_slugs_in(caption),
            "_thumb_src": [m.get("thumbnail_url") if is_video else m.get("media_url"),
                           m.get("thumbnail_url"), m.get("media_url")],
        })
    return items


def fetch_instagram(cfg: dict, env: dict, new_secrets: dict, report: dict) -> list[dict]:
    token = env.get("IG_TOKEN")
    if not token:
        raise C.FetchError("IG_TOKEN tanımlı değil.")
    try:
        new, expires_in = refresh_instagram_token(token)
        if new != token:
            new_secrets["IG_TOKEN"] = new
            token = new
        if expires_in:
            report["instagram_token_expires_at"] = (
                datetime.now(timezone.utc) + timedelta(seconds=int(expires_in))).replace(microsecond=0).isoformat()
    except C.FetchError as e:
        report.setdefault("warnings", []).append(f"Instagram anahtarı yenilenemedi: {e}")
    limit = cfg["max_items_per_platform"]
    url = (f"https://graph.instagram.com/me/media?fields={IG_FIELDS}&limit={limit}&access_token="
           + urllib.parse.quote(token))
    data = C.http_json(url)
    if "error" in data:
        raise C.FetchError("Instagram hata döndürdü: " + C.redact(json.dumps(data["error"])[:300]))
    return normalize_instagram(data)


# ---------- TikTok ----------

TT_FIELDS = "id,title,video_description,create_time,cover_image_url,share_url"


def refresh_tiktok_token(key: str, secret: str, refresh: str) -> dict:
    body = urllib.parse.urlencode({"client_key": key, "client_secret": secret,
                                   "grant_type": "refresh_token", "refresh_token": refresh}).encode()
    data = C.http_json("https://open.tiktokapis.com/v2/oauth/token/", data=body, method="POST",
                       headers={"Content-Type": "application/x-www-form-urlencoded"})
    if not data.get("access_token"):
        raise C.FetchError("TikTok anahtarı yenilenemedi: " + C.redact(str(data.get("error_description")
                                                                        or data.get("error") or "")[:200]))
    return data


def normalize_tiktok(data: dict) -> list[dict]:
    err = (data.get("error") or {}).get("code", "ok")
    if err != "ok":
        raise C.FetchError(f"TikTok hata döndürdü: {err}")
    items = []
    for v in (data.get("data") or {}).get("videos", []):
        if not v.get("id") or not v.get("share_url"):
            continue
        text = v.get("title") or v.get("video_description") or ""
        items.append({
            "platform": "tiktok",
            "id": str(v["id"]),
            "kind": "video",
            "title": C.title_from_caption(text),
            "url": v["share_url"],
            "published": C.parse_time(int(v.get("create_time", 0))).isoformat(),
            "ad": C.is_ad(v.get("video_description") or v.get("title")),
            "guides": C.guide_slugs_in(v.get("video_description")),
            "_thumb_src": [v.get("cover_image_url")],
        })
    return items


def fetch_tiktok(cfg: dict, env: dict, new_secrets: dict, report: dict) -> list[dict]:
    key, secret, refresh = (env.get("TIKTOK_CLIENT_KEY"), env.get("TIKTOK_CLIENT_SECRET"),
                            env.get("TIKTOK_REFRESH_TOKEN"))
    if not (key and secret and refresh):
        raise C.FetchError("TikTok anahtarları tanımlı değil.")
    tok = refresh_tiktok_token(key, secret, refresh)
    if tok.get("refresh_token") and tok["refresh_token"] != refresh:
        new_secrets["TIKTOK_REFRESH_TOKEN"] = tok["refresh_token"]
    if tok.get("refresh_expires_in"):
        report["tiktok_refresh_expires_at"] = (
            datetime.now(timezone.utc) + timedelta(seconds=int(tok["refresh_expires_in"]))).replace(microsecond=0).isoformat()
    body = json.dumps({"max_count": min(20, cfg["max_items_per_platform"])}).encode()
    data = C.http_json("https://open.tiktokapis.com/v2/video/list/?fields=" + TT_FIELDS, data=body,
                       method="POST", headers={"Authorization": "Bearer " + tok["access_token"],
                                               "Content-Type": "application/json"})
    return normalize_tiktok(data)


# ---------- birleştirme ----------

def finalize(items: list[dict], cfg: dict) -> list[dict]:
    """Bağlantıları doğrular, sıralar, sınırlar ve kapakları indirir."""
    clean = [i for i in items if C.host_allowed(i["url"], cfg["allowed_link_hosts"])]
    clean.sort(key=lambda i: i["published"], reverse=True)
    clean = clean[: cfg["max_items_per_platform"]]
    for it in clean:
        srcs = it.pop("_thumb_src", None) or []
        size = it.pop("_thumb_size", SIZE_TALL)
        it["thumb"] = store_thumb(it["platform"], it["id"], srcs, size, cfg["allowed_image_hosts"])
    return clean


def configured(cfg: dict, name: str) -> bool:
    p = cfg["platforms"].get(name) or {}
    if name == "youtube":
        return bool(p.get("channel_id"))
    return bool(p.get("profile_url"))


def prune_media(content: dict) -> None:
    keep = {i.get("thumb") for p in content["platforms"].values() for i in p.get("items", [])}
    for f in C.MEDIA_DIR.glob("*.jpg"):
        if f.name not in keep:
            f.unlink()


def _comparable(content: dict) -> str:
    c = json.loads(json.dumps(content))
    c.pop("generated_at", None)
    for p in c["platforms"].values():
        p.pop("updated_at", None)
    return json.dumps(c, sort_keys=True, ensure_ascii=False)


def run(cfg: dict, env: dict) -> tuple[dict, dict, dict]:
    previous = {"platforms": {}}
    if C.CONTENT_FILE.exists():
        previous = json.loads(C.CONTENT_FILE.read_text(encoding="utf-8"))
    new_secrets: dict = {}
    report: dict = {"ran_at": C.now_iso(), "errors": {}, "warnings": []}
    content = {"generated_at": C.now_iso(), "platforms": {}}
    fetchers = {
        "youtube": lambda: fetch_youtube(cfg),
        "instagram": lambda: fetch_instagram(cfg, env, new_secrets, report),
        "tiktok": lambda: fetch_tiktok(cfg, env, new_secrets, report),
    }
    for name, fn in fetchers.items():
        old = previous["platforms"].get(name, {})
        if not configured(cfg, name):
            content["platforms"][name] = {"status": "not_configured", "items": []}
            continue
        try:
            items = finalize(fn(), cfg)
            content["platforms"][name] = {"status": "ok", "items": items,
                                          "updated_at": old.get("updated_at")}
            if items != old.get("items"):
                content["platforms"][name]["updated_at"] = C.now_iso()
        except Exception as e:  # tek platformun hatası diğerlerini durdurmasın
            report["errors"][name] = str(e) if isinstance(e, C.FetchError) else f"Beklenmeyen veri ({type(e).__name__})"
            content["platforms"][name] = {"status": "error", "items": old.get("items", []),
                                          "updated_at": old.get("updated_at")}
    return content, new_secrets, report


def main() -> int:
    cfg = C.load_config()
    env = dict(os.environ)
    content, new_secrets, report = run(cfg, env)

    in_actions = env.get("GITHUB_ACTIONS") == "true"
    if new_secrets:
        out = env.get("NEW_SECRETS_FILE")
        if out:
            with open(out, "w", encoding="utf-8") as fh:
                for k, v in new_secrets.items():
                    if in_actions:
                        print(f"::add-mask::{v}")
                    fh.write(f"{k}={v}\n")
            os.chmod(out, 0o600)
        else:
            report["warnings"].append("Yenilenen anahtarlar kaydedilemedi: NEW_SECRETS_FILE yok.")

    changed = True
    if C.CONTENT_FILE.exists():
        old = json.loads(C.CONTENT_FILE.read_text(encoding="utf-8"))
        changed = _comparable(old) != _comparable(content)
    if changed:
        C.CONTENT_FILE.parent.mkdir(parents=True, exist_ok=True)
        C.CONTENT_FILE.write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        prune_media(content)
    report["content_changed"] = changed

    rp = Path(env.get("FETCH_REPORT") or (C.DATA_DIR / ".last_run.json"))
    rp.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    for name, p in content["platforms"].items():
        line = f"{name}: {p['status']}, {len(p['items'])} içerik"
        if name in report["errors"]:
            line += f" — HATA: {report['errors'][name]}"
        print(line)
    for w in report["warnings"]:
        print("UYARI:", w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
