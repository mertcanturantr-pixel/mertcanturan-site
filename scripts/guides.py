"""Rehberler: dosyaları okur, doğrular, sayfa parçalarını ve paylaşım görsellerini üretir."""
from __future__ import annotations

import html
import json
import re
import sys
import unicodedata
from datetime import date, datetime, timezone
from pathlib import Path

import markdown
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402

GUIDES_DIR = C.ROOT / "guides"
FONT_SRC = C.ROOT / "fonts" / "src"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TOPICS = {  # rehber listesindeki konu grupları; sıra, listedeki sıradır
    "baslangic": "Başlangıç ve araçlar",
    "gunluk": "Günlük işler",
    "guvenlik": "Güvenlik ve gizlilik",
    "is": "İş ve meslek",
    "egitim": "Öğrenci ve öğretmen",
    "icerik": "Görsel, video ve içerik",
    "uretim": "Para ve üretim",
    "diger": "Diğer",
}

TYPES = {
    "kontrol-listesi": "Kontrol listesi",
    "adim-adim": "Adım adım",
    "sablon": "Komut şablonu",
    "karsilastirma": "Karşılaştırma",
    "dosya": "Olay dosyası",
    "soru-cevap": "Soru-cevap",
}
STAGES = {"hazir", "iskelet"}
STALE_DAYS = 180
# Şablon alanı: köşeli parantez içinde BÜYÜK HARFLİ metin. Metin HTML'e çevrildikten sonra aranır; bu yüzden
# tırnak (&quot;) ve kesme (&#x27;) varlık olarak gelir. Küçük harf içeren köşeli parantez alan sayılmaz.
_PH_CHAR = r"(?:[A-ZÇĞİÖŞÜÂÎÛ0-9 ,./:;()²!?+%-]|&quot;|&#x27;|&amp;)"
PLACEHOLDER_RE = re.compile(r"\[((?:[A-ZÇĞİÖŞÜÂÎÛ0-9]|&quot;)" + _PH_CHAR + r"{1,110})\]")
VERDICTS = {"Çalışıyor": "yes", "Şartlı çalışıyor": "maybe", "Bu haliyle çalışmıyor": "no"}
RESERVED_SLUGS = {"sablonlar", "feed", "github"}
MONEY_PATH = "yapay-zekayla-para-kazanmak/"
e = html.escape


# ---------- okuma ve doğrulama ----------

def parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("Rehber dosyası '---' ile başlamalı.")
    try:
        head, body = text[4:].split("\n---\n", 1)
    except ValueError:
        raise ValueError("Rehberin üst bilgisi '---' ile kapanmalı.") from None
    meta: dict = {"changes": []}
    for line in head.splitlines():
        if not line.strip():
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if k == "change":
            d, _, note = v.partition(" ")
            meta["changes"].append({"date": d, "note": note.strip()})
        else:
            meta[k] = v
    return meta, body


def slugify(text: str) -> str:
    t = C.tr_lower(text)
    t = t.translate(str.maketrans("çğıöşüâîû", "cgiosuaiu"))
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-") or "bolum"


