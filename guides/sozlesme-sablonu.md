---
title: Yapay zekâya sözleşme okuturken: 6 kural ve 4 komut şablonu
slug: sozlesme-sablonu
seo_title: ChatGPT'ye sözleşme okutmak: 6 kural ve komut şablonu
description: Sözleşmeyi yapay zekâya okutmadan önce yapman gerekenler; maddeleri alıntılatan inceleme, özet, sürüm karşılaştırma ve soru listesi şablonları.
summary: Bir sözleşmeyi yapay zekâya okutmadan önce yapman gerekenler ve maddeleri alıntılatarak inceleten, doldurup kopyalayabileceğin dört komut şablonu.
keywords: chatgpt'ye sözleşme okutmak, yapay zeka ile sözleşme inceleme, kira sözleşmesi kontrol, sözleşme özeti çıkarma, iki sözleşmeyi karşılaştırma, sözleşme analiz prompt, sözleşme pdf yapay zeka güvenli mi
type: sablon
audience: Herkes, İş yerleri
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm.
change: 2026-11-16 Tam rehbere çevrildi: dört şablon, temsili örnek çıktı, uzun ve taranmış belge, sık hatalar; 2026-11-16 dört rollü denetim: örnek çıktının açıklamasına TBK m.325 ve m.342 notu, iç bağlantılar ve soru başlıkları eklendi.
video:
video_title:
draft: false
---

Elinde imzalaman istenen bir kira, iş ya da hizmet sözleşmesi var ve on iki sayfa. Yapay zekâya okutmak, maddeleri hızlıca gözden geçirmenin pratik bir yolu. Ama araç senin yerine karar veren bir avukat değil: Metinde olmayan bir maddeden söz edebilir, yanlış bir kanun maddesi gösterebilir, en önemli maddeyi hiç görmeyebilir.

Kısaca: Yapay zekâ sözleşmeyi hızlıca gözden geçirmek için işe yarar, ama tespitlerine ancak kontrol edersen güvenebilirsin. Kişisel bilgileri çıkar, her tespiti maddenin aynen alıntısıyla iste, alıntıyı sözleşmede bul, kanun maddesini kendin aç. Aşağıda önce altı kural, sonra dört şablon var: tam inceleme, sade özet, iki sürümü karşılaştırma ve karşı tarafa soru listesi.

Sözleşmeyi sıfırdan yapay zekâya yazdırıyorsan [sözleşme kontrol rehberine](rehber:yapay-zeka-sozlesme-kontrol) bak.

## Sözleşmeyi yüklemeden önce: 6 kural {#kurallar}

