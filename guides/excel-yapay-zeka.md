---
title: Excel ve Google E-Tablolar'da yapay zekâ: formül yazdırmak, veriyi temizlemek, hatayı bulmak
slug: excel-yapay-zeka
seo_title: Excel'de yapay zekâyla formül yazdırmak ve veri temizlemek
description: Türkçe Excel'de yapay zekâya formül yazdırmak, dağınık veriyi temizletmek ve sonucu kontrol etmek: İngilizce formül neden hata veriyor, hazır komutlar.
summary: Ne istediğini tarif et, formülü yapay zekâ yazsın. Türkçe Excel'de İngilizce formülün neden çalışmadığı, veriyi temizletmek, hatayı buldurmak ve sonucu kontrol etmek için komutlar.
keywords: excel yapay zeka formül yazdırma, chatgpt excel formülü, türkçe excel formül hatası, vlookup türkçe düşeyara, chatgpt formülü türkçe excel'de çalışmıyor, excel noktalı virgül virgül farkı, excel veri temizleme yapay zeka, telefon numarası düzenleme formülü, google e-tablolar yapay zeka formül, excel formül açıklatma
type: adim-adim
audience: Herkes, Çalışanlar, Küçük işletmeler, Muhasebe ve finans
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: anahtar kelimeler, Kısaca ve sık hatalar eklendi, başlıklar soru biçimine çevrildi, doğrulanamayan Microsoft bağlantısı çıkarıldı, iç bağlantılar artırıldı.
video:
video_title:
draft: true
---

Elinde iki bin satırlık bir müşteri listesi var. İsimlerin kimi büyük harf, kimi küçük; telefonların kimi "0532", kimi "+90 532" diye başlıyor. Üstüne bir de "geçen ay ödemesi gecikenlerin toplamı" isteniyor ve ÇOKETOPLA'nın sırasını hatırlamıyorsun. Yapay zekâ bu formülü saniyeler içinde yazar; yeter ki ona Türkçe Excel kullandığını söyle ve sonucu birkaç satırda kontrol et.

Kısaca: Yapay zekâya sütunlarını ve istediğin sonucu tarif et, formülü o yazsın, hesabı formül yapsın. Komutun başına "Türkçe Excel kullanıyorum, Türkçe işlev adları ve noktalı virgül kullan" yaz; yoksa `VLOOKUP` gibi İngilizce bir formül alırsın ve Türkçe Excel'de hata verir. Kişisel veri içeren dosyayı yükleme, yalnız sorunu anlat. Formülü kullanmadan önce sonucunu bildiğin iki üç satırda dene.

## Yapay zekâ tabloda en çok nerede işe yarıyor? {#ne-ise-yarar}

Üç işte gerçekten zaman kazandırıyor:

1. Formül yazmak ve açıklamak. Ne istediğini düz Türkçeyle anlatıyorsun, formülü o yazıyor. Başkasından kalma, anlamadığın bir formülü de satır satır açıklatabiliyorsun.
2. Hata bulmak. #YOK, #DEĞER! ya da yanlış toplam veren bir formülün neden bozulduğunu çoğu zaman ilk denemede buluyor.
3. Temizlik planı çıkarmak. Dağınık bir sütunu nasıl düzelteceğini, hangi formülle ya da hangi menüyle yapacağını sıralıyor.

