"""Ortak yardımcılar: ayarlar, güvenli HTTP, bağlantı ve metin kontrolleri."""
from __future__ import annotations

import json
import re
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
MEDIA_DIR = DATA_DIR / "media"
CONTENT_FILE = DATA_DIR / "content.json"
TZ = ZoneInfo("Europe/Istanbul")
USER_AGENT = "mertcanturan.com-icerik-guncelleyici/1.0"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_IMAGE_BYTES = 8 * 1024 * 1024

AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz",
         "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]


def load_config() -> dict:
    return json.loads((ROOT / "config.json").read_text(encoding="utf-8"))


class FetchError(Exception):
    """Dış kaynaktan veri alınamadı. Mesaj asla erişim anahtarı içermez."""


_SECRET_PARAMS = re.compile(r"(access_token|refresh_token|client_secret|code)=[^&\s]+", re.I)


def redact(text: str) -> str:
    return _SECRET_PARAMS.sub(r"\1=***", str(text))


def http_request(url: str, *, data: bytes | None = None, headers: dict | None = None,
                 method: str | None = None, timeout: int = 20, max_bytes: int = MAX_JSON_BYTES) -> bytes:
    if not url.startswith("https://"):
        raise FetchError("Yalnızca https adreslerine istek atılır.")
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"User-Agent": USER_AGENT, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(max_bytes + 1)
    except urllib.error.HTTPError as e:
        detail = ""
        try:
            detail = e.read(2000).decode("utf-8", "replace")
        except Exception:
            pass
        raise FetchError(redact(f"HTTP {e.code} ({urllib.parse.urlsplit(url).netloc}): {detail[:300]}")) from None
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        raise FetchError(redact(f"Bağlantı kurulamadı ({urllib.parse.urlsplit(url).netloc}): {e}")) from None
    if len(body) > max_bytes:
        raise FetchError("Yanıt beklenenden büyük, işlenmedi.")
    return body


def http_json(url: str, **kw) -> dict:
    body = http_request(url, **kw)
    try:
        return json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise FetchError("Yanıt geçerli JSON değil.") from None


def host_allowed(url: str, allowed: list[str]) -> bool:
    try:
        parts = urllib.parse.urlsplit(url)
    except ValueError:
        return False
    if parts.scheme != "https" or not parts.hostname:
        return False
    host = parts.hostname.lower()
    return any(host == a or host.endswith("." + a) for a in allowed)


def tr_lower(text: str) -> str:
    return text.replace("I", "ı").replace("İ", "i").lower()


_FOLD = str.maketrans("âîûıöüşğç", "aiuiousgc")


def search_fold(text: str) -> str:
    """Arama için: küçük harf, şapka ve Türkçe harfler sadeleşir ("Yapay Zekâ" ve "yapay zeka" eşleşir)."""
    return tr_lower(text).translate(_FOLD)


_AD_TAGS = ("#reklam", "#tanıtım", "#tanitim", "#işbirliği", "#isbirligi", "#sponsorlu", "#ücretliortaklık", "#ucretliortaklik")


def is_ad(text: str | None) -> bool:
    if not text:
        return False
    low = tr_lower(unicodedata.normalize("NFC", text))
    return any(tag in low for tag in _AD_TAGS)


_HASHTAG_TAIL = re.compile(r"(\s*#\S+)+\s*$")


def title_from_caption(caption: str | None, limit: int = 90) -> str:
    """Açıklamanın ilk anlamlı satırını başlık olarak kullanır."""
    if not caption:
        return ""
    for line in caption.splitlines():
        line = _HASHTAG_TAIL.sub("", line).strip()
        if line and not line.startswith("#"):
            break
    else:
        return ""
    line = re.sub(r"\s+", " ", line)
    if len(line) > limit:
        cut = line[:limit].rsplit(" ", 1)[0]
        line = cut.rstrip(" ,.;:-") + "…"
    return line


def guide_slugs_in(text: str | None) -> list[str]:
    if not text:
        return []
    return re.findall(r"mertcanturan\.com/rehber/([a-z0-9-]+)", text.lower())


def parse_time(value) -> datetime:
    """ISO 8601 metni ya da Unix zamanını UTC datetime'a çevirir."""
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, tz=timezone.utc)
    v = str(value).strip()
    if v.endswith("Z"):
        v = v[:-1] + "+00:00"
    if re.search(r"[+-]\d{4}$", v):  # Instagram: 2026-11-16T09:00:00+0000
        v = v[:-2] + ":" + v[-2:]
    dt = datetime.fromisoformat(v)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def tr_date(iso: str, *, with_year: bool | None = None, now: datetime | None = None) -> str:
    dt = parse_time(iso).astimezone(TZ)
    now = (now or datetime.now(timezone.utc)).astimezone(TZ)
    if with_year is None:
        with_year = dt.year != now.year
    s = f"{dt.day} {AYLAR[dt.month - 1]}"
    return f"{s} {dt.year}" if with_year else s


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
