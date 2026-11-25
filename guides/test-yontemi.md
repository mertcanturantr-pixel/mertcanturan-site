---
title: Yapay zekâ araçlarını nasıl test ediyorum, sen de nasıl test edersin?
slug: test-yontemi
seo_title: Yapay zekâ aracı nasıl test edilir? 5 adım ve puan tablosu
description: Videolardaki testlerin kuralları ve aynı yöntemi kendi işinde kullanman için 30 dakikalık test planı, puan tablosu şablonu ve sık yapılan test hataları.
summary: Videolardaki testlerin kuralları: işi nasıl seçiyorum, araçları aynı koşulda nasıl deniyorum, sonucu nasıl puanlıyorum. Kendi işinde kullanman için şablon ve puan tablosu.
keywords: yapay zeka aracı nasıl test edilir, chatgpt claude gemini karşılaştırma testi, yapay zeka değerlendirme kriterleri, yapay zeka puan tablosu, şirket için yapay zeka aracı seçimi
type: adim-adim
audience: Herkes, İş yerleri
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm.
change: 2026-11-16 Tam rehbere çevrildi: test planı şablonu, puan kartı, sık test hataları, 1 Ağustos 2026 reklam kuralı.
change: 2026-11-16 dört rollü denetim: reklam kuralının yönetmelik maddesi ve Ticaret Bakanlığı kaynağı, soru biçimli başlıklar ve iç bağlantılar eklendi.
video:
video_title:
draft: false
---

Bir yapay zekâ aracı hakkında "harika" ya da "işe yaramaz" demek kolay. Zor olan, bunu neye göre söylediğini gösterebilmek. Bu sayfada videolardaki testlerde izlediğim kuralları yazdım; bir sonuca katılmasan bile nasıl varıldığını görebilesin diye. İkinci yarısında da aynı yöntemi kendi işinde, bir aracı satın almadan ya da ekibine önermeden önce nasıl kullanacağını anlattım.

Kısaca: Bir yapay zekâ aracını test etmek için doğru sonucunu bildiğin gerçek bir iş seç, aynı işi aynı komutla birden fazla araca ver, çıktıyı tek tek kontrol et, riskini not et ve dört ölçütte (doğruluk, kullanılabilirlik, risk, zaman ve maliyet) gerekçeli puan ver. Bir aracı tek bir denemeyle değerlendirme; en az üç farklı iş ya da aynı işi üç kez dene.

## Videolardaki testler hangi 5 adımla yapılıyor? {#bes-adim}

1. **Gerçek bir iş seçerim.** Demo için uydurulmuş bir soru değil, birinin gerçekten yapması gereken bir iş: bir sözleşme taslağı, zor bir e-posta, bir sunum, küçük bir uygulama. Araç şirketlerinin tanıtımda gösterdiği örnekler, aracın en iyi yaptığı işlerdir; senin işin o olmayabilir.
2. **Aynı işi birden fazla araca veririm.** Aynı komut, aynı malzeme, aynı süre. Bir araca ek ipucu verirsem ya da komutu düzeltirsem bunu videoda söylerim. Testin tarihini, aracın planını ve varsa model adını kaydederim; aynı araç birkaç ay sonra farklı sonuç verebilir.
3. **Çıktıyı kontrol ederim.** Kaynakları tek tek açarım, kodu çalıştırırım, hukuki bir iddia varsa mevzuattan okurum. Nasıl yaptığım [kontrol rehberinde](rehber:yapay-zeka-cevabini-kontrol-etmek).
4. **Riskleri not ederim.** Kişisel veri, telif ve sözleşme açısından o aracı bu işte kullanmanın neye mal olabileceğine bakarım.
5. **Puanı gerekçesiyle veririm.** Neyin iyi, neyin kötü olduğunu ekranda gösteririm. Sonucu beğenmesem de sırayı değiştirmem.

## Puan nasıl veriliyor? {#puanlama}

Her aracı dört ölçütte 1'den 5'e kadar puanlarım:

| Ölçüt | Ne soruyorum? | 1 puan | 5 puan |
| --- | --- | --- | --- |
| Doğruluk | Kontrol ettiğim iddiaların ne kadarı doğru çıktı? | Önemli bir uydurma ya da hata var | Kontrol ettiğim her iddia doğru |
| Kullanılabilirlik | Çıktıyı işime koymak için ne kadar düzeltmem gerekti? | Baştan yazmam gerekti | Küçük düzeltmeyle kullanılabilir |
| Risk | Bu işte kullanmanın kişisel veri, telif ya da sözleşme açısından bir sakıncası var mı? | Bu iş için kullanılmamalı | Belirgin bir risk yok |
| Zaman ve maliyet | İşi ne kadar sürede ve hangi ücretle yaptı? | Elle yapmaktan uzun ya da pahalı | Belirgin zaman ve para kazancı |

