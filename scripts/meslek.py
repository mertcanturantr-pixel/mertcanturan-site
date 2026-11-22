"""Mesleğine göre yapay zekâ aracı: data/meslekler.json'dan tek sayfa üretir.

Sayfa JavaScript olmadan da okunur: bütün meslekler, işler ve komutlar düz HTML'dir (arama motorları ve
yapay zekâ aramaları için). JavaScript yalnızca soruları gösterir ve seçilen mesleğin bölümünü plana çevirir.
Hiçbir seçim kaydedilmez, hiçbir yere gönderilmez; sayfada ağ isteği yapan kod yoktur.
"""
from __future__ import annotations

import json
from html import escape as e
from pathlib import Path

import common as C
import guides as G

DATA_FILE = C.ROOT / "data" / "meslekler.json"
JOB_PATH = "meslegine-gore-yapay-zeka/"
MIN_TASKS = 3          # bir meslek en az bu kadar yayındaki rehbere bağlı işle görünür
MIN_JOBS = 4           # sayfa en az bu kadar meslekle üretilir
MAX_PICK = 3


def load(path: Path | None = None) -> dict | None:
    p = path or DATA_FILE
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def refs(data: dict) -> list[tuple[str, str]]:
    """(kaynak, rehber:hedef) çiftleri; testler hepsinin var olduğunu kontrol eder."""
    out = []
    for m in data["meslekler"]:
        out += [(f'{m["slug"]}/{t["id"]}', t["rehber"]) for t in m["isler"]]
    for k, v in data["deneyim"].items():
        out += [(f"deneyim/{k}", a["rehber"]) for a in v["adimlar"]]
    for grp in ("veri", "butce"):
        out += [(f"{grp}/{k}", v["rehber"]) for k, v in data[grp].items()]
    return out


def available(data: dict, guides: list[dict]) -> list[dict]:
    """Yalnızca bu derlemede yayında olan rehberlere bağlı işleri bırakır; az işi kalan mesleği düşürür."""
    have = {g["slug"]: {sid for sid, _ in g["toc"]} for g in guides}
    jobs = []
    for m in data["meslekler"]:
        tasks = []
        for t in m["isler"]:
            slug, _, anchor = t["rehber"].partition("#")
            if slug in have:
                tasks.append(dict(t, rehber=slug + ("#" + anchor if anchor in have[slug] else "")))
        if len(tasks) >= MIN_TASKS:
            jobs.append(dict(m, isler=tasks))
    return jobs


def ready(data: dict | None, guides: list[dict]) -> bool:
    return bool(data) and len(available(data, guides)) >= MIN_JOBS


def _link(target: str, text: str, have: set[str]) -> str:
    slug = target.partition("#")[0]
    if slug not in have:
        return e(text)
    return f'<a href="rehber:{e(target)}">{e(text)}</a>'


