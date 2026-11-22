---
title: Emlakçılar için yapay zekâ: ilan metni, sanal döşeme ve müşteri yazışmaları
slug: emlakcilar-icin-yapay-zeka
seo_title: Emlakçılar için yapay zekâ: ilan, sanal döşeme ve kurallar
description: Emlak danışmanları için yapay zekâyla ilan metni, sanal döşeme ve müşteri mesajları; EİDS yetki doğrulaması, yanıltıcı ilan riski ve müşteri verisi.
summary: Emlak danışmanı için yapay zekâ: doğru bilgiyle ilan metni, sanal döşenmiş görselde etiket, müşteri yazışmaları ve bölge özeti; EİDS, yanıltıcı ilan riski ve müşteri verisi.
keywords: emlakçılar için yapay zeka, chatgpt ile emlak ilanı yazma, emlak ilan metni örneği, sanal döşeme, virtual staging, eids yetki doğrulama, satılık ilan yetki doğrulama 2026, emlak danışmanı yapay zeka, emlakcilar icin yapay zeka
type: sablon
audience: Emlak danışmanları
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: EİDS tarihleri kaynağa göre düzeltildi (satılıkta 1 Şubat 2026), reklam yönetmeliğinin yapay zekâ kuralı sanal döşemeye bağlandı, 6502 ve KVKK tam adları, Kısaca yeniden yazıldı
video:
video_title:
draft: true
---

Bir emlak danışmanının gününün büyük kısmı yazıyla geçiyor: ilan metinleri, müşteri mesajları, mal sahibine bilgi notları, portföy sunumları. Yapay zekâ bu yazıları hızlandırabilir ve boş bir odayı döşenmiş gibi gösteren görseller üretebilir. Ama emlak ilanı, tüketicinin büyük bir karar verdiği bir bilgi: Yanlış bir metrekare, olmayan bir manzara ya da gerçekte boş olan bir evin döşenmiş fotoğrafı, hem müşteri kaybı hem de hukuki sorun demek.

Kısaca: Yapay zekâyı emlak ilanında yalnızca yazı için kullan; metrekare, oda, kat ve aidat gibi bilgileri tapudan, iskândan ve kendi ölçümünden al. Sanal döşenmiş görselin üstüne "temsilidir" yaz ve aynı odanın gerçek fotoğrafını da koy. Satılık taşınmaz ilanlarında Elektronik İlan Doğrulama Sistemi (EİDS) yetki doğrulaması 1 Şubat 2026'dan beri zorunlu; yapay zekâ bu süreci değiştirmiyor.

## Yapay zekâya emlak ilanı nasıl yazdırılır? {#ilan}

```sablon
Aşağıdaki bilgilerle bir [SATILIK / KİRALIK] konut ilanı yaz.
Bilgiler (sadece bunları kullan):
- Konum: [İL / İLÇE / MAHALLE, SOKAK YAZMA]
- Brüt / net m²: [M²]
- Oda sayısı, kat, bina yaşı: [BİLGİ]
- Isınma, otopark, asansör, site içi: [BİLGİ]
- Öne çıkan özellikler: [GERÇEK ÖZELLİKLER]
- Ulaşım ve yakın yerler (gerçek mesafelerle): [BİLGİ]
- Fiyat ve aidat: [BİLGİ]
Biçim: İlk cümle evin en güçlü özelliği. Sonra kısa paragraf, sonra madde madde özellikler. 
Kurallar: Bilgilerde olmayan bir özellik, manzara, mesafe ya da yatırım vaadi ekleme. "Kaçırılmayacak fırsat", "değeri kesin artacak" gibi ifadeler kullanma.
```

"Değeri kesin artacak", "kira getirisi garantili" gibi ifadeler tüketiciyi yanıltabilir. 6502 sayılı Tüketicinin Korunması Hakkında Kanun ve Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği yanıltıcı reklamı yasaklıyor; Ticaret Bakanlığı'na bağlı Reklam Kurulu bu tür ilanlara idari para cezası verebiliyor. Brüt ve net metrekareyi ayrı ve doğru yazmak, sonradan çıkan anlaşmazlıkların bir kısmını baştan önler.

## Sanal döşeme serbest mi, nasıl etiketlenir? {#sanal-doseme}

Boş bir evin fotoğrafını yapay zekâyla döşenmiş gibi göstermek (sanal döşeme), alıcının evi hayal etmesine yardım ediyor. Ama:

- Görselin üstüne ya da hemen altına açıkça "Sanal olarak döşenmiştir, temsilidir" yaz.
- Aynı odanın gerçek, boş fotoğrafını da ilana koy.
- Duvar rengini, zemini, pencereyi, manzarayı ya da odanın boyutunu değiştirme. Sadece mobilya ekle.
- Kusurları (çatlak, nem lekesi) yapay zekâyla gizleme.

Etiket yalnızca nezaket değil. 1 Ağustos 2026'da yürürlüğe giren reklam yönetmeliği değişikliğine göre reklamda yapay zekâ kullanımı tüketicinin ekonomik davranışını önemli ölçüde etkileyebilecekse, bu kullanım açık ve ayırt edilebilir biçimde belirtilmeli. Boş bir evi döşenmiş gösteren ilan görseli bu kapsama girebilir.

