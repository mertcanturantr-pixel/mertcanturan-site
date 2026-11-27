"""Siteyi dist/ klasörüne üretir: ana sayfa, rehberler, site haritası.

Kullanım:
  python scripts/build.py                  # canlı site (GitHub Pages)
  python scripts/build.py --preview        # önizleme: bağlantılar index.html ile biter
  python scripts/build.py --preview --demo # önizleme + örnek video verisi (yayına çıkmaz)
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import urllib.parse
import sys
from datetime import datetime, timezone
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402
import guides as G  # noqa: E402
import repos as R  # noqa: E402
import meslek as M  # noqa: E402

SRC = C.ROOT / "src"
DIST = C.ROOT / "dist"
FIXTURES = C.ROOT / "tests" / "fixtures"
PLATFORM_ORDER = ["youtube", "instagram", "tiktok"]
LABELS = {"youtube": "YouTube", "instagram": "Instagram", "tiktok": "TikTok"}
FOLLOW = {"youtube": "YouTube'da abone ol", "instagram": "Instagram'da takip et", "tiktok": "TikTok'ta takip et"}
SLUG_RE = G.SLUG_RE

e = html.escape


# ---------- bağlantılar ----------

class Links:
    def __init__(self, depth: int, explicit_index: bool):
        self.root = "../" * depth
        self.explicit = explicit_index

    def page(self, path: str) -> str:
        """path: '' (ana sayfa), 'rehber/', 'rehber/x/'"""
        target = self.root + path
        if self.explicit:
            target += "index.html"
        return target or "./"

    @property
    def home(self) -> str:
        return "" if (self.root == "") else self.page("")


# ---------- video akışı ----------

def render_card(item: dict, links: Links, guide_slugs: set[str]) -> str:
    title = item.get("title") or "Videoyu izle"
    if item.get("thumb"):
        w, h = (640, 360) if item.get("_wide") else (360, 640)
        img = (f'<img src="{links.root}media/{e(item["thumb"])}" alt="" width="{w}" height="{h}" '
               f'loading="lazy" decoding="async">')
        thumb_cls = "thumb"
    else:
        img, thumb_cls = e(LABELS[item["platform"]]), "thumb noimg"
    badge = '<span class="badge">Reklam</span>' if item.get("ad") else ""
    meta = [f'<time datetime="{e(item["published"])}">{e(C.tr_date(item["published"]))}</time>']
    for slug in item.get("guides", []):
        if slug in guide_slugs:
            meta.append(f'<a href="{e(links.page("rehber/" + slug + "/"))}">Rehberi aç</a>')
            break
    return (f'<li class="card"><a class="main" href="{e(item["url"])}" target="_blank" rel="noopener">'
            f'<div class="{thumb_cls}">{img}{badge}</div><h3>{e(title)}</h3>'
            f'<span class="sr-only"> ({LABELS[item["platform"]]}, yeni sekmede açılır)</span></a>'
            f'<p class="meta">{"".join(meta)}</p></li>')


def render_feed(content: dict, cfg: dict, links: Links, guide_slugs: set[str]) -> str:
    panels, tabs = [], []
    for name in PLATFORM_ORDER:
        pc = cfg["platforms"].get(name) or {}
        data = content.get("platforms", {}).get(name) or {"items": []}
        if not pc.get("profile_url") or data.get("status") == "not_configured":
            continue
        items = data.get("items", [])
        wide = False
        if name == "youtube":
            long_items = [i for i in items if i.get("kind") == "video"]
            if long_items:
                items, wide = long_items, True
                if len(items) >= 3:  # üç sütunlu ızgarada yarım satır kalmasın
                    items = items[:6] if len(items) >= 6 else items[:3]
        for i in items:
            i["_wide"] = wide
        pid = f"panel-{name}"
        first = not panels
        tabs.append(f'<button class="tab" type="button" role="tab" id="tab-{name}" aria-controls="{pid}" '
                    f'aria-selected="{"true" if first else "false"}"{"" if first else " tabindex=\"-1\""}>'
                    f'{LABELS[name]}</button>')
        follow_url = pc["profile_url"] + ("?sub_confirmation=1" if name == "youtube" else "")
        body = (f'<ul class="grid {"wide" if wide else "tall"}">'
                + "".join(render_card(i, links, guide_slugs) for i in items) + "</ul>") if items else \
            '<p class="empty">İlk videolar yakında burada olacak.</p>'
        panels.append(
            f'<div class="panel" role="tabpanel" id="{pid}" aria-labelledby="tab-{name}"{"" if first else " data-hidden"}>'
            f'<h3 class="panel-title">{LABELS[name]}</h3>{body}'
            f'<div class="panel-foot"><a class="btn {"solid" if first else "line"}" href="{e(follow_url)}">'
            f'{FOLLOW[name]}</a></div></div>')
    if not panels:
        return ""
    intro = "Her yeni video kendiliğinden burada da görünür."
    if len(panels) > 1:
        intro += " İzlemek istediğin platformu seç."
    if len(panels) == 1:  # tek platform varsa sekmeye gerek yok
        tablist = ""
        panels[0] = panels[0].replace(' role="tabpanel"', "").replace(' aria-labelledby="tab-youtube"', "")
        panels[0] = re.sub(r' aria-labelledby="tab-\w+"', "", panels[0])
    else:
        tablist = f'<div class="tabs" role="tablist" aria-label="Platform seç">{"".join(tabs)}</div>'
    return f'''  <section class="block feed" id="videolar">
    <div class="wrap">
      <div class="feed-head">
        <div>
          <h2>Son videolar</h2>
          <p class="intro">{intro}</p>
        </div>
        {tablist}
      </div>
      {"".join(panels)}
    </div>
  </section>
'''


SUBLABEL = {"youtube": "Uzun videolar", "instagram": "Kısa videolar", "tiktok": "Kısa videolar"}

NAV_JS = """(function(){
  var f=document.querySelector('.follow'),b=f&&f.querySelector('.follow-btn');if(!b)return;
  function set(o){f.classList.toggle('open',o);b.setAttribute('aria-expanded',o)}
  b.addEventListener('click',function(){set(b.getAttribute('aria-expanded')!=='true')});
  document.addEventListener('click',function(e){if(!f.contains(e.target))set(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&f.classList.contains('open')){set(false);b.focus()}});
})();"""


def render_follow(cfg: dict) -> str:
    items = [(n, cfg["platforms"][n]["profile_url"]) for n in PLATFORM_ORDER
             if (cfg["platforms"].get(n) or {}).get("profile_url")]
    lis = "".join(f'<li><a href="{e(u)}" rel="me">{LABELS[n]}<span class="sub">{SUBLABEL[n]}</span></a></li>'
                  for n, u in items)
    chevron = ('<svg width="12" height="8" viewBox="0 0 12 8" aria-hidden="true"><path d="M1 1.5l5 5 5-5" fill="none" '
               'stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    return (f'    <div class="follow"><button class="follow-btn" type="button" aria-expanded="false" '
            f'aria-controls="follow-list">Takip et {chevron}</button>'
            f'<ul class="follow-list" id="follow-list" aria-label="Sosyal medya hesapları">{lis}</ul></div>')


def render_archor(cfg: dict) -> tuple[str, str]:
    a = cfg.get("archor") or {}
    if not a.get("show"):
        return "", ""
    if a.get("url") and not str(a["url"]).startswith("https://"):
        raise ValueError("config.json: archor.url https:// ile başlamalı.")
    name = (f'<a href="{e(a["url"])}">Archor Teknoloji</a>' if a.get("url") else "Archor Teknoloji")
    collab = (f'      <p class="archor-note">Ürünün için yazılım geliştirme ya da kod incelemesi arıyorsan, '
              f'bu işleri kurucusu olduğum {name} yapıyor. Video iş birliği ile bu hizmetler birbirinden ayrıdır; '
              f'biri diğerinin şartı değildir.</p>\n')
    about = ('        <p>Archor Teknoloji adlı yazılım şirketinin de kurucusuyum. Archor\'un müşterisi ya da rakibi '
             'olan bir ürünü incelersem bunu videoda açıkça söylerim.</p>\n')
    return collab, about


TABS_JS = """(function(){
  var tabs=[].slice.call(document.querySelectorAll('.tab'));if(!tabs.length)return;
  function sel(t,focus){tabs.forEach(function(x){var on=x===t;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;
    var p=document.getElementById(x.getAttribute('aria-controls'));p.hidden=!on;p.removeAttribute('data-hidden')});if(focus)t.focus()}
  tabs.forEach(function(t,i){t.addEventListener('click',function(){sel(t)});
    t.addEventListener('keydown',function(ev){var n=ev.key==='ArrowRight'?i+1:ev.key==='ArrowLeft'?i-1:null;
      if(n===null)return;ev.preventDefault();sel(tabs[(n+tabs.length)%tabs.length],true)})});
  sel(tabs[0]);
})();"""


# ---------- rehber blokları ----------

def _draft(g: dict) -> str:
    if g.get("stage") == "iskelet":
        return '<span class="draft">İskelet</span>'
    return '<span class="draft">Taslak</span>' if g.get("draft") else ""


def _guide_href(links: Links, g: dict) -> str:
    return e(links.page("rehber/" + g["slug"] + "/"))


def render_guides_home(guides: list[dict], links: Links) -> str:
    sheets = "".join(
        f'<li><a class="sheet" href="{_guide_href(links, g)}"><span class="kind">{e(g["type_label"])}{_draft(g)}</span>'
        f'<h3>{e(g["title"])}</h3><p>{e(g["summary"])}</p>'
        f'<span class="foot"><span>Son kontrol: {e(C.tr_date(g["checked"], with_year=True))} · {g["minutes"]} dk</span>'
        f'<strong>Rehberi aç</strong></span></a></li>' for g in guides[:3])
    if len(guides) < 3:
        sheets += '<li><p class="sheet-soon">Yeni rehberler videolarla birlikte buraya eklenecek.</p></li>'
    return f'''  <section class="block" id="rehberler">
    <div class="wrap guides-home">
      <div>
        <h2>Videoda anlatırım, rehberini burada bırakırım.</h2>
        <p class="intro">Videolarda bahsettiğim kontrol listeleri, komut şablonları ve adım adım anlatımlar burada. Her rehberde kaynaklar ve son kontrol tarihi yazar.</p>
        <p class="hand">ücretsiz, kayıt yok</p>
        <div class="cta"><a class="btn line" href="{e(links.page("rehber/"))}">Tüm rehberler</a></div>
      </div>
      <ul class="sheets">{sheets}</ul>
    </div>
  </section>
'''


def render_guide_index(guides: list[dict], links: Links, email: str, filter_min: int, tpl_count: int = 0,
                       money_href: str | None = None, repo_href: str | None = None, repo_count: int = 0,
                       job_href: str | None = None) -> str:
    def row(g):
        text = C.search_fold(" ".join([g["title"], g["summary"], g["type_label"], " ".join(g["audience"]),
                                       G.TOPICS[g["topic"]], " ".join(t for _, t in g["toc"]), g.get("keywords", "")]))
        aud = f' · {e(", ".join(g["audience"]))}' if g["audience"] else ""
        return (f'<li data-text="{e(text)}"><a href="{_guide_href(links, g)}">'
                f'<span class="kind">{e(g["type_label"])}{_draft(g)}</span><h3>{e(g["title"])}</h3><p>{e(g["summary"])}</p>'
                f'<span class="when">{g["minutes"]} dk okuma{aud}</span></a></li>')
    groups = [(t, lbl, sorted((g for g in guides if g["topic"] == t), key=lambda g: C.search_fold(g["title"])))
              for t, lbl in G.TOPICS.items()]
    groups = [x for x in groups if x[2]]
    sections = "".join(
        f'<section class="guide-group" data-topic="{t}" aria-labelledby="konu-{t}">'
        f'<h2 id="konu-{t}">{e(lbl)} <span class="n">{len(gs)}</span></h2>'
        f'<ul class="guide-list">{"".join(row(g) for g in gs)}</ul></section>' for t, lbl, gs in groups)
    tools = ""
    if len(guides) >= filter_min:
        chips = ['<button type="button" class="chip" data-topic="" aria-pressed="true">Hepsi</button>']
        chips += [f'<button type="button" class="chip" data-topic="{t}" aria-pressed="false">{e(lbl)}</button>'
                  for t, lbl, _ in groups]
        tools = (f'<div class="guide-tools"><label class="search"><span class="sr-only">Rehberlerde ara</span>'
                 f'<input type="search" placeholder="Ara: CV, KDV, fotoğraf, gizlilik" autocomplete="off"></label>'
                 f'<div class="chips" role="group" aria-label="Konu">{"".join(chips)}</div>'
                 f'<p class="found" data-found aria-live="polite" hidden></p></div>')
    body = sections if guides else '<ul class="guide-list"><li><p class="empty">İlk rehber yakında burada.</p></li></ul>'
    subject = "Rehber%20%C3%B6nerisi"
    money = (f'<p class="money-link">Yapay zekâyla para kazanma yöntemlerinin karneleri tek sayfada: '
             f'<a href="{e(money_href)}">işe yarayan yollar ve tuzaklar</a></p>') if money_href else ""
    if repo_href:
        money += (f'<p class="money-link">Kanallarda konuşulan GitHub depolarından işe yarayanlar: '
                  f'<a href="{e(repo_href)}">GitHub depoları ({repo_count})</a></p>')
    by_slug = {g["slug"]: g for g in guides}
    starters = [by_slug[s] for s in START_GUIDES if s in by_slug]
    start = ""
    if len(starters) >= 3 or job_href:
        items = "".join(f'<li><a href="{_guide_href(links, g)}">{e(g["title"])}</a></li>' for g in starters)
        job = (f'<p class="start-job"><b>Mesleğine göre başlamak ister misin?</b> Beş soruyu cevapla, işine göre araç, '
               f'hazır komut ve kuralları gör. <a class="btn solid" href="{e(job_href)}">Planımı çıkar</a></p>') if job_href else ""
        lst = f'<ol class="start-list">{items}</ol>' if len(starters) >= 3 else ""
        start = (f'<section class="start-box" aria-labelledby="buradan-basla"><h2 id="buradan-basla">Yeni başlıyorsan buradan başla</h2>'
                 f'{lst}{job}</section>')
    tpl_link = (f' · <a href="{e(links.page("rehber/sablonlar/"))}">Bütün komut şablonları ({tpl_count})</a>'
                if tpl_count else "")
    return f'''<div class="doc doc-index">
  <h1>Rehberler</h1>
  <p class="lede">Videolarda bahsettiğim kontrol listeleri, komut şablonları ve adım adım anlatımlar. Ücretsiz, kayıt istemez. Her rehberde kaynaklar ve son kontrol tarihi yazar.</p>
  <p class="index-meta">{len(guides)} rehber{tpl_link} · <a href="feed.xml">Yeni rehberleri RSS ile takip et</a></p>
  {tools}{start}{money}
  <div class="guide-groups">{body}</div>
  <p class="empty" data-empty hidden>Bu aramaya uyan rehber yok. Başka bir kelime dene.</p>
  <aside class="suggest"><p><b>Hangi konuda rehber istersin?</b> Bir sonraki rehberi senin sorundan yazabilirim.</p>
  <a class="btn line" href="mailto:{e(email)}?subject={subject}">Konu öner</a></aside>
</div>'''


SHORT_RE = re.compile(r"^[a-z0-9-]{2,24}$")
SHORT_RESERVED = {"rehber", "fonts", "og", "media", G.MONEY_PATH.strip("/"), M.JOB_PATH.strip("/")}


def write_short_links(out_dir: Path, cfg: dict, published: set[str], has_job: bool) -> dict[str, str]:
    """data/kisa.json: videoda söylenen kısa adresler (mertcanturan.com/ayar). Hedef yayında değilse rehber listesine gider."""
    f = C.DATA_DIR / "kisa.json"
    if not f.exists():
        return {}
    base, made = cfg["site_url"].rstrip("/"), {}
    for short, target in json.loads(f.read_text(encoding="utf-8")).get("links", {}).items():
        if not SHORT_RE.match(short) or short in SHORT_RESERVED:
            raise ValueError(f"kisa.json: '{short}' kısa adres olarak kullanılamaz.")
        if not re.match(r"^[a-z0-9/-]+/(#[a-z0-9-]+)?$", target):
            raise ValueError(f"kisa.json: '{short}' hedefi site içi bir sayfa olmalı (ör. rehber/adres/ ya da rehber/adres/#bolum).")
        m = re.match(r"^rehber/([a-z0-9-]+)/(#[a-z0-9-]+)?$", target)
        if (m and m.group(1) not in published) or (target == M.JOB_PATH and not has_job):
            target = "rehber/"
        url = f"{base}/{target}"
        (out_dir / short).mkdir(parents=True, exist_ok=True)
        (out_dir / short / "index.html").write_text(
            f'<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8"><title>Yönlendiriliyor</title>'
            f'<meta name="robots" content="noindex"><link rel="canonical" href="{e(url)}">'
            f'<meta http-equiv="refresh" content="0; url={e(url)}"></head>'
            f'<body><p><a href="{e(url)}">Sayfaya git</a></p></body></html>\n', encoding="utf-8")
        made[short] = target
    return made


START_GUIDES = ["hangi-yapay-zeka", "yapay-zekaya-iyi-komut-yazmak", "yapay-zeka-cevabini-kontrol-etmek",
                "yapay-zekaya-ne-yazilmaz", "yapay-zeka-gizlilik-ayarlari"]

INTERNAL_RE = re.compile(r'href="rehber:([a-z0-9-]+)(#[a-z0-9-]+)?"')


LINK_RE = re.compile(r'<a href="rehber:([a-z0-9-]+)(#[a-z0-9-]+)?">(.*?)</a>', re.S)


def resolve_internal(html_text: str, links: Links, known: dict[str, set[str]], source: str,
                     unpublished: set[str] = frozenset()) -> str:
    """Rehber içi bağlantıları (rehber:slug#bolum) sayfanın konumuna göre çevirir; olmayan rehber ya da bölümde hata verir."""
    def sub(m):
        if m.group(1) not in known:
            raise ValueError(f"{source}: '{m.group(1)}' adında bir rehber yok (bağlantı: rehber:{m.group(1)}).")
        if m.group(2) and m.group(2)[1:] not in known[m.group(1)]:
            raise ValueError(f"{source}: '{m.group(1)}' rehberinde '{m.group(2)}' bölümü yok.")
        return f'href="{e(links.page("rehber/" + m.group(1) + "/"))}{m.group(2) or ""}"'

    def unlink(m):  # yayında olmayan rehbere bağlantı: düz metin kalsın, rehber yayınlanınca bağlantı gelir
        if m.group(1) in unpublished:
            print(f"UYARI: {source}: '{m.group(1)}' henüz yayında değil; bağlantı düz metin olarak gösterildi.",
                  file=sys.stderr)
            return m.group(3)
        return m.group(0)
    return INTERNAL_RE.sub(sub, LINK_RE.sub(unlink, html_text))


def guide_title_tag(g: dict) -> str:
    """Arama sonucunda kesilmesin: seo_title varsa o; marka adı yalnızca sığıyorsa eklenir."""
    t = g.get("seo_title") or g["title"]
    branded = f"{t} · Mertcan Turan"
    return branded if len(branded) <= 60 else t


def render_guide_page(g: dict, links: Links, email: str, related: list[dict], video_item: dict | None,
                      money_href: str | None = None, subscribe_url: str | None = None,
                      job_href: str | None = None) -> str:
    video = ""
    if g.get("video"):
        thumb = ""
        if video_item and video_item.get("thumb"):
            thumb = f'<img src="{links.root}media/{e(video_item["thumb"])}" alt="" width="160" height="90" loading="lazy">'
        title = g.get("video_title") or (video_item or {}).get("title") or "Videoyu izle"
        video = (f'<a class="video-box" href="{e(g["video"])}" target="_blank" rel="noopener">{thumb}<div>'
                 f'<b>Bu rehberin videosu</b><span>{e(title)}</span></div></a>')
    toc = ""
    if len(g["toc"]) >= 3:
        items = "".join(f'<li><a href="#{sid}">{e(t)}</a></li>' for sid, t in g["toc"])
        toc = (f'<nav class="toc" aria-label="Bu rehberde"><details data-toc><summary>Bu rehberde ({len(g["toc"])} bölüm)</summary>'
               f'<ol>{items}</ol></details></nav>')
    aud = f'<span>Kimler için: {e(", ".join(g["audience"]))}</span>' if g["audience"] else ""
    changes = "".join(f'<li><time datetime="{e(c["date"])}">{e(C.tr_date(c["date"], with_year=True))}</time> {e(c["note"])}</li>'
                      for c in g["changes"])
    rel = ""
    if related:
        rel = ('<section class="related"><h2>Diğer rehberler</h2><ul class="sheets">' + "".join(
            f'<li><a class="sheet" href="{_guide_href(links, r)}"><span class="kind">{e(r["type_label"])}</span>'
            f'<h3>{e(r["title"])}</h3><p>{e(r["summary"])}</p></a></li>' for r in related) + "</ul></section>")
    subj = urllib.parse.quote(f'Rehber hatası: {g["title"]}')
    sub = (f'<p class="money-link">Yeni rehberler videolarla birlikte geliyor. '
           f'<a href="{e(subscribe_url)}" rel="noopener">YouTube kanalına abone ol</a>, ilk sen gör.</p>') if subscribe_url else ""
    money = ""
    if money_href and g.get("karnes"):
        money = (f'<p class="money-link">Bu rehberdeki karneler, diğer yöntemlerle birlikte tek sayfada: '
                 f'<a href="{e(money_href)}">Yapay zekâyla para kazanmak: işe yarayan yollar ve tuzaklar</a></p>')
    if job_href:
        money += (f'<p class="money-link">Mesleğine göre hangi işte hangi aracı kullanacağını tek sayfada gör: '
                  f'<a href="{e(job_href)}">Mesleğine göre yapay zekâ planını çıkar</a></p>')
    checked = (f'<span class="checked">kontrol edildi</span><span>Son kontrol: <time datetime="{e(g["checked"])}">'
               f'{e(C.tr_date(g["checked"], with_year=True))}</time></span>')
    if g.get("stage") == "iskelet":
        checked = '<span class="checked">içerik planı</span>'
    draft_bar = ""
    if g.get("stage") == "iskelet":
        draft_bar = ('<p class="draft-bar">İskelet: Bu rehberin içeriği videosuyla birlikte yazılacak. '
                     'Önizlemede görünür, canlı sitede yayınlanmaz.</p>')
    elif g.get("draft"):
        draft_bar = '<p class="draft-bar">Taslak: Onayından sonra yayınlanır. Canlı sitede şu an görünmez.</p>'
    
    return f'''<article class="guide{" has-toc" if toc else ""}">
  <header class="guide-head">
    {draft_bar}<p class="crumb"><a href="{e(links.page("rehber/"))}">Rehberler</a> <span aria-hidden="true">/</span> {e(g["type_label"])}</p>
    <h1>{e(g["title"])}</h1>
    <p class="lede">{e(g["summary"])}</p>
    <div class="doc-meta">
      {checked}
      <span>Yazan: <a href="{e(links.page(""))}#hakkimda">Mertcan Turan</a></span>
      <span>{g["minutes"]} dk okuma</span>
      {aud}
      <span class="doc-actions"><button class="act" type="button" data-share>Bağlantıyı paylaş</button><button class="act" type="button" onclick="window.print()">Yazdır ya da PDF kaydet</button></span>
      <span class="share-status" role="status" aria-live="polite"></span>
    </div>
    {video}
  </header>
  <div class="guide-body{" has-toc" if toc else ""}">
    {toc}
    <div class="prose">{g["html"]}</div>
  </div>
  <footer class="guide-end">
    <details class="changes"><summary>Değişiklik geçmişi</summary><ul>{changes}</ul></details>
    <p class="doc-note">Bu rehber genel bilgilendirme amaçlıdır; avukatlık hizmeti ya da kişiye özel hukuki danışmanlık değildir. Araçların ayarları ve kuralları değişebilir; bu yüzden son kontrol tarihine bak. Bir hata gördüysen <a href="mailto:{e(email)}?subject={subj}">bana yaz</a>, düzelteyim.</p>
    {money}{sub}{rel}
  </footer>
</article>'''


GUIDE_JS = """(function(){
  // içindekiler: geniş ekranda açık, telefonda kapalı başlar (ilk paragraf yukarıda kalsın)
  var td=document.querySelector('[data-toc]');if(td&&window.matchMedia('(min-width:1180px)').matches)td.open=true;
  // kontrol listesi ilerlemesi (kaydedilmez)
  [].forEach.call(document.querySelectorAll('ul.checklist'),function(ul){
    var boxes=ul.querySelectorAll('input[type=checkbox]');if(!boxes.length)return;
    var p=document.createElement('p');p.className='progress';p.setAttribute('aria-live','polite');
    ul.parentNode.insertBefore(p,ul);
    function upd(){var n=0;[].forEach.call(boxes,function(b){if(b.checked)n++});
      p.textContent=n+' / '+boxes.length+' kontrol tamam'+(n===boxes.length?'. Hepsi tamam.':'');p.classList.toggle('done',n===boxes.length)}
    ul.addEventListener('change',upd);upd();
  });
  function copy(text,done){
    if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(text).then(function(){done(true)},function(){done(false)})}
    else{var t=document.createElement('textarea');t.value=text;t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();
      var ok=false;try{ok=document.execCommand('copy')}catch(e){}document.body.removeChild(t);done(ok)}
  }
  // şablonlar
  [].forEach.call(document.querySelectorAll('[data-tpl]'),function(box){
    var code=box.querySelector('code'),status=box.querySelector('.tpl-status');
    box.addEventListener('input',function(ev){var f=ev.target.getAttribute('data-f');if(!f)return;
      [].forEach.call(code.querySelectorAll('mark'),function(m){if(m.getAttribute('data-f')===f){
        m.textContent=ev.target.value||'['+f+']';m.classList.toggle('filled',!!ev.target.value)}})});
    function say(ok,extra){status.textContent=ok?'Kopyalandı.'+(extra||''):'Kopyalanamadı. Metni seçip elle kopyala.'}
    box.querySelector('.tpl-copy').addEventListener('click',function(){copy(code.textContent,function(ok){say(ok)})});
    [].forEach.call(box.querySelectorAll('[data-open]'),function(a){a.addEventListener('click',function(){
      copy(code.textContent,function(ok){say(ok,' Açılan sayfaya yapıştır.')})})});
  });
  // paylaş
  var sh=document.querySelector('[data-share]');
  if(sh){var st=document.querySelector('.share-status');sh.addEventListener('click',function(){
    var url=location.href.split('#')[0];
    if(navigator.share){navigator.share({title:document.title,url:url}).catch(function(){});return}
    copy(url,function(ok){st.textContent=ok?'Bağlantı kopyalandı.':'Kopyalanamadı.'})})}
  // rehber listesi: konu ve arama
  var groups=document.querySelectorAll('.guide-group'),chips=document.querySelectorAll('.chip[data-topic]'),q=document.querySelector('.search input');
  if(groups.length&&(chips.length||q)){var topic='',empty=document.querySelector('[data-empty]'),found=document.querySelector('[data-found]');
    function tr(s){s=s.replace(/I/g,'ı').replace(/İ/g,'i').toLowerCase();var a='âîûıöüşğç',b='aiuiousgc',o='';
      for(var i=0;i<s.length;i++){var k=a.indexOf(s[i]);o+=k>-1?b[k]:s[i]}return o}
    function apply(){var term=q?tr(q.value.trim()):'',shown=0;
      [].forEach.call(groups,function(sec){var n=0,inTopic=!topic||sec.getAttribute('data-topic')===topic;
        [].forEach.call(sec.querySelectorAll('li'),function(li){var ok=inTopic&&(!term||(li.getAttribute('data-text')||'').indexOf(term)>-1);
          li.hidden=!ok;if(ok)n++});sec.hidden=!n;shown+=n});
      if(empty)empty.hidden=shown>0;
      if(found){found.hidden=!term||!shown;found.textContent=shown+' rehber bulundu'}}
    [].forEach.call(chips,function(c){c.addEventListener('click',function(){topic=c.getAttribute('data-topic');
      [].forEach.call(chips,function(x){x.setAttribute('aria-pressed',x===c)});apply()})});
    if(q)q.addEventListener('input',apply);
  }
})();"""

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 30"><rect x="1" y="1" width="28" height="28" rx="8" '
           'fill="#16224F"/><path d="M8.5 15.5l4.2 4.2L21.5 10" fill="none" stroke="#FFE04A" stroke-width="3.2" '
           'stroke-linecap="round" stroke-linejoin="round"/></svg>\n')


