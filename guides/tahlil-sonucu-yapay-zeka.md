---
title: Tahlil sonucunu yapay zekâya sormak: neyi anlatabilir, neyi asla söyleyemez?
slug: tahlil-sonucu-yapay-zeka
seo_title: Kan tahlili sonucunu yapay zekâya sormak: güvenli kullanım
description: Tahlil sonucunu yapay zekâya sorarken kimliğini çıkarmak, terimleri anlamak, doktora soru hazırlamak; teşhis ve ilaç kararında neden kullanılmamalı.
summary: Tahlil sonucunu yapay zekâya sormak: kimlik bilgilerini çıkarmak, değerleri ve terimleri anlamak, doktora soru listesi hazırlamak, acil belirtiler ve yapay zekânın asla yapamayacakları.
keywords: tahlil sonucu yapay zeka, kan tahlili yorumlama chatgpt, chatgpt'ye tahlil sonucu sormak, e-nabız tahlil sonucu nasıl okunur, referans aralığı dışında değer, tahlil sonucu yüksek çıktı, doktora sorulacak sorular, sağlık verisi kvkk, tahlil sonucu yapay zekaya yorumlatma
type: sablon
topic: guvenlik
audience: Herkes
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: ChatGPT Health durumu Kasım 2026'ya göre netleştirildi, KVKK tam adı, Kısaca alıntılanabilir hâle getirildi, başlıklar soru biçimine çevrildi, iç bağlantılar
video:
video_title:
draft: false
---

e-Nabız'a tahlil sonucun düşüyor; bazı değerlerin yanında yukarı ya da aşağı ok var ve doktor randevun bir hafta sonra. Merakla sonucu ChatGPT'ye yapıştırıyorsun. Yapay zekâ burada gerçekten işe yarayabilir: Terimleri anlatabilir, bir değerin genelde neyle ilişkili olduğunu söyleyebilir, doktoruna ne soracağını hazırlamana yardım edebilir. Ama teşhis koyamaz, seni muayene edemez ve geçmişini bilmez. Ve sağlık bilgin, paylaşabileceğin en hassas bilgilerden biri.

Kısaca: Tahlil sonucunu yapay zekâya sorabilirsin, ama yalnızca terimleri anlamak ve doktoruna soru hazırlamak için; teşhis koyamaz, seni muayene edemez. Değerleri yapıştırmadan önce adını, T.C. kimlik numaranı ve kurum bilgilerini çıkar, laboratuvarın referans aralıklarını ekle. İlacını ya da tedavini onun cevabına göre değiştirme; belirtilerin varsa randevuyu bekleme.

## Tahlil sonucunu yüklemeden önce neyi çıkarmalısın? {#gizlilik}

Sağlık verisi, 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) m.6'ya göre özel nitelikli kişisel veri. Bir sohbet aracına yüklediğinde o şirketin sunucusuna gidiyor.

- [ ] PDF ya da ekran görüntüsü yerine yalnızca değerleri yaz ya da kopyala.
- [ ] Ad, soyad, T.C. kimlik numarası, protokol numarası, hastane adı, barkod: hiçbiri gerekmiyor; çıkar.
- [ ] Yaşını ve cinsiyetini yazabilirsin; referans aralıkları buna göre değişiyor.
- [ ] Aracın sohbetleri eğitimde kullanma ayarını kontrol et; ayrıntısı [gizlilik ayarları rehberinde](rehber:yapay-zeka-gizlilik-ayarlari).

OpenAI, Ocak 2026'da duyurduğu ve tıbbi kayıt bağlanabilen ayrı sağlık bölümünü (ChatGPT Health) Temmuz 2026'da ABD'deki kullanıcılara açtı. Kasım 2026 itibarıyla bu bölüm Türkiye'de yok; Türkiye'den kullanıyorsan sıradan sohbet içinde soruyorsun ve genel gizlilik ayarların geçerli. Neleri hiç yazmaman gerektiği [ne yazılmaz rehberinde](rehber:yapay-zekaya-ne-yazilmaz).

## Yapay zekâya tahlil sonucu nasıl sorulur? {#sablon}

```sablon
[YAŞ] yaşında bir [KADIN / ERKEK] için tahlil sonuçları aşağıda. Teşhis koymadan şunları yap:
1. Her değerin neyi ölçtüğünü bir cümleyle açıkla.
2. Laboratuvarın referans aralığının dışında kalan değerleri listele ve bu tür bir sapmanın genelde hangi durumlarla ilişkili olabileceğini, ciddi olmayan nedenler dahil, kısaca yaz.
3. Doktoruma sorabileceğim beş soru öner.
4. Bu sonuçlarda doktora daha erken gitmemi gerektirebilecek bir durum varsa açıkça söyle.
Kullandığım ilaçlar: [VARSA, İLAÇ ADLARI]
Sonuçlar (değer, birim, referans aralığı):
[SONUÇLAR]
```

