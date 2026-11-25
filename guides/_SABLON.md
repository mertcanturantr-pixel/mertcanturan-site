---
title: Başlık, okuyanın elde edeceği sonucu söylesin
slug: kisa-adres
seo_title: İsteğe bağlı. Arama sonucunda görünen başlık, en fazla 65 (ideali 60) karakter. Başlık 60 karakteri geçiyorsa yaz.
description: İsteğe bağlı. Arama sonucundaki açıklama, en fazla 160 karakter. Yoksa summary kullanılır.
summary: Tek cümle, en fazla 200 karakter. Kime ve ne zaman yarayacağını söyle.
type: kontrol-listesi
topic: baslangic
audience: Herkes
published: 2026-12-01
checked: 2026-12-01
change: 2026-12-01 İlk sürüm.
video:
video_title:
draft: true
---

Bu dosya yayınlanmaz (adı alt çizgiyle başlıyor). Yeni rehber için kopyala, adını değiştir.

## Alanlar

- topic (rehber listesindeki konu grubu): baslangic | gunluk | guvenlik | is | egitim | icerik | uretim
- type: kontrol-listesi | adim-adim | sablon | karsilastirma
- audience: virgülle ayır (Herkes, İş yerleri, Hukukçular, Yazılımcılar)
- change: her güncellemede yeni bir satır ekle: `change: 2027-01-10 Ayar menüsünün yeni adı eklendi.`
- checked: içeriği en son ne zaman baştan sona doğruladığın. 180 günü geçerse derleme uyarı verir.
- video: rehberin anlatıldığı video. Video açıklamasına da `mertcanturan.com/rehber/kisa-adres` yaz.

## Yazım kuralları

1. İlk iki cümle sorunu ve rehberin ne vereceğini söyler. Giriş paragrafı uzamaz.
2. Her somut iddia (tarih, sayı, ayar adı, kanun maddesi) birincil kaynağa dayanır ve Kaynaklar bölümünde bağlantısıyla durur.
3. Bir aracın ayar adı ya da menüsü yazılıyorsa, o gün ekranda kontrol edilir ve `checked` tarihi güncellenir.
4. Hukuki konu genel bilgi düzeyinde kalır; kişiye özel tavsiye verilmez.
5. Sponsorlu bir ürün geçiyorsa bu açıkça yazılır.
6. Kontrol listesi maddesi `- [ ] **Kısa emir.** Açıklama.` biçimindedir.
7. Komut şablonu ```sablon bloğuna yazılır; doldurulacak alanlar [BÜYÜK HARF] ile gösterilir. Adında METİN ya da METNİ geçen alan geniş kutu olur.

8. "Gerçekten kazandırır mı?" karnesi ```karne bloğuna yazılır (örnek aşağıda). Her satır "Alan: değer". Zorunlu alanlar: Yöntem, İddia, Başlangıç maliyeti, İlk gelire kadar, Gereken beceri, Türkiye'den yapılabilir mi, Platform kuralı, Karar. Karar yalnızca "Çalışıyor", "Şartlı çalışıyor" ya da "Bu haliyle çalışmıyor" olur. Olumlu kararda en az bir "İlk adım", olumsuz kararda "Bunun yerine" zorunlu.
9. Karnede kazanç rakamı yalnızca "İddia" alanında, iddianın kendisi olarak geçer. Bağlantı, kullanıcı adı ve kişi ya da kurs adı yazılmaz; iddiayı ele alırız, kişiyi değil. Kripto, borsa ve kumar yöntemleri bu formata girmez. Bir yöntemin tek karnesi olur. Bu kurallara uymayan karne derlemede hata verir.
10. En az 3 karne ve en az bir olumlu karar olunca `/yapay-zekayla-para-kazanmak/` sayfası kendiliğinden açılır. 90 günden eski karnede "Yeniden kontrol bekliyor" yazar.

## Karne örneği

```karne
Yöntem: Yüzsüz yapay zekâ YouTube kanalı
İddia: Yapay zekâ sesiyle otomatik video üret, kanal ayda 3.000 dolar kazandırsın.
Başlangıç maliyeti: Araç abonelikleri; ayda birkaç yüz lira.
İlk gelire kadar: Önce para kazanma programının eşiğini geçmek gerekir; aylar sürebilir.
Gereken beceri: Konu seçimi, senaryo ve kurgu.
Türkiye'den yapılabilir mi: Evet.
Platform kuralı: Seri üretilen, birbirini tekrar eden videolar reklam geliri alamıyor.
Bunun yerine: Yapay zekâyı senaryo ve kurgu için kullan, kendi bilgini anlattığın bir kanal aç.
Karar: Bu haliyle çalışmıyor
```

## Kontrol listesi örneği

- [ ] **Kısa emir.** Neden önemli olduğunu anlatan bir iki cümle.

## Kaynaklar

- [Kaynağın adı](https://ornek.gov.tr/)


## Kalıcı bölüm adresi

Video açıklamasından bağlantı verilecek bölüme kalıcı adres ver: `## Air Canada, 2022-2024 {#air-canada}`. Başlık sonradan değişse de adres değişmez. Aynı adres bir rehberde iki kez verilirse derleme durur.

## SAHA notları ve sır saklama

SAHA notuna verilen cevapta müvekkil, dava, büro ya da çalışılan şirketle ilgili hiçbir olay anonim de olsa kullanılmaz. Örnek kamuya açık bir olaydan ya da kurgudan gelir; kurguysa metinde "temsili örnek" yazar.