def render_templates_page(guides: list[dict], links: Links) -> str:
    """Bütün rehberlerdeki komut şablonları tek sayfada."""
    n, groups = 0, []
    for g in guides:
        if not g.get("templates"):
            continue
        anchors = {sid for sid, _ in g["toc"]}
        href = _guide_href(links, g)
        items = []
        for t in g["templates"]:
            where = href + ("#" + t["anchor"] if t["anchor"] in anchors else "")
            title = t["title"] or g["title"]
            items.append(f'<li><h3>{e(title)}</h3>{G._template_block(e(t["code"]), n)}'
                         f'<p class="tpl-src">Nasıl kullanılacağı rehberde: <a href="{where}">{e(g["title"])}</a></p></li>')
            n += 1
        groups.append(f'<section class="tpl-group"><h2>{e(g["title"])}{_draft(g)}</h2><ul>{"".join(items)}</ul></section>')
    return f'''<div class="doc doc-index">
  <p class="crumb"><a href="{e(links.page("rehber/"))}">Rehberler</a> <span aria-hidden="true">/</span> Şablonlar</p>
  <h1>Komut şablonları</h1>
  <p class="lede">Rehberlerdeki bütün şablonlar bir arada. Alanları doldur, metni kopyala, kullandığın yapay zekâya yapıştır. Yazdıkların tarayıcında kalır, hiçbir yere gönderilmez.</p>
  <p class="index-meta">{n} şablon</p>
  {"".join(groups)}
</div>'''


