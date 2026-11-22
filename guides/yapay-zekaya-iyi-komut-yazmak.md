---
title: Yapay zekâdan işe yarar cevap almak için komutu 5 parçayla kur
slug: yapay-zekaya-iyi-komut-yazmak
seo_title: Yapay zekâya iyi komut (prompt) yazmak: 5 parça ve şablon
description: Komutu beş parçayla kur: durum, görev, malzeme, biçim, örnek. Uydurmayı azaltan cümleler, önce-sonra örneği ve doldurup kopyalayacağın şablon.
summary: Kötü cevabın çoğu eksik bağlamdan geliyor. Komutu beş parçayla kur, uydurmayı azaltan üç cümleyi ekle, ilk cevabı ikinci turda düzelt. Doldurup kopyalayacağın şablonla.
type: sablon
audience: Herkes
keywords: prompt nasıl yazılır, iyi prompt örnekleri, chatgpt komut örnekleri türkçe, yapay zekaya nasıl soru sorulur, prompt şablonu, yapay zeka uydurmasın diye ne yazılmalı
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm. "Uydurmayı azaltan 3 cümle" rehberi bunun içine alındı.
change: 2026-11-16 Açılış ve örnekler yeniden yazıldı; şablon metindeki beş parça ve üç kuralla aynı hâle getirildi; sık hatalar ve sonraki adım eklendi.
change: 2026-11-16 dört rollü denetim: Kısaca paragrafı, soru biçimli başlıklar, belge içindeki gizli talimat uyarısı, dürüst sınır bölümü ve iç bağlantılar eklendi.
video:
video_title:
draft: true
---

ChatGPT'ye "Ödemeyi geciktiren müşteriye mail yaz" de, gelen metin büyük ihtimalle "Sayın Yetkili, umarım iyisinizdir" diye başlar ve hiçbir müşteriye olduğu gibi gönderilemez. Araç bu işi yapabilir. Yapamadığı şey senin kafandakini tahmin etmek: Müşterin kim, kaç aydır bekliyorsun, onunla yine çalışmak istiyor musun? Bilmediği her yeri en sıradan ihtimalle dolduruyor.

Kısaca: Yapay zekâdan işe yarar cevap almak için komutu beş parçayla kur: durum (kimsin, ne oluyor), görev (tam olarak ne istiyorsun), malzeme (neye dayansın), biçim (uzunluk, ton, şekil) ve varsa örnek. Uydurmayı azaltmak için "emin değilsen söyle", "kaynağı alıntıla" ve "yalnızca verdiğim metne dayan" cümlelerini ekle; ilk cevabı beğenmezsen aynı sohbette neyi beğenmediğini somut olarak söyle.

Aşağıda bir komutu beş parçaya ayırıyorum ve aynı isteğin kötü ve iyi yazılmış hâlini yan yana koyuyorum. Doldurup kopyalayacağın şablon en altta.

## Yapay zekâ neden sıradan cevap veriyor? {#neden}

Yapay zekâ senin kim olduğunu, ne için sorduğunu ve sonucu nerede kullanacağını bilmiyor. Bilmediği her şeyi en sıradan ihtimalle doldurunca cevap da en sıradan cevap oluyor.

İyi bir komut için süslü kelime gerekmiyor. Bir insana iş verirken ne söylüyorsan onu yaz: kime, ne için, ne uzunlukta, hangi tonda.

## İyi bir komutun beş parçası nedir? {#bes-parca}

Her komutta beşini birden yazman gerekmiyor. Cevap kötü geldiyse eksik olan genellikle bunlardan biri.

### 1. Durum: kimsin, ne oluyor?

"Serbest çalışan bir grafik tasarımcıyım, müşterim ödemeyi iki aydır geciktiriyor" cümlesini eklediğinde cevap da değişir. Bu cümle olmadan gelen metin herkese gönderilebilecek bir şablondur; cümleyle birlikte araç, tasarımcıyla müşterisi arasındaki ilişkiye göre yazar.

### 2. Görev: tam olarak ne istiyorsun?

"Yardım et" bir görev değil. "Müşterime gönderecek kısa ve kibar bir hatırlatma mesajı yaz" bir görev. Fiil net olsun: yaz, özetle, karşılaştır, eleştir, listele, hesapla.

### 3. Malzeme: neye dayansın?

Elinde bir metin, tablo ya da belge varsa yapıştır. Yapay zekâ senin verdiğin metinden çalışınca daha az uydurur, sen de cevabı o metinle karşılaştırıp kontrol edebilirsin. Yapıştırmadan önce isimleri ve numaraları çıkar; nedenini [yapay zekâya ne yazılmaz rehberinde](rehber:yapay-zekaya-ne-yazilmaz) anlattım. Bir de şunu bil: Başkasından gelen bir e-posta ya da web'den kopyaladığın bir metin, içine gizlenmiş talimatlar taşıyabilir (komut enjeksiyonu). Cevap beklemediğin bir yöne saparsa malzemeye bak.

