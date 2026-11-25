---
title: Uzun PDF'leri yapay zekâyla okumak: özet, soru-cevap ve kaçırılmaması gerekenler
slug: uzun-pdf-okumak
seo_title: Uzun PDF'i yapay zekâyla özetlemek: doğru yöntem ve komutlar
description: Yüz sayfalık bir raporu, yönetmeliği ya da tezi yapay zekâyla okumak: hangi araç, nasıl parçalanır, hangi komutlar, ortadaki bilgiyi kaçırmamak için kontrol.
summary: Yüz sayfalık bir raporu, yönetmeliği ya da tezi yapay zekâyla okumak: araç seçimi, belgeyi hazırlamak, işe yarayan komutlar ve uzun belgede yapay zekânın kaçırdığı yerleri yakalamak.
keywords: yapay zeka ile pdf özetleme, uzun pdf özetleme, chatgpt pdf yükleme ve soru sorma, claude pdf okuma, gemini pdf özet, ihale şartnamesi yapay zeka ile okuma, taranmış pdf metne çevirme ocr, pdf özeti sayfa numarasıyla, lost in the middle ortada kaybolma, pdf ozetleme yapay zeka
type: adim-adim
audience: Herkes, İş yerleri, Öğrenciler
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: başlıklar soru biçimine çevrildi, araç tablosuna tarih bağlamı ve iç bağlantılar eklendi.
video:
video_title:
draft: false
---

Önünde 140 sayfalık bir faaliyet raporu, bir ihale şartnamesi ya da bir yönetmelik var ve yarına kadar ne dediğini bilmen gerekiyor. Yapay zekâya yüklemek mantıklı; ama "bunu özetle" dediğinde aldığın beş paragraflık özet, belgenin önemli bir maddesini atlamış olabilir. Uzun belgelerde yapay zekânın bilinen bir zayıflığı var: Başı ve sonu iyi hatırlarken ortadaki bilgiyi daha sık kaçırıyor.

Kısaca: Belgeyi hazırla (taranmışsa metne çevir), tek seferde "özetle" demek yerine ne aradığını söyle, uzun belgeyi bölüm bölüm işle, kararını etkileyecek her bilgi için sayfa numarası iste ve rakamları belgeden kontrol et.

## Yapay zekâ uzun PDF'te neden bilgi kaçırıyor? {#ortada-kaybolma}

Stanford ve başka kurumlardan araştırmacıların 2023'te yayımladığı "Lost in the Middle" çalışması, dil modellerinin uzun bir metinde aranan bilgi başta ya da sondayken daha iyi, ortadayken daha kötü sonuç verdiğini gösterdi. Modeller o tarihten beri çok gelişti ve uzun metinlerde daha iyi; ama pratikte hâlâ şu oluyor: Yüz sayfalık bir belgenin 47. sayfasındaki bir istisna, genel bir özette görünmeyebiliyor.

Bu yüzden uzun belgede asıl yöntem özet istemek değil, soru sormak ve kaynak göstermesini istemek.

## 1. Belgeyi yüklemeden önce ne yapmalısın? {#hazirla}

- **Metin seçilebiliyor mu?** PDF'te fareyle bir cümleyi seçmeyi dene. Seçemiyorsan belge taranmış bir resim; yapay zekâ yazıyı tanımaya çalışır ve rakamları yanlış okuyabilir. Önce bir metin tanıma (OCR) aracıyla metne çevir; Google Drive'da PDF'i Google Dokümanlar ile açmak ya da Adobe Acrobat'ın metin tanıma özelliği bu iş için yeterli.
- **Kişisel bilgi var mı?** Belgede kimlik numarası, müşteri adları, sağlık bilgisi varsa önce çıkar ya da kurumsal bir araç kullan. Neyin yüklenmemesi gerektiği [ne yazılmaz rehberinde](rehber:yapay-zekaya-ne-yazilmaz).
- **Gereksiz kısımları at.** Ekler, boş sayfalar, uzun tablolar senin sorunla ilgisizse, yalnızca ilgili bölümleri yükle.

## 2. Uzun PDF için hangi yapay zekâ aracı uygun? {#arac}

Kasım 2026 itibarıyla genel tablo:

| İş | Uygun araç türü |
| --- | --- |
| Bir belgeyi bir kez okuyup soru sormak | ChatGPT, Claude ya da Gemini'ye dosya yüklemek |
| Birçok belgeden düzenli olarak soru sormak (ders notları, mevzuat seti) | Gemini Notebook (eski adıyla NotebookLM) gibi kaynak gösteren araçlar; ayrıntısı [Gemini Notebook rehberinde](rehber:notebooklm) |
| Aynı belgeyle günlerce çalışmak | Claude ya da ChatGPT'de proje açıp belgeyi projeye eklemek |
| Şirket belgesi | Şirketin kurumsal aracı (Microsoft 365 Copilot, kurumsal ChatGPT ya da Claude) |