NOT_FOUND = '''<div class="doc doc-index">
  <h1>Bu sayfa yok</h1>
  <p class="lede">Bağlantı eski olabilir ya da adres yanlış yazılmış olabilir. Aradığın şey büyük ihtimalle rehberlerdedir.</p>
  <p><a class="btn solid" href="/rehber/">Rehberlere git</a> <a class="btn line" href="/">Ana sayfaya dön</a></p>
</div>'''



VERDICT_LABEL = {"yes": "Çalışıyor", "maybe": "Şartlı çalışıyor", "no": "Bu haliyle çalışmıyor"}
VERDICT_ORDER = {"yes": 0, "maybe": 1, "no": 2}
TR_KEY = "Türkiye'den yapılabilir mi"


def collect_karnes(guides: list[dict]) -> list[dict]:
    rows = []
    for g in guides:
        for k in g.get("karnes", []):
            rows.append({**k, "guide": g})
    seen: dict[str, str] = {}
    for r in rows:
        key = C.tr_lower(r["Yöntem"]).strip()
        if key in seen:
            raise ValueError(f"'{r['Yöntem']}' yöntemi iki karnede var ({seen[key]} ve {r['guide']['slug']}). "
                             "Bir yöntemin tek karnesi olur; güncellemeyi o karnede yap.")
        seen[key] = r["guide"]["slug"]
    rows.sort(key=lambda r: (VERDICT_ORDER[r["verdict"]], C.tr_lower(r["Yöntem"])))
    return rows


