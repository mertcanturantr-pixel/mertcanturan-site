# Kod haritası · mertcanturan.com

Son güncelleme: 2026-11-22 (depo: github.com/mertcanturantr-pixel/mertcanturan-site). 70 hazır rehber (dört rollü denetimden geçti), 2 iskelet; mesleğine göre yapay zekâ aracı; llms-full.txt.

## 1. Kök düzen

| Yol | Ne |
| --- | --- |
| `config.json` | Site adresi, iletişim e-postası, platform hesapları, izinli alan adları, Archor anahtarı |
| `scripts/` | Statik site üreticisi ve veri çekiciler (Python) |
| `src/` | `layout.html` (her sayfanın iskeleti), `home.html` (ana sayfa), `site.css`, `bench.js` (ana sayfa test tezgâhı) |
| `guides/` | Rehberler (Markdown + ön bilgi). `_SABLON.md` yazım şablonu, `_KATALOG.md` 51 başlıklık konu listesi; `_` ile başlayanlar yayınlanmaz |
| `data/` | `content.json` (çekilen videolar), `media/` (indirilen kapaklar), `plan.json` (57 video ve bağlı rehber), `meslekler.json` (meslek aracı verisi: 12 meslek, işler, komutlar, rehber hedefleri) |
| `fonts/` | Kendi sunduğumuz woff2 yazı tipleri; `fonts/src/` OG görseli için TTF |
| `tests/` | `test_site.py` ve `fixtures/` (örnek rehberler, demo video verisi) |
| `.github/workflows/site.yml` | 3 saatte bir ve her push'ta: test, veri çek, derle, plan kontrolü, Pages'e yayın |
| `compliance/REVIEW.md` | Hukuk ve KVKK denetim kaydı (depoda yok; yerel kopyada, .gitignore) |

## 2. Betikler

| Dosya | Görev |
| --- | --- |
| `scripts/common.py` | HTTP yardımcıları, alan adı izinleri, Türkçe tarih ve küçük harf, reklam etiketi tespiti |
| `scripts/feeds.py` | YouTube RSS, Instagram ve TikTok API'den içerik çeker, token yeniler, kapakları indirir |
| `scripts/guides.py` | Rehberleri okur ve doğrular; Markdown → HTML (kontrol listesi, ```sablon, ```karne, SAHA notu, içindekiler); JSON-LD, Atom, llms.txt, OG görseli, apple-touch-icon |
| `scripts/build.py` | Bütün sayfaları üretir: ana sayfa, `/rehber/`, rehber sayfaları, `/rehber/sablonlar/`, `/yapay-zekayla-para-kazanmak/` (karnelerden), 404, favicon, sitemap/robots (yalnız canlı) |
| `scripts/meslek.py` | `/meslegine-gore-yapay-zeka/` aracı: veriyi okur, yalnız yayındaki rehberlere bağlı işleri bırakır (meslek başına ≥3 iş, sayfa için ≥4 meslek), statik HTML + soru-cevap JS; ağ isteği ve kayıt yok |
| `scripts/repos.py` | `repos/*.md` GitHub depo sayfalarını okur ve doğrular (lisans, arşiv, zorunlu bölümler, 90 gün eskime); JSON-LD |
| `scripts/repo_meta.py` | CI'da GitHub API'den yıldız, lisans, arşiv durumunu çekip `data/repos_meta.json`'a yazar; lisans değişirse derleme durur |
| `scripts/plan_check.py` | Her video için rehberin videodan 1 gün önce yayında olup olmadığını kontrol eder (çıkış 1 geç, 2 eksik) |
| `scripts/tiktok_auth.py` | TikTok için yerel tek seferlik yetkilendirme |

## 3. Testler ve kapılar

- `python3 -m unittest discover -s tests` (pytest kurulu değil)
- `python3 scripts/plan_check.py`
- Önizleme: `python3 scripts/build.py --preview --demo --out ../preview`; canlı derleme: `python3 scripts/build.py`
- Testler gerçek rehberleri değil `tests/fixtures/guides/` klasörünü kullanır (`G.GUIDES_DIR` yaması).

## 4. Belgeler

- `README.md`: kurulum (Pages, Instagram, TikTok, sırlar, rehber yazımı)
- Rehber yazım kuralları: `guides/_SABLON.md` ve mertcanturan-yazi-standardi becerisi

## 5. "X'i değiştireceğim, nereye bakarım?"

