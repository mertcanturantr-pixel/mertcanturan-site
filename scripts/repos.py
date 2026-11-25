"""GitHub depoları bölümü: repos/*.md dosyalarını okur, doğrular, sayfa parçalarını üretir."""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402
import guides as G  # noqa: E402

REPOS_DIR = C.ROOT / "repos"
META_FILE = C.ROOT / "data" / "repos_meta.json"  # CI'da GitHub API'den tazelenir (scripts/repo_meta.py)
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
CATEGORIES = {
    "yerel": "Kendi bilgisayarında yapay zekâ",
    "belge": "Belge, PDF ve arşiv",
    "otomasyon": "Otomasyon ve ajanlar",
    "ses-video": "Ses, video ve altyazı",
    "gorsel": "Görsel üretim",
    "gelistirici": "Yazılımcılar için",
    "ogrenme": "Öğrenme kaynakları",
    "guvenlik": "Güvenlik ve gizlilik",
}
DIFFICULTY = {"kolay": "Kolay: kur, kullan", "orta": "Orta: biraz terminal", "zor": "Zor: sunucu ya da kod bilgisi"}
# Açık kaynak lisansları (SPDX). Listede olmayan lisans için license_note zorunlu ve sayfada uyarı görünür.
OPEN_LICENSES = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "GPL-2.0", "GPL-3.0", "LGPL-2.1", "LGPL-3.0",
                 "AGPL-3.0", "MPL-2.0", "ISC", "Unlicense", "CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0", "0BSD", "Zlib"}
COPYLEFT = {"GPL-2.0", "GPL-3.0", "AGPL-3.0", "LGPL-2.1", "LGPL-3.0", "MPL-2.0", "CC-BY-SA-4.0"}
REQUIRED_SECTIONS = ("Ne işe yarar", "Kurulum", "Dikkat")
STALE_DAYS = 90
e = html.escape


def _meta_overrides() -> dict:
    if META_FILE.exists():
        return json.loads(META_FILE.read_text(encoding="utf-8"))
    return {}


def validate(m: dict, name: str, today: date) -> list[str]:
    for req in ("name", "slug", "repo", "category", "summary", "license", "stars", "checked", "difficulty", "cost"):
        if not m.get(req):
            raise ValueError(f"{name}: '{req}' alanı boş.")
    if not G.SLUG_RE.match(m["slug"]):
        raise ValueError(f"{name}: adres (slug) yalnızca küçük harf, rakam ve tire içerebilir.")
    if not REPO_RE.match(m["repo"]):
        raise ValueError(f"{name}: 'repo' sahip/ad biçiminde olmalı (ör. ollama/ollama).")
    if m["category"] not in CATEGORIES:
        raise ValueError(f"{name}: 'category' şunlardan biri olmalı: {', '.join(CATEGORIES)}.")
    if m["difficulty"] not in DIFFICULTY:
        raise ValueError(f"{name}: 'difficulty' kolay, orta ya da zor olmalı.")
    if len(m["summary"]) > 200:
        raise ValueError(f"{name}: özet 200 karakteri geçmemeli.")
    if m["license"].upper() in ("YOK", "NONE", "NOASSERTION"):
        raise ValueError(f"{name}: lisansı olmayan depo önerilmez; lisans yoksa bütün hakları sahibinde kalır.")
    if m["license"] not in OPEN_LICENSES and not m.get("license_note"):
        raise ValueError(f"{name}: '{m['license']}' açık kaynak lisansı listesinde değil; 'license_note' ile ne anlama geldiğini yaz.")
    chk = G._valid_date(m["checked"], "checked", name)
    if chk > today:
        raise ValueError(f"{name}: son kontrol tarihi ileri bir tarih olamaz.")
    warnings = []
    if (today - chk).days > STALE_DAYS:
        warnings.append(f"{name}: depo bilgisi {STALE_DAYS} günden eski; lisansı ve son güncellemeyi yeniden kontrol et.")
    return warnings