def _valid_date(value: str, field: str, name: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError:
        raise ValueError(f"{name}: '{field}' tarihi YYYY-AA-GG biçiminde olmalı.") from None


def validate(meta: dict, name: str, cfg: dict, today: date) -> list[str]:
    """Hatalı rehberde ValueError verir; uyarıları döndürür."""
    for req in ("title", "slug", "summary", "type", "published", "checked"):
        if not meta.get(req):
            raise ValueError(f"{name}: '{req}' alanı boş.")
    if meta.get("topic") and meta["topic"] not in TOPICS:
        raise ValueError(f"{name}: 'topic' şunlardan biri olmalı: {', '.join(TOPICS)}.")
    if not SLUG_RE.match(meta["slug"]):
        raise ValueError(f"{name}: adres (slug) yalnızca küçük harf, rakam ve tire içerebilir.")
    if meta["slug"] in RESERVED_SLUGS:
        raise ValueError(f"{name}: '{meta['slug']}' adresi sitede başka bir sayfa için ayrılmış.")
    if meta["type"] not in TYPES:
        raise ValueError(f"{name}: 'type' şunlardan biri olmalı: {', '.join(TYPES)}.")
    pub = _valid_date(meta["published"], "published", name)
    chk = _valid_date(meta["checked"], "checked", name)
    if chk < pub:
        raise ValueError(f"{name}: son kontrol tarihi yayın tarihinden önce olamaz.")
    if chk > today:
        raise ValueError(f"{name}: son kontrol tarihi ileri bir tarih olamaz.")
    for ch in meta["changes"]:
        _valid_date(ch["date"], "change", name)
    if meta.get("video") and not C.host_allowed(meta["video"], cfg["allowed_link_hosts"]):
        raise ValueError(f"{name}: video bağlantısı YouTube, Instagram ya da TikTok olmalı.")
    stage = meta.get("stage", "hazir")
    if stage not in STAGES:
        raise ValueError(f"{name}: 'stage' hazir ya da iskelet olmalı.")
    if stage == "iskelet" and meta.get("draft", "false").lower() != "true":
        raise ValueError(f"{name}: iskelet aşamasındaki rehber yayınlanamaz; önce içeriği tamamla (stage: hazir).")
    if len(meta["summary"]) > 200:
        raise ValueError(f"{name}: özet 200 karakteri geçmemeli; arama sonuçlarında kesilir.")
    if len(meta.get("seo_title", "")) > 65:
        raise ValueError(f"{name}: seo_title 65 karakteri geçmemeli; arama sonucunda kesilir.")
    if len(meta.get("description", "")) > 160:
        raise ValueError(f"{name}: description 160 karakteri geçmemeli; arama sonucunda kesilir.")
    warnings = []
    if not meta.get("seo_title") and len(meta["title"]) > 60 and meta.get("draft", "false").lower() != "true":
        warnings.append(f"{name}: başlık {len(meta['title'])} karakter; aramada kesilmemesi için 'seo_title' ekle.")
    if (today - chk).days > STALE_DAYS:
        warnings.append(f"{name}: son kontrol {STALE_DAYS} günden eski. İçeriği yeniden doğrula.")
    return warnings


def load(cfg: dict, include_drafts: bool = False, today: date | None = None) -> tuple[list[dict], list[str]]:
    today = today or datetime.now(C.TZ).date()
    guides, warnings = [], []
    for f in sorted(GUIDES_DIR.glob("*.md")):
        if f.name.startswith("_"):
            continue  # yazım şablonu ve notlar
        meta, body = parse_front_matter(f.read_text(encoding="utf-8"))
        warnings += validate(meta, f.name, cfg, today)
        meta["draft"] = meta.get("draft", "false").lower() == "true"
        meta["stage"] = meta.get("stage", "hazir")
        meta["topic"] = meta.get("topic") or "diger"
        if meta["draft"] and not include_drafts:
            continue
        meta["audience"] = [a.strip() for a in meta.get("audience", "").split(",") if a.strip()]
        meta["type_label"] = TYPES[meta["type"]]
        words = len(re.findall(r"\w+", re.sub(r"```.*?```", " ", body, flags=re.S)))
        meta["minutes"] = max(1, round(words / 200))
        try:
            meta["html"], meta["toc"], meta["has_template"], meta["saha"] = render_body(body)
        except ValueError as err:
            raise ValueError(f"{f.name}: {err}") from None
        meta["templates"] = extract_templates(body)
        meta["body_md"] = body
        meta["karnes"] = extract_karnes(body)
        if meta["saha"] and not meta["draft"]:
            raise ValueError(f"{f.name}: {meta['saha']} SAHA notu doldurulmadan rehber yayınlanamaz.")
        if not meta["changes"]:
            meta["changes"] = [{"date": meta["published"], "note": "İlk sürüm."}]
        meta["changes"].sort(key=lambda c: c["date"], reverse=True)
        guides.append(meta)
    slugs = [g["slug"] for g in guides]
    if len(slugs) != len(set(slugs)):
        raise ValueError("Aynı adresi (slug) kullanan iki rehber var.")
    guides.sort(key=lambda g: g["published"], reverse=True)
    return guides, warnings


# ---------- içerik ----------

def _template_block(code_html: str, n: int) -> str:
    """```sablon blokunu doldurulabilir, kopyalanabilir bir şablona çevirir."""
    fields, seen = [], set()
    for m in PLACEHOLDER_RE.finditer(code_html):
        name = m.group(1)
        if name not in seen:
            seen.add(name)
            fields.append(name)
    body = PLACEHOLDER_RE.sub(lambda m: f'<mark data-f="{m.group(1)}">[{m.group(1)}]</mark>', code_html)
    inputs = []
    for i, name in enumerate(fields):  # name zaten HTML'e çevrilmiş metin; ikinci kez kaçırılmaz
        fid = f"t{n}-f{i}"
        plain = html.unescape(name)
        head = re.split(r",\s*ÖRNEĞİN\b", plain)[0].strip() or plain
        low = C.tr_lower(head)
        label = {"i": "İ", "ı": "I"}.get(low[0], low[0].upper()) + low[1:]
        if "METİN" in name or "METNİ" in name or "DÖKÜM" in name:
            ctrl = f'<textarea id="{fid}" data-f="{name}" rows="4"></textarea>'
        else:
            ctrl = f'<input id="{fid}" data-f="{name}" type="text" autocomplete="off">'
        inputs.append(f'<div class="tpl-field"><label for="{fid}">{e(label)}</label>{ctrl}</div>')
    return (
        f'<div class="tpl" data-tpl>'
        f'<div class="tpl-head"><b>Doldur, kopyala, yapıştır</b>'
        f'<span>Alanları doldur, metin aşağıda kendiliğinden değişir. Sonra kopyala.</span></div>'
        f'<div class="tpl-fields">{"".join(inputs)}</div>'
        f'<pre class="tpl-text" tabindex="0" aria-label="Komut şablonu metni"><code>{body}</code></pre>'
        f'<div class="tpl-actions"><button type="button" class="tpl-copy">Şablonu kopyala</button>'
        f'<span class="tpl-open">Kopyalayıp aç: '
        f'<a href="https://chatgpt.com/" target="_blank" rel="noopener" data-open>ChatGPT</a> '
        f'<a href="https://claude.ai/new" target="_blank" rel="noopener" data-open>Claude</a> '
        f'<a href="https://gemini.google.com/app" target="_blank" rel="noopener" data-open>Gemini</a></span>'
        f'<span class="tpl-status" role="status" aria-live="polite"></span></div>'
        f'<p class="tpl-note">Bu alanlara yazdıkların yalnızca tarayıcında kalır, hiçbir yere gönderilmez. '
        f'Kopyaladığın metni bir yapay zekâ aracına yapıştırmadan önce kişisel veri içerip içermediğini kontrol et.</p>'
        f'</div>')


KARNE_FIELDS = [  # (alan, zorunlu mu) — sıra sayfadaki sıradır
    ("Yöntem", True), ("İddia", True), ("Başlangıç maliyeti", True), ("İlk gelire kadar", True),
    ("Gereken beceri", True), ("Türkiye'den yapılabilir mi", True), ("Platform kuralı", True),
    ("Vergi", False), ("İlk adım", False), ("Bunun yerine", False), ("Karar", True),
]
KARNE_KEYS = {k for k, _ in KARNE_FIELDS}
# Gelir vaadi gibi okunan ifade: "ayda 30 bin TL", "günde 100 dolar", "haftada 5.000 ₺"
INCOME_RE = re.compile(r"\b(ayda|günde|haftada|yılda|aylık|günlük|haftalık)\s+[^.;]{0,20}?\d[\d.,]*\s*(bin|milyon)?\s*"
                       r"(tl|₺|lira|dolar|\$|usd|euro|€)", re.I)
# Sponsorluk kurallarındaki kırmızı çizgi: yatırım ve kumar yöntemleri bu sayfaya girmez
RED_LINE_RE = re.compile(r"(kripto|coin|bitcoin|ethereum|altcoin|nft|borsa|forex|hisse senedi|kaldıraç|vadeli işlem|trading|al-sat sinyali|yatırım robotu|yatırım tavsiye|bahis|iddaa|kumar|casino|slot)", re.I)
URL_RE = re.compile(r"(https?://|www\.)", re.I)
HANDLE_RE = re.compile(r"(?<![\w.])@[A-Za-z0-9_.]{2,}")
KARNE_STALE_DAYS = 90


def parse_karne(text: str) -> dict:
    """```karne blokunun düz metnini doğrular, alanlarına ayırır. Hata varsa ValueError."""
    data: dict = {"İlk adım": []}
    for line in text.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"Karne satırı 'Başlık: değer' biçiminde olmalı: {line.strip()!r}")
        k, v = (p.strip() for p in line.split(":", 1))
        if not k or not v:
            raise ValueError(f"Karne satırında başlık ya da değer boş: {line.strip()!r}")
        if k not in KARNE_KEYS:
            raise ValueError(f"Karnede bilinmeyen alan: {k!r}. Kullanılabilenler: " + ", ".join(KARNE_KEYS))
        if URL_RE.search(v):
            raise ValueError(f"Karnede bağlantı olmaz ({k}); kaynaklar rehberin Kaynaklar bölümüne yazılır.")
        if HANDLE_RE.search(v):
            raise ValueError(f"Karnede kullanıcı adı olmaz ({k}): iddiayı ele alırız, kişiyi değil.")
        if k == "İlk adım":
            data[k].append(v)
        elif k in data:
            raise ValueError(f"Karnede '{k}' alanı iki kez yazılmış.")
        else:
            data[k] = v
    missing = [k for k, req in KARNE_FIELDS if req and k not in data]
    if missing:
        raise ValueError("Karnede eksik alan: " + ", ".join(missing) + ".")
    if data["Karar"] not in VERDICTS:
        raise ValueError("Karnede 'Karar' şunlardan biri olmalı: " + ", ".join(VERDICTS) + ".")
    verdict = VERDICTS[data["Karar"]]
    if verdict in ("yes", "maybe") and not data["İlk adım"]:
        raise ValueError(f"'{data['Yöntem']}' karnesi olumlu; okurun başlayabilmesi için en az bir 'İlk adım' yaz.")
    if verdict == "no" and "Bunun yerine" not in data:
        raise ValueError(f"'{data['Yöntem']}' karnesi olumsuz; 'Bunun yerine' alanında işe yarayan yolu yaz.")
    for k, v in data.items():
        values = v if isinstance(v, list) else [v]
        for one in values:
            if k != "İddia" and INCOME_RE.search(one):
                raise ValueError(f"'{data['Yöntem']}' karnesinde gelir vaadi gibi okunan ifade var ({k}): {one!r}. "
                                 "Kazanç rakamı yalnızca 'İddia' alanında, iddianın kendisi olarak yazılabilir.")
    every = " ".join(" ".join(v) if isinstance(v, list) else str(v) for v in data.values())
    if RED_LINE_RE.search(every):
        raise ValueError(f"'{data['Yöntem']}': yatırım, kripto ve kumar yöntemleri karne formatına girmez (kırmızı çizgi).")
    data["verdict"] = verdict
    return data