Toplam puandan çok her ölçütün gerekçesine bakarım. Bir araç hızlı ama yanlışsa, bunu tek bir sayının arkasına saklamam. Doğrulukta 1 alan bir aracı, diğer ölçütlerde ne kadar iyi olursa olsun o iş için önermem.

## Sponsorlu testlerde kurallar değişir mi? {#is-birligi}

Bir şirketle iş birliği yaptığımda da test aynı yöntemle yapılır. Ayrıca:

- Kendim denemediğim ürünü tanıtmam.
- Ücret, ücretsiz abonelik ya da hediye ürün aldığım her paylaşımda başta "Reklam" ya da "Tanıtım" yazar ve reklam verenin adını söylerim; 1 Ağustos 2026'dan beri Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği'nin 23/A maddesi de bunu istiyor. Bunu videoda hem yazılı hem sözlü yaparım; hikâyede, canlı yayında ve kısa videoda da kaydırmadan görünür olur. "#işbirliği" ya da "#sponsorlu" etiketini tek başına kullanmam.
- Olumsuz bulguları gizlemem; şirket test sonucunu yayından önce değiştiremez.
- Bir ürünle satış ortaklığı gibi ticari bir bağım varsa, o üründen söz ettiğim her yerde bunu söylerim.

## Kendi testini yap: 30 dakikalık plan {#kendi-testin}

Bir aracı satın almadan ya da ekibine önermeden önce şu sırayla ilerle:

1. **İşi seç (5 dakika).** Ekibinin her hafta yaptığı ve doğru sonucunu bildiğin bir iş seç. Geçen ay yazdığın bir rapor, cevapladığın bir müşteri e-postası, hazırladığın bir tablo. Doğru cevabı bildiğin bir iş, kontrolü kolaylaştırır.
2. **Malzemeyi temizle (5 dakika).** Kişisel ve gizli bilgileri çıkar ya da rol adlarıyla değiştir. Neyi araca vermemen gerektiği [bu rehberde](rehber:yapay-zekaya-ne-yazilmaz).
3. **Komutu bir kez yaz (5 dakika).** Bütün araçlara aynı komutu ver. Komutu nasıl kuracağın [iyi komut rehberinde](rehber:yapay-zekaya-iyi-komut-yazmak).
4. **Çalıştır ve kaydet (10 dakika).** Her aracın ilk cevabını olduğu gibi kaydet. Bir aracın cevabını beğenmeyip yeniden ürettiysen bunu da not et.
5. **Puanla (5 dakika).** Aşağıdaki şablonu doldur. Puanı vermeden önce her ölçüt için bir cümlelik gerekçe yaz.

```sablon
Test tarihi: [TARİH]
İş: [NE YAPTIRDIN, BİR CÜMLE]
Doğru sonucu nasıl biliyorum: [ELİNDEKİ DOĞRU CEVAP YA DA KONTROL YÖNTEMİ]
Komut (bütün araçlara aynı): [KOMUT]

Araç 1: [ARAÇ ADI, PLAN, MODEL]
- Doğruluk (1-5): [PUAN] · Gerekçe: [GEREKÇE]
- Kullanılabilirlik (1-5): [PUAN] · Gerekçe: [GEREKÇE]
- Risk (1-5): [PUAN] · Gerekçe: [GEREKÇE]
- Zaman ve maliyet (1-5): [PUAN] · Gerekçe: [GEREKÇE]

Araç 2: [ARAÇ ADI, PLAN, MODEL]
- Doğruluk (1-5): [PUAN] · Gerekçe: [GEREKÇE]
- Kullanılabilirlik (1-5): [PUAN] · Gerekçe: [GEREKÇE]
- Risk (1-5): [PUAN] · Gerekçe: [GEREKÇE]
- Zaman ve maliyet (1-5): [PUAN] · Gerekçe: [GEREKÇE]

Karar: [HANGİ ARAÇ, HANGİ İŞ İÇİN, HANGİ KOŞULLA]
Yeniden test tarihi: [3 AY SONRASI]
```

## Örnek puan kartı (temsili) {#ornek}

Aşağıdaki kart temsilidir, gerçek bir testin sonucu değildir; şablonun nasıl doldurulduğunu göstermek için yazıldı.

