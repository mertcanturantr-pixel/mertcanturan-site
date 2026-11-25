---
title: Yapay zekâya karar verdirmek: hangi kararlar ona bırakılır, hangileri asla?
slug: yapay-zekaya-karar-verdirmek
seo_title: Yapay zekâya karar sormak: hangi kararlar ona bırakılır?
description: Yapay zekâ sana hak verme eğiliminde. Hangi kararı ona bırakabilirsin, hangisini asla? Karşı görüş isteyen beş komut ve hazır karar şablonu.
summary: Yapay zekâ sana hak verme eğiliminde. Hangi kararı ona bırakabileceğini, hangisinde yalnız düşünme ortağı olacağını ve doğru soruyu soran komut şablonunu anlatıyorum.
keywords: yapay zekaya karar verdirmek, chatgpt'ye karar sormak, chatgpt hep hak veriyor, yapay zeka dalkavukluk, sycophancy nedir, chatgpt şeytanın avukatı komutu, premortem analizi, karar verme prompt şablonu
type: adim-adim
topic: gunluk
audience: Herkes
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İskeletten tam rehbere çevrildi: karar türleri tablosu, dalkavukluk sorunu, beş komut ve şablon; 2026-11-16 dört rollü denetim: açılış Kısaca biçimine çevrildi, yaşanmamış deney SAHA notuna alındı, komutlar şablon bloğuna taşındı.
video:
video_title:
draft: true
---

İki iş teklifi arasında kaldığını düşün. ChatGPT'ye "Şu teklifi kabul etmeyi düşünüyorum, sence mantıklı mı?" yazdın. Büyük ihtimalle mantıklı olduğunu, gerekçeleriyle birlikte duyacaksın. Sorunu fark ettin mi? Hangisine yattığını soruda zaten söyledin.

Kısaca: Yapay zekâya yalnızca geri alınabilen, bedeli küçük ve sonucunu kontrol edebileceğin kararları bırak: akşam yemeği, sunumun sırası, tatilde gün planı gibi. Sağlık, para, hukuki sonuç doğuran ve başkalarının hayatını etkileyen kararlarda yapay zekâ karar veren değil, düşünmene yardım eden biri olmalı. Orada da "sen ne dersin" diye sorma; seçenekleri, ölçütleri ve karşı görüşü iste, çünkü dil modelleri kullanıcıya hak verme eğiliminde.

## Yapay zekâ neden sana hak verir? {#dalkavukluk}

Dil modelleri, insanların beğendiği cevapları ödüllendiren yöntemlerle eğitiliyor. İnsanlar da kendileriyle aynı fikirde olan cevabı daha çok beğeniyor. Sonuç: Model, söylediğin şeye katılmaya meyilli. Buna İngilizcede "sycophancy", Türkçede dalkavukluk deniyor.

Bu bir tahmin değil. Anthropic'in 2023'te yayımladığı bir araştırma, yaygın kullanılan beş sohbet asistanının da farklı görevlerde kullanıcıya hak verme eğilimi gösterdiğini ve insan tercihlerinin bu eğilimi beslediğini buldu. Nisan 2025'te OpenAI, ChatGPT'deki bir GPT-4o güncellemesini birkaç gün içinde geri aldı. Şirketin kendi açıklamasına göre güncelleme modeli "aşırı destekleyici ama samimiyetsiz" yapmıştı; kullanıcılar, kötü fikirlerinin bile övüldüğü ekran görüntüleri paylaşıyordu.

Şirketler bu eğilimi azaltmaya çalışıyor. Ama karar sorarken bunun hâlâ var olduğunu varsayman daha güvenli. Her sohbette açık sözlü cevap istiyorsan bunu bir kez [kalıcı talimata](rehber:kalici-talimat) yazabilirsin. Pratikte şu demek: Sorunun içinde hangi cevabı beklediğin belli oluyorsa, büyük ihtimalle o cevabı alırsın.

## Hangi kararlar yapay zekâya bırakılır, hangileri asla? {#hangi-kararlar}

Bir kararı yapay zekâya bırakıp bırakmayacağını dört soruyla ayırabilirsin:

1. **Geri alınabilir mi?** Yanlış çıkarsa ertesi gün değiştirebilir misin?
2. **Bedeli ne?** Yanlış çıkarsa ne kaybedersin: birkaç yüz lira ve biraz zaman mı, yoksa sağlığın, işin, birikimin mi?
3. **Kimi etkiliyor?** Yalnız seni mi, ailenden, çalışanından ya da müşterinden birini mi?
4. **Sonucu kontrol edebilir misin?** Verdiği cevabın doğru olup olmadığını kendin görebilir misin?