def _karne_block(code_html: str) -> str:
    """```karne blokunu "Gerçekten kazandırır mı?" karnesine çevirir."""
    d = parse_karne(html.unescape(code_html))
    rows = []
    for k, _ in KARNE_FIELDS:
        if k in ("Yöntem", "İddia", "Karar") or k not in d or (k == "İlk adım" and not d[k]):
            continue
        if k == "İlk adım":
            val = "<ol>" + "".join(f"<li>{e(x)}</li>" for x in d[k]) + "</ol>"
            label = "İlk adımlar" if len(d[k]) > 1 else "İlk adım"
        else:
            val, label = e(d[k]), k
        rows.append(f"<div><dt>{e(label)}</dt><dd>{val}</dd></div>")
    return (f'<section class="karne" data-verdict="{d["verdict"]}" aria-label="Karne: {e(d["Yöntem"])}">'
            f'<p class="karne-name">{e(d["Yöntem"])}</p>'
            f'<p class="karne-claim"><span>İddia</span>{e(d["İddia"])}</p>'
            f'<dl>{"".join(rows)}</dl><p class="karne-verdict"><span>Karar</span><b>{e(d["Karar"])}</b></p></section>')


def extract_karnes(body: str) -> list[dict]:
    """Rehberdeki karneleri en yakın H2 bölümünün adresiyle toplar (para kazanma sayfası için)."""
    out, anchor, used, block = [], "", set(), None
    for line in body.splitlines():
        if block is not None:
            if line.strip() == "```":
                d = parse_karne("\n".join(block))
                d["anchor"] = anchor
                out.append(d)
                block = None
            else:
                block.append(line)
            continue
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            heading, fixed = _heading(m.group(1))
            anchor = fixed or slugify(heading)
            while anchor in used and not fixed:
                anchor += "-2"
            used.add(anchor)
        elif line.strip() == "```karne":
            block = []
    return out


