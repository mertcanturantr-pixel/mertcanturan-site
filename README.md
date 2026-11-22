# mertcanturan.com

Statik kişisel site. GitHub Actions üç saatte bir YouTube, Instagram ve TikTok'taki son paylaşımları çeker, kapak görsellerini siteye indirir, siteyi yeniden üretir ve GitHub Pages'te yayınlar. Ziyaretçinin tarayıcısı bu platformlara bağlanmaz; çerez ya da takip kodu yoktur.

## Klasörler

| Yol | Ne işe yarar |
| --- | --- |
| `config.json` | Alan adı, e-posta, platform profil adresleri |
| `guides/*.md` | Rehberler. Her dosya bir sayfa olur: `/rehber/<slug>/` |
| `src/` | Sayfa iskeleti, ana sayfa içeriği, stil dosyası |
| `scripts/feeds.py` | Platformlardan içerik çeker → `data/content.json`, `data/media/` |
| `scripts/build.py` | Siteyi `dist/` klasörüne üretir |
| `scripts/tiktok_auth.py` | TikTok hesabını bir kez bağlamak için yardımcı |
| `tests/` | Testler ve önizleme için örnek veri |

## Yerelde çalıştırma

```bash
pip install -r requirements.txt
python -m unittest discover -s tests
python scripts/build.py                    # canlı sürüm → dist/
python scripts/build.py --preview --demo   # örnek videolarla önizleme (yayına çıkmaz)
```

## İlk kurulum

### 1. Depo ve yayın

1. GitHub'da **herkese açık** bir depo aç ve bu klasörü gönder. (GitHub Pages özel depoda ücretli plan ister. Depoda gizli bilgi yoktur; anahtarlar Secrets'ta durur.)
2. Settings → Pages → Source: **GitHub Actions**.
3. Alan adını aldıktan sonra Settings → Pages → Custom domain: `mertcanturan.com`. DNS'te GitHub'ın gösterdiği A ve CNAME kayıtlarını gir, "Enforce HTTPS" kutusunu işaretle.

### 2. YouTube

Ek bir şey gerekmez. Kanalın herkese açık RSS akışı kullanılır (`config.json` → `channel_id`). Akış son 15 videoyu verir.

### 3. Instagram

Gereken: **profesyonel hesap** (İçerik üreticisi ya da İşletme). Kişisel hesapta API çalışmaz.

1. developers.facebook.com → uygulama oluştur → **Instagram** ürünü → "API setup with Instagram login".
2. Instagram hesabını ekle, `instagram_business_basic` iznini ver, panelden **erişim anahtarını oluştur** (60 gün geçerli).
3. GitHub → Settings → Secrets and variables → Actions → `IG_TOKEN`.
4. `config.json` → `platforms.instagram.profile_url` alanına profil adresini yaz.

Anahtar her çalışmada yenilenir ve yeni değeri GitHub'a kaydedilir (bkz. adım 5). **60 gün boyunca hiç yenilenmezse ölür** ve panelden yeniden alınması gerekir.

### 4. TikTok

1. developers.tiktok.com → uygulama oluştur → **Login Kit** ve **Display API** ürünlerini ekle, `user.info.basic` ve `video.list` izinlerini seç.
2. Yönlendirme adresi (Redirect URI): `https://mertcanturan.com/`
3. Uygulama incelemeye girmeden önce **Sandbox** modunda kendi hesabını "Target user" olarak ekle.
4. Kendi bilgisayarında:
   ```bash
   export TIKTOK_CLIENT_SECRET=...   # ekrana basılmaz
   python scripts/tiktok_auth.py --client-key KEY --redirect-uri https://mertcanturan.com/
   gh secret set TIKTOK_REFRESH_TOKEN < .tiktok_tokens && rm .tiktok_tokens
   ```
5. Secrets: `TIKTOK_CLIENT_KEY`, `TIKTOK_CLIENT_SECRET`, `TIKTOK_REFRESH_TOKEN`.
6. `config.json` → `platforms.tiktok.profile_url`.
7. Kalıcı kullanım için uygulamayı TikTok incelemesine gönder (demo videosu ve site adresi ister).

Yenileme anahtarı 365 gün geçerlidir ve her çalışmada yenilenir.

