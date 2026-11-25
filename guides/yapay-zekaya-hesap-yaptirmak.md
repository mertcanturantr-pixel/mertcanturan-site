---
title: Yapay zekâya hesap yaptırmak: KDV, yüzde, taksit ve neden "kodla hesapla" demelisin
slug: yapay-zekaya-hesap-yaptirmak
seo_title: Yapay zekâya doğru hesap yaptırmak: KDV, yüzde, taksit
description: Yapay zekâ neden basit hesapta yanılır, kodla hesaplatmak ve Excel formülü istemek; KDV dahil-hariç, yüzde değişim ve taksit için şablonlar ve kontrol.
summary: Sohbet robotları hesapta yanılabiliyor. Hesabı kodla ya da formülle yaptırmak, KDV dahil ve hariç fiyat, yüzde değişim, taksit ve faiz hesabında doğru soru ve sonucu kontrol etmek.
keywords: chatgpt hesap hatası yapıyor, yapay zeka matematik yanlış, chatgpt ile hesap yapma, kdv dahil fiyattan kdv hariç hesaplama, kdv hesaplama formülü yüzde 20, yüzde artış hesaplama, kredi taksit hesaplama yapay zeka, chatgpt kod çalıştırarak hesapla, excel formülü yazdırma, yapay zeka hesap makinesi
type: sablon
topic: gunluk
audience: Herkes, Esnaf
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: KDV kararı künyesi ve tarih bağlamı eklendi, başlıklar soru biçimine çevrildi, iç bağlantılar artırıldı.
video:
video_title:
draft: false
---

ChatGPT'ye bir fatura toplatıyorsun, sonuç makul görünüyor ve geçiyorsun. Sonra hesap makinesiyle kontrol ettiğinde bir kalemin atlandığını ya da bir yüzdenin yanlış uygulandığını görüyorsun. Dil modelleri hesap makinesi değil: Metni kelime kelime tahmin ederek yazıyorlar ve sayılarla çalışırken de bazen bu tahmini yapıyorlar. Uzun toplama, ondalıklı sayılar, birden fazla adımı olan hesaplar ve Türkçe sayı biçimi (binlik nokta, ondalık virgül) en sık hata yapılan yerler.

Kısaca: Hesabı yapay zekânın "kafadan" yapmasını isteme. "Bunu kod çalıştırarak hesapla" de ya da sana bir Excel formülü yazdır. Formülü ve bir örnek sonucu kendin kontrol et. Para, vergi ve sözleşme gibi konularda son kontrolü hesap makinesi ya da bir uzman yapsın.

## Neden yanılıyor? {#neden}

Bir dil modeli "1.247,50 + 389,90" gördüğünde, bunu bir hesap makinesi gibi toplamıyor; doğru olması en olası görünen sonucu yazıyor. Kısa ve yaygın hesaplarda genellikle doğru tutturuyor. Ama:

- Çok kalemli toplamlarda bir kalemi atlayabiliyor.
- Binlik ayıracı ondalık sanabiliyor (1.247 → bir virgül iki yüz kırk yedi).
- Çok adımlı hesaplarda bir ara sonucu yanlış taşıyabiliyor.
- Yüzde artış ve azalışta tabanı karıştırabiliyor.

Kasım 2026 itibarıyla ChatGPT, Gemini ve Claude hesap ya da veri analizi için kod çalıştırabiliyor; bazı planlarda ve uygulamalarda bu özellik kapalı ya da sınırlı olabilir. Kodla yapılan hesap, tahmin değil gerçek hesap.

## Yapay zekâya hesap nasıl doğru yaptırılır? {#kod}

```sablon
Aşağıdaki hesabı kafadan yapma; kod çalıştırarak hesapla. Önce verileri bir tablo olarak göster ki doğru okuduğunu kontrol edeyim, sonra hesabı yap ve sonucu iki ondalıkla, Türk biçiminde (binlik nokta, ondalık virgül) yaz.
Veriler: [VERİLER]
Hesap: [NE HESAPLANACAK]
```

İlk adımı (verileri tablo olarak göstermek) atlama: Hataların çoğu hesapta değil, sayıyı yanlış okumakta.

Kod çalıştıramayan bir araç kullanıyorsan ya da sonucu kendi dosyanda tekrar kullanacaksan, formül iste:

```sablon
Bu hesabı Excel'de yapmak istiyorum. A sütununda [NE], B sütununda [NE] var, veriler 2. satırdan başlıyor. Türkçe Excel için formülü yaz (noktalı virgülle) ve formülün her parçasının ne yaptığını tek cümleyle açıkla.
```

Formüllerle ilgili daha fazlası [Excel rehberinde](rehber:excel-yapay-zeka).

## KDV dahil ve hariç fiyat nasıl hesaplanır? {#kdv}

Kasım 2026 itibarıyla Türkiye'de 3065 sayılı Katma Değer Vergisi Kanunu'na göre uygulanan oranlar yüzde 1, yüzde 10 ve yüzde 20; genel oran 10 Temmuz 2023'ten beri yüzde 20. Hangi mal ya da hizmete hangi oranın uygulandığı mevzuatla belirleniyor; emin değilsen muhasebecine sor, yapay zekâya sorma.