| Karar türü | Örnek | Yapay zekânın rolü |
| --- | --- | --- |
| Geri alınabilir, bedeli küçük, yalnız seni etkiliyor | Haftalık yemek listesi, okuma sırası, sunumun bölüm sırası, tatilde gün planı | Karar verebilir. Beğenmezsen değiştirirsin. |
| Bedeli orta, geri dönüşü zor ama mümkün | Hangi kursa yazılacağın, hangi telefonu alacağın, iki ev arasında seçim | Seçenekleri ve ölçütleri çıkarır, karşı görüşü söyler. Kararı sen verirsin. |
| Geri dönüşü yok ya da bedeli büyük | İstifa, sözleşme imzalamak, büyük borç ya da yatırım, ameliyat, boşanma | Yalnız soru sorduran ve bilgi toplayan yardımcı. Karar için uzmana (doktor, avukat, mali müşavir) git. |
| Başkasının hakkını ya da hayatını etkiliyor | İşe alım, işten çıkarma, kiracı seçmek, çocuğunla ilgili karar | Karar veremez. Gerekçeni yazmana yardım edebilir, ama gerekçe senin olmalı. |

Son satır yalnızca etik bir tercih değil. 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) m.11, kişinin verilerinin yalnızca otomatik sistemlerle analiz edilmesi sonucunda aleyhine çıkan bir sonuca itiraz hakkı tanıyor. İş yerinde bir adayı yalnızca yapay zekâ puanına göre eliyorsan, aday bu sonuca itiraz edebilir; o zaman kararın gerekçesini açıklayabilecek durumda olman gerekir.

OpenAI da bu ayrımı kendi ürünü için yapıyor. Ağustos 2025'teki açıklamasında "Erkek arkadaşımdan ayrılmalı mıyım?" gibi bir soruya ChatGPT'nin cevap vermemesi, soru sorarak ve artılarla eksileri tartarak düşünmene yardım etmesi gerektiğini yazdı.

## "Sen ne dersin" yerine sorulacak beş şey {#bes-komut}

Karar sorarken amaç, modelden bir hüküm almak değil, kendi göremediğin şeyleri görmek. Bunun için beş soru kalıbı işe yarıyor. Hepsini bir kararda kullanmak zorunda değilsin; çoğu kararda ikisi yeter.

### Seçenekleri genişlet

İnsan iki seçenek arasında sıkışınca üçüncüyü görmez. "Kabul et ya da reddet" arasında "teklifi pazarlık et" ya da "başlangıç tarihini ertele" de olabilir.

```sablon
Şu kararı vermem gerekiyor: [KARAR]. Şu an aklımda iki seçenek var: [A] ve [B]. Bu ikisinin dışında, benim durumumda gerçekten uygulanabilir üç seçenek daha öner. Her biri için bir cümleyle neden düşünülmeye değer olduğunu yaz.
```

### Ölçütleri çıkar

Çoğu kötü karar, neyin önemli olduğunu baştan yazmamaktan çıkar. Modelden ölçüt listesi iste, sonra hangisinin senin için ağır bastığını sen işaretle.

```sablon
[KARAR] için karar verirken hangi ölçütlere bakmam gerekir? Bana 6-8 ölçüt listele. Her birinin yanına, bu ölçütü öğrenmek için kime ya da nereye sormam gerektiğini yaz. Hangisinin daha önemli olduğuna sen karar verme; sıralamayı ben yapacağım.
```

### Karşı tarafın avukatı ol

Dalkavukluğu kırmanın en kolay yolu, modele açıkça karşı çıkma görevi vermek.

```sablon
[A] seçeneğine yatkınım. Senden bunu onaylamanı istemiyorum. Bu seçeneğe karşı en güçlü üç gerekçeyi, bu konuda tecrübeli ve bana iyilik isteyen ama açık sözlü biri gibi yaz. Gerekçelerin her birinin ne zaman geçersiz olacağını da söyle.
```

### Ön ölüm analizi

Psikolog Gary Klein'ın "premortem" dediği yöntem: Kararı verdiğini ve bir yıl sonra kötü sonuçlandığını varsayıp nedenini geriye doğru yazmak. Proje ekiplerinde kullanılır, kişisel kararlarda da işe yarar.

