---
title: NotebookLM (yeni adıyla Gemini Notebook) ile kendi belgelerinden kaynak gösteren asistan kurmak
slug: notebooklm
seo_title: NotebookLM (Gemini Notebook) nasıl kullanılır? Belge asistanı
description: NotebookLM'in yeni adı Gemini Notebook. PDF, ders notu ve videolarından kaynak numaralı cevap, sesli özet; ücretsiz planda 50 kaynak sınırı ve gizlilik.
summary: NotebookLM, Temmuz 2026'dan beri Gemini Notebook adıyla sürüyor. PDF, not ve videolarından kaynak gösteren asistan kurmak: kurulum, komutlar, ücretsiz sınırlar ve gizlilik.
keywords: notebooklm nasıl kullanılır, gemini notebook nedir, notebooklm türkçe, notebooklm ücretsiz mi, notebooklm kaynak sınırı, pdf özet çıkarma yapay zeka, ders notu yapay zeka, sesli özet audio overview, notebooklm gizlilik
type: adim-adim
audience: Herkes, Öğrenciler
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: Gemini Notebook adı ve tarihi (16 Temmuz 2026) doğrulandı, adres bilgisi düzeltildi, plan sınırları ve 5 saatlik kullanım sınırı, gizlilik ifadesi resmî sayfaya göre güncellendi, kaynaklar eklendi.
video:
video_title:
draft: true
---

