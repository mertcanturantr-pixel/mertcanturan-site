# mertcanturan.com · Hukuk ve ürün uyumu kısa denetimi

Değerlendirme günü: 16 Kasım 2026 · Kapsam: statik tek sayfa (index.html), yayına alınmadı.
Rol denetimi alt ajansız yapıldı: sequential_self_review.

## Site ne yapıyor
- Çerez, analitik, harici yazı tipi, harici betik ve form yok. Dış kaynak çağrısı yok (sistem yazı tipleri).
- Kişisel veri yalnızca ziyaretçi e-posta gönderirse (mailto) toplanır.
- Barındırma sağlayıcısı henüz seçilmedi: sunucu günlükleri (IP) sağlayıcıya göre değişir.

## Modül kararları
| Modül | Karar | Gerekçe |
| --- | --- | --- |
| privacy | applies | E-posta yazışması kişisel veri işler. Sitede kısa bilgi notu var; KVKK m.10 aydınlatmasının tamamı (veri sorumlusu kimliği, hukuki sebep, alıcı grupları, haklar) için metin ONAY BEKLİYOR. |
| cookies_sdks | not_applicable | Çerez ve SDK yok. Analitik eklenirse yeniden açılır. |
| transfers | unknown | E-posta sağlayıcısı ve barındırma yurt dışındaysa KVKK m.9 aktarım değerlendirmesi gerekir. Sağlayıcı seçilince açılacak. |
| ecommerce, consumer, payments | not_applicable | Satış ve ödeme yok. |
| marketing | not_applicable (şimdilik) | Bülten yok. Bülten açılırsa ticari elektronik ileti onayı ve İYS ayrıca değerlendirilir. |
| content (5651) | applies [Muhtemel] | 5651 m.3 içerik sağlayıcının tanıtıcı bilgilerini sitede bulundurmasını ister. Ad soyad ve e-posta var; yönetmelikteki tam liste (ör. adres) doğrulanmadı: unverified. |
| sector: avukatlık | applies [Muhtemel] | Hakkımda'da unvan var. Avukatlık hizmeti tanıtılmıyor, büroya bağlantı yok, "genel bilgilendirme" notu var. Meslek kuralları açısından son değerlendirme Mertcan Turan'da. |
| accessibility | engineering_recommendation | Anlamlı başlık yapısı, odak göstergesi, yeterli kontrast, mobil görünüm kontrol edildi (ekran görüntüsüyle). |
| ai | not_applicable | Sitede yapay zekâ özelliği yok. |

## Çalıştırılan kontroller
- 1280 px ve 390 px genişlikte ekran görüntüsü alındı; taşma ve hizalama hatası düzeltildi.
- Harici istek yok (dosyada http çağrısı yalnızca YouTube bağlantısı).

## Yayın öncesi açık işler (kim: Mertcan)
1. is@mertcanturan.com posta kutusunu aç; açılmadan yayına alma (bağlantı boşa düşer).
2. Gizlilik metnini tam KVKK aydınlatmasına çevir ve onayla (sağlayıcı adları belli olunca).
3. 5651 tanıtıcı bilgi listesini doğrula; gerekiyorsa künye satırı ekle.
4. Instagram ve TikTok hesapları açılınca bağlantıları ekle.
5. Fotoğraf eklenecekse "MT" kutusu yerine gerçek fotoğraf konur.

Karar: BLOCKED (yayın için) — 1, 2 ve 3 tamamlanınca yeniden değerlendirilir.

## Güncelleme · 16 Kasım 2026 · Video akışı ve rehberler

Kapsam: platform içerik akışı (YouTube RSS, Instagram API with Instagram Login, TikTok Display API), GitHub Actions + Pages, /rehber sayfaları.

Kararlar:
- Gömme kodu (embed.js, iframe) kullanılmadı. Kapaklar derleme sırasında indirilip yeniden kodlanıyor; ziyaretçi tarayıcısı üçüncü taraflara istek atmıyor. Testle doğrulandı: canlı derlemede dış kaynaklı script/img/stylesheet yok. [Kesin, yerel test]
- Gizlilik metnine "kapaklar sitede saklanır, tıklayınca platforma geçersin" eklendi.
- Ticari reklam: açıklamasında #reklam / #işbirliği / #sponsorlu geçen içerik "Reklam" etiketiyle gösteriliyor. Etiketin konması paylaşım yapanın sorumluluğunda; site yalnızca okuyor. [Muhtemel: Ticari Reklam Yönetmeliği değişikliğiyle uyumlu yön]
- Rehberlerde genel bilgilendirme notu ve son kontrol tarihi zorunlu alan.
- Erişim anahtarları yalnızca GitHub Secrets'ta; loglarda maskeleniyor, hata mesajlarından ayıklanıyor (testli).

Yeni açık konu (YAYIN ENGELİ):
- Barındırma GitHub Pages olursa GitHub ziyaretçi IP adreslerini güvenlik amacıyla kaydeder ve işler (ABD). Bu KVKK m.9 yurt dışı aktarım sorusu açar. Karar: (a) GitHub Pages + aydınlatmaya barındırıcıyı ekle + m.9 dayanağını belirle (standart sözleşme ve Kurul bildirimi gerekip gerekmediği), ya da (b) Türkiye'de barındırma + Actions'tan dosya aktarımı. Karar sahibi: Mertcan. [Muhtemel]
- TikTok uygulaması incelemeden geçmeden yalnız Sandbox'ta çalışır; Sandbox'ın kalıcı kullanıma uygunluğu doğrulanmadı. [Tahmin]