def render(data: dict, guides: list[dict], links, email: str) -> str:
    jobs = available(data, guides)
    titles = {g["slug"]: g["title"] for g in guides}
    have = set(titles)
    n = 1000  # şablon kimlikleri rehber sayfalarıyla çakışmasın

    def opt(name: str, value: str, label: str, typ: str = "radio", extra: str = "") -> str:
        return (f'<label class="jt-opt"><input type="{typ}" name="{name}" value="{e(value)}"{extra}>'
                f'<span>{e(label)}</span></label>')

    job_opts = "".join(opt("meslek", m["slug"], m["ad"], extra=f' data-veri="{e(m["veri"])}"') for m in jobs)
    exp_opts = "".join(opt("deneyim", k, v["ad"]) for k, v in data["deneyim"].items())
    data_opts = "".join(opt("veri", k, v["ad"]) for k, v in data["veri"].items())
    budget_opts = "".join(opt("butce", k, v["ad"]) for k, v in data["butce"].items())

    sections = []
    for m in jobs:
        tasks = []
        for t in m["isler"]:
            slug = t["rehber"].partition("#")[0]
            tpl = G._template_block(e(t["komut"]), n)
            n += 1
            tasks.append(
                f'<li class="jtask" data-task="{e(t["id"])}"><h4>{e(t["ad"])}</h4><p>{e(t["nasil"])}</p>'
                f'<p class="jtool"><b>Araç:</b> {e(t["arac"])}</p>{tpl}'
                f'<p class="tpl-src">Ayrıntısı rehberde: {_link(t["rehber"], titles.get(slug, slug), have)}</p></li>')
        reds = "".join(f"<li>{e(x)}</li>" for x in m["kirmizi"])
        sections.append(
            f'<section class="job-sec" id="{e(m["slug"])}" data-job="{e(m["slug"])}">'
            f'<h3>{e(m["baslik"])}</h3><p class="job-sum">{e(m["ozet"])}</p>'
            f'<div class="job-red"><p class="mlabel">Başlamadan önce üç kural</p><ul>{reds}</ul></div>'
            f'<p class="mlabel job-tasks-label">İşler ve hazır komutlar</p>'
            f'<ul class="job-tasks">{"".join(tasks)}</ul>'
            f'<button type="button" class="chip jt-more" hidden>Bu meslekteki diğer işleri de göster</button>'
            f'</section>')

    def block(key: str, title: str, inner: str) -> str:
        return f'<template data-blk="{e(key)}"><div class="jt-blk"><h3>{e(title)}</h3>{inner}</div></template>'

    def guide_ref(target: str) -> str:
        # bağlantı metni rehberin adı: ekran okuyucuda "Rehbere git" gibi aynı metinli bağlantılar oluşmasın
        slug = target.partition("#")[0]
        if slug not in have:
            return ""
        return f'<span class="jt-ref">Rehber: {_link(target, titles[slug], have)}</span>'

    blocks = []
    for k, v in data["deneyim"].items():
        steps = "".join(f'<li>{e(a["metin"])} {guide_ref(a["rehber"])}</li>' for a in v["adimlar"])
        blocks.append(block(f"deneyim-{k}", "İlk iki hafta", f'<ol class="msteps">{steps}</ol>'))
    for k, v in data["veri"].items():
        blocks.append(block(f"veri-{k}", "Bilgilerin için kural", f'<p>{e(v["metin"])} {guide_ref(v["rehber"])}</p>'))
    for k, v in data["butce"].items():
        blocks.append(block(f"butce-{k}", "Bütçe", f'<p>{e(v["metin"])} {guide_ref(v["rehber"])}</p>'))

    jump = "".join(f'<a href="#{e(m["slug"])}">{e(m["ad"])}</a>' for m in jobs)
    subject = "Meslek%20%C3%B6nerisi"
    return f'''<div class="doc job">
  <p class="crumb"><a href="{e(links.page("rehber/"))}">Rehberler</a> <span aria-hidden="true">/</span> Mesleğine göre yapay zekâ</p>
  <h1>Mesleğine göre yapay zekâ: kendi planını çıkar</h1>
  <p class="lede">Mesleğini ve en çok vaktini alan işleri seç; hangi işte hangi aracı nasıl kullanacağını, hazır komutunu ve dikkat etmen gereken kuralları tek sayfada gör.</p>
  <p class="index-meta">{len(jobs)} meslek · 5 soru · Seçimlerin bu sayfada kalır; hiçbir yere gönderilmez, kaydedilmez.</p>
  <form class="jt" data-jt hidden novalidate>
    <fieldset class="jt-step"><legend>1. Mesleğin ne?</legend><div class="jt-opts">{job_opts}</div></fieldset>
    <fieldset class="jt-step" data-need="meslek" hidden><legend>2. En çok vaktini alan işler hangileri? <span>En fazla {MAX_PICK} iş seçebilirsin.</span></legend>
      <div class="jt-opts" data-tasks></div><p class="jt-hint" data-pickhint aria-live="polite"></p></fieldset>
    <fieldset class="jt-step" data-need="meslek" hidden><legend>3. Yapay zekâyı ne kadar kullanıyorsun?</legend><div class="jt-opts">{exp_opts}</div></fieldset>
    <fieldset class="jt-step" data-need="meslek" hidden><legend>4. İşinde çoğunlukla hangi bilgilerle çalışıyorsun?</legend><div class="jt-opts">{data_opts}</div>
      <p class="jt-hint" data-verihint></p></fieldset>
    <fieldset class="jt-step" data-need="meslek" hidden><legend>5. Yapay zekâ için bütçen ne?</legend><div class="jt-opts">{budget_opts}</div></fieldset>
    <p class="jt-err" data-err role="alert"></p>
    <div class="jt-actions" data-need="meslek" hidden><button type="submit" class="btn solid">Planımı göster</button></div>
  </form>
  <section class="jt-result" data-result hidden tabindex="-1" aria-labelledby="plan-baslik">
    <h2 id="plan-baslik" data-plantitle>Planın</h2>
    <div data-plan></div>
    <p class="jt-next">Mesleğinin kuralları ve seçtiğin işlerin hazır komutları bu kutunun hemen altında.</p>
    <div class="jt-actions"><button type="button" class="btn line" data-copyplan>Planı metin olarak kopyala</button>
      <button type="button" class="btn line" data-printplan>Planı yazdır</button>
      <button type="button" class="btn line" data-restart>Baştan başla</button>
      <span class="tpl-status" data-planstatus aria-live="polite"></span></div>
  </section>
  <section class="jobs" aria-labelledby="meslekler"><h2 id="meslekler" data-alljobs>Meslek meslek işler, hazır komutlar ve kurallar</h2>
    <nav class="mjump" aria-label="Meslekler">{jump}</nav>
    {"".join(sections)}
  </section>
  {"".join(blocks)}
  <aside class="suggest"><p><b>Mesleğin listede yok mu?</b> Bana yaz; en çok istenen meslekler için işleri ve komutları ekleyeyim.</p>
  <a class="btn line" href="mailto:{e(email)}?subject={subject}">Meslek öner</a></aside>
  <p class="doc-note">Bu sayfa genel bilgilendirme amaçlıdır; hukuki ya da mali danışmanlık değildir. Araç adları örnektir; sayfada satış ortaklığı (affiliate) bağlantısı yok. Araçların özellikleri ve fiyatları sık değişiyor, bağlantı verilen rehberlerde son kontrol tarihi yazar.</p>
</div>'''