### 4. Biçim: cevap nasıl görünsün?

Uzunluğu, tonu ve şekli söyle: "En fazla 120 kelime", "madde madde değil, düz metin", "tablo olarak: madde, risk, neden". "Suçlayıcı olmasın" gibi sınırlar da biçimin parçası. Bunları söylemezsen araç genellikle gereğinden uzun ve gereğinden madde işaretli yazıyor.

### 5. Örnek: neye benzesin?

Beğendiğin bir örnek varsa ver. "Şu e-postanın tonunda yaz" demek, tonu tarif etmeye çalışmaktan daha çok işe yarar.

## Kötü komut ve iyi komut: aynı istek {#ornek}

Bu iki komut aynı işi istiyor.

İlk komut:

```
Ödemeyi geciktiren müşteriye mail yaz.
```

Bu komuta gelecek cevabı tahmin etmek zor değil: uzun, resmî ve genel bir metin. Müşterinin kim olduğunu, aranızdaki ilişkiyi ve ne kadar beklediğini bilmeyen araç her ihtimali kapsamaya çalışır.

İkinci komut:

```
Serbest çalışan bir grafik tasarımcıyım. Bir kafeye logo ve menü tasarladım, işi eylül başında teslim ettim. 18.000 TL'lik faturayı o gün kestim ama iki aydır ödeme yok. Müşteriyle ilişkim iyi, sahibi samimi biri. Tekrar iş almak istiyorum ama artık ödemenin bir tarihe bağlanmasını istiyorum.

Ona WhatsApp'tan göndereceğim kısa bir mesaj taslağı yaz. Samimi ama net olsun, en fazla 6 cümle. Suçlayıcı olmasın. Sonunda ödeme için somut bir tarih sorsun.
```

İkinci komutta durum, görev ve biçim var. Bu komuta gelen mesajda düzelteceğin şey azalır.

Temsili bir cevap (gerçek bir aracın çıktısı değil; ikinci komuttan beklenecek sonuca örnek):

> Merhaba Selin Hanım, umarım işler yolundadır. Eylülde teslim ettiğim logo ve menü işinin faturası hâlâ açık görünüyor. Sizinle çalışmaktan memnunum, yeni işlerde de birlikte olmak isterim. Ödemeyi hangi gün yapabileceğinizi yazabilir misiniz? Bir aksilik varsa da konuşup bir yol bulalım.

> SAHA: İki komutu da aynı araçta dene, gelen iki cevabı ekran görüntüsüyle ekle. Hangi araç ve hangi tarih olduğunu yaz. Gerçek çıktı gelince yukarıdaki temsili cevabı onunla değiştireceğiz.

## Yapay zekânın uydurmasını azaltan üç cümle {#uydurma}

Yapay zekâ bazen var olmayan bir kaynağı, yanlış bir tarihi ya da hiç yaşanmamış bir olayı doğru bilgiyle aynı özgüvenle yazar. Bunun nedenlerinden birini, yazarları arasında OpenAI araştırmacılarının da bulunduğu bir ekip Eylül 2025'te yayımladığı makalede anlattı: Bu sistemleri ölçen testlerin çoğunda yanlış cevap da "bilmiyorum" da sıfır puan alıyor. Sistem de emin olmadığı yerde susmak yerine tahmin etmeyi öğreniyor. Bizim sınavlardaki "dört yanlış bir doğruyu götürür" kuralının tam tersi.

Modelin nasıl eğitildiğini değiştiremezsin ama ondan ne istediğini değiştirebilirsin. Komutunun sonuna şu cümleleri ekle:

```
Emin olmadığın yerde "emin değilim" yaz; tahmin ediyorsan bunun tahmin olduğunu belirt.
Her bilgi için kaynağını ve kaynaktaki ilgili cümleyi aynen alıntıla.
Yalnızca sana verdiğim metne dayan; metinde olmayan bir şeyi ekleme.
```

Birinci cümle araca boş bırakma izni veriyor. İkincisi kontrolü kolaylaştırıyor: Alıntıyı kaynakta bulamıyorsan o bilgiye güvenmezsin. Üçüncüsü, bir belge üzerinde çalışırken aracı o belgenin dışına çıkmaktan alıkoyuyor.

Bu cümleler uydurmayı bitirmez. Araç daha seyrek uydurur, uydurduğunda da yakalaman kolaylaşır. Para, sağlık ya da hukukla ilgili bir işte cevabı yine [kontrol listesinden](rehber:yapay-zeka-cevabini-kontrol-etmek) geçir.

## İlk cevap kötüyse ne yazmalı? {#ikinci-tur}

