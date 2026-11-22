---
title: Muhasebeciler için yapay zekâ: mükellef yazışmaları, mevzuat takibi ve sır saklama
slug: muhasebeciler-icin-yapay-zeka
seo_title: Muhasebeciler için yapay zekâ: işe yarayan yerler ve sınırlar
description: Mali müşavir ve muhasebeciler için yapay zekâ: mükellefe açıklama, mevzuat özeti, Excel ve mutabakat; mükellef verisi, sır saklama, doğrulama.
summary: Mali müşavir ve muhasebeci için yapay zekâ: mükellefe sade açıklama, mevzuat değişikliği özeti, Excel ve mutabakat işleri; mükellef verisi, sır saklama ve uydurma mevzuat riski.
keywords: muhasebeciler için yapay zeka, mali müşavir chatgpt kullanımı, smmm yapay zeka, mükellefe mesaj şablonu, tebliğ özeti yapay zeka, banka ekstresi sınıflandırma, excel mutabakat yapay zeka, mükellef bilgisi chatgpt gizlilik
type: sablon
audience: Mali müşavirler, Muhasebeciler
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: kurum ve kanun adları tamamlandı, başlıklar soru biçimine çevrildi, iç bağlantılar eklendi.
video:
video_title:
draft: true
---

Bir mali müşavirlik bürosunda ay sonu: beyanname dönemi, mükelleflerden gelen sonu gelmeyen sorular, yeni bir tebliğ, karşılaştırılması gereken iki Excel dosyası. Yapay zekâ bu yükün bir kısmını hafifletebilir: mükellefe bir vergi kuralını sade dille anlatan bir mesaj, bir tebliğin ilk okuması, karmaşık bir formül. Ama muhasebede iki kırmızı çizgi var: Mükellefin bilgisi bir sır ve yapay zekânın yazdığı oran, süre ya da madde numarası yanlış olabilir.

Kısaca: Mali müşavir yapay zekâyı mükellefe sade açıklama, mevzuatın ilk okuması ve Excel işlerinde güvenle kullanabilir; ama mükellef adı, vergi numarası ve tutarları çıkararak ya da kurumsal planlı bir araçla. Her oranı ve süreyi Gelir İdaresi Başkanlığı'nın (GİB) kaynaklarından ve Resmî Gazete'den doğrula. Hesapları sohbette değil, Excel formülüyle ya da kodla yaptır.

## Mükellefe vergi kuralını sade dille nasıl anlatırsın? {#mukellef}

Mükelleflerin çoğu vergi dilini anlamıyor. Yapay zekâ, senin bildiğin kuralı sade bir mesaja çevirmekte iyi:

```sablon
Bir mükellefime şu konuyu sade bir dille anlatan kısa bir mesaj yaz: [KONU, ÖRNEĞİN "BU AY KDV İADESİNİN NEDEN GECİKECEĞİ"].
Doğru bilgiler (sadece bunları kullan): [SENİN BİLDİĞİN KURAL, TARİH VE TUTARLAR, MÜKELLEF ADI OLMADAN]
Ton: saygılı, net, teknik terim varsa parantez içinde açıklama. En fazla 120 kelime. Benim vermediğim bir oran, tarih ya da madde ekleme.
```

## Yeni tebliğ ya da kanun değişikliği nasıl özetletilir? {#mevzuat}

Yeni bir tebliğ ya da kanun değişikliği yayımlandığında, metnin kendisini (Resmî Gazete'den ya da GİB'in sitesinden aldığın metni) yapay zekâya verip ilk özeti çıkartabilirsin:

```sablon
Aşağıdaki mevzuat metnini oku ve şunları çıkar:
1. Kimleri etkiliyor?
2. Ne değişiyor (eski kural / yeni kural)?
3. Yürürlük tarihi ve varsa geçiş hükümleri.
4. Mükelleflerimiz için yapılması gereken işler.
Her maddenin yanına metnin ilgili fıkrasını yaz. Metinde olmayan bir şey ekleme; belirsiz yerleri "belirsiz" diye işaretle.
Metin: [METİN]
```

