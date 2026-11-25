---
title: WhatsApp Business'ta yapay zekâ: hazır yanıtlar, otomatik mesaj ve robot kurmanın sınırları
slug: whatsapp-business-yapay-zeka
seo_title: WhatsApp Business'ta yapay zekâ: hazır yanıt ve otomatik mesaj
description: WhatsApp Business'ta yapay zekâyla hazır yanıt, karşılama ve uzakta mesajı; API'de robot kurmanın kuralları, Meta'nın 2026 yasağı ve izinsiz tanıtım mesajı.
summary: Esnaf ve küçük işletme için WhatsApp Business: yapay zekâyla hazır yanıt seti, karşılama ve uzakta mesajı, katalog metni; robot kurmanın kuralları ve tanıtım mesajında izin.
keywords: whatsapp business yapay zeka, whatsapp business hızlı yanıt nasıl eklenir, whatsapp karşılama mesajı örnekleri, uzakta mesajı örneği, whatsapp chatbot kurmak, whatsapp business api yapay zeka yasağı, whatsapp kampanya mesajı iys, esnaf whatsapp mesaj şablonu
type: sablon
topic: is
audience: Esnaf, İş yerleri
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: İYS ve onay kuralları netleştirildi, API ücretlendirmesi düzeltildi, iç bağlantılar ve soru başlıkları eklendi.
video:
video_title:
draft: true
---

Bir kuaför, bir pastane ya da bir tesisatçı için WhatsApp, telefonun yerini almış durumda. Gün boyu aynı sorular geliyor: "Kaçta açıksınız?", "Fiyat ne kadar?", "Yarın yer var mı?" WhatsApp Business'ın ücretsiz uygulamasında bu sorular için hazır yanıtlar ve otomatik mesajlar var; yapay zekâ ise bu metinleri bir akşamda hazırlamana yardım ediyor. Müşteriyle kendi kendine konuşan bir robot ise ayrı ve daha zor bir iş.

Kısaca: Küçük bir işletme için WhatsApp Business'ta yapay zekânın en güvenli kullanımı, hazır yanıtları ve otomatik mesajları ona yazdırmak: İşletmeni bir kez anlat, on beş hazır yanıt, bir karşılama ve bir uzakta mesajı al, uygulamanın kendi ayarlarına ekle. Müşteriye kendi kendine cevap veren bir robot ancak WhatsApp Business Platform (API) ile kurulabiliyor ve 15 Ocak 2026'dan beri genel amaçlı sohbet robotları orada yasak. Müşteriye onayı olmadan kampanya mesajı atma.

## 1. İşletmeni bir kez anlat {#tanit}

Önce yapay zekâya işletmeni tanıt. Bunu bir kez yazarsan sonraki bütün metinler aynı bilgiye dayanır:

```sablon
Benim bir [İŞLETME TÜRÜ] işletmem var. Bilgiler:
- Adres ve semt: [ADRES]
- Çalışma saatleri: [SAATLER]
- Hizmetler ve fiyatlar: [LİSTE]
- Randevu nasıl alınıyor: [YÖNTEM]
- Ödeme seçenekleri: [NAKİT, KART, HAVALE...]
- Sık gelen sorular: [SORULAR]
- Müşterilerime nasıl hitap ederim: [SİZ / SEN, RESMÎ / SAMİMİ]
Bu bilgileri aklında tut; sana WhatsApp mesajları yazdıracağım. Benim vermediğim bir fiyat, saat ya da hizmet uydurma.
```

## 2. Hızlı yanıt seti nasıl hazırlanır? {#hazir-yanitlar}

```sablon
Bu bilgilere göre WhatsApp için 15 hazır yanıt yaz. Her biri:
- Kısa olsun (en fazla üç cümle).
- Telefon ekranında rahat okunsun.
- Bir kısayol adı olsun (örneğin /saat, /fiyat, /adres).
Konular: çalışma saatleri, adres ve yol tarifi, fiyat listesi, randevu alma, randevu iptali, ödeme seçenekleri, kampanya yokken "indirim var mı" sorusu, geç kalan müşteri, teşekkür, olumsuz yorum sonrası özür, [İŞLETMEYE ÖZEL KONULAR].
```