| Hesap | Formül | Örnek (yüzde 20) |
| --- | --- | --- |
| KDV hariç fiyattan KDV dahil fiyat | hariç × (1 + oran) | 1.000 × 1,20 = 1.200 |
| KDV dahil fiyattan KDV hariç fiyat | dahil ÷ (1 + oran) | 1.200 ÷ 1,20 = 1.000 |
| KDV dahil fiyatın içindeki KDV | dahil − dahil ÷ (1 + oran) | 1.200 − 1.000 = 200 |

En yaygın hata: KDV dahil fiyattan KDV'yi çıkarırken yüzde 20 indirim yapmak. 1.200'ün yüzde 20'si 240; ama içindeki KDV 200. Yapay zekâ da bu hatayı yapabiliyor.

## Yüzde artış ve azalış nasıl hesaplanır? {#yuzde}

- Fiyat 800'den 1.000'e çıktıysa artış: (1.000 − 800) ÷ 800 = yüzde 25.
- Fiyat 1.000'den 800'e indiyse düşüş: (1.000 − 800) ÷ 1.000 = yüzde 20.

Aynı fark, hangi sayıdan baktığına göre farklı yüzde. "Yüzde 25 zam yapıp sonra yüzde 25 indirim yaparsam eski fiyata dönerim" yanlış: 1.000 → 1.250 → 937,50. Yapay zekâya yüzde sorarken tabanı açıkça yaz: "800'e göre yüzde kaç arttı?"

## Kredi taksitini yapay zekâya hesaplatabilir misin? {#taksit}

Kredi, taksitli alışveriş ve kredi kartı hesapları bileşik faiz, vergiler (KKDF, BSMV) ve masraflar içerdiği için karmaşık. Yapay zekâ bunları kabaca tahmin edebilir ama banka ekranındaki sonuçla aynı çıkmayabilir.

```sablon
[TUTAR] TL'lik bir krediyi aylık [ORAN] faizle [AY] ayda eşit taksitle ödersem, aylık taksit ve toplam geri ödeme ne olur? Kod çalıştırarak hesapla. Vergi ve masrafları dahil etme, bunu ayrıca belirt. Sonucun bankanın hesabından neden farklı olabileceğini kısaca açıkla.
```

Kesin rakam için bankanın ödeme planına bak; karar vermeden önce yıllık maliyet oranını karşılaştır. Bu bir yatırım ya da kredi tavsiyesi değil; finansal kararlarda bir uzmana danış.

## Hesabın sonucunu nasıl kontrol edersin? {#kontrol}

- [ ] Yapay zekâ verileri doğru okumuş mu? (Tablo olarak göstermesini istemiştin.)
- [ ] Sonuç mantıklı bir büyüklükte mi? (100 TL'lik bir ürünün KDV'si 2.000 TL çıkmaz.)
- [ ] Bir kalemi hesap makinesiyle tekrar et.
- [ ] Yüzdelerde taban doğru mu?
- [ ] Ondalık ve binlik ayıraçları doğru mu?

Hesaptaki rakam bir rapora ya da habere dayanıyorsa, rakamın kendisini kaynağından nasıl doğrulayacağın [kontrol rehberinde](rehber:yapay-zeka-cevabini-kontrol-etmek#rakamlar).

## Sık yapılan hatalar {#hatalar}

- **Sohbette uzun bir listeyi toplatmak.** Kod ya da tablo kullan.
- **KDV'yi indirim gibi çıkarmak.** Formül tablosuna bak.
- **Vergi oranını yapay zekâya sormak.** Oranlar ve istisnalar değişiyor; resmî kaynağa ya da muhasebecine sor.
- **Sonucu kontrol etmeden fatura ya da teklife yazmak.** Bir rakam hatası, müşteriyle anlaşmazlık demek.

## Dürüst sınır {#sinir}

Kod çalıştıran yapay zekâ basit ve orta karmaşıklıktaki hesaplarda güvenilir; ama veriyi yanlış girersen sonuç da yanlış olur. Vergi beyannamesi, maaş bordrosu, kıdem tazminatı gibi mevzuata bağlı hesaplarda kurallar değiştiği için bir muhasebeci ya da resmî hesaplama aracı kullan; esnaf için muhasebeciye hazırlık [küçük işletme rehberinde](rehber:kucuk-isletme-yapay-zeka#muhasebe), muhasebecilerin yapay zekâyı nerede kullanıp nerede bırakması gerektiği [muhasebeciler rehberinde](rehber:muhasebeciler-icin-yapay-zeka#birakma).

## Sonraki adım {#sonraki-adim}

Son aldığın bir faturayı ya da market fişini yapay zekâya "kod çalıştırarak" toplat ve sonucu fişle karşılaştır. Sonra aynı şeyi "kafadan" toplatıp farkı gör.

## Kaynaklar

- 3065 sayılı Katma Değer Vergisi Kanunu ve oranlar: [Gelir İdaresi Başkanlığı](https://www.gib.gov.tr/)
- 7346 sayılı Cumhurbaşkanı Kararı (genel oran yüzde 18'den yüzde 20'ye, indirimli oran yüzde 8'den yüzde 10'a), Resmî Gazete 7 Temmuz 2023, yürürlük 10 Temmuz 2023: [Resmî Gazete](https://www.resmigazete.gov.tr/)