- [ ] **Kişisel verileri çıkar.** Ad-soyad, T.C. kimlik numarası, adres, telefon ve IBAN gibi bilgileri metinden sil ya da [KİRACI], [ADRES] gibi etiketlerle değiştir. İnceleme için bu bilgilere ihtiyaç yok.
- [ ] **Gizlilik yükümlülüğünü kontrol et.** Sözleşmede ya da iş yerinin kurallarında gizlilik hükmü varsa, metni başka bir şirketin aracına yüklemenin buna aykırı olup olmadığına bak. Şirketin taslağını kişisel hesabındaki bir araca yapıştırma.
- [ ] **Aracın veri ayarlarına bak.** Kullandığın aracın yazdıklarını modeli geliştirmek için kullanıp kullanmadığını kontrol et ve gerekiyorsa kapat. Üç araçta nasıl yapıldığı [ne yazılmaz rehberinde](rehber:yapay-zekaya-ne-yazilmaz#ayarlar).
- [ ] **Her tespiti alıntıyla iste.** Araçtan her tespit için ilgili maddenin metnini aynen alıntılamasını iste. Alıntıyı sözleşmede bulamıyorsan o tespite güvenme.
- [ ] **Kanun maddelerini kendin aç.** Araç bir kanun ya da madde numarası yazarsa, maddeyi Mevzuat Bilgi Sistemi'nde açıp kendin oku. Nasıl yapılacağı [kontrol rehberinde](rehber:yapay-zeka-cevabini-kontrol-etmek#hukuk).
- [ ] **Sonuç doğuran kararı araca bırakma.** İmza, fesih ya da dava gibi bir adım atmadan önce, bedel ya da süre büyükse bir avukata danış.

## Şablon 1: Maddeleri alıntılatarak inceleme {#inceleme}

En çok kullanacağın şablon bu. Sözleşme metnini yapıştırmadan önce kişisel verileri çıkardığından emin ol.

```sablon
Sen dikkatli bir sözleşme inceleme asistanısın. Aşağıdaki [SÖZLEŞME TÜRÜ] sözleşmesini [BENİM TARAFIM] tarafının bakış açısından incele. Sözleşme Türk hukukuna tabi.

Kurallar:
- Yalnızca aşağıdaki metne dayan. Metinde olmayan bir şeyi varsayma.
- Her tespit için ilgili maddenin numarasını ve metnini aynen alıntıla.
- Emin olmadığın yerde "emin değilim" yaz.
- Bir kanun maddesinden söz edersen numarasını yaz ve doğrulanması gerektiğini belirt.
- Sözleşmede olması beklenip olmayan maddeleri ayrıca listele.

Çıktıyı şu sütunlarla bir tablo olarak ver: Madde | Alıntı | Risk | Neden önemli | Karşı tarafa sorulacak soru

Özellikle şu konulara bak: [ÖNCELİKLİ KONULAR]

Sözleşme metni:
"""
[SÖZLEŞME METNİ]
"""
```

Örnek doldurma: sözleşme türü "konut kira", taraf "kiracı", öncelikli konular "depozito, erken çıkış, aidat ve bakım giderleri, kira artışı".

## Temsili örnek çıktı {#ornek}

Aşağıdaki tablo temsilidir; bir konut kira sözleşmesi için iyi bir cevabın neye benzediğini göstermek için yazıldı.

| Madde | Alıntı | Risk | Neden önemli | Karşı tarafa sorulacak soru |
| --- | --- | --- | --- | --- |
| 4 | "Kira bedeli her yıl yüzde 60 oranında artırılır." | Yüksek | Konut kirasında yıllık artış, bir önceki yılın on iki aylık TÜFE ortalamasını geçemez (TBK m.344, doğrulanmalı). Aşan kısım geçersiz olabilir. | Artış maddesini "TÜFE on iki aylık ortalaması" olarak değiştirebilir miyiz? |
| 7 | "Kiracı, kira süresi dolmadan çıkarsa kalan sürenin tüm kirasını öder." | Yüksek | Erken çıkışta kiracının sorumluluğu kanunda sınırlandırılmış olabilir; bu madde kanundan ağır görünüyor. Emin değilim, kontrol edilmeli. | Erken çıkışta makul bir bildirim süresiyle çıkış mümkün mü? |
| 9 | "Depozito, sözleşme bitiminde iade edilir." | Orta | İade süresi ve hangi kesintilerin yapılabileceği yazmıyor. | Depozito kaç gün içinde, hangi hesaba iade edilecek? |
| Yok | (Sözleşmede bulunamadı) | Orta | Aidat ve büyük onarım giderlerinin kime ait olduğu yazılmamış. | Aidat ve çatı, kalorifer gibi büyük onarımları kim ödeyecek? |

Bu cevapta dikkat edilecek iki yer var: Araç, emin olmadığı 7. maddede bunu söylemiş; kanun maddesini de doğrulanması gerektiği notuyla vermiş. Senin işin, her alıntıyı sözleşmede bulmak ve 6098 sayılı Türk Borçlar Kanunu'nun (TBK) 344. maddesini Mevzuat Bilgi Sistemi'nde açıp okumak. Aracın emin olamadığı erken çıkış konusu TBK m.325'te, depozitonun (güvence) üst sınırı ve nasıl tutulacağı da TBK m.342'de düzenleniyor; bunları da kendin oku. Kira sözleşmesinde gerçek bir uyuşmazlık varsa sonucu sözleşmenin tamamı ve olayın ayrıntısı belirler; bir avukata danış.

## Şablon 2: Sade özet {#ozet}

Sözleşmeyi önce genel olarak anlamak istiyorsan:

```sablon
Aşağıdaki sözleşmeyi hukukçu olmayan biri için özetle. Şu başlıkları kullan: Taraflar ve konu, Benim yükümlülüklerim, Karşı tarafın yükümlülükleri, Ödemeler ve tarihler, Sözleşme nasıl biter, Bana en ağır gelebilecek üç madde.

Her başlığın altında ilgili madde numarasını yaz. Metinde olmayan bir şey ekleme. Benim tarafım: [BENİM TARAFIM].

"""
[SÖZLEŞME METNİ]
"""
```

## Şablon 3: İki sürümü karşılaştırma {#karsilastirma}

Karşı taraf taslağı değiştirip geri gönderdiyse, neyin değiştiğini görmek için:

```sablon
Aşağıda aynı sözleşmenin iki sürümü var. İkinci sürümde değişen, eklenen ve silinen her maddeyi listele.

Her değişiklik için: madde numarası, eski metin (aynen), yeni metin (aynen), değişikliğin [BENİM TARAFIM] için anlamı.

Yalnızca gerçekten değişen yerleri yaz. Biçim ve yazım farklarını ayrı bir başlıkta, kısaca belirt.

BİRİNCİ SÜRÜM:
"""
[ESKİ METİN]
"""

İKİNCİ SÜRÜM:
"""
[YENİ METİN]
"""
```

Uzun sözleşmelerde araç bazı değişiklikleri atlayabilir ya da biçim farkını içerik değişikliği sanabilir. Önemli bir sözleşmede Word'ün "Karşılaştır" özelliğiyle (Gözden Geçir sekmesi) de kontrol et; o, yapay zekâdan daha güvenilir bir fark listesi verir.

## Şablon 4: Karşı tarafa soru listesi {#sorular}

İncelemeden sonra, karşı tarafa göndereceğin nazik bir e-posta taslağı için:

```sablon
Aşağıdaki inceleme notlarıma göre, [KARŞI TARAF] tarafına göndereceğim kısa ve nazik bir e-posta taslağı yaz. Ton: [TON, ÖRNEĞİN "SAMİMİ AMA NET"].

Her soruyu madde numarasıyla yaz. Suçlayıcı ya da hukuki tehdit içeren bir dil kullanma. Değişiklik önerisi varsa somut metin öner.

İnceleme notlarım:
[NOTLAR]
```

Zor e-postaların genel kuralları [zor e-postalar rehberinde](rehber:zor-e-postalar).

## Uzun ya da taranmış sözleşmede ne yapmalı? {#uzun-belge}

- **Taranmış PDF:** Metin yerine resim içeren bir PDF'te araç yazıyı tanımaya çalışır ve rakamları yanlış okuyabilir. Önce metni seçilebilir hâle getir (çoğu PDF okuyucunun metin tanıma özelliği var) ya da en azından bedel, tarih ve süre gibi rakamları elle kontrol et.
- **Çok uzun sözleşme:** Araçlar uzun metnin ortasındaki maddeleri gözden kaçırabilir. 30-40 sayfayı aşan bir sözleşmeyi bölüm bölüm ver ve her bölüm için ayrı inceleme iste. Uzun belgeyle çalışmanın genel yolu [uzun PDF rehberinde](rehber:uzun-pdf-okumak).
- **Ekler:** Ekler (teknik şartname, fiyat listesi) çoğu zaman ana metinden önemlidir. Onları da ver; "Ek-2'de belirtilen" diye geçen her şeyi araç ancak Ek-2'yi görürse değerlendirebilir.

## Yapay zekânın cevabını nasıl kontrol edersin? {#okuma}

- **Önce alıntıları kontrol et.** Tablodaki her alıntıyı sözleşmede ara (Ctrl + F). Bulamadığın satırı sil.
- **"Emin değilim" yazan yerleri işaretle.** Bunlar bir uzmana sorman gereken yerler.
- **Eksik maddeler listesine ayrıca bak.** Olmayan bir maddeyi görmek, olan bir maddeyi okumaktan zordur; araç burada işe yarar.
- **Son sütunu kullan.** "Karşı tarafa sorulacak soru" sütunu, imzadan önce netleştirmen gerekenlerin listesi.

## Sık yapılan hatalar {#hatalar}

- **"Bu sözleşme iyi mi?" diye sormak.** Genel bir soru, "genel olarak dengeli görünüyor" gibi genel bir cevap getirir. Hangi taraf olduğunu ve neye baktığını söyle.
- **Alıntıyı kontrol etmemek.** Araç, sözleşmede olmayan bir cümleyi tırnak içinde yazabilir. Alıntı yoksa tespit de yoktur.
- **Kanun maddesine güvenmek.** Yapay zekâ kanun numarasını doğru, madde numarasını yanlış yazabilir; ya da yürürlükten kalkmış bir hükmü gösterebilir.
- **Kimlik bilgileriyle yüklemek.** Kiracının T.C. kimlik numarası, kefilin adresi incelemeye hiçbir şey katmaz. Çıkar.

## Dürüst sınır {#sinir}

Yapay zekâ, sözleşmedeki açık sorunları yakalamakta iyi; senin durumuna özel riski tartmakta zayıf. Bir maddenin senin için ne kadar kötü olduğu, pazarlık gücüne, sektörün alışkanlıklarına ve ileride ne yapmayı planladığına bağlı. Bunları araca anlatsan bile, sonucun sorumluluğunu taşımaz. Bedeli yüksek ya da seni uzun süre bağlayan bir sözleşmede bu şablonlar, avukata gitmeden önce sorularını hazırlamana yarar.

## Sonraki adım {#sonraki-adim}

Elindeki bir sözleşmeyi (eski bir kira sözleşmesi de olur) Şablon 1 ile dene ve her alıntıyı metinde bul. Kaç tespitin gerçekten sözleşmede olduğunu görmek, bu araca ne kadar güvenebileceğini sana gösterir.

## Kaynaklar

- Kişisel Verileri Koruma Kurumu, "Üretken Yapay Zekâ ve Kişisel Verilerin Korunması Rehberi (15 Soruda)", 24 Kasım 2025: [kvkk.gov.tr](https://www.kvkk.gov.tr/Icerik/8547/uretken-yapay-zeka-ve-kisisel-verilerin-korunmasi-rehberi-15-soruda)
- 6098 sayılı Türk Borçlar Kanunu m.325 (kiralananın sözleşmeye aykırı geri verilmesi), m.342 (güvence) ve m.344 (kira bedelinin belirlenmesi): [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/)