_ATTR_ID = re.compile(r"\s*\{#([A-Za-z0-9_-]+)\}\s*$")


def _heading(raw: str) -> tuple[str, str | None]:
    """Başlık metnini ve varsa "{#adres}" ile verilmiş kalıcı adresi ayırır."""
    m = _ATTR_ID.search(raw)
    text = _ATTR_ID.sub("", raw) if m else raw
    return re.sub(r"[*_`]", "", text), (m.group(1) if m else None)


def extract_templates(body: str) -> list[dict]:
    """Rehberdeki ```sablon bloklarını en yakın başlıkla birlikte toplar (şablon kütüphanesi için)."""
    out, heading, anchor, used, block = [], "", "", set(), None
    for line in body.splitlines():
        if block is not None:
            if line.strip() == "```":
                out.append({"title": heading, "anchor": anchor, "code": "\n".join(block)})
                block = None
            else:
                block.append(line)
            continue
        m = re.match(r"^(#{2,3})\s+(.+?)\s*$", line)
        if m:
            heading, fixed = _heading(m.group(2))
            if m.group(1) == "##":
                anchor = fixed or slugify(heading)
                while anchor in used and not fixed:
                    anchor += "-2"
                used.add(anchor)
        elif line.strip() == "```sablon":
            block = []
    return out