def _stale(r: dict) -> str:
    """Platform kuralları hızlı değişir: 90 günden eski karne okura açıkça söylenir."""
    age = (datetime.now(C.TZ).date() - datetime.fromisoformat(r["guide"]["checked"]).date()).days
    if age > G.KARNE_STALE_DAYS:
        return '<span class="stale">Yeniden kontrol bekliyor</span>'
    return ""


def money_page_ready(rows: list[dict], minimum: int) -> bool:
    """Sayfa boş ya da tek taraflı görünmesin: en az `minimum` karne ve en az bir olumlu karar."""
    return len(rows) >= minimum and any(r["verdict"] in ("yes", "maybe") for r in rows)


def _karne_href(links: Links, r: dict) -> str:
    anchors = {sid for sid, _ in r["guide"]["toc"]}
    frag = "#" + r["anchor"] if r["anchor"] in anchors else ""
    return _guide_href(links, r["guide"]) + frag


def _fact(label: str, value: str) -> str:
    return f"<div><dt>{e(label)}</dt><dd>{e(value)}</dd></div>"


def render_money_page(rows: list[dict], links: Links, email: str, demo_note: bool = False) -> str:
    good = [r for r in rows if r["verdict"] != "no"]
    bad = [r for r in rows if r["verdict"] == "no"]
    counts = {v: sum(1 for r in rows if r["verdict"] == v) for v in VERDICT_LABEL}
    last = max(r["guide"]["checked"] for r in rows)
    note = ('<p class="draft-bar">Önizleme: Bu sayfadaki karneler örnektir, gerçek bir denemeye dayanmaz. '
            'Canlı sitede yalnızca yayındaki rehberlerin karneleri görünür.</p>') if demo_note else ""

    def card_good(r):
        steps = "".join(f"<li>{e(x)}</li>" for x in r["İlk adım"])
        facts = "".join(_fact(k, r[k]) for k in ("Başlangıç maliyeti", "İlk gelire kadar", "Gereken beceri",
                                                  "Türkiye'den yapılabilir mi", "Platform kuralı"))
        return (f'<li class="mcard" data-verdict="{r["verdict"]}"><div class="mcard-head"><h3>{e(r["Yöntem"])}</h3>'
                f'<span class="verdict v-{r["verdict"]}">{VERDICT_LABEL[r["verdict"]]}</span></div>'
                f'<dl class="facts">{facts}</dl><p class="mlabel">Nereden başlarsın</p><ol class="msteps">{steps}</ol>'
                f'<p class="mfoot"><a href="{_karne_href(links, r)}">Karnenin tamamı ve kaynaklar</a>'
                f'<span>Son kontrol: {e(C.tr_date(r["guide"]["checked"], with_year=True))}{_draft(r["guide"])}{_stale(r)}</span></p></li>')

    def card_bad(r):
        return (f'<li class="mcard" data-verdict="no"><div class="mcard-head"><h3>{e(r["Yöntem"])}</h3>'
                f'<span class="verdict v-no">{VERDICT_LABEL["no"]}</span></div>'
                f'<p class="mclaim"><span>Anlatılan</span>{e(r["İddia"])}</p>'
                f'<dl class="facts">{_fact("Neden olmuyor", r["Platform kuralı"])}'
                f'{_fact("Türkiye’den yapılabilir mi", r[TR_KEY])}</dl>'
                f'<p class="mlabel">Bunun yerine</p><p class="minstead">{e(r["Bunun yerine"])}</p>'
                f'<p class="mfoot"><a href="{_karne_href(links, r)}">Karnenin tamamı ve kaynaklar</a>'
                f'<span>Son kontrol: {e(C.tr_date(r["guide"]["checked"], with_year=True))}{_draft(r["guide"])}{_stale(r)}</span></p></li>')

    trs = "".join(
        f'<tr data-verdict="{r["verdict"]}"><th scope="row"><a href="{_karne_href(links, r)}">{e(r["Yöntem"])}</a></th>'
        f'<td data-label="Karar"><span class="verdict v-{r["verdict"]}">{VERDICT_LABEL[r["verdict"]]}</span></td>'
        f'<td data-label="Başlangıç maliyeti">{e(r["Başlangıç maliyeti"])}</td>'
        f'<td data-label="İlk gelire kadar">{e(r["İlk gelire kadar"])}</td>'
        f'<td data-label="Türkiye’den">{e(r[TR_KEY])}</td>'
        f'<td data-label="Son kontrol"><time datetime="{e(r["guide"]["checked"])}">'
        f'{e(C.tr_date(r["guide"]["checked"], with_year=True))}</time></td></tr>' for r in rows)
    chips = (f'<button type="button" class="chip" data-v="" aria-pressed="true">Hepsi ({len(rows)})</button>'
             + "".join(f'<button type="button" class="chip" data-v="{v}" aria-pressed="false">{lbl} ({counts[v]})</button>'
                       for v, lbl in VERDICT_LABEL.items() if counts[v]))
    good_html = (f'<section class="msec" id="ise-yarayan"><h2>İşe yarayan yollar</h2>'
                 f'<p class="intro">Kolay değil ama gerçek. "Şartlı" olanlarda şartı okumadan başlama.</p>'
                 f'<ul class="mcards">{"".join(card_good(r) for r in good)}</ul></section>')
    bad_html = (f'<section class="msec" id="uzak-dur"><h2>Bu haliyle işe yaramayanlar</h2>'
                f'<p class="intro">Anlatıldığı haliyle para getirmeyen yöntemler. Nedenini ve aynı emekle ne yapabileceğini yazdım.</p>'
                f'<ul class="mcards">{"".join(card_bad(r) for r in bad)}</ul></section>') if bad else ""
    subject = urllib.parse.quote("Test önerisi")
    return f'''<div class="doc money">
  {note}<p class="crumb"><a href="{e(links.home or "./")}">Ana sayfa</a> <span aria-hidden="true">/</span> Para kazanmak</p>
  <h1>Yapay zekâyla para kazanmak: işe yarayan yollar ve tuzaklar</h1>
  <p class="lede">İnternette "yapay zekâyla şunu yap, şu kadar kazan" diye anlatılan yöntemleri tek tek inceliyorum. Burada gelir vaadi yok. Her yolun maliyeti, ilk paraya kadar geçen süresi ve şartı yazıyor.</p>
  <p class="index-meta">{len(rows)} yöntem incelendi · Son kontrol: {e(C.tr_date(last, with_year=True))}</p>
  <nav class="mjump" aria-label="Bu sayfada"><a href="#ise-yarayan">İşe yarayan yollar ({len(good)})</a>{'<a href="#uzak-dur">Bu haliyle işe yaramayanlar (' + str(len(bad)) + ')</a>' if bad else ''}<a href="#tablo">Bütün kararlar</a><a href="#nasil">Bu sayfa nasıl hazırlanıyor</a></nav>
  {good_html}
  {bad_html}
  <section class="msec" id="tablo"><h2>Bütün kararlar tek tabloda</h2>
    <div class="chips" role="group" aria-label="Karara göre süz">{chips}</div>
    <p class="sr-only" role="status" aria-live="polite" data-mcount></p>
    <div class="mtable-wrap"><table class="mtable"><caption class="sr-only">İncelenen yöntemler ve kararlar</caption>
      <thead><tr><th scope="col">Yöntem</th><th scope="col">Karar</th><th scope="col">Başlangıç maliyeti</th><th scope="col">İlk gelire kadar</th><th scope="col">Türkiye’den</th><th scope="col">Son kontrol</th></tr></thead>
      <tbody>{trs}</tbody></table></div>
  </section>
  <section class="msec" id="nasil"><h2>Bu sayfa nasıl hazırlanıyor</h2>
    <ul class="mrules">
      <li>Her yöntemin karnesi aynı soruları cevaplar: başlangıç maliyeti, ilk gelire kadar süre, gereken beceri, Türkiye'den yapılıp yapılamadığı ve platformun kuralı. Dayandığı kaynaklar rehberinde yazar.</li>
      <li>Kazanç rakamı yazmıyorum. Ne kadar kazanacağın emeğine, becerine ve biraz da şansa bağlı; bunu kimse önceden bilemez.</li>
      <li>Bu sayfada satış ortaklığı (affiliate) bağlantısı yok.</li>
      <li>Bir karnede hata gördüysen ya da yöntemin sahibiysen ve bir bilgiyi düzeltmek istiyorsan bana yaz; kaynağıyla birlikte inceleyip gerekiyorsa karneyi güncellerim.</li>
      <li>Platform kuralları sık değişiyor. Her karnenin son kontrol tarihi yanında; eskiyen karneyi yeniden kontrol ederim.</li>
      <li>Kripto, borsa ve kumar yöntemlerini bu formatta incelemiyorum.</li>
      <li>Gelir başlarsa vergi ve fatura yükümlülüğü doğar. Nasıl yapacağını başlamadan önce bir mali müşavirle konuş.</li>
    </ul>
    <aside class="suggest"><p><b>Test etmemi istediğin bir yöntem var mı?</b> Gördüğün bir "şöyle yap, böyle kazan" videosunu bana yaz, sıradaki karneyi ondan hazırlayayım.</p>
    <a class="btn line" href="mailto:{e(email)}?subject={subject}">Yöntem öner</a></aside>
    <p class="doc-note">Bu sayfa genel bilgilendirme amaçlıdır; yatırım, vergi ya da hukuk danışmanlığı değildir.</p>
  </section>
</div>'''