Çıkan metinleri WhatsApp Business'ta Ayarlar > İşletme araçları > Hızlı yanıtlar bölümüne ekle. Mesaj yazarken "/" işaretine basınca kısayollar çıkar.

> SAHA: WhatsApp Business'ın Türkçe arayüzünde İşletme araçları menüsünün ve Hızlı yanıtlar ekranının güncel adlarını ekran görüntüsüyle kaydet.

## 3. Karşılama ve uzakta mesajı örneği {#otomatik-mesaj}

WhatsApp Business'ın ücretsiz uygulamasında iki otomatik mesaj var: Seninle ilk kez ya da uzun süre sonra yazışan müşteriye giden karşılama mesajı ve mesai dışında giden uzakta mesajı.

```sablon
Bir karşılama mesajı ve bir uzakta mesajı yaz.
Karşılama: Müşteriyi selamlasın, en sık iki soruya cevap versin (saat ve randevu) ve "Size nasıl yardımcı olabilirim?" diye bitsin. En fazla 300 karakter.
Uzakta: Mesai dışında olduğumuzu, [SAAT]'te döneceğimizi söylesin. Acil durumlar için [VARSA ACİL YOL]. En fazla 250 karakter.
```

## 4. Katalog ve ürün açıklamaları {#katalog}