İlk cevabı beğenmeyince sohbeti kapatıp başka bir araca geçme. Aynı sohbette neyi beğenmediğini söylemek, sıfırdan başlamaktan genelde daha hızlı sonuç verir; araç ilk cevabı ve senin itirazını birlikte görür.

"Daha iyi yap" yerine şöyle söyle:

- "Çok resmî olmuş, arkadaşıma yazar gibi yaz."
- "Üçüncü paragrafı çıkar, geri kalanı aynı kalsın."
- "Bu cevapta emin olmadığın yerler hangileri? Tek tek söyle."
- "Bir avukat bu metni okusa neye itiraz ederdi?"

Son iki soruyla araca kendi cevabını eleştirtmiş olursun; ilk turda görmediği zayıf noktalar böyle ortaya çıkabiliyor.

## Aynı şeyi her seferinde yazmamak: kalıcı talimat {#kalici}

Her sohbette "Türk hukukuna göre cevap ver, kısa yaz" diye başlıyorsan bunu bir kez kaydedebilirsin. ChatGPT'de özel talimatlar ve projeler, Claude'da projeler, Gemini'de Gem'ler bu işi görüyor. Kaydettiğin talimat, o alandaki her sohbetin başına kendiliğinden ekleniyor. Üç araçta nasıl kurulacağı ve içine ne yazılmaması gerektiği [kalıcı talimat rehberinde](rehber:kalici-talimat#sablon).

> SAHA: Kendi kalıcı talimatını (ya da bir kısmını) örnek olarak paylaşır mısın? Okurlar için en öğretici kısım bu olabilir. İçinde müvekkil, işveren ya da büroya ait bilgi kalmasın.

## Komut yazarken sık yapılan hatalar {#hatalar}

- Bir komuta beş iş sığdırmak. "Özetle, eleştir, yeniden yaz, başlık öner ve tabloya dök" dersen her biri yarım kalır. Önce birini iste, sonra ötekini.
- "Kısa yaz" deyip uzunluğu söylememek. "Kısa" araç için üç paragraf da olabilir. Kelime ya da cümle sayısı ver.
- Malzemeyi komutun ortasına gömmek. Uzun bir metin yapıştıracaksan talimatı önce yaz, metni sonra, açıkça ayırarak.
- Aracın verdiği bilgiyi kontrol etmeden ikinci komuta geçmek. Yanlış bir rakam ikinci, üçüncü cevaba da taşınır.

## Komut şablonu {#sablon}

Metindeki beş parça ve üç kural aynen burada. Kullanmadığın alanı silebilirsin.

```sablon
Durum: [DURUM]

Görev: [GÖREV]

Biçim: [BİÇİM]

Örnek (varsa, bu tonda yaz): [ÖRNEK METİN]

Kurallar:
- Emin olmadığın yerde "emin değilim" yaz; tahmin ediyorsan bunun tahmin olduğunu belirt.
- Her bilgi için kaynağını ve kaynaktaki ilgili cümleyi aynen alıntıla.
- Yalnızca sana verdiğim metne dayan; metinde olmayan bir şeyi ekleme.

Malzeme:
"""
[MALZEME METNİ]
"""
```

Doldurulmuş bir örnek: Durum "Küçük bir kafe işletiyorum, Google'da 3 yıldızlı haksız bir yorum aldım", görev "Yoruma verilecek kısa ve sakin bir cevap yaz", biçim "En fazla 80 kelime, özür dileyen ama suçu kabul etmeyen bir ton". Malzemeye yorumun kendisini yapıştırırsın.

## Dürüst sınır {#sinir}

İyi bir komut cevabı belirgin biçimde iyileştirir ama modelin bilmediği bir şeyi bildirmez ve uydurmayı sıfırlamaz. Güncel bilgi, fiyat ya da mevzuat istiyorsan aracın web'de arama yaptığından emin ol ve kaynakları kendin aç. Hangi aracın senin işinde daha iyi olduğunu da komut değil, deneme gösterir; yöntemi [test yöntemi rehberinde](rehber:test-yontemi#kendi-testin).

## Sonraki adım {#sonraki-adim}

Bu hafta en sık yazdığın bir isteği seç, şablonla yeniden kur ve iki cevabı karşılaştır. Hazır komutlarla başlamak istersen [zor e-postalar](rehber:zor-e-postalar) ve [Excel](rehber:excel-yapay-zeka) rehberlerindeki şablonlara bak; hepsi bu beş parçayla kurulu.

## Kaynaklar

- Kalai, Nachum, Vempala ve Zhang, [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664), arXiv, 4 Eylül 2025 · [OpenAI'ın özeti](https://openai.com/index/why-language-models-hallucinate/)
- Anthropic, [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview): komut yazımı üzerine resmî rehber