MONEY_JS = """(function(){
  var chips=document.querySelectorAll('.money .chip'),rows=document.querySelectorAll('.mtable tbody tr'),st=document.querySelector('[data-mcount]');
  if(!chips.length)return;
  [].forEach.call(chips,function(c){c.addEventListener('click',function(){var v=c.getAttribute('data-v'),n=0;
    [].forEach.call(chips,function(x){x.setAttribute('aria-pressed',x===c)});
    [].forEach.call(rows,function(r){var ok=!v||r.getAttribute('data-verdict')===v;r.hidden=!ok;if(ok)n++});
    if(st)st.textContent=n+' yöntem gösteriliyor.'})});
})();"""


def money_home(href: str, n: int) -> str:
    return (f'  <section class="block money-cta"><div class="wrap"><div class="money-box">'
            f'<h2>Yapay zekâyla para kazanmak: hangi yol gerçekten işe yarıyor?</h2>'
            f'<p>Anlatılan {n} yöntemi tek tek inceledim; maliyetini, süresini ve şartını yazdım. Gelir vaadi yok.</p>'
            f'<a class="btn solid" href="{e(href)}">Karneleri gör</a></div></div></section>\n')


def money_json_ld(cfg: dict, rows: list[dict]) -> str:
    base = cfg["site_url"].rstrip("/")
    url = f"{base}/{G.MONEY_PATH}"
    return G._ld([
        {"@context": "https://schema.org", "@type": "WebPage", "url": url, "inLanguage": "tr",
         "name": "Yapay zekâyla para kazanmak: işe yarayan yollar ve tuzaklar",
         "dateModified": max(r["guide"]["checked"] for r in rows), "author": {"@id": base + "/#kisi"}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": base + "/"},
            {"@type": "ListItem", "position": 2, "name": "Para kazanmak", "item": url}]},
    ])