**İş:** Bir müşteriye, geciken teslimat için özür ve yeni tarih bildiren e-posta. **Doğru sonuç:** Geçen ay gerçekten gönderilmiş, müşterinin olumlu cevap verdiği e-posta.

| Ölçüt | Araç A | Araç B |
| --- | --- | --- |
| Doğruluk | 4 · Yeni tarihi doğru yazdı, sipariş numarasını yanlış yere koydu | 5 · Bütün bilgiler doğru |
| Kullanılabilirlik | 4 · İki cümleyi kısaltmam yetti | 2 · Çeviri kokan, fazla resmî bir dil; baştan yazdım |
| Risk | 5 · Kişisel veri vermedim | 5 · Kişisel veri vermedim |
| Zaman ve maliyet | 4 · Bir dakika, ücretsiz plan | 4 · Bir dakika, ücretsiz plan |

**Karar:** Müşteri e-postaları için Araç A; tarih ve numaraları göndermeden önce elle kontrol. Araç B'nin doğruluğu daha iyi ama dili bu iş için uygun değil. Bu, B'nin her işte kötü olduğu anlamına gelmiyor.

## Sık yapılan test hataları {#hatalar}

- **Tek denemeyle karar vermek.** Aynı komut aynı araçta her seferinde biraz farklı cevap verir. Tek bir iyi ya da kötü cevap şans olabilir. Aynı işi en az üç kez dene ya da üç farklı iş seç.
- **Komutu bir araçta düzeltip diğerinde düzeltmemek.** İlk cevabı beğenmediğin araca ikinci şans verdiysen, diğerine de ver. Yoksa komutu değil, sabrını test etmiş olursun.
- **Doğru cevabını bilmediğin bir iş seçmek.** Doğrusunu bilmediğin bir konuda en akıcı yazan araç kazanır. Akıcılık doğruluk değildir.
- **Ücretsiz planla ücretli planı karşılaştırmak.** Aynı şirketin ücretsiz ve ücretli planı farklı modeller kullanabilir. Hangi planı test ettiğini yaz.
- **Türkçe işi İngilizce test etmek.** İşin Türkçe yapılacaksa testi de Türkçe yap. Araçların Türkçe performansı İngilizceden farklı olabilir.
- **Tarih yazmamak.** Bir araç birkaç ay içinde yeni modele geçebilir. Tarihsiz bir test sonucu, eskidiğini bilmeyen bir sonuçtur.

## Dürüst sınır {#sinir}

Videolardaki testler birkaç iş ve birkaç denemeyle yapılıyor. Bu, bir aracın o iş için nasıl davrandığını gösterir; aracın her işte nasıl olduğunu göstermez. Benim sonucum senin işine uymayabilir. Bu yüzden asıl önerim, kendi işinle yukarıdaki planı uygulaman.

Puanlar benim değerlendirmem; laboratuvar ölçümü değil. Kurallarım ise sabit: Aynı koşul, gösterilen gerekçe, gizlenmeyen olumsuz bulgu.

## Sonraki adım {#sonraki-adim}

Bu hafta ekibinin en çok vakit harcadığı tekrar eden işi seç ve 30 dakikalık planı iki araçla uygula. Hangi araçlarla başlayacağına karar vermek için [hangi yapay zekâ rehberine](rehber:hangi-yapay-zeka) bak. Test ettiğin aracı ekipte kullanmaya karar verirsen kuralları [şirket yapay zekâ politikası rehberiyle](rehber:sirket-yapay-zeka-politikasi#taslak) yaz.

## Kaynaklar

- Ticaret Bakanlığı, Reklam Kurulu, "Sosyal Medya Etkileyicileri Tarafından Yapılan Ticari Reklam ve Haksız Ticari Uygulamalar Hakkında Kılavuz", 7 Mayıs 2021: [ticaret.gov.tr](https://ticaret.gov.tr/haberler/ticaret-bakanligi-sosyal-medya-etkileyicileri-icin-kilavuz-yayimladi)
- Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği'nde değişiklik, Resmî Gazete 1 Temmuz 2026 (33297), yürürlük 1 Ağustos 2026: [Resmî Gazete](https://www.resmigazete.gov.tr/eskiler/2026/07/20260701-9.htm) · [Ticaret Bakanlığı duyurusu](https://ticaret.gov.tr/haberler/ticaret-bakanligi-tarafindan-ticari-reklam-ve-haksiz-ticari-uygulamalar-yonetmeliginde-yapilan-degisikliklerle-tuketicilerin-aldatici-reklam-ve-ticari-uygulamalara-karsi-korunmasi-guclendiriliyor)