| İş | Dosya |
| --- | --- |
| Ana sayfa metni | `src/home.html`; meta açıklama ve OG görseli `scripts/build.py` → `build()` |
| Menü, üst bar, alt bilgi | `src/layout.html`, `render_follow()` |
| Yeni rehber | `guides/<slug>.md` (`_SABLON.md`'den), `_KATALOG.md` durumu, gerekiyorsa `data/plan.json` |
| Rehber blok türü (şablon, karne vb.) | `guides.py` → `render_body()`, `_template_block()`, `_karne_block()`; stil `site.css` sonu |
| Rehber listesi, arama, filtre | `build.py` → `render_guide_index()`, `GUIDE_JS` |
| Karne kuralları (zorunlu alan, gelir vaadi, kırmızı çizgi) | `guides.py` → `KARNE_FIELDS`, `parse_karne()`; yazım kuralı `guides/_SABLON.md` |
| Para kazanma sayfası | `build.py` → `collect_karnes()`, `money_page_ready()`, `render_money_page()`, `MONEY_JS`; eşik `config.json` → `money_page_min`; önizleme örnekleri `tests/fixtures/demo_karneler.json` |
| Yapılandırılmış veri | `guides.py` → `json_ld()`, `site_json_ld()`, `index_json_ld()` |
| Arama başlığı ve açıklaması | Rehber üst bilgisinde `seo_title` (≤65) ve `description` (≤160); `build.py` → `guide_title_tag()` |
| Video açıklamasından bölüme bağlantı | Başlığa kalıcı adres: `## Başlık {#adres}` (`attr_list`); `guides.py` → `render_body()`, `_heading()` |
| Rehber sonu (abone ol, ilgili rehberler, imza) | `build.py` → `render_guide_page()`; ilgili rehber sırası önce birbirine bağlantı verenler |
| Meslek aracı (meslek, iş, komut, kural) | `data/meslekler.json`; görünüm `scripts/meslek.py` → `render()`, `JS`; stil `site.css` sonu ("mesleğine göre"); test `JobToolTests` |
| Rehber listesi başındaki "buradan başla" kutusu | `build.py` → `START_GUIDES`, `render_guide_index()` |
| Yapay zekâ aramaları için tam metin | `guides.py` → `llms_full()` → `/llms-full.txt` (yalnız yayındaki rehberler) |
| GitHub depoları | `repos/<slug>.md` (`repos/_SABLON.md`), `build.py` → `render_repo_index()`, `render_repo_page()` |
| Video akışı ve kartlar | `build.py` → `render_feed()`, `render_card()`; veri `feeds.py` |

## 6. Bilinen tuzaklar

- Site 25 Kasım 2026'da GitHub Pages'te yayına açıldı (mertcanturan.com). SAHA notu olmayan 28 rehber `draft: false`; SAHA notu kapanan rehberde `draft: false` yapılınca yayına girer.

- Önizleme derlemesi bağlantıları `index.html` ile bitirir; canlı derleme bitirmez (`Links` sınıfı). 404 sayfası kök yollu (`/`) bağlantı kullanır.
- Taslak ve iskelet rehberler yalnız önizlemede çıkar; yayındaki rehber taslağa bağlantı verirse bağlantı düz metne döner (uyarı basılır).
- SAHA notu olan ya da `stage: iskelet` olan rehber yayınlanamaz (derleme hata verir).
- `sablonlar`, `feed` ve `github` rehber adresi olarak kullanılamaz.
- `kontrol-listesi` rehberi 16 Kasım'da `yapay-zeka-cevabini-kontrol-etmek` adresine taşındı; `kontrol-listesi` artık yalnız bir rehber türü (`type`).
- Kırmızı çizgi taraması (`RED_LINE_RE`) karnenin bütün alanlarına uygulanır; "Bunun yerine" alanında bile kripto, borsa, bahis geçemez.
- Reklam etiketi listesi `common.py` → `_AD_TAGS`; `#tanıtım` 1 Ağustos 2026 kuralı için eklendi.
- Para kazanma sayfası en az `money_page_min` karne ve en az bir olumlu karar yoksa hiç üretilmez; bağlantıları da kaybolur. Aynı yöntemin iki karnesi derlemeyi durdurur.
- `--demo` örnek karneleri yalnız önizlemede kullanır; canlı derlemede `--demo` reddedilir.
- Meslek aracı canlı derlemede yayındaki rehber sayısı yetmezse hiç üretilmez (bağlantıları da kaybolur); rehberler taslakken yalnız önizlemede görünür.
- Komut şablonu alanları yalnız `[BÜYÜK HARF VE RAKAM]` biçiminde doldurulabilir olur; köşeli parantez içinde `/` ya da virgül olursa alan oluşmaz.
- Yatay kaydırmalı kart şeridinde `position:absolute` öğeler kartın dışına taşmasın diye `.card{position:relative}` gerekli.