Gerçek sanılabilecek yapay zekâ görselleri için genel kurallar [etiket rehberinde](rehber:yapay-zeka-icerik-etiketi).

> SAHA: Bir emlak danışmanıyla konuş: Sanal döşenmiş görseller müşterinin ilgisini artırıyor mu, yoksa evi görünce hayal kırıklığı mı yaratıyor? Kimliğini belirtmeden bir iki cümle ekle.

## EİDS yetki doğrulaması ne istiyor? {#eids}

Ticaret Bakanlığı'nın Elektronik İlan Doğrulama Sistemi (EİDS) ile emlak işletmelerinin verdiği kiralık ilanlarda yetki doğrulaması daha önce başladı; 1 Şubat 2026'dan beri konut, arsa ve iş yeri dahil bütün satılık taşınmaz ilanlarında da zorunlu. Mal sahibinin e-Devlet üzerinden senin işletmene yetki vermesi gerekiyor; doğrulama olmadan ilan yayımlanamıyor. Bu süreçte yapay zekâya bir rol yok; ama ilan metnindeki bilgilerin yetki verilen taşınmazla birebir uyması gerekiyor.

## Müşteri mesajları için şablon {#yazisma}

```sablon
[ALICI / KİRACI / MAL SAHİBİ] için şu konuda kısa ve profesyonel bir mesaj yaz: [KONU, ÖRNEĞİN "TEKLİFİNİZİ MAL SAHİBİNE İLETTİM, CEVAP BEKLİYORUM"]. Söz verme, tarih uydurma; sadece verdiğim bilgileri kullan. Ton: [SAMİMİ / RESMÎ].
```

Mal sahibine haftalık bilgi notu, gösterim sonrası geri bildirim özeti ve teklif yazışmaları için de aynı yaklaşım işe yarar. Zor müşteri konuşmaları için [zor e-postalar rehberine](rehber:zor-e-postalar) bak.

## Bölge ve fiyat bilgisini yapay zekâdan almak güvenli mi? {#bolge}

Yapay zekâya bir semtin özelliklerini, ulaşımını ve sosyal olanaklarını özetletebilirsin; ama:

- Güncel fiyat, kira ve satış rakamlarını yapay zekâdan alma; resmî ve güvenilir veri kaynaklarından ve kendi işlemlerinden al.
- İmar durumu, deprem riski, tapu şerhleri gibi bilgileri ilgili belediyeden, tapu müdürlüğünden ya da resmî sistemlerden kontrol et. Yapay zekâ bu konularda yanlış ya da eski bilgi verebilir.
- Derinlemesine bir bölge araştırması için [derin araştırma rehberindeki](rehber:derin-arastirma) kontrol yöntemini kullan.

## Müşteri verisini yapay zekâya yazabilir misin? {#kvkk}

Alıcı ve kiracıların kimlik bilgileri, gelir durumları ve telefonları, 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) kapsamında kişisel veri; bunları korumak veri sorumlusu olarak senin işletmenin yükümlülüğü. Bir mesaj yazdırırken müşterinin adını, telefonunu ya da kimlik bilgilerini yapay zekâya yapıştırma. Tapu ve kimlik belgelerini sohbet araçlarına yükleme; nedenleri [e-Devlet belgeleri rehberinde](rehber:e-devlet-belgesi-yapay-zeka).

## Sık yapılan hatalar {#hatalar}

- **Yapay zekânın eklediği "deniz manzarası".** Her ilan metnini bilgilerle karşılaştır.
- **Sanal döşemeyi etiketlememek.**
- **Fiyat ve getiri tahminini ilana koymak.**
- **Aynı metni farklı ilanlara kopyalamak.** İlan siteleri ve müşteriler fark ediyor.

## Dürüst sınır {#sinir}

Yapay zekâ yazıyı hızlandırır; bölgeyi tanımanın, mal sahibiyle güven ilişkisinin ve doğru fiyatlamanın yerini tutmaz. İlan ve reklam kuralları ile taşınmaz ticareti mevzuatı değişebiliyor; şüpheli bir durumda odana ya da bir hukukçuya danış.

## Sonraki adım {#sonraki-adim}

Portföyündeki bir ilanı şablonla yeniden yazdır ve eski metinle karşılaştır. Sanal döşeme kullanıyorsan, etiketlerin ve gerçek fotoğrafların ilanda olduğunu kontrol et.

## Kaynaklar

- EİDS ile satılık taşınmaz ilanlarında 1 Şubat 2026'dan itibaren yetki doğrulaması: [Hukuki Haber, 2 Ocak 2026](https://www.hukukihaber.net/satilik-konut-ilanlarina-yetki-sarti-geliyor) · [Ticaret Bakanlığı](https://ticaret.gov.tr/)
- 6502 sayılı Tüketicinin Korunması Hakkında Kanun: [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/)
- Taşınmaz Ticareti Hakkında Yönetmelik: [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/)
- Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği'nde değişiklik, Resmî Gazete 1 Temmuz 2026 (33297): [Resmî Gazete](https://www.resmigazete.gov.tr/eskiler/2026/07/20260701-9.htm)