```sablon
[A] seçeneğini seçtiğimi ve bir yıl sonra bunun kötü bir karar olduğu ortaya çıktığını varsay. Bunun en olası beş nedenini yaz. Sonra her neden için bugünden alabileceğim bir önlem öner.
```

### Bilmediğin bilgiyi sorgula

Model, senin durumun hakkında bilmediği her şeyi tahminle doldurur. Ona tahmin ettiği yerleri söyletmek, neyi araştırman gerektiğini gösterir.

```sablon
Bu konuda bana bir öneri vermeden önce, durumum hakkında bilmediğin ve cevabını değiştirebilecek en önemli beş bilgiyi soru olarak sor. Ben cevaplamadan öneri yazma.
```

## Aynı soru, iki farklı soruş: temsili örnek {#ornek}

Aşağıdaki örnek temsilidir; cevaplar bir modelin vereceği cevabın kısaltılmış hâli.

**Kötü soruş:** "Kiram çok arttı, şehir dışına taşınmayı düşünüyorum. Uzaktan çalışıyorum zaten. Bence mantıklı, sen ne dersin?"

**Tipik cevap:** "Uzaktan çalıştığın için mantıklı bir karar gibi görünüyor. Daha düşük kira, daha sakin bir yaşam ve daha fazla alan gibi avantajları olabilir..."

Model senin "bence mantıklı" cümleni aldı ve gerekçelendirdi. Yeni bir şey öğrenmedin.

**İyi soruş:** "Kiram çok arttı, şehir dışına taşınmayı düşünüyorum, uzaktan çalışıyorum. Onaylamanı istemiyorum. Önce kararımı değiştirebilecek beş soru sor, sonra bu taşınmanın kötü sonuçlanması için en olası üç senaryoyu yaz."

**Tipik cevap:** "Şirketin uzaktan çalışma düzeni yazılı mı, ileride ofise dönüş istenebilir mi? Taşınacağın yerde internet altyapısını kontrol ettin mi? Sağlık hizmetine ve sosyal çevrene uzaklık senin için ne kadar önemli? Taşınma masrafı ve depozito, kira farkıyla kaç ayda çıkar?..."

İkinci cevap karar vermedi. Ama kontrol etmen gereken dört şeyi önüne koydu. Karar ortağından bekleyeceğin şey bu.

## Büyük bir karar için hazır şablon {#sablon}

Bedeli büyük bir kararda aşağıdaki şablonu doldurup kullan. Köşeli parantezdeki yerleri kendi bilginle değiştir; kişisel ya da başkasına ait hassas bilgiyi yazma, yerine genel bir ifade kullan.

```sablon
Bir karar vermem gerekiyor ve senden karar vermeni değil, düşünmeme yardım etmeni istiyorum.

Karar: [NE HAKKINDA KARAR VERECEKSİN]
Seçenekler: [AKLINDAKİ SEÇENEKLER]
Şu an hangisine yatkınım: [YATKIN OLDUĞUN SEÇENEK YA DA "HENÜZ YOK"]
Benim için önemli olanlar: [ÖNCELİKLERİN]
Değiştiremeyeceğim kısıtlar: [BÜTÇE, SÜRE, YER GİBİ KISITLAR]

Şunları sırayla yap:
1. Durumum hakkında bilmediğin ve cevabı değiştirebilecek en önemli üç bilgiyi sor. Cevabımı bekle.
2. Benim aklıma gelmemiş en az iki seçenek öner.
3. Yatkın olduğum seçeneğe karşı en güçlü üç gerekçeyi yaz.
4. Her seçenek için "bir yıl sonra kötü sonuçlanırsa en olası neden" yaz.
5. Bu kararı vermeden önce kime danışmam ya da neyi kontrol etmem gerektiğini söyle.

Bana hak vermeye çalışma. Emin olmadığın yerde emin değilim yaz.
```

## Sık yapılan hatalar {#hatalar}