Katalogdaki ürün ve hizmetler için kısa açıklamalar da yapay zekâya yazdırılabilir. Fiyatı ve içeriği sen ver; "uygun fiyatlı", "en kaliteli" gibi kanıtlayamayacağın iddiaları çıkar. Ayrıntılı ürün açıklaması şablonu [esnaf rehberinde](rehber:kucuk-isletme-yapay-zeka#aciklama).

## WhatsApp'ta yapay zekâ robotu kurulabilir mi? {#robot}

Ücretsiz WhatsApp Business uygulamasında yapay zekâyla müşteriye kendi kendine cevap veren bir robot kuramazsın; bunun için WhatsApp Business Platform (API) gerekiyor. API'yi doğrudan Meta'dan ya da bir aracı firmadan kullanıyorsun. Meta, Temmuz 2025'ten beri işletmenin başlattığı şablon mesajları (pazarlama, bilgilendirme, kimlik doğrulama) mesaj başına ücretlendiriyor; müşterinin yazdığı mesaja 24 saat içinde verilen hizmet cevapları ise ücretsiz. Aracı firmanın kendi aylık ücreti ayrıca eklenir.

Burada Meta'nın kuralına dikkat: 15 Ocak 2026'dan beri WhatsApp Business API'de genel amaçlı yapay zekâ sohbet robotları yasak. Bu yüzden ChatGPT ve Copilot'un WhatsApp hatları kapandı. İşletmeye özel kullanımlar ise serbest: sık sorulan sorular, randevu, sipariş takibi, müşteri desteği. Yani robotun "her soruyu cevaplayan" bir asistan değil, senin işletmenin işini yapan bir asistan olmalı.

Robot kurmadan önce kapsam, yasak konular, insana aktarma, KVKK ve test için [sohbet robotu kontrol listesine](rehber:sohbet-robotu-kurmadan-once) bak; müşteriye robotla konuştuğunu nasıl söyleyeceğin [şeffaflık bölümünde](rehber:sohbet-robotu-kurmadan-once#seffaflik). [Air Canada örneğinde](rehber:yapay-zeka-hatalari#air-canada) görüldüğü gibi, robotun verdiği söz senin sözün sayılabilir.

> SAHA: Meta'nın WhatsApp Business uygulamasına eklediği yapay zekâ özelliklerinden ("Business AI" gibi) Türkiye'de hangisi açık? Kendi uygulamanda kontrol et ve ne gördüğünü yaz.

## Kampanya mesajı için izin ve İYS gerekir mi? {#izin}

WhatsApp'tan müşterine kampanya, indirim ya da yeni ürün mesajı atmak, 6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun'a göre ticari elektronik ileti sayılır. Bireysel müşteriye göndermek için önceden onayı gerekiyor ve ticari elektronik ileti gönderen işletmelerin İleti Yönetim Sistemi'ne (İYS) kaydolması ve onayları oraya işlemesi bekleniyor. Alıcı esnaf ya da tacirse önceden onay şartı yok, ama o da reddederse artık gönderemezsin. Müşterinin sana sipariş için yazmış olması, ona kampanya mesajı atma izni vermez.

- [ ] Kampanya mesajı göndereceğin her numara için onayın var mı, nasıl ve ne zaman alındığını gösterebilir misin?
- [ ] Mesajda işletmenin adı ve müşterinin mesaj almayı reddedebileceği yol yazıyor mu?
- [ ] İşletmen İYS'ye kayıtlı mı, onaylar İYS'ye işlendi mi? Kendi durumunu İYS'nin sitesindeki sık sorulan sorulardan kontrol et.

Sipariş onayı, randevu hatırlatması ve kargo bilgisi gibi bilgilendirme mesajları ise tanıtım içermiyorsa onay gerektirmiyor; içine "bu arada yeni kampanyamız var" eklersen tanıtım mesajına döner.

## Sık yapılan hatalar {#hatalar}

- **Yapay zekânın yazdığı fiyatı kontrol etmeden kaydetmek.** Hazır yanıttaki eski bir fiyat, müşteriye verilmiş söz gibi algılanır.
- **Çok uzun hazır yanıtlar.** WhatsApp'ta kimse paragraf okumaz.
- **Herkese toplu kampanya mesajı.** İzinsiz mesaj hem şikâyete hem de numaranın kısıtlanmasına yol açabilir.
- **Müşteri bilgisini yapay zekâya yapıştırmak.** Hazır yanıt yazdırmak için müşterinin adına, numarasına ihtiyaç yok.

## Dürüst sınır {#sinir}

Hazır yanıtlar ve otomatik mesajlar, küçük bir işletme için çoğu zaman robottan daha iyi çalışır: ucuz, kontrollü ve müşteri yine bir insanla konuştuğunu bilir. Robot, mesaj trafiği çok yüksek ve sorular gerçekten tekrar ediyorsa mantıklı. İzinsiz ticari ileti idari para cezasına yol açar ve 6563 sayılı Kanun'a göre bir defada birden fazla alıcıya gönderimde ceza on katına kadar artırılabilir. Bu yüzden çok sayıda kişiye toplu kampanya göndermeden önce onay kayıtlarını bir avukata ya da İYS konusunda deneyimli bir danışmana kontrol ettir.

## Sonraki adım {#sonraki-adim}

Bu akşam işletme tanıtım şablonunu doldur ve on beş hazır yanıtı yazdır. Yarın en sık gelen üç soruya bu yanıtlarla cevap ver ve gerekirse düzelt. Google yorumları için [yorum cevaplama rehberine](rehber:google-yorumlarina-cevap) geç.

## Kaynaklar

- WhatsApp Business Yardım Merkezi, hızlı yanıtlar ve otomatik mesajlar: [faq.whatsapp.com](https://faq.whatsapp.com/)
- WhatsApp Business API'de genel amaçlı sohbet robotu yasağı, 15 Ocak 2026: [TechCrunch](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform/) · [respond.io açıklaması](https://respond.io/blog/whatsapp-general-purpose-chatbots-ban)
- 6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun ve Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik: [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/)
- İleti Yönetim Sistemi: [iys.org.tr](https://iys.org.tr/)
- Meta, WhatsApp Business Platform fiyatlandırması: [developers.facebook.com](https://developers.facebook.com/docs/whatsapp/pricing)