SAFETY_BOX = (
    '<aside class="repo-safety"><b>Kurmadan önce</b><ul>'
    '<li>Depoyu yalnızca resmî GitHub adresinden indir. Adı benzeyen kopyalar zararlı yazılım taşıyabilir.</li>'
    '<li>Yıldız sayısı güvenlik kanıtı değil; çok yıldızlı depolarda da açık çıkabiliyor.</li>'
    '<li>Terminale yapıştıracağın komutun ne yaptığını önce oku.</li>'
    '<li>API anahtarını ve şifreni kimseyle paylaşma, ayar dosyalarını herkese açık bir yere yükleme.</li>'
    '<li>İş bilgisayarına kurmadan önce şirketinin bilgi işleminden izin al.</li></ul></aside>')


def render_repo_index(repos: list[dict], links: Links, email: str) -> str:
    rows = []
    for r in repos:
        text = C.search_fold(" ".join([r["name"], r["repo"], r["summary"], r["category_label"], " ".join(r["audience"]),
                                       r.get("keywords", "")]))
        tested = ' <span class="tested">Mertcan denedi</span>' if r["tested"] else ""
        rows.append(
            f'<li data-type="{e(r["category"])}" data-text="{e(text)}"><a href="{e(links.page("rehber/github/" + r["slug"] + "/"))}">'
            f'<span class="kind">{e(r["category_label"])}{_draft(r)}{tested}</span><h2>{e(r["name"])}</h2><p>{e(r["summary"])}</p>'
            f'<span class="when">{e(R.DIFFICULTY[r["difficulty"]])} · Lisans: {e(r["license"])} · Son kontrol: '
            f'{e(C.tr_date(r["checked"], with_year=True))}</span></a></li>')
    counts = {c: sum(1 for r in repos if r["category"] == c) for c in R.CATEGORIES}
    chips = [f'<button type="button" class="chip" data-type="" aria-pressed="true">Hepsi ({len(repos)})</button>']
    chips += [f'<button type="button" class="chip" data-type="{c}" aria-pressed="false">{e(lbl)} ({counts[c]})</button>'
              for c, lbl in R.CATEGORIES.items() if counts[c]]
    subject = urllib.parse.quote("Depo önerisi")
    return f"""<div class="doc doc-index">
  <p class="crumb"><a href="{e(links.page("rehber/"))}">Rehberler</a> <span aria-hidden="true">/</span> GitHub depoları</p>
  <h1>İşe yarayan GitHub depoları</h1>
  <p class="lede">Kanallarda her gün "bu GitHub deposu hayatını değiştirecek" paylaşımları dönüyor. Burada yalnızca gerçek bir işi çözenleri topluyorum: ne işe yaradığı, kimin işine yaradığı, kurmanın ne kadar zor olduğu ve lisansının neye izin verdiği.</p>
  <p class="index-meta">{len(repos)} depo · Lisans ve son güncelleme bilgisi düzenli olarak GitHub'dan kontrol edilir</p>
  <details class="repo-how"><summary>Depoları nasıl seçiyorum</summary><ul>
    <li>Bakımı sürüyor: GitHub'da arşivlenmiş depoyu listeye almıyorum.</li>
    <li>Lisansı açık: lisansı olmayan depoyu önermiyorum, çünkü lisans yoksa kullanım hakkı da yok. Açık kaynak sayılmayan lisansları ayrıca işaretliyorum.</li>
    <li>Gerçek bir işi çözüyor ve kurulumu belgelenmiş.</li>
    <li>Kendim kurup denediklerimde "Mertcan denedi" yazar; yazmayanlarda bilgiler deponun kendi belgelerinden.</li>
  </ul></details>
  <div class="guide-tools"><div class="chips" role="group" aria-label="Kategori">{"".join(chips)}</div>
  <label class="search"><span class="sr-only">Depolarda ara</span><input type="search" placeholder="Depolarda ara" autocomplete="off"></label></div>
  <ul class="guide-list">{"".join(rows) or '<li><p class="empty">İlk depolar yakında burada.</p></li>'}</ul>
  <p class="empty" data-empty hidden>Bu aramaya uyan depo yok. Başka bir kelime dene.</p>
  <aside class="suggest"><p><b>Denememi istediğin bir depo var mı?</b> Bir videoda gördüğün depoyu bana yaz, işe yarıyor mu bakayım.</p>
  <a class="btn line" href="mailto:{e(email)}?subject={subject}">Depo öner</a></aside>
</div>"""


def render_repo_page(r: dict, links: Links, email: str) -> str:
    facts = [("Depo", f'<a href="https://github.com/{e(r["repo"])}" rel="noopener">github.com/{e(r["repo"])}</a>'),
             ("Ne işe yarar", e(r["category_label"])),
             ("Kurulum", e(R.DIFFICULTY[r["difficulty"]])),
             ("Maliyet", e(r["cost"])),
             ("Lisans", e(R.license_text(r)) + (f'<br><span class="lic-note">{e(r["license_note"])}</span>' if r.get("license_note") else "")),
             ("Yıldız", f'{e(r["stars"])} <span class="muted">({e(C.tr_date(r["checked"], with_year=True))} itibarıyla)</span>')]
    if r["audience"]:
        facts.insert(2, ("Kimin için", e(", ".join(r["audience"]))))
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)
    tested = '<span class="checked">Mertcan denedi</span>' if r["tested"] else '<span class="checked">belgelerinden derlendi</span>'
    draft_bar = '<p class="draft-bar">Taslak: Onayından sonra yayınlanır. Canlı sitede şu an görünmez.</p>' if r.get("draft") else ""
    subj = urllib.parse.quote(f'Depo sayfası hatası: {r["name"]}')
    return f"""<article class="guide repo">
  <header class="guide-head">
    {draft_bar}<p class="crumb"><a href="{e(links.page("rehber/"))}">Rehberler</a> <span aria-hidden="true">/</span> <a href="{e(links.page("rehber/github/"))}">GitHub depoları</a></p>
    <h1>{e(r["name"])}</h1>
    <p class="lede">{e(r["summary"])}</p>
    <div class="doc-meta">{tested}<span>Son kontrol: <time datetime="{e(r["checked"])}">{e(C.tr_date(r["checked"], with_year=True))}</time></span></div>
    <dl class="facts repo-facts">{dl}</dl>
  </header>
  <div class="guide-body"><div class="prose">{r["html"]}{SAFETY_BOX}</div></div>
  <footer class="guide-end">
    <p class="doc-note">Bu sayfa bilgilendirme amaçlıdır; depo ve içindeki yazılım sahiplerine aittir, benimle bir ticari bağı yoktur. Bir hata gördüysen <a href="mailto:{e(email)}?subject={subj}">bana yaz</a>, düzelteyim.</p>
    <p class="money-link"><a href="{e(links.page("rehber/github/"))}">Bütün depolara dön</a></p>
  </footer>
</article>"""


# ---------- sayfa iskeleti ----------