JS = """(function(){
  var f=document.querySelector('[data-jt]');if(!f)return;
  f.hidden=false;
  var res=document.querySelector('[data-result]'),plan=res.querySelector('[data-plan]'),secs=document.querySelectorAll('.job-sec'),
      all=document.querySelector('.jobs'),err=f.querySelector('[data-err]'),MAX=%(max)d;
  function val(n){var x=f.querySelector('input[name='+n+']:checked');return x?x.value:''}
  function sec(slug){return document.getElementById(slug)}
  function tasksOf(slug){return sec(slug).querySelectorAll('.jtask')}
  function fillTasks(slug){var box=f.querySelector('[data-tasks]');box.innerHTML='';
    [].forEach.call(tasksOf(slug),function(li){var l=document.createElement('label');l.className='jt-opt';
      var i=document.createElement('input');i.type='checkbox';i.name='is';i.value=li.getAttribute('data-task');
      var s=document.createElement('span');s.textContent=li.querySelector('h4').textContent;l.appendChild(i);l.appendChild(s);box.appendChild(l)})}
  function limit(){var boxes=f.querySelectorAll('input[name=is]'),n=f.querySelectorAll('input[name=is]:checked').length;
    [].forEach.call(boxes,function(b){b.disabled=!b.checked&&n>=MAX});
    f.querySelector('[data-pickhint]').textContent=n>=MAX?'En fazla '+MAX+' iş seçebilirsin; değiştirmek için birini kaldır.':''}
  f.addEventListener('change',function(ev){var t=ev.target;
    if(t.name==='meslek'){fillTasks(t.value);[].forEach.call(f.querySelectorAll('[data-need]'),function(x){x.hidden=false});
      var v=t.getAttribute('data-veri'),r=f.querySelector('input[name=veri][value='+v+']');if(r&&!val('veri'))r.checked=true;
      f.querySelector('[data-verihint]').textContent=r?'Bu meslek için çoğu zaman uygun olan seçili; senin durumun farklıysa değiştir.':'';limit()}
    if(t.name==='is')limit();err.textContent=''});
  function first(n){var x=f.querySelector('input[name='+n+']:not(:disabled)');if(x)x.focus()}
  function clone(key){var t=document.querySelector('template[data-blk="'+key+'"]');return t?t.content.cloneNode(true):document.createDocumentFragment()}
  function show(slug,picked){[].forEach.call(secs,function(s){s.hidden=s.id!==slug});
    var s=sec(slug),more=s.querySelector('.jt-more');
    [].forEach.call(tasksOf(slug),function(li){li.hidden=picked.length&&picked.indexOf(li.getAttribute('data-task'))<0});
    more.hidden=!picked.length||picked.length===tasksOf(slug).length;
    all.querySelector('[data-alljobs]').hidden=true;all.querySelector('.mjump').hidden=true}
  function reset(){[].forEach.call(secs,function(s){s.hidden=false;[].forEach.call(s.querySelectorAll('.jtask'),function(li){li.hidden=false});
    s.querySelector('.jt-more').hidden=true});all.querySelector('[data-alljobs]').hidden=false;all.querySelector('.mjump').hidden=false}
  [].forEach.call(document.querySelectorAll('.jt-more'),function(b){b.addEventListener('click',function(){
    var shown=b.parentNode.querySelectorAll('.jtask[hidden]');
    [].forEach.call(shown,function(li){li.hidden=false});b.hidden=true;
    if(shown.length){var h=shown[0].querySelector('h4');h.tabIndex=-1;h.focus()}})});
  f.addEventListener('submit',function(ev){ev.preventDefault();
    var m=val('meslek'),d=val('deneyim'),v=val('veri'),b=val('butce');
    var picked=[].map.call(f.querySelectorAll('input[name=is]:checked'),function(x){return x.value});
    var miss=[],at='';function need(ok,label,n){if(!ok){miss.push(label);if(!at)at=n}}
    need(m,'meslek','meslek');need(picked.length,'en az bir iş','is');need(d,'yapay zekâyı ne kadar kullandığın','deneyim');
    need(v,'çalıştığın bilgi türü','veri');need(b,'bütçe','butce');
    if(miss.length){err.textContent='Planı çıkarmak için şunları da seç: '+miss.join(', ')+'.';first(at);return}
    plan.innerHTML='';plan.appendChild(clone('veri-'+v));plan.appendChild(clone('deneyim-'+d));plan.appendChild(clone('butce-'+b));
    var name=f.querySelector('input[name=meslek]:checked').nextSibling.textContent;
    res.querySelector('[data-plantitle]').textContent=name+' için yapay zekâ planın';
    show(m,picked);f.hidden=true;res.hidden=false;res.focus();res.scrollIntoView({block:'start'})});
  function line(el){var c=el.cloneNode(true),u=[];[].forEach.call(c.querySelectorAll('a'),function(a){u.push(a.href);a.parentNode.removeChild(a)});
    return c.textContent.replace(/\\s+/g,' ').trim()+(u.length?' '+u.join(' '):'')}
  function txt(){var out=[res.querySelector('[data-plantitle]').textContent,''];
    [].forEach.call(plan.querySelectorAll('.jt-blk'),function(b){out.push(b.querySelector('h3').textContent);
      [].forEach.call(b.querySelectorAll('p,li'),function(p){out.push('- '+line(p))});out.push('')});
    var s=document.querySelector('.job-sec:not([hidden])');
    [].forEach.call(s.querySelectorAll('.job-red li'),function(li){out.push('Kural: '+li.textContent)});out.push('');
    [].forEach.call(s.querySelectorAll('.jtask:not([hidden])'),function(li){out.push(li.querySelector('h4').textContent);
      out.push(li.querySelector('p').textContent);out.push('Komut: '+li.querySelector('code').textContent);
      var a=li.querySelector('.tpl-src a');if(a)out.push('Rehber: '+a.href);out.push('')});
    out.push(location.href.split('#')[0]);return out.join('\\n')}
  var st=res.querySelector('[data-planstatus]');
  res.querySelector('[data-copyplan]').addEventListener('click',function(){var t=txt();
    function done(ok){st.textContent=ok?'Plan kopyalandı.':'Kopyalanamadı; sayfayı yazdırabilirsin.'}
    if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(function(){done(true)},function(){done(false)})}
    else{var a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();
      var ok=false;try{ok=document.execCommand('copy')}catch(x){}document.body.removeChild(a);done(ok)}});
  res.querySelector('[data-printplan]').addEventListener('click',function(){window.print()});
  res.querySelector('[data-restart]').addEventListener('click',function(){f.reset();f.querySelector('[data-tasks]').innerHTML='';
    f.querySelector('[data-pickhint]').textContent='';f.querySelector('[data-verihint]').textContent='';err.textContent='';
    [].forEach.call(f.querySelectorAll('[data-need]'),function(x){x.hidden=true});reset();res.hidden=true;f.hidden=false;st.textContent='';
    f.scrollIntoView({block:'start'});first('meslek')});
})();""" % {"max": MAX_PICK}


def json_ld(cfg: dict, jobs: list[dict]) -> str:
    base = cfg["site_url"].rstrip("/")
    url = f"{base}/{JOB_PATH}"
    return G._ld([
        {"@context": "https://schema.org", "@type": "WebPage", "url": url, "inLanguage": "tr",
         "name": "Mesleğine göre yapay zekâ: kendi planını çıkar",
         "about": [m["baslik"] for m in jobs], "author": {"@id": base + "/#kisi"}, "isAccessibleForFree": True},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": base + "/"},
            {"@type": "ListItem", "position": 2, "name": "Rehberler", "item": base + "/rehber/"},
            {"@type": "ListItem", "position": 3, "name": "Mesleğine göre yapay zekâ", "item": url}]},
    ])


def home_cta(href: str, n: int) -> str:
    return (f'  <section class="block money-cta"><div class="wrap"><div class="money-box">'
            f'<h2>Mesleğinde yapay zekâ nereye yarar?</h2>'
            f'<p>{n} meslek için en çok vakit alan işler, hazır komutlar ve dikkat edilecek kurallar. '
            f'Beş soruyu cevapla, kendi planını çıkar.</p>'
            f'<a class="btn solid" href="{e(href)}">Planımı çıkar</a></div></div></section>\n')