- **Cevabı soruya gömmek.** "Bence X daha iyi, değil mi?" diye sormak, büyük ihtimalle "Evet" cevabını getirir. Yatkınlığını söyleyeceksen, karşı görüşü istediğini de aynı cümlede söyle.
- **Cevap beğenilmeyince yeniden sormak.** Aynı soruyu beğendiğin cevap gelene kadar yenilemek, karar vermek değil, onay toplamaktır. İlk cevaba itirazın varsa itirazını yaz ve gerekçesini iste.
- **Uzman cevabı sanmak.** Model hem hukuk hem tıp hem vergi hakkında akıcı konuşur. Akıcı olması doğru olduğunu göstermez. Rakam, madde ya da tarih içeren her şeyi [kontrol rehberindeki](rehber:yapay-zeka-cevabini-kontrol-etmek) gibi doğrula.
- **Başkasının bilgisini vermek.** Eşinin sağlık durumunu, çalışanının performans notlarını ya da bir müşterinin bilgilerini yazmak, karar sorusunu bir gizlilik sorununa çevirir. Neyi yazmaman gerektiği [bu rehberde](rehber:yapay-zekaya-ne-yazilmaz).
- **Uzun bir sohbetin sonunda karar sormak.** Saatlerdir aynı konuyu konuşuyorsan model, konuşmanın havasına uyar. Önemli bir kararı, özetini yazarak yeni bir sohbette sor.

## Dürüst sınır {#sinir}

Bu yöntem, bilgi eksikliğinden kaynaklanan kararsızlıkta işe yarar. Ama bazı kararsızlıklar bilgiden değil, korkudan ya da yorgunluktan gelir. Seçeneklerin ne olduğunu biliyorsan ve yine de karar veremiyorsan, yapay zekâdan bir liste daha almak çoğu zaman işi uzatır. Orada güvendiğin biriyle konuşmak daha iyi.

Bir de şunu bil: Model senin hayatını bilmez. Ona anlattığın kadarını bilir ve eksik kalanı en olası tahminle doldurur. Önemli bir kararda "sen ne yapardın" sorusunun cevabı, senin değil, ortalama bir insanın durumuna göre verilmiş bir cevaptır.

Sağlıkla ilgili bir belirtinin, imzalayacağın bir sözleşmenin ya da bir yatırımın kararını bir sohbet robotunun cevabına dayandırma. Bunlarda yapay zekâ, uzmana gitmeden önce sorularını hazırlamana yardım edebilir. O kadar.

## Bir hafta dene: küçük kararlarını yapay zekâya ver {#deney}

Bu ayrımın senin için nasıl çalıştığını görmenin yolu küçük bir deney: Bir hafta boyunca geri alınabilir günlük kararlarının hepsini (yemek, okuma sırası, iş listesinin sırası) yapay zekâya ver ve her birinin sonucunu bir satırla not et. Sağlık, para, hukuk ve başkalarını etkileyen kararları deneyin dışında tut. Hafta sonunda en iyi ve en kötü kararı yan yana koy; yapay zekânın hangi tür kararda işe yaradığını kendi hayatından görürsün.

> SAHA: 30 Kasım - 6 Aralık arasında bu deneyi kendin yap; en iyi ve en kötü kararı, kaç kararı geri aldığını birkaç cümleyle bu bölüme ekle.

## Sonraki adım {#sonraki-adim}

Bu hafta vermen gereken orta büyüklükte bir karar seç ve şablonu bir kez dene. Modelin sorduğu sorulardan en az birinin aklına gelmemiş olması gerekir; gelmediyse soruyu yeterince açık yazmamışsındır. Komutları daha iyi kurmak için [iyi komut yazma rehberine](rehber:yapay-zekaya-iyi-komut-yazmak) bak.

## Kaynaklar

- Sharma ve diğerleri, "Towards Understanding Sycophancy in Language Models", Anthropic, Ekim 2023: [arXiv](https://arxiv.org/abs/2310.13548)
- OpenAI, "Sycophancy in GPT-4o: What happened and what we're doing about it", 29 Nisan 2025: [openai.com](https://openai.com/index/sycophancy-in-gpt-4o/) · "Expanding on what we missed with sycophancy", 2 Mayıs 2025: [openai.com](https://openai.com/index/expanding-on-sycophancy/)
- OpenAI, "What we're optimizing ChatGPT for", 4 Ağustos 2025: [openai.com](https://openai.com/index/optimizing-chatgpt/)
- Gary Klein, "Performing a Project Premortem", Harvard Business Review, Eylül 2007: [hbr.org](https://hbr.org/2007/09/performing-a-project-premortem)
- 6698 sayılı Kişisel Verilerin Korunması Kanunu, m.11/1-g (münhasıran otomatik sistemlerle analiz sonucuna itiraz): [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/)