Yapay zekâya mevzuatı metin vermeden sorma; eski bir kuralı güncel sanabilir, madde numarası uydurabilir. [Avukatlar için anlattığımız](rehber:avukatlar-icin-yapay-zeka#dogrulama) uydurma kaynak riski muhasebede de aynı; kontrol yöntemi [kontrol rehberinde](rehber:yapay-zeka-cevabini-kontrol-etmek#hukuk).

> SAHA: Bir mali müşavirle konuş: Yapay zekâyı en çok hangi işte kullanıyor, hangi işte hiç kullanmıyor? İzin alarak, kimliğini ve mükellef bilgisi vermeden bir iki cümle ekle.

## Excel ve banka mutabakatında yapay zekâ {#excel}

- **Formül:** Karmaşık bir DÜŞEYARA, ÇAPRAZARA ya da koşullu toplam formülü yazdırmak. Ayrıntısı [Excel rehberinde](rehber:excel-yapay-zeka).
- **İki listeyi karşılaştırmak:** Banka hareketleri ile muhasebe kayıtları arasındaki farkları bulmak için formül ya da kod.
- **Banka hareketlerini sınıflandırmak:** Açıklama sütununa göre hareketleri kategorilere ayırmak. Kişi adlarını ve hesap numaralarını çıkararak çalış.

Hesapları sohbet içinde "kafadan" yaptırma; nedenleri [hesap rehberinde](rehber:yapay-zekaya-hesap-yaptirmak).

## Mükellef bilgisi yapay zekâya yazılabilir mi? {#sir}

3568 sayılı Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik Kanunu ve meslek ahlak kuralları, meslek mensuplarına işleri dolayısıyla öğrendikleri sırları saklama yükümlülüğü getiriyor. Mükellef verisi aynı zamanda 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) kapsamında kişisel veri ve çoğu zaman ticari sır.

- [ ] Kişisel bir yapay zekâ hesabına mükellef adı, vergi numarası, kimlik numarası, banka bilgisi ya da gerçek tutarlar yapıştırma.
- [ ] Mükellef verisiyle çalışman gerekiyorsa, verilerin eğitimde kullanılmadığı ve sözleşmeyle korunduğu kurumsal bir plan kullan ve bunu büro politikana yaz.
- [ ] Bir belgeyle çalışmadan önce isimleri ve numaraları "Mükellef A", "Firma B" gibi etiketlerle değiştir.
- [ ] Gizli bir belgeyi analiz etmen gerekiyorsa [yerel model rehberindeki](rehber:yerel-model#gizli-belge) seçeneği değerlendir.

Büro için kısa bir kullanım politikası yazmak istersen [şirket politikası rehberindeki](rehber:sirket-yapay-zeka-politikasi#taslak) taslağı kullan.

## Hangi işler yapay zekâya bırakılmaz? {#birakma}

- Beyanname, bildirge ve resmî kayıtların son hâli.
- Vergi oranı, istisna ve süre kararları.
- Mükellefe "bu işlem vergisizdir" ya da "ceza çıkmaz" gibi sonuç bildiren tavsiyeler.
- e-Defter, e-Fatura ve muhasebe programına doğrudan veri girişi; yapay zekânın hazırladığı bir veri, sisteme girmeden önce kontrol edilmeli.

## Sık yapılan hatalar {#hatalar}

- **Oranı yapay zekâya sormak.** Resmî kaynaktan al.
- **Mükellef dosyasını kişisel hesaba yüklemek.**
- **Yapay zekânın mesajını kontrol etmeden mükellefe göndermek.** Yanlış bir tarih, ceza demek olabilir.
- **Eski bilgiyle cevap.** Yapay zekânın bilgisi belli bir tarihte kalmış olabilir; güncel değişiklikleri bilmeyebilir.

## Dürüst sınır {#sinir}

Yapay zekâ yazışmayı, ilk okumayı ve tablo işlerini hızlandırıyor; mesleki muhakemenin ve sorumluluğun yerini tutmuyor. Vergi mevzuatı sık değişiyor ve istisnalar çok; her mesleki kararın sorumluluğu meslek mensubunda. Meslek odanın ve TÜRMOB'un yapay zekâ konusundaki güncel duyurularını takip et.

## Sonraki adım {#sonraki-adim}

Bu ay mükelleflerinden en çok gelen üç soruyu seç ve her biri için sade açıklama şablonuyla bir mesaj hazırla; kaydedip tekrar kullan. Bir sonraki mevzuat değişikliğinde özet şablonunu dene ve özetini metinle karşılaştır.

## Kaynaklar

- Gelir İdaresi Başkanlığı, mevzuat: [gib.gov.tr](https://www.gib.gov.tr/)
- Resmî Gazete: [resmigazete.gov.tr](https://www.resmigazete.gov.tr/)
- 3568 sayılı Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik Kanunu: [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/)
- TÜRMOB: [turmob.org.tr](https://www.turmob.org.tr/)