def page(layout: str, cfg: dict, links: Links, *, title: str, description: str, path: str, main: str,
         scripts: str = "", banner: str = "", og_type: str = "website", has_feed: bool = False,
         on_guides: bool = False, og_image: str = "site", head_extra: str = "") -> str:
    base = cfg["site_url"].rstrip("/")
    head_extra = (f'<meta property="og:image" content="{e(base)}/og/{e(og_image)}.png">\n'
                  '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
                  f'<meta property="og:image:alt" content="{e(title)}">\n'
                  '<meta name="twitter:card" content="summary_large_image">\n'
                  f'<link rel="alternate" type="application/atom+xml" title="Rehberler" href="{e(base)}/rehber/feed.xml">'
                  + ("\n" + head_extra if head_extra else ""))
    yt = cfg["platforms"]["youtube"]["profile_url"]
    social = "".join(f'<a href="{e(cfg["platforms"][n]["profile_url"])}" rel="me">{LABELS[n]}</a> &nbsp;|&nbsp; '
                     for n in PLATFORM_ORDER if (cfg["platforms"].get(n) or {}).get("profile_url"))
    nav_feed = f'      <a href="{links.home}#videolar">Videolar</a>\n' if has_feed else ""
    out = layout
    rep = {
        "{{main}}": main, "{{title}}": e(title), "{{description}}": e(description),
        "{{canonical}}": e(cfg["site_url"].rstrip("/") + "/" + path), "{{og_type}}": og_type,
        "{{root}}": links.root, "{{home}}": links.home, "{{guides_href}}": e(links.page("rehber/")),
        "{{guides_current}}": ' aria-current="page"' if on_guides else "", "{{nav_feed}}": nav_feed,
        "{{youtube_url}}": e(yt), "{{social}}": social, "{{email}}": e(cfg["contact_email"]),
        "{{year}}": str(datetime.now(C.TZ).year), "{{scripts}}": scripts, "{{banner}}": banner,
        "{{follow}}": render_follow(cfg), "{{nav_js}}": NAV_JS, "{{head_extra}}": head_extra,
    }
    for k, v in rep.items():
        out = out.replace(k, v)
    if "{{" in out:
        raise ValueError("Doldurulmamış şablon alanı kaldı: " + re.findall(r"\{\{\w+\}\}", out)[0])
    return out