def load(include_drafts: bool = False, today: date | None = None) -> tuple[list[dict], list[str]]:
    today = today or datetime.now(C.TZ).date()
    overrides = _meta_overrides()
    out, warnings = [], []
    if not REPOS_DIR.exists():
        return [], []
    for f in sorted(REPOS_DIR.glob("*.md")):
        if f.name.startswith("_"):
            continue
        m, body = G.parse_front_matter(f.read_text(encoding="utf-8"))
        ov = overrides.get(m.get("repo", ""), {})
        # GitHub API'den gelen güncel bilgi elle yazılanın önüne geçer; lisans değiştiyse derleme durur
        # GitHub, tanımadığı lisanslar için (ör. n8n'in Sustainable Use License'ı) "NOASSERTION" döner;
        # bu bir değişiklik değil, GitHub'ın lisansı belirleyememesi. Dosyadaki elle doğrulanmış lisans geçerli kalır.
        if ov.get("license") in ("NOASSERTION", "OTHER"):
            ov = {k: v for k, v in ov.items() if k != "license"}
        if ov.get("license") and m.get("license") and ov["license"] != m["license"]:
            raise ValueError(f"{f.name}: GitHub'daki lisans ({ov['license']}) dosyadakiyle ({m['license']}) aynı değil. "
                             "Lisans değişikliğini incele, sonra dosyayı güncelle.")
        for k in ("stars", "pushed_at", "fetched_at"):
            if ov.get(k):
                m[k] = ov[k]
        m["archived"] = bool(ov.get("archived")) or str(m.get("archived", "false")).lower() == "true"
        m["tested"] = str(m.get("tested", "false")).lower() == "true"  # yalnız Mertcan gerçekten kurduysa true
        warnings += validate(m, f.name, today)
        m["draft"] = m.get("draft", "false").lower() == "true"
        if m["archived"] and not m["draft"]:
            raise ValueError(f"{f.name}: depo GitHub'da arşivlenmiş; artık bakımı yapılmayan bir depo önerilmez.")
        if m["draft"] and not include_drafts:
            continue
        heads = re.findall(r"^##\s+(.+?)\s*$", body, flags=re.M)
        missing = [s for s in REQUIRED_SECTIONS if not any(h.startswith(s) for h in heads)]
        if missing:
            raise ValueError(f"{f.name}: eksik bölüm: {', '.join(missing)}.")
        try:
            m["html"], m["toc"], _, m["saha"] = G.render_body(body)
        except ValueError as err:
            raise ValueError(f"{f.name}: {err}") from None
        if m["saha"] and not m["draft"]:
            raise ValueError(f"{f.name}: SAHA notu doldurulmadan depo sayfası yayınlanamaz.")
        m["category_label"] = CATEGORIES[m["category"]]
        m["audience"] = [a.strip() for a in m.get("audience", "").split(",") if a.strip()]
        out.append(m)
    slugs = [r["slug"] for r in out]
    if len(slugs) != len(set(slugs)):
        raise ValueError("Aynı adresi (slug) kullanan iki depo sayfası var.")
    names = [r["repo"].lower() for r in out]
    if len(names) != len(set(names)):
        raise ValueError("Aynı GitHub deposu iki kez eklenmiş.")
    out.sort(key=lambda r: (list(CATEGORIES).index(r["category"]), C.tr_lower(r["name"])))
    return out, warnings


def license_text(r: dict) -> str:
    lic = r["license"]
    if lic not in OPEN_LICENSES:
        return f"{lic} (açık kaynak lisansı değil)"
    if lic in COPYLEFT:
        return f"{lic} (değiştirip dağıtırsan aynı lisansla paylaşman gerekir)"
    return f"{lic} (ticari kullanım dahil serbest; lisans metnini korumak gerekir)"


def json_ld(r: dict, cfg: dict) -> str:
    base = cfg["site_url"].rstrip("/")
    url = f'{base}/rehber/github/{r["slug"]}/'
    return G._ld([
        {"@context": "https://schema.org", "@type": "SoftwareSourceCode", "name": r["name"],
         "description": r["summary"], "codeRepository": f'https://github.com/{r["repo"]}',
         "license": r["license"], "url": url, "inLanguage": "tr", "dateModified": r["checked"],
         "author": {"@id": base + "/#kisi"}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": base + "/"},
            {"@type": "ListItem", "position": 2, "name": "Rehberler", "item": base + "/rehber/"},
            {"@type": "ListItem", "position": 3, "name": "GitHub depoları", "item": base + "/rehber/github/"},
            {"@type": "ListItem", "position": 4, "name": r["name"], "item": url}]},
    ])