def render_body(body: str) -> tuple[str, list[tuple[str, str]], bool]:
    out = markdown.markdown(body, extensions=["sane_lists", "tables", "fenced_code", "attr_list"], output_format="html")
    # kontrol listesi: gerçek onay kutuları
    counter = iter(range(10_000))

    def check(m):
        i = next(counter)
        return f'<li class="check"><input type="checkbox" id="c{i}"><label for="c{i}">'
    out = re.sub(r"<li>(?:<p>)?\[ \]\s*", check, out)
    out = re.sub(r'(<li class="check">.*?)(</p>)?</li>', lambda m: m.group(1) + "</label></li>", out, flags=re.S)
    out = re.sub(r"<ul>(\s*<li class=\"check\">)", r'<ul class="checklist">\1', out)
    # SAHA notları: Mertcan'ın kendi deneyimiyle dolduracağı yerler
    saha = [0]

    def saha_box(m):
        saha[0] += 1
        return ('<aside class="saha"><b>Mertcan\'ın eklemesi gereken</b>' + m.group(1).strip() + '</aside>')
    out = re.sub(r"<blockquote>\s*<p>SAHA:\s*(.*?)</p>\s*</blockquote>", lambda m: saha_box(m), out, flags=re.S)
    # karneler
    out = re.sub(r'<pre><code class="language-karne">(.*?)</code></pre>',
                 lambda m: _karne_block(m.group(1)), out, flags=re.S)
    # şablonlar
    tcount = iter(range(1000))
    has_tpl = "language-sablon" in out
    out = re.sub(r'<pre><code class="language-sablon">(.*?)</code></pre>',
                 lambda m: _template_block(m.group(1).rstrip("\n"), next(tcount)), out, flags=re.S)
    # başlıklara bağlantı ve içindekiler
    toc, used = [], set()

    def h2(m):
        text = re.sub(r"<[^>]+>", "", m.group(2))
        sid = m.group(1) or slugify(text)  # "## Başlık {#adres}" ile verilen adres kalıcıdır
        if m.group(1) and sid in used:
            raise ValueError(f"Aynı bölüm adresi iki kez verilmiş: #{sid}")
        while sid in used:
            sid += "-2"
        used.add(sid)
        toc.append((sid, html.unescape(text)))
        return f'<h2 id="{sid}">{m.group(2)}</h2>'
    out = re.sub(r'<h2(?: id="([^"]+)")?>(.*?)</h2>', h2, out)
    return out, toc, has_tpl, saha[0]


# ---------- yapılandırılmış veri ----------

def json_ld(g: dict, cfg: dict) -> str:
    base = cfg["site_url"].rstrip("/")
    url = f'{base}/rehber/{g["slug"]}/'
    data = [
        {"@context": "https://schema.org", "@type": "Article", "headline": g["title"],
         "description": g.get("description") or g["summary"], "inLanguage": "tr", "datePublished": g["published"],
         "dateModified": g["checked"], "mainEntityOfPage": url, "image": f'{base}/og/{g["slug"]}.png',
         "isAccessibleForFree": True,
         "author": {"@type": "Person", "@id": base + "/#kisi", "name": "Mertcan Turan", "url": base + "/#hakkimda"},
         "publisher": {"@id": base + "/#kisi"}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": base + "/"},
            {"@type": "ListItem", "position": 2, "name": "Rehberler", "item": base + "/rehber/"},
            {"@type": "ListItem", "position": 3, "name": g["title"], "item": url}]},
    ]
    raw = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return f'<script type="application/ld+json">{raw}</script>'