def build(preview: bool = False, demo: bool = False, out_dir: Path = DIST) -> Path:
    cfg = C.load_config()
    content_path = C.CONTENT_FILE
    media_dir = C.MEDIA_DIR
    banner = ""
    if demo:
        cfg = json.loads(json.dumps(cfg))
        for n in ("instagram", "tiktok"):
            cfg["platforms"][n]["profile_url"] = cfg["platforms"][n]["profile_url"] or f"https://www.{n}.com/"
        cfg["archor"] = {"show": True, "url": None}
        content_path = FIXTURES / "demo_content.json"
        media_dir = FIXTURES / "demo_media"
        banner = ('<div class="preview-bar">Önizleme: Videolar ve Instagram/TikTok bağlantıları örnektir. '
                  'Archor cümleleri canlı sitede ayarla açılır.</div>\n')
    content = json.loads(content_path.read_text(encoding="utf-8")) if content_path.exists() else {"platforms": {}}
    all_guides, warnings = G.load(cfg, include_drafts=True)
    guides = [g for g in all_guides if preview or not g["draft"]]
    unpublished = {g["slug"] for g in all_guides if g not in guides}
    for w in warnings:
        print("UYARI:", w, file=sys.stderr)
    slugs = {g["slug"] for g in guides if not g.get("draft")}
    layout = (SRC / "layout.html").read_text(encoding="utf-8")

    # para kazanma sayfası: karneler rehberlerden toplanır; yeterli karne yoksa sayfa hiç üretilmez
    money_rows = collect_karnes(guides)
    money_demo = False
    if demo and not money_page_ready(money_rows, cfg.get("money_page_min", 3)):
        demo_guide = {"slug": "yapay-zeka-yan-is-gercekleri", "toc": [], "checked": datetime.now(C.TZ).date().isoformat(),
                      "draft": False, "stage": "hazir"}
        demo_karnes = json.loads((FIXTURES / "demo_karneler.json").read_text(encoding="utf-8"))
        money_rows = collect_karnes([{**demo_guide, "karnes": [dict(G.parse_karne(t), anchor="") for t in demo_karnes]}])
        money_demo = True
    has_money = money_page_ready(money_rows, cfg.get("money_page_min", 3))
    job_data = M.load()
    has_job = M.ready(job_data, guides)
    job_guides = {r.partition("#")[0] for _, r in M.refs(job_data)} if has_job else set()
    all_repos, repo_warn = R.load(include_drafts=True)
    for w in repo_warn:
        print("UYARI:", w, file=sys.stderr)
    repos = [r for r in all_repos if preview or not r["draft"]]
    has_repos = bool(repos)

    if out_dir.exists():
        shutil.rmtree(out_dir)
    (out_dir / "fonts").mkdir(parents=True)
    shutil.copy(SRC / "site.css", out_dir / "site.css")
    for f in (C.ROOT / "fonts").glob("*.woff2"):
        shutil.copy(f, out_dir / "fonts" / f.name)
    used = {i.get("thumb") for p in content.get("platforms", {}).values() for i in p.get("items", []) if i.get("thumb")}
    if used:
        (out_dir / "media").mkdir()
        for name in used:
            if (media_dir / name).exists():
                shutil.copy(media_dir / name, out_dir / "media" / name)

    # ana sayfa
    L0 = Links(0, preview)
    feed = render_feed(content, cfg, L0, slugs)
    main = (SRC / "home.html").read_text(encoding="utf-8")
    main = main.replace("{{feed}}", feed).replace("{{guides_home}}", render_guides_home(guides, L0))
    main = main.replace("{{youtube_url}}", e(cfg["platforms"]["youtube"]["profile_url"]))
    main = main.replace("{{guides_href}}", e(L0.page("rehber/")))
    archor_collab, archor_about = render_archor(cfg)
    main = main.replace("{{archor_collab}}", archor_collab).replace("{{archor_about}}", archor_about)
    main = main.replace("{{email}}", e(cfg["contact_email"]))
    main = main.replace("{{money_home}}", (M.home_cta(L0.page(M.JOB_PATH), len(M.available(job_data, guides)))
                                           if has_job else "")
                        + (money_home(L0.page(G.MONEY_PATH), len(money_rows)) if has_money else ""))
    scripts = "<script>\n" + (SRC / "bench.js").read_text(encoding="utf-8") + (TABS_JS if feed else "") + "\n</script>"
    (out_dir / "index.html").write_text(page(
        layout, cfg, L0, title="Mertcan Turan · Yapay zekâyı gerçekten test ediyorum",
        description="Yapay zekâ araçlarını gerçek işlerde deniyorum: hangisi işini kolaylaştırıyor, hangisiyle kendi işini kurabilirsin, hangisi sadece reklam.",
        path="", main=main, scripts=scripts, banner=banner, has_feed=bool(feed),
        head_extra=G.site_json_ld(cfg)), encoding="utf-8")

    # rehberler
    email = cfg["contact_email"]
    by_url = {i["url"]: i for p in content.get("platforms", {}).values() for i in p.get("items", [])}
    guide_js = "<script>\n" + GUIDE_JS + "\n</script>"
    L1 = Links(1, preview)
    (out_dir / "rehber").mkdir()
    (out_dir / "rehber" / "index.html").write_text(page(
        layout, cfg, L1, title="Rehberler · Mertcan Turan",
        description="Videolarda bahsettiğim kontrol listeleri, komut şablonları ve adım adım rehberler. Ücretsiz, kayıt istemez.",
        path="rehber/", main=render_guide_index(guides, L1, email, cfg.get("guides_filter_min", 4),
                                                tpl_count=sum(len(g["templates"]) for g in guides),
                                                money_href=L1.page(G.MONEY_PATH) if has_money else None,
                                                repo_href=L1.page("rehber/github/") if has_repos else None,
                                                repo_count=len(repos),
                                                job_href=L1.page(M.JOB_PATH) if has_job else None),
        scripts=guide_js, banner=banner, has_feed=bool(feed), on_guides=True, og_image="rehberler",
        head_extra=G.index_json_ld(cfg, "Rehberler", "rehber/")), encoding="utf-8")
    has_tpl_page = any(g["templates"] for g in guides)
    if has_tpl_page:
        (out_dir / "rehber" / "sablonlar").mkdir()
        (out_dir / "rehber" / "sablonlar" / "index.html").write_text(page(
            layout, cfg, Links(2, preview), title="Komut şablonları · Mertcan Turan",
            description="Rehberlerdeki bütün yapay zekâ komut şablonları bir arada: doldur, kopyala, yapıştır. Ücretsiz, kayıt istemez.",
            path="rehber/sablonlar/", main=render_templates_page(guides, Links(2, preview)), scripts=guide_js,
            banner=banner, has_feed=bool(feed), on_guides=True, og_image="rehberler",
            head_extra=G.index_json_ld(cfg, "Komut şablonları", "rehber/sablonlar/")), encoding="utf-8")
    (out_dir / "rehber" / "feed.xml").write_text(G.atom_feed([g for g in guides if not g.get("draft")], cfg),
                                                 encoding="utf-8")
    L2 = Links(2, preview)
    for g in guides:
        d = out_dir / "rehber" / g["slug"]
        d.mkdir()
        others = [o for o in guides if o["slug"] != g["slug"] and not o.get("draft")]
        links_out = set(re.findall(r'href="rehber:([a-z0-9-]+)', g["html"]))
        others.sort(key=lambda o: o["published"], reverse=True)
        others.sort(key=lambda o: o["type"] != g["type"])  # aynı türdekiler önce
        # birbirine bağlantı veren rehberler en önce (konu yakınlığı)
        others.sort(key=lambda o: not (o["slug"] in links_out or f'href="rehber:{g["slug"]}' in o["html"]))
        body = render_guide_page(g, L2, email, others[:3], by_url.get(g.get("video", "")),
                                 L2.page(G.MONEY_PATH) if has_money else None,
                                 cfg["platforms"]["youtube"].get("profile_url"),
                                 L2.page(M.JOB_PATH) if has_job and g["slug"] in job_guides else None)
        body = resolve_internal(body, L2, {o["slug"]: {sid for sid, _ in o["toc"]} for o in all_guides},
                                g["slug"] + ".md", unpublished)
        robots = '<meta name="robots" content="noindex">' if g.get("draft") else ""
        (d / "index.html").write_text(page(
            layout, cfg, L2, title=guide_title_tag(g), description=g.get("description") or g["summary"],
            path=f'rehber/{g["slug"]}/', main=body, scripts=guide_js, banner=banner, og_type="article",
            has_feed=bool(feed), on_guides=True, og_image=g["slug"],
            head_extra=G.json_ld(g, cfg) + robots), encoding="utf-8")

    if has_repos:
        L2r, L3 = Links(2, preview), Links(3, preview)
        (out_dir / "rehber" / "github").mkdir()
        (out_dir / "rehber" / "github" / "index.html").write_text(page(
            layout, cfg, L2r, title="İşe yarayan GitHub depoları · Mertcan Turan",
            description="Yapay zekâ ve verimlilik için gerçekten işe yarayan GitHub depoları: ne işe yaradığı, kurulum zorluğu, lisansı ve son kontrol tarihi.",
            path="rehber/github/", main=render_repo_index(repos, L2r, email), scripts=guide_js, banner=banner,
            has_feed=bool(feed), on_guides=True, og_image="github",
            head_extra=G.index_json_ld(cfg, "GitHub depoları", "rehber/github/")), encoding="utf-8")
        for r in repos:
            d = out_dir / "rehber" / "github" / r["slug"]
            d.mkdir()
            robots = '<meta name="robots" content="noindex">' if r["draft"] else ""
            (d / "index.html").write_text(page(
                layout, cfg, L3, title=f'{r["name"]}: ne işe yarar, nasıl kurulur · Mertcan Turan', description=r["summary"],
                path=f'rehber/github/{r["slug"]}/', main=render_repo_page(r, L3, email), scripts=guide_js, banner=banner,
                og_type="article", has_feed=bool(feed), on_guides=True, og_image="github",
                head_extra=R.json_ld(r, cfg) + robots), encoding="utf-8")

    if has_money:
        L1m = Links(1, preview)
        (out_dir / G.MONEY_PATH).mkdir(parents=True)
        (out_dir / G.MONEY_PATH / "index.html").write_text(page(
            layout, cfg, L1m, title="Yapay zekâyla para kazanmak: işe yarayan yollar ve tuzaklar · Mertcan Turan",
            description="Yapay zekâyla para kazanma yöntemleri tek tek: maliyeti, ilk gelire kadar süresi, "
                        "Türkiye'den yapılabilir mi. Gelir vaadi yok.",
            path=G.MONEY_PATH, main=render_money_page(money_rows, L1m, email, money_demo),
            scripts="<script>\n" + MONEY_JS + "\n</script>", banner=banner, has_feed=bool(feed),
            og_image="para-kazanmak", head_extra=money_json_ld(cfg, money_rows)), encoding="utf-8")

    if has_job:
        Lj = Links(1, preview)
        known = {o["slug"]: {sid for sid, _ in o["toc"]} for o in all_guides}
        body = resolve_internal(M.render(job_data, guides, Lj, email), Lj, known, "data/meslekler.json", unpublished)
        (out_dir / M.JOB_PATH).mkdir(parents=True)
        (out_dir / M.JOB_PATH / "index.html").write_text(page(
            layout, cfg, Lj, title="Mesleğine göre yapay zekâ: kendi planını çıkar · Mertcan Turan",
            description="Avukat, muhasebeci, öğretmen, emlakçı, esnaf ve yazılımcı için: işine göre hangi yapay zekâ "
                        "aracını nasıl kullanacağın, hazır komutlar ve kurallar.",
            path=M.JOB_PATH, main=body,
            scripts=guide_js + "\n<script>\n" + M.JS + "\n</script>", banner=banner, has_feed=bool(feed),
            on_guides=True, og_image="meslek", head_extra=M.json_ld(cfg, M.available(job_data, guides))), encoding="utf-8")

    # simge, 404 ve yapay zekâ aramaları için özet
    write_short_links(out_dir, cfg, {g["slug"] for g in guides if not g.get("draft")}, has_job)
    (out_dir / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    G.apple_touch_icon(out_dir / "apple-touch-icon.png")
    L404 = Links(0, False)
    L404.root = "/"
    (out_dir / "404.html").write_text(page(
        layout, cfg, L404, title="Sayfa bulunamadı · Mertcan Turan", description="Aradığın sayfa bulunamadı.",
        path="404.html", main=NOT_FOUND, banner=banner,
        head_extra='<meta name="robots" content="noindex">'), encoding="utf-8")
    (out_dir / "llms.txt").write_text(G.llms_txt([g for g in guides if not g.get("draft")], cfg, has_money,
                                                 job=has_job), encoding="utf-8")
    (out_dir / "llms-full.txt").write_text(G.llms_full([g for g in guides if not g.get("draft")], cfg), encoding="utf-8")

    # paylaşım görselleri
    og = out_dir / "og"
    G.og_image(og / "site.png", "Yapay zekâ her şeyi emin bir sesle söylüyor. Ben kontrol ediyorum.",
               "Yapay zekâyı gerçek işlerde deniyorum", "abartısız")
    G.og_image(og / "rehberler.png", "Videoda anlatırım, rehberini burada bırakırım.", "Rehberler", "ücretsiz, kayıt yok")
    if has_repos:
        G.og_image(og / "github.png", "İşe yarayan GitHub depoları", "Rehberler", "lisansı ve kurulumuyla")
    if has_job:
        G.og_image(og / "meslek.png", "Mesleğine göre yapay zekâ: kendi planını çıkar", "Araç", "beş soru, hazır komutlar")
    if has_money:
        G.og_image(og / "para-kazanmak.png", "Yapay zekâyla para kazanmak: işe yarayan yollar ve tuzaklar",
                   "Gerçekten kazandırır mı?", "gelir vaadi yok")
    for g in guides:
        G.og_image(og / f'{g["slug"]}.png', g["title"], g["type_label"],
                   "son kontrol " + C.tr_date(g["checked"], with_year=True))

    # arama motorları ve alan adı (yalnız canlı)
    if not preview:
        base = cfg["site_url"].rstrip("/")
        urls = [(base + "/", None), (base + "/rehber/", None)] + (
            [(base + "/rehber/sablonlar/", None)] if has_tpl_page else []) + (
            [(base + "/" + G.MONEY_PATH, max(r["guide"]["checked"] for r in money_rows))] if has_money else []) + (
            [(base + "/" + M.JOB_PATH, None)] if has_job else []) + (
            [(base + "/rehber/github/", None)] + [(f'{base}/rehber/github/{r["slug"]}/', r["checked"]) for r in repos]
            if has_repos else []) + [
            (f'{base}/rehber/{g["slug"]}/', g["checked"]) for g in guides if not g.get("draft")]
        sm = "".join(f"<url><loc>{e(u)}</loc>" + (f"<lastmod>{m}</lastmod>" if m else "") + "</url>" for u, m in urls)
        (out_dir / "sitemap.xml").write_text(
            f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n',
            encoding="utf-8")
        (out_dir / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n", encoding="utf-8")
        if cfg.get("custom_domain"):
            (out_dir / "CNAME").write_text(cfg["custom_domain"] + "\n", encoding="utf-8")
    return out_dir


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--preview", action="store_true", help="bağlantıları index.html ile bitir")
    ap.add_argument("--demo", action="store_true", help="örnek video verisiyle önizleme (yayına çıkmaz)")
    ap.add_argument("--out", default=str(DIST))
    a = ap.parse_args()
    if a.demo and not a.preview:
        ap.error("--demo yalnızca --preview ile kullanılabilir; örnek veri canlı siteye çıkmamalı.")
    out = build(preview=a.preview, demo=a.demo, out_dir=Path(a.out))
    print("Site üretildi:", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