### 5. Anahtarların kendiliğinden yenilenmesi

GitHub'da **fine-grained personal access token** oluştur:
- Repository access: yalnızca bu depo
- Permissions → Secrets: **Read and write**

Bu token'ı `SECRETS_PAT` adıyla Secrets'a ekle. Bu olmazsa Instagram anahtarı 60 gün sonra, TikTok anahtarı yenileme sırasında değişirse hemen çalışmaz hale gelir.

## Günlük kullanım

**Video paylaştığında** hiçbir şey yapman gerekmez. En geç üç saat içinde sitede görünür. Hemen görmek istersen: Actions → "Siteyi güncelle" → Run workflow.

**Reklam etiketi:** Açıklamasında `#reklam`, `#işbirliği` ya da `#sponsorlu` geçen paylaşım sitede "Reklam" etiketiyle gösterilir. Bu etiketi her sponsorlu paylaşımın açıklamasına zaten yazman gerekiyor; site aynı etiketi okur.

**Videoyu rehbere bağlamak:** Video açıklamasına `mertcanturan.com/rehber/<slug>` yaz. Sitede o videonun kartında "Rehberi aç" bağlantısı çıkar.

**Bir platform hata verirse** site o platformun son başarılı içeriklerini göstermeye devam eder. GitHub çalışmayı başarısız sayar ve sana e-posta gönderir. Mesajda hangi platformun neden güncellenemediği yazar.

## Rehber eklemek

`guides/_SABLON.md` dosyasını kopyala, adını değiştir (`guides/kisa-adres.md`) ve doldur. Alt çizgiyle başlayan dosyalar yayınlanmaz.

Üst bilgi alanları:

| Alan | Ne yazılır |
| --- | --- |
| `title`, `summary` | Başlık ve en fazla 200 karakterlik özet |
| `slug` | Adres: `mertcanturan.com/rehber/<slug>`. Videoda söyleyeceğin adres budur |
| `type` | `kontrol-listesi`, `adim-adim`, `sablon` ya da `karsilastirma` |
| `audience` | Virgülle: `Herkes, İş yerleri` |
| `published`, `checked` | Yayın ve son doğrulama tarihi (YYYY-AA-GG). `checked` 180 günü geçerse derleme uyarır |
| `change` | Her güncellemede bir satır: `change: 2027-01-10 Ayar adı güncellendi.` |
| `video`, `video_title` | Rehberin videosu. Video sitede varsa kapağı otomatik gelir |
| `draft` | `true` iken yalnız önizlemede görünür, canlıda yayınlanmaz |

İçerikte kullanılabilenler:
- Kontrol listesi: `- [ ] **Kısa emir.** Açıklama.` Sitede işaretlenebilir kutu olur (işaretler kaydedilmez).
- Komut şablonu: ```` ```sablon ```` bloğu. `[BÜYÜK HARF]` alanları doldurma kutusuna dönüşür; adında METİN/METNİ geçen alan geniş kutu olur. Ziyaretçinin yazdıkları tarayıcıda kalır.
- Üç ya da daha fazla `##` başlığı varsa "Bu rehberde" içindekiler listesi kendiliğinden çıkar.

Her rehber için otomatik üretilenler: paylaşım görseli (`/og/<slug>.png`), arama motoru bilgisi (Article ve BreadcrumbList), RSS akışına kayıt (`/rehber/feed.xml`), site haritasında son kontrol tarihi. Dört ya da daha fazla rehber olunca liste sayfasında tür filtresi ve arama kutusu açılır (`config.json` → `guides_filter_min`).

## Bilinen sınırlar

- YouTube akışında Shorts ayrımı, bağlantının `/shorts/` içermesine göre yapılır. Bu YouTube'un resmî olarak belgelediği bir davranış değildir.
- GitHub, herkese açık depolarda 60 gün hiç etkinlik olmazsa zamanlanmış çalışmaları durdurur. Yeni içerik geldikçe depoya kayıt düştüğü için düzenli paylaşımda sorun olmaz.
- TikTok kapak bağlantıları birkaç saat sonra geçersiz olur; bu yüzden kapaklar indirilip depoda saklanır.