Referans aralığını mutlaka ekle: Laboratuvardan laboratuvara değişiyor ve yapay zekâ kendi bildiği aralığı kullanırsa yanlış bir değerlendirme yapabilir.

## Cevabı nasıl okumalı? {#okuma}

- **"İlişkili olabilir" teşhis değil.** Yüksek bir değerin on farklı nedeni olabilir; çoğu ciddi değil. Yapay zekâ bazen en korkutucu olanı öne çıkarıyor, bazen de ciddi bir durumu hafife alıyor.
- **Tek bir değer tek başına anlam taşımayabilir.** Doktor sonucu belirtilerine, muayenene, geçmiş sonuçlarına ve ilaçlarına göre değerlendiriyor.
- **Eski sonuçlarla karşılaştırma.** e-Nabız'daki önceki sonuçlarını da eklersen yapay zekâ değişimi gösterebilir; ama yorumu yine doktorun.

Yapay zekânın verdiği bir bilgi seni endişelendirdiyse, bir sağlık kuruluşunun ya da Sağlık Bakanlığı'nın sayfasından kontrol et; forum ve sosyal medya kaynaklarına güvenme. Bir cevabı kontrol etmenin genel yolu [kontrol rehberinde](rehber:yapay-zeka-cevabini-kontrol-etmek).

## Yapay zekânın cevabıyla asla ne yapmamalısın? {#asla}

- İlacını yapay zekânın cevabına göre bırakma, dozunu değiştirme ya da yeni ilaca başlama.
- Doktorun söylediğiyle yapay zekânın söylediği çelişiyorsa yapay zekâya güvenme; doktoruna sor, gerekirse ikinci bir doktora danış.
- Çocuğunun ilaç dozunu yapay zekâya sorma; ilacın prospektüsüne, eczacına ya da doktora sor.

Sağlık, para ve hukuk kararlarını neden yapay zekâya bırakmaman gerektiği [karar rehberinde](rehber:yapay-zekaya-karar-verdirmek).

## Ne zaman randevuyu beklemeden doktora gitmelisin? {#acil}

Tahlil sonucundan bağımsız olarak göğüs ağrısı, nefes darlığı, bilinç bulanıklığı, ani güçsüzlük, şiddetli karın ağrısı, yüksek ateş ya da kanama gibi belirtilerin varsa randevuyu bekleme; acile git ya da 112'yi ara. Sonucunda "kritik değer" ibaresi varsa ya da laboratuvar seni aradıysa aynı gün bir doktora ulaş.

## Doktora giderken soru listesini nasıl kullanmalısın? {#doktor}

Yapay zekânın hazırladığı soru listesini telefonuna kaydet ya da yazdır. Muayenede "İnternette okudum" yerine "Şu değerin neden yüksek olduğunu ve neyi takip etmemiz gerektiğini öğrenmek istiyorum" demek, kısa muayene süresinde daha verimli bir konuşma sağlıyor.

## Sık yapılan hatalar {#hatalar}

- **PDF'yi olduğu gibi yüklemek.** Kimlik bilgilerini çıkar.
- **Referans aralığını vermemek.**
- **Cevabı teşhis sanmak.**
- **Kaygıyla aynı soruyu tekrar tekrar sormak.** Farklı cevaplar kaygını artırır; listeni hazırla ve doktoru bekle.

## Dürüst sınır {#sinir}

Yapay zekâ bir tahlil sonucunu doktordan daha sabırla açıklayabilir ama doktordan daha doğru yorumlayamaz. Sonucun, sağlık geçmişin ve muayenen birlikte değerlendirildiğinde anlam kazanıyor. Bu sayfa tıbbi tavsiye değil; sağlığınla ilgili kararlar için doktoruna danış.

## Sonraki adım {#sonraki-adim}

Son tahlil sonucunu e-Nabız'dan aç, değerleri kimlik bilgisi olmadan kopyala ve şablonla bir soru listesi hazırla. Listeyi bir sonraki doktor randevuna götür. Resmî belgelerle çalışırken nelere dikkat etmen gerektiği [e-Devlet belgeleri rehberinde](rehber:e-devlet-belgesi-yapay-zeka).

## Kaynaklar

- 6698 sayılı KVKK, m.6 (özel nitelikli kişisel veriler): [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/)
- e-Nabız: [enabiz.gov.tr](https://enabiz.gov.tr/)
- OpenAI, "Introducing ChatGPT Health", 7 Ocak 2026 (tıbbi kayıt bağlantısı yalnızca ABD'de): [openai.com](https://openai.com/index/introducing-chatgpt-health/)