Araçların yükleyebileceğin dosya boyutu ve sayfa sınırları plana göre değişiyor ve sık güncelleniyor; güncel sınırı aracın yardım sayfasından kontrol et. Çok büyük bir belgede araç belgenin bir kısmını okumadan cevap verebilir. Belge çok uzunsa bölerek ver. Birden çok kaynağı tarayıp rapor yazdırmak istiyorsan bu ayrı bir iş; [derin araştırma rehberine](rehber:derin-arastirma) bak.

## 3. "Özetle" yerine ne sormalısın? {#komutlar}

**Ne aradığını söyle:**

```sablon
Ekteki belgeyi [AMACIM, ÖRNEĞİN "BU İHALEYE GİRİP GİRMEYECEĞİME KARAR VERMEK"] için okuyorum.
Benim için şunları bul:
1. [ARADIĞIN BİLGİ 1, ÖRNEĞİN "TEKLİF SON TARİHİ VE TESLİM YERİ"]
2. [ARADIĞIN BİLGİ 2, ÖRNEĞİN "İSTENEN BELGELER"]
3. [ARADIĞIN BİLGİ 3, ÖRNEĞİN "CEZA VE TEMİNAT MADDELERİ"]

Her bilgi için sayfa numarasını ve ilgili cümleyi aynen alıntıla. Belgede bulamadığın bilgi için "belgede bulunamadı" yaz; tahmin etme.
```

**İstisnaları ve şartları ayrıca iste:** Özetler genellikle ana kuralı verir, istisnaları atlar.

```sablon
Belgede geçen bütün istisnaları, "ancak", "şu durumda hariç", "aksi kararlaştırılmadıkça" gibi ifadelerle başlayan şartları sayfa numarasıyla listele.
```

**Rakamları ve tarihleri topla:**

```sablon
Belgede geçen bütün tarihleri, süreleri, tutarları ve oranları bir tabloya çıkar: Değer | Ne anlama geldiği | Sayfa. Hiçbir rakamı yuvarlama ya da hesaplama; belgede yazdığı gibi yaz.
```

## 4. Yüzlerce sayfalık belge nasıl bölünür? {#bolum-bolum}

Yüzlerce sayfalık bir belgede:

1. Önce içindekiler bölümünü ver ve "Bu belgenin yapısını ve hangi bölümünün benim amacımla ilgili olduğunu söyle" diye sor.
2. İlgili bölümleri tek tek yükle ve her biri için yukarıdaki komutlardan birini kullan.
3. En sonda bütün bölümlerin notlarını birleştirip "Bu notlara dayanarak karar için en önemli beş noktayı sırala" diye sor.

Bu yöntem daha uzun sürer ama ortadaki bilgiyi kaçırma riskini ciddi şekilde azaltır.

## 5. Yapay zekânın özetini nasıl kontrol edersin? {#kontrol}

- [ ] Kararını etkileyen her bilgi için verilen sayfa numarasına git ve cümleyi kendin oku.
- [ ] Tablodaki rakamları belgedeki rakamlarla tek tek karşılaştır.
- [ ] "Belgede bulunamadı" denen bir bilgiyi belgede Ctrl + F ile kendin ara; bazen araç bulamadığı bilgiyi yok sayar.
- [ ] Kararını en çok etkileyen iki üç bölümü yapay zekâya değil, kendine oku.

Özetteki bir rakamı, tarihi ya da kanun maddesini dış kaynaktan doğrulaman gerekiyorsa adımlar [kontrol rehberinde](rehber:yapay-zeka-cevabini-kontrol-etmek#nereden).

## Sık yapılan hatalar {#hatalar}

- **Tek cümlelik "özetle" komutu.** En kısa yol gibi görünür, en çok bilgiyi kaçıran yoldur.
- **Sayfa numarası istememek.** Kaynağı olmayan bir özeti kontrol edemezsin.
- **Taranmış belgeye güvenmek.** Resim olarak taranmış bir PDF'teki "5.000.000 TL" yapay zekânın gözünde "500.000 TL" olabilir.
- **Özeti karar belgesi gibi kullanmak.** Özet, hangi bölümü okuman gerektiğini söyler; o bölümü okumanın yerine geçmez.

## Dürüst sınır {#sinir}

Yapay zekâ uzun bir belgeyi senden çok daha hızlı tarar ama senin kadar dikkatli okumaz. Para, sağlık ya da hukuki sonuç doğuran bir kararın dayandığı belgede, yapay zekâ sana nereye bakacağını gösterir; okuma işini yine sen yaparsın. Sözleşmeler için ayrı şablonlar [sözleşme okutma rehberinde](rehber:sozlesme-sablonu#uzun-belge).

## Sonraki adım {#sonraki-adim}

Elindeki uzun bir belgeyle "Ne aradığını söyle" komutunu dene ve verilen her sayfa numarasını kontrol et. Kaç tanesinin doğru çıktığı, o araca uzun belgelerde ne kadar güvenebileceğini sana gösterir.

## Kaynaklar

- Liu ve diğerleri, "Lost in the Middle: How Language Models Use Long Contexts", 2023 (Transactions of the ACL, 2024): [arXiv](https://arxiv.org/abs/2307.03172)