Bir işte ise dikkatli olmak gerekiyor: sayıları sohbete yapıştırıp toplamı yapay zekâya hesaplatmak. Dil modelleri hesap makinesi değil; uzun bir listede bir rakamı atlayabiliyor ya da yanlış toplayabiliyor. Kural basit: hesabı yapay zekâ değil, onun yazdığı formül yapsın. Neden yanıldığı ve kodla hesaplatma yolu [hesap rehberinde](rehber:yapay-zekaya-hesap-yaptirmak#neden).

## ChatGPT'nin verdiği formül Türkçe Excel'de neden çalışmıyor? {#turkce-excel}

Yapay zekâya Excel formülü sorduğunda büyük ihtimalle İngilizce işlev adlarıyla ve virgülle ayrılmış bir formül alırsın: `=VLOOKUP(A2,F:G,2,FALSE)`. Excel'in Türkçe sürümünde bu formül çalışmaz. Türkçe Excel iki şey ister: Türkçe işlev adı (`DÜŞEYARA`, `YANLIŞ`) ve bağımsız değişkenler arasında noktalı virgül. Aynı formülün Türkçesi şöyle: `=DÜŞEYARA(A2;F:G;2;YANLIŞ)`.

Bunu komutun başında bir kez söylemek bütün sorunu çözüyor: "Türkçe Excel kullanıyorum, Türkçe işlev adları ve noktalı virgül kullan." Aşağıdaki şablonların hepsinde bu cümle var.

En sık kullanılan işlevlerin Türkçe karşılıkları:

| İngilizce | Türkçe Excel | Ne yapar |
| --- | --- | --- |
| IF | EĞER | Koşula göre iki sonuçtan birini verir |
| SUMIF / SUMIFS | ETOPLA / ÇOKETOPLA | Koşula uyan satırları toplar |
| COUNTIF / COUNTIFS | EĞERSAY / ÇOKEĞERSAY | Koşula uyan satırları sayar |
| VLOOKUP | DÜŞEYARA | Bir tabloda değeri arayıp yanındaki sütunu getirir |
| XLOOKUP | ÇAPRAZARA | DÜŞEYARA'nın yenisi; her yöne arar |
| INDEX / MATCH | İNDİS / KAÇINCI | Eski sürümlerde ÇAPRAZARA'nın yerine kullanılır |
| IFERROR | EĞERHATA | Hata yerine senin istediğin değeri gösterir |
| TRIM | KIRP | Fazla boşlukları siler |
| PROPER | YAZIM.DÜZENİ | Her kelimenin ilk harfini büyütür |
| SUBSTITUTE | YERİNEKOY | Metindeki bir parçayı başka bir parçayla değiştirir |
| TEXTJOIN | METİNBİRLEŞTİR | Birden fazla hücreyi araya ayraç koyarak birleştirir (Excel 2019 ve sonrası) |
| TODAY | BUGÜN | Bugünün tarihini verir |

Hata adları da Türkçe: İngilizcedeki #N/A, Türkçe Excel'de #YOK olarak görünür; #VALUE! ise #DEĞER!.

Bir de sürüm meselesi var. ÇAPRAZARA, Microsoft 365 ve Excel 2021 ile geldi. Dosyan Excel 2019 ya da daha eski bir sürümde açılacaksa yapay zekâya bunu söyle, sana DÜŞEYARA ya da İNDİS ve KAÇINCI ile yazsın.

Google E-Tablolar'da durum biraz farklı. Google'ın yardım sayfasına göre E-Tablolar'da işlevlerin dilini İngilizce ve 21 başka dil arasında değiştirebiliyorsun. Ondalık ayırıcıyı tablonun yerel ayarı belirliyor; Türkiye ayarında ondalık ayırıcı virgül olduğu için formüllerde bağımsız değişkenler noktalı virgülle ayrılır. Hangi dili ve yerel ayarı kullandığını komutta söylemen yeterli.

> SAHA: Kendi bilgisayarındaki Excel'de ve Google E-Tablolar'da yukarıdaki DÜŞEYARA örneğini dene. İngilizce formülü yapıştırınca ne oldu, ekranda hangi hata çıktı? Ekran görüntüsü al.

## Yapay zekâya formül nasıl yazdırılır? {#formul}

Yapay zekâ senin dosyanı görmüyor. Bu yüzden en çok işe yarayan şey, sütunlarını ve iki üç örnek satırı tarif etmek. Gerçek müşteri bilgisi yerine uydurma örnek satırlar yaz; formül için gerçek veri gerekmiyor.

```sablon
Türkçe Excel kullanıyorum, Türkçe işlev adları ve noktalı virgül kullan. Excel sürümüm: [EXCEL SÜRÜMÜ]

Tablom şöyle:
[SÜTUNLAR METNİ]

Örnek satırlar (uydurma):
[ÖRNEK SATIRLAR METNİ]

İstediğim sonuç: [İSTEDİĞİM SONUÇ]
Formülü hangi hücreye yazacağım: [HÜCRE]

Bana tek bir formül ver. Altına formülün her parçasının ne yaptığını iki üç cümleyle açıkla.
Örnek satırlarda formülün ne sonuç vereceğini de yaz ki kontrol edebileyim.
```

Temsili bir örnek. Sütunları şöyle tarif ettin: A müşteri, B fatura tarihi, C tutar, D durum ("Ödendi" ya da "Ödenmedi"). İstediğin sonuç: ödenmemiş ve 30 günden eski faturaların toplamı. Beklediğin cevap buna benzer:

`=ÇOKETOPLA(C2:C500;D2:D500;"Ödenmedi";B2:B500;"<"&BUGÜN()-30)`

Formül C sütununu topluyor ama yalnızca iki koşulu birlikte sağlayan satırları: D sütununda "Ödenmedi" yazacak ve B sütunundaki tarih bugünden 30 gün öncesinden eski olacak. Yapay zekâ bunu sana açıklamazsa iste; açıklamasını okuduğunda formülün ne yaptığını anlamıyorsan, o formülü kullanma.

## Anlamadığın bir formülü nasıl açıklatırsın? {#aciklatmak}

Başkasından kalan bir dosyada uzun bir formülle karşılaştın ve ne yaptığını bilmiyorsun. Silmek de, dokunmamak da riskli.

```sablon
Türkçe Excel kullanıyorum. Aşağıdaki formülü bir Excel bilmeyene anlatır gibi parça parça açıkla:

[FORMÜL METNİ]

Sonra şunları yaz:
1. Bu formül hangi durumda yanlış sonuç verebilir?
2. Daha kısa ya da daha okunur bir yazımı var mı? Varsa ver, ama aynı sonucu verdiğini nasıl kontrol edeceğimi de söyle.
```

## Hata veren formülün sebebini nasıl buldurursun? {#hata}

Hata mesajını ve formülü birlikte ver. Yalnızca "formülüm çalışmıyor" dersen tahmin yürütür.

```sablon
Türkçe Excel kullanıyorum. Şu formül hata veriyor:

Formül: [FORMÜL METNİ]
Gördüğüm hata ya da yanlış sonuç: [HATA]
Formülün baktığı hücrelerde ne var: [HÜCRE İÇERİKLERİ METNİ]

Hatanın en olası üç sebebini sırayla yaz. Her biri için nasıl kontrol edeceğimi ve düzeltilmiş formülü ver.
```

En sık karşılaşılan sebepler şunlar, yapay zekâ da genellikle bunlardan birini bulur:

- Sayı gibi görünen ama metin olarak saklanan hücreler. Hücrenin sol üst köşesinde küçük yeşil bir üçgen varsa büyük ihtimalle budur. Toplamlar eksik çıkar, aramalar #YOK verir.
- Aranan değerde gizli bir boşluk. "Ahmet" ile "Ahmet " Excel için iki farklı metin. KIRP işlevi bunu temizler.
- Kaydırırken kayan aralık. Formülü aşağı çektiğinde arama tablosunun adresi de kayıyorsa `$` işaretiyle sabitlemek gerekir: `$F$2:$G$500`.
- Tarihin metin olarak yazılması. "15.11.2026" hücrede metin olarak duruyorsa tarih karşılaştırmaları çalışmaz.

## Dağınık veri yapay zekâyla nasıl temizlenir? {#temizlik}

Burada iki yol var ve hangisini seçeceğin verinin ne kadar hassas olduğuna bağlı.

Birinci yol, yapay zekâya veriyi değil sorunu anlatmak. Ona temizlik formüllerini yazdırıyorsun, formülleri kendi dosyanda çalıştırıyorsun. Veri bilgisayarından hiç çıkmıyor. Müşteri listesi, çalışan bilgisi ya da telefon numarası gibi kişisel veri içeren her dosyada bu yolu kullan.

Örneğin telefon numaraları "0532 123 45 67", "+90 532 123 4567" ve "(0532) 123-45-67" diye karışık yazılmışsa, hepsini 10 haneli tek bir biçime getiren formül şu olabilir:

`=SAĞDAN(YERİNEKOY(YERİNEKOY(YERİNEKOY(YERİNEKOY(A2;" ";"");"-";"");"(";"");")";"");10)`

Formül önce boşlukları, tireleri ve parantezleri siliyor, sonra sağdan 10 karakteri alıyor. Böylece başta 0 ya da +90 olması fark etmiyor: üçü de "5321234567" oluyor. Ama yurt dışı numarası ya da eksik haneli bir numara varsa yanlış sonuç verir; sonucu birkaç satırda gözle kontrol et.

```sablon
Türkçe Excel kullanıyorum, Türkçe işlev adları ve noktalı virgül kullan.

Temizlemem gereken sütun: [SÜTUN]
Bu sütunda gördüğüm sorunlar (uydurma örneklerle): [SORUNLAR METNİ]
Sonuçta her hücrenin nasıl görünmesini istiyorum: [İSTENEN BİÇİM]

Bana yan sütuna yazacağım bir temizleme formülü ver. Formülün hangi örnekte yanlış sonuç verebileceğini de söyle.
Formülle çözülmüyorsa Excel menüsünden adım adım nasıl yapacağımı yaz.
```

İkinci yol, dosyayı doğrudan yapay zekâ aracına yüklemek. Bazı araçlar dosyayı okuyup kendisi düzeltebiliyor. Kişisel veri içermeyen dosyalarda (ürün listesi, stok, kendi harcamaların) bu hızlıdır. Kişisel veri içeren bir dosyayı yüklemeden önce ad, telefon, e-posta ve kimlik numarası sütunlarını sil ya da "Müşteri 1, Müşteri 2" gibi kodlarla değiştir. Bir müşteri listesini olduğu gibi yüklemek, o kişilerin verisini başka bir şirkete aktarmak demek; neye dikkat edeceğin [yapay zekâya ne yazılmaz](rehber:yapay-zekaya-ne-yazilmaz) rehberinde.

## Özet tabloyu (pivot) yapay zekâ kurabilir mi? {#ozet-tablo}

Yapay zekâ özet tabloyu (pivot) senin yerine kuramaz ama sana hangi alanı nereye sürükleyeceğini söyleyebilir. Sorunu şöyle sor: "Satış tablomda A sütununda tarih, B'de şube, C'de tutar var. Her şubenin aylık toplamını görmek istiyorum. Türkçe Excel'de özet tabloyu adım adım nasıl kurarım, hangi alanı Satırlar'a, hangisini Sütunlar'a koyarım?" Hangi grafiğin uygun olduğunu da aynı şekilde sorabilirsin. Menü adlarının senin Excel sürümünde biraz farklı olabileceğini akılda tut.

## Excel'deki Copilot ya da E-Tablolar'daki Gemini daha mı iyi? {#copilot-gemini}

Microsoft 365'teki Copilot ve Google Workspace'teki Gemini, aynı işleri dosyanın içinden, veriyi görerek yapıyor. Kasım 2026 itibarıyla hangi planda hangi özelliğin açık olduğu sık değişiyor ve ikisi de en geniş hâliyle ücretli planlarda çalışıyor; kendi planında ne olduğunu Microsoft ve Google'ın yardım sayfasından kontrol et. Bu rehberdeki yöntem ücretsiz sohbet araçlarıyla da çalışıyor. Dosyanın içindeki asistanı kullanıyorsan da aynı kurallar geçerli: ne istediğini net tarif et, sonucu formülle doğrula, kişisel veriye dikkat et.

> SAHA: Excel'de Copilot'u ya da E-Tablolar'da Gemini'yi kendi hesabında denediysen hangi planda olduğunu ve ilk denemede ne yaptığını iki cümleyle yaz. Denemediysen bu notu silelim.

## Formüle güvenmeden önce hangi beş kontrolü yapmalısın? {#kontrol}

- [ ] **Bildiğin bir satırda dene.** Sonucunu elle bildiğin iki üç satırda formülün aynı sonucu verdiğini gör.
- [ ] **Uç durumları dene.** Boş hücre, sıfır, metin olarak yazılmış sayı ve listede olmayan bir değerle ne oluyor?
- [ ] **Aşağı çekince aralık kayıyor mu?** Sabit kalması gereken adreslerde `$` var mı?
- [ ] **Toplamı başka yoldan karşılaştır.** Özet tablo ya da filtreyle bulduğun toplam, formülün toplamıyla aynı mı?
- [ ] **Açıklamasını anladın mı?** Formülün ne yaptığını birine anlatamıyorsan kullanma.

## Sık yapılan hatalar {#hatalar}

- **Excel sürümünü ve dilini söylememek.** İngilizce ya da senin Excel'inde olmayan bir işlevle (ör. eski sürümde ÇAPRAZARA) yazılmış formül alırsın.
- **Gerçek müşteri listesini yapıştırmak.** Formül için uydurma örnek satırlar yeter; kişisel veri sohbete girmez.
- **Toplamı sohbete hesaplatmak.** Uzun listede rakam atlanabilir; formül iste.
- **Formülü tek satırda deneyip bütün sütuna uygulamak.** Boş hücre, metin olarak saklanmış sayı ve listede olmayan değer en sık sürprizi çıkarır.
- **Kuralı yapay zekâdan almak.** KDV oranı, faiz ya da prim gibi bir kuralı yapay zekâ söyledi diye formüle koymak; oranın kendisini resmî kaynaktan al.

## Dürüst sınır {#sinir}

Formülün doğru çalışması, sonucun doğru olduğu anlamına gelmez. KDV oranı, gecikme faizi, prim ya da vergi gibi bir kural yanlış girildiyse formül o yanlışı kusursuz biçimde hesaplar. Yapay zekâya formülü yazdırabilirsin, ama kuralın kendisini (hangi oran, hangi tarihten itibaren) muhasebecinden ya da resmî kaynaktan al. Yapay zekânın söylediği bir oranı formüle doğrudan koyma. Muhasebe dosyalarında nereye kadar güvenilebileceği [muhasebeciler rehberinde](rehber:muhasebeciler-icin-yapay-zeka#excel).

## Sonraki adım {#sonraki-adim}

Bugün dosyalarından birinde seni en çok uğraştıran sütunu seç ve temizleme şablonunu dene. Formülü kendi dosyanda iki üç satırda kontrol ettikten sonra bütün sütuna uygula. Esnafsan fiyat ve stok hesabı için [küçük işletme rehberindeki](rehber:kucuk-isletme-yapay-zeka#hesap) öneriye bak; komutlarını daha iyi kurmak istersen [yapay zekâya iyi komut yazmak](rehber:yapay-zekaya-iyi-komut-yazmak) rehberine geç.

## Kaynaklar

- [Microsoft Destek: DÜŞEYARA işlevi](https://support.microsoft.com/tr-tr/Excel/functions/vlookup-function)
- [Microsoft Destek: Kategorilerine göre Excel işlevleri (Türkçe adlar)](https://support.microsoft.com/tr-TR/Excel/excel-functions-by-category)
- [Microsoft Destek: Arama ve başvuru işlevleri](https://support.microsoft.com/tr-tr/Excel/lookup-and-reference-functions-reference)
- [Google E-Tablolar Yardım: İşlev listesi ve işlev dili](https://support.google.com/docs/table/25273?hl=tr)
- [Google E-Tablolar Yardım: Sayı biçimi ve yerel ayar](https://support.google.com/docs/answer/56470?hl=tr)