def _ld(data) -> str:
    raw = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return f'<script type="application/ld+json">{raw}</script>'


def site_json_ld(cfg: dict) -> str:
    """Ana sayfa: site ve kişi bilgisi (arama motorları ve yapay zekâ aramaları için)."""
    base = cfg["site_url"].rstrip("/")
    same = [p["profile_url"] for p in cfg["platforms"].values() if (p or {}).get("profile_url")]
    return _ld([
        {"@context": "https://schema.org", "@type": "WebSite", "@id": base + "/#site", "url": base + "/",
         "name": "Mertcan Turan", "inLanguage": "tr", "publisher": {"@id": base + "/#kisi"}},
        {"@context": "https://schema.org", "@type": "Person", "@id": base + "/#kisi", "name": "Mertcan Turan",
         "url": base + "/", "jobTitle": ["Avukat", "Yazılım geliştirici"],
         "description": "Yapay zekâ araçlarını gerçek işlerde test eden içerik üreticisi; avukat ve yazılım geliştirici.",
         "knowsAbout": ["Yapay zekâ", "Yazılım geliştirme"], "sameAs": same},
    ])


def index_json_ld(cfg: dict, name: str, path: str) -> str:
    base = cfg["site_url"].rstrip("/")
    items = [{"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": base + "/"},
             {"@type": "ListItem", "position": 2, "name": "Rehberler", "item": base + "/rehber/"}]
    if path != "rehber/":
        items.append({"@type": "ListItem", "position": 3, "name": name, "item": f"{base}/{path}"})
    return _ld([{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}])


def llms_txt(guides: list[dict], cfg: dict, has_money: bool = False, job: bool = False) -> str:
    """Yapay zekâ aramaları için sade site özeti (llmstxt.org önerisi)."""
    base = cfg["site_url"].rstrip("/")
    lines = ["# Mertcan Turan", "",
             "> Yapay zekâ araçlarını gerçek işlerde test eden Türkçe içerik: hangi araç işe yarıyor, "
             "hangisiyle iş kurulabilir, hangisi risk taşıyor. Rehberler ücretsiz ve kayıt istemez; "
             "her rehberde kaynaklar ve son kontrol tarihi yazar.", "", "## Rehberler", ""]
    lines += [f'- [{g["title"]}]({base}/rehber/{g["slug"]}/): {g["summary"]} (son kontrol {g["checked"]})'
              for g in guides]
    lines += ["", "## Diğer", "", f"- [Tüm rehberler]({base}/rehber/)", f"- [Hakkımda]({base}/#hakkimda)",
              f"- [Bütün rehberlerin tam metni]({base}/llms-full.txt)"]
    if job:
        lines.append(f"- [Mesleğine göre yapay zekâ]({base}/meslegine-gore-yapay-zeka/): 12 meslek için işler, "
                     "araçlar, hazır komutlar ve dikkat edilecek kurallar")
    if has_money:
        lines.append(f"- [Yapay zekâyla para kazanmak: incelenen yöntemlerin karneleri]({base}/{MONEY_PATH}): "
                     "her yöntemin maliyeti, süresi, şartı ve kararı; gelir vaadi yok")
    return "\n".join(lines) + "\n"


def llms_full(guides: list[dict], cfg: dict) -> str:
    """Yayındaki rehberlerin tam metni tek dosyada (yapay zekâ aramaları ve alıntı için)."""
    base = cfg["site_url"].rstrip("/")

    def clean(md: str) -> str:
        md = re.sub(r"\(rehber:([a-z0-9-]+)(#[a-z0-9-]+)?\)", lambda m: f"({base}/rehber/{m.group(1)}/{m.group(2) or ''})", md)
        md = re.sub(r"\s*\{#[a-z0-9-]+\}", "", md)
        md = re.sub(r"^```sablon\s*$", "```", md, flags=re.M)
        md = "\n".join(l for l in md.splitlines() if not l.startswith("> SAHA:"))
        return md.strip()

    parts = ["# Mertcan Turan · Rehberlerin tam metni", "",
             f"> Kaynak: {base}/rehber/ · Her rehberin başında adresi ve son kontrol tarihi yazar. "
             "Alıntı yaparken rehberin adresini kaynak olarak göster.", ""]
    for g in sorted(guides, key=lambda g: g["slug"]):
        parts += [f'# {g["title"]}', "", f'Adres: {base}/rehber/{g["slug"]}/  ',
                  f'Son kontrol: {g["checked"]} · Yazan: Mertcan Turan', "", clean(g.get("body_md", "")), "", "---", ""]
    return "\n".join(parts) + "\n"