ChatGPT'ye bir PDF yüklediğinde, cevap bazen belgeden, bazen modelin genel bilgisinden geliyor ve hangisi olduğunu her zaman anlayamıyorsun. Google'ın NotebookLM aracı (16 Temmuz 2026'dan beri adı Gemini Notebook) bunu farklı çözüyor: Senin eklediğin kaynaklara dayanarak cevap veriyor ve her cevabın yanına, belgenin hangi cümlesinden geldiğini gösteren bir numara koyuyor. Numaraya tıklayınca o cümleyi görüyorsun.

Kısaca: Ders notu, mevzuat seti, uzun rapor gibi belli bir belge yığınından soru soracaksan NotebookLM (Gemini Notebook) genel sohbet araçlarından daha uygun, çünkü cevabın hangi cümleye dayandığını gösteriyor. Ücretsiz planda bir not defterine 50 kaynak ekleyebiliyorsun. Kişisel hesapta yüklediklerin, geri bildirim vermediğin sürece modeli eğitmek için kullanılmıyor. Yine de numaraya tıklayıp asıl cümleyi okumadan cevaba güvenme.

Ad değişikliği hakkında bilmen gereken tek şey şu: Araç ayrı bir ürün olarak devam ediyor, adres aynı (notebooklm.google) ve eski bağlantılar çalışmaya devam ediyor. Gemini uygulamasında oluşturduğun not defterleri de bu siteyle eşitleniyor. İnsanlar hâlâ çoğunlukla "NotebookLM" diye aradığı için bu sayfada iki adı da kullanıyorum.

## NotebookLM nasıl kurulur? {#kurulum}

1. notebooklm.google adresine Google hesabınla gir. İstersen Gemini uygulamasındaki not defterleri bölümünden de başlayabilirsin.
2. Yeni bir not defteri oluştur.
3. Kaynak ekle: PDF, Google Dokümanlar ve Slaytlar, web sayfası bağlantısı, YouTube videosu, ses dosyası ya da yapıştırılmış metin.
4. Soldaki kaynak listesinden hangi kaynakların cevaplara dahil olacağını seç.
5. Ortadaki sohbet alanından soru sor.

Arayüz dilini ve cevap dilini Türkçe yapabilirsin. Kaynaklar Türkçe, İngilizce ya da karışık olabilir.

> SAHA: Gemini Notebook'un Türkçe arayüzünde çıktı dili ayarının yerini ve adını kontrol et; bir Türkçe PDF yükleyip soru sor ve cevaptaki kaynak numaralarının nasıl göründüğünü ekran görüntüsüyle kaydet.

## Ücretsiz planda sınırlar ne? {#sinirlar}

Google'ın plan sayfasına göre (Kasım 2026 itibarıyla, "değişebilir" notuyla):

| Plan | Not defteri sayısı | Not defteri başına kaynak |
|---|---|---|
| Ücretsiz (yapay zekâ planı yok) | 100 | 50 |
| Google AI Plus | 200 | 100 |
| Google AI Pro | 500 | 300 |
| Google AI Ultra | 500 | 500-600 |

Kaynak başına sınır planlardan bağımsız: en fazla 500 bin kelime ya da yerel yüklemede 200 MB. Sayfa sınırı yok.

Soru ve üretim hakları ise sabit bir sayı değil. 2 Eylül 2026'dan beri kişisel hesaplarda kullanım sınırı günlük değil, beş saatte bir yenileniyor ve sorunun karmaşıklığına, sohbetin uzunluğuna, kaynak sayısına ve kullandığın özelliğe (sesli özet, video özet gibi) göre hesaplanıyor. Yani kısa sorularla gün boyu rahat çalışırsın; üst üste sesli ve video özet ürettiğinde sınıra daha çabuk gelirsin.

Pratikte ücretsiz plan, bir dönemlik ders notu ya da birkaç yüz sayfalık bir rapor seti için yeter.

## Hangi işlerde gerçekten işe yarıyor? {#kullanimlar}

**Ders notları ve sınava hazırlık:** Bir dersin bütün slaytlarını ve notlarını bir not defterine koy. Sonra şunu sor:

```sablon
Bu kaynaklara dayanarak [KONU] hakkında sınavda çıkabilecek 10 soru hazırla. Her sorunun cevabını ve cevabın hangi kaynakta geçtiğini yaz. Kaynaklarda olmayan bir bilgiyi soru yapma.
```

Öğrenciler için diğer kullanımlar [öğrenci rehberinde](rehber:ogrenciler-icin#notlar).

**Mevzuat ya da kural seti:** Bir kanunun, yönetmeliğin ve ilgili rehberlerin metinlerini ekle. "Şu durumda süre ne?" gibi sorularda cevabın hangi maddeden geldiğini görürsün. Yine de maddeyi kendin aç ve oku; eklediğin metnin güncel hâli olup olmadığını da mevzuat.gov.tr'den kontrol et. Nasıl yapılacağı [kontrol rehberinde](rehber:yapay-zeka-cevabini-kontrol-etmek#hukuk).

```sablon
Yalnızca eklediğim kaynaklara dayanarak cevap ver: [SORU]. Cevabın dayandığı madde numarasını ve kaynağın adını yaz. Kaynaklarda açık bir cevap yoksa "kaynaklarda yok" de, tahmin yürütme.
```

**Uzun raporlar:** Birkaç yıllık faaliyet raporunu ya da bir sektör raporunu ekleyip karşılaştırmalı soru sor: "Üç yılın raporlarında hedeflerdeki değişiklikleri tablo olarak çıkar."

**Toplantı ve görüşme kayıtları:** Ses dosyalarını yükleyip "Alınan kararları ve sorumluları listele" diye sor. Kaydı almadan önce katılımcılara haber ver ve izinlerini al; ayrıntısı [toplantı özeti rehberinde](rehber:toplanti-ozeti#izin).

**Sesli özet (Audio Overview):** Kaynaklarından iki sunucunun sohbet ettiği podcast tarzı bir ses dosyası üretiyor; Türkçe dahil 50'den fazla dilde. Yolda, sporda dinlemek için iyi. Ama bu bir özet: Sunucular bazı ayrıntıları basitleştirebilir ya da yanlış vurgulayabilir. Sınavdan önce tek kaynağın bu olmasın.

## Kaynak numaraları nasıl kullanılır? {#kaynak-numaralari}

Aracın asıl farkı kaynak numaraları; kullanmazsan diğer araçlardan farkı kalmaz. Bir karara ya da sınava dayanak olacak her cevapta:

- Numaraya tıkla ve cevabın dayandığı cümleyi oku.
- Cümle cevabı gerçekten destekliyor mu, yoksa araç bir yorum mu eklemiş, kontrol et.
- Numara olmayan bir iddia varsa, onu araçtan değil, belgeden doğrula.

Araç yalnızca senin kaynaklarına dayansa da, kaynakları yanlış okuyabilir ya da iki ayrı bilgiyi birleştirip yeni bir sonuç çıkarabilir. Numara bu yüzden var.

## Yüklediğim belgeler güvende mi? {#gizlilik}

Google'ın plan sayfasında kişisel hesaplar için yazan şu: Verilerin, geri bildirim vermediğin sürece Gemini Notebook'u eğitmek için kullanılmıyor. Geri bildirim verirsen (beğen/beğenme düğmesi gibi) Google o etkileşimin tamamını inceleyebiliyor. Workspace ve Workspace for Education hesaplarında yüklediklerin, soruların ve cevaplar yapay zekâ modellerini eğitmek için kullanılmıyor. Her iki durumda da belgelerin Google'ın sunucusunda işleniyor. Bu yüzden:

- Müşteri dosyaları, sağlık kayıtları, kimlik bilgisi içeren belgeler yükleme. Başkasının kişisel verisini yüklemek 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) açısından da sorun çıkarabilir.
- Hassas bir belgeyle çalıştığın not defterinde geri bildirim düğmelerine basma.
- İş belgelerini kişisel Google hesabına değil, şirketin Google Workspace hesabındaki Gemini Notebook'a yükle (şirketin izin veriyorsa).
- Bir not defterini paylaşırken, içindeki bütün kaynakları paylaştığını bil.

Genel kurallar [ne yazılmaz rehberinde](rehber:yapay-zekaya-ne-yazilmaz), diğer araçların ayarları [gizlilik ayarları rehberinde](rehber:yapay-zeka-gizlilik-ayarlari).

> SAHA: Kendi hesabında Gemini Notebook'ta geri bildirim (beğen/beğenme) düğmesine bastığında çıkan uyarı metnini ekran görüntüsüyle kaydet; Google'ın "geri bildirim verirsen inceleyebiliriz" uyarısı arayüzde nasıl görünüyor, 1-2 cümleyle yaz.

## Sık yapılan hatalar {#hatalar}

- **Her şeyi tek not defterine koymak.** Alakasız kaynaklar cevapları karıştırır. Her ders, proje ya da konu için ayrı not defteri aç.
- **Taranmış PDF'i olduğu gibi yüklemek.** Metni seçilemeyen, resim olarak taranmış PDF'lerde araç yazıyı okuyamayabilir ya da yanlış okuyabilir. Önce metin tanıma (OCR) yaptır.
- **Sesli özeti kaynak sanmak.** Sesli özet bir yorum; kaynağın yerine geçmez.
- **Kaynak numarasına tıklamamak.** Aracı seçme sebebini boşa çıkarmak demek.
- **Eski mevzuat metni yüklemek.** Araç, verdiğin metnin yürürlükte olup olmadığını bilmez; değişiklikten önceki hâli yüklediysen eski hükmü kaynak numarasıyla birlikte, çok ikna edici biçimde verir.

## Nerede işe yaramaz? {#sinir}

NotebookLM, verdiğin kaynakların içinde soru sormak için çok iyi; kaynakların dışındaki dünya hakkında soru sormak için tasarlanmadı. Kaynaklarındaki bir hatayı da düzeltmez, aynen aktarır. Güncel bir bilgi arıyorsan ya da kaynakların eksikse, [derin araştırma](rehber:derin-arastirma) ya da arama daha doğru yer. Google aracın adını, sınırlarını ve özelliklerini sık değiştiriyor; bu sayfa 16 Kasım 2026'da kontrol edildi.

## Sonraki adım {#sonraki-adim}

Bu hafta okuman gereken en uzun belgeyi (bir ders kitabı bölümü, bir rapor, bir sözleşme seti) NotebookLM'e yükle ve üç soru sor; her cevabın kaynak numarasına tıkla. Uzun belgeleri diğer araçlarla okumanın yolları [uzun PDF rehberinde](rehber:uzun-pdf-okumak).

## Kaynaklar

- Google, "NotebookLM is now Gemini Notebook", 16 Temmuz 2026: [blog.google](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)
- Google Workspace Updates, ad değişikliği ve bağlantıların çalışmaya devam etmesi, 16 Temmuz 2026: [workspaceupdates.googleblog.com](https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html)
- Google, beş saatte bir yenilenen kullanım sınırları, 28 Ağustos 2026: [blog.google](https://blog.google/innovation-and-ai/products/gemini-notebook/new-flexible-usage-limits/)
- Gemini Notebook Yardım, planlar, sınırlar ve eğitim verisi: [support.google.com](https://support.google.com/notebooklm/answer/16213268)
- Gemini Notebook Yardım, sık sorulan sorular ve kaynak başına sınır: [support.google.com](https://support.google.com/notebooklm/answer/16269187)
- Sesli özetlerin 50'den fazla dile açılması, Nisan 2025: [9to5Google](https://9to5google.com/2025/04/29/notebooklm-audio-overviews-languages/)