def apple_touch_icon(path: Path) -> None:
    S = 4
    im = Image.new("RGB", (180 * S, 180 * S), INK)
    d = ImageDraw.Draw(im)
    d.line([(50 * S, 95 * S), (78 * S, 123 * S), (132 * S, 62 * S)], fill=YEL, width=18 * S, joint="curve")
    for x, y in ((50, 95), (78, 123), (132, 62)):
        r = 9 * S
        d.ellipse([x * S - r, y * S - r, x * S + r, y * S + r], fill=YEL)
    im = im.resize((180, 180), Image.Resampling.LANCZOS)
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, "PNG", optimize=True)


def atom_feed(guides: list[dict], cfg: dict) -> str:
    base = cfg["site_url"].rstrip("/")
    updated = max((g["checked"] for g in guides), default=date.today().isoformat())
    entries = "".join(
        f'<entry><title>{e(g["title"])}</title><link href="{base}/rehber/{g["slug"]}/"/>'
        f'<id>{base}/rehber/{g["slug"]}/</id><published>{g["published"]}T09:00:00+03:00</published>'
        f'<updated>{g["checked"]}T09:00:00+03:00</updated><summary>{e(g["summary"])}</summary></entry>'
        for g in guides)
    return ('<?xml version="1.0" encoding="utf-8"?><feed xmlns="http://www.w3.org/2005/Atom">'
            f'<title>Mertcan Turan · Rehberler</title><link href="{base}/rehber/"/>'
            f'<link rel="self" href="{base}/rehber/feed.xml"/><id>{base}/rehber/</id>'
            f'<updated>{updated}T09:00:00+03:00</updated><author><name>Mertcan Turan</name></author>'
            f'{entries}</feed>\n')


# ---------- paylaşım görseli ----------

INK, PAPER, RED, YEL = "#16224F", "#F6F7FB", "#E23B2E", "#FFE04A"


def _font(name: str, size: int, axes: list[float] | None = None):
    f = ImageFont.truetype(str(FONT_SRC / name), size)
    if axes:
        try:
            f.set_variation_by_axes(axes)
        except OSError:
            pass
    return f


def _wrap(draw, text, font, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= width or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def og_image(path: Path, title: str, kicker: str, note: str) -> None:
    """1200×630 paylaşım görseli (WhatsApp, LinkedIn, X önizlemesi)."""
    W, H, S = 1200, 630, 2
    im = Image.new("RGB", (W * S, H * S), PAPER)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W * S, 22 * S], fill=INK)
    size = 76
    while True:
        f = _font("Bricolage.ttf", size * S, [96, 760, 94])
        lines = _wrap(d, title, f, (W - 160) * S)
        if len(lines) <= 4 or size <= 48:
            break
        size -= 6
    small = _font("Bricolage.ttf", 30 * S, [24, 650, 100])
    d.text((80 * S, 78 * S), kicker, font=small, fill=RED)
    y = 138 * S
    for ln in lines[:4]:
        d.text((80 * S, y), ln, font=f, fill=INK)
        y += int(size * 1.08 * S)
    d.line([(80 * S, (H - 112) * S), ((W - 80) * S, (H - 112) * S)], fill=INK, width=3 * S)
    mark = _font("Bricolage.ttf", 32 * S, [32, 750, 100])
    d.rounded_rectangle([80 * S, (H - 86) * S, 120 * S, (H - 46) * S], radius=10 * S, fill=INK)
    d.line([(89 * S, (H - 66) * S), (97 * S, (H - 58) * S), (112 * S, (H - 75) * S)], fill=YEL, width=5 * S)
    d.text((136 * S, (H - 88) * S), "Mertcan Turan", font=mark, fill=INK)
    hand = _font("Caveat.ttf", 44 * S, [650])
    tw = d.textlength(note, font=hand)
    d.text(((W - 80) * S - tw, (H - 92) * S), note, font=hand, fill=RED)
    im = im.resize((W, H), Image.Resampling.LANCZOS)
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, "PNG", optimize=True)
