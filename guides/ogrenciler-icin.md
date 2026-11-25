---
title: Öğrenci için yapay zekâ: ödevde, sınava çalışırken ve ders notunda dürüst ve verimli kullanım
slug: ogrenciler-icin
seo_title: Öğrenciler için yapay zekâ: ders çalışmak ve doğru kullanım
description: Yapay zekâyı kopya aracı değil öğretmen gibi kullanmak: konu anlatımı, kendini sınama, not özeti, yazım düzeltme ve okul kurallarına uymak için komutlar.
summary: Yapay zekâyı ödevi yazdırmak için değil, öğrenmek için kullanmak: konu anlattırma, kendini sınama, ders notundan soru üretme, yazını düzeltme ve okulun kurallarına uyma.
keywords: öğrenciler için yapay zeka, yapay zeka ile ders çalışmak, chatgpt ile sınava hazırlık, yapay zekaya soru sordurmak, ders notu özeti çıkarma, chatgpt ödev yaptırmak kopya mı, yapay zeka konu anlatımı, üniversite yapay zeka kuralları, meb yapay zeka etik kılavuzu, yok yapay zeka etik rehberi
type: adim-adim
topic: egitim
audience: Öğrenciler
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: MEB etik kılavuzunun tarihi (Ocak 2026) ve YÖK rehberinin içeriği kaynağa göre düzeltildi, Kısaca kısaltıldı, başlıklar soru biçimine çevrildi.
video:
video_title:
draft: false
---

Yapay zekâ bir öğrenci için iki şeyden biri olabilir: Ödevi senin yerine yazan bir kopya aracı ya da gece ikide bile soru sorabileceğin sabırlı bir öğretmen. İlki kısa vadede zaman kazandırır ama sınavda, mülakatta ve işte seni yalnız bırakır. İkincisi seni gerçekten daha iyi yapar. Bu sayfa ikincisi için.

Kısaca: Yapay zekâya cevabı değil açıklamayı sor ve sınava çalışırken seni sınamasını iste. Ödevini kendin yaz, yapay zekâya yalnız düzelttir; verdiği her bilgiyi ve kaynağı kontrol et. Kullanım sınırını okulun ve hocan belirliyor; kullandıysan ödevde açıkça söyle.

## 1. Cevabı değil, konuyu nasıl anlattırırsın? {#anlattir}

Bir matematik sorusunda takıldın. "Cevap ne?" diye sorarsan cevabı alırsın; bir sonraki soruda yine takılırsın. Şunu dene:

```sablon
[KONU] konusunda bu soruyu çözemiyorum: [SORU].
Cevabı söyleme. Önce bana bu tür soruları çözmek için gereken fikri basit bir örnekle anlat. Sonra bana ilk adımı ipucu olarak ver ve benim denememi bekle. Yanlış yaparsam nerede hata yaptığımı söyle ama doğru cevabı yine söyleme.
```

Bu yöntem daha yavaş görünür ama sınavda soruyu sen çözersin.

## 2. Sınava çalışırken kendini nasıl sınarsın? {#sina}

Sınava çalışırken en çok işe yarayan yöntemlerden biri, okuduğunu hatırlamaya çalışmak ve kendini sınamak. Yapay zekâ bunun için iyi bir partner:

```sablon
[DERS] dersinden [KONU] konusunda sınava çalışıyorum. Bana [SAYI] soru sor, her seferinde bir tane. Ben cevaplayınca doğru mu yanlış mı söyle ve kısa bir açıklama yap. Zorlandığım konuları sonunda listele.
```

Ders notlarını ya da slaytları yüklersen sorular senin dersine göre olur. Bunun için [Gemini Notebook (eski adıyla NotebookLM)](rehber:notebooklm) özellikle uygun; cevabın notlarının neresinden geldiğini gösteriyor.

## 3. Ders notundan çalışma özeti nasıl çıkarılır? {#notlar}

Dağınık notlarını düzenli bir özete çevirmek için:

```sablon
Aşağıdaki ders notlarımı düzenli bir çalışma özetine çevir: başlıklar, her başlığın altında kısa maddeler, önemli tanımlar ve formüller ayrı bir kutuda. Notlarımda olmayan bir bilgi ekleme; eksik ya da çelişkili gördüğün yerleri sonunda soru olarak listele.

[NOTLAR]
```

Son cümleyi atlama: Yapay zekâ notlardaki boşlukları kendi bilgisiyle doldurmaya meyillidir; hocanın anlattığından farklı bir şey ekleyebilir.

## 4. Ödevine yapay zekâdan nasıl geri bildirim alırsın? {#yazi}

Ödevini kendin yaz, sonra yapay zekâdan geri bildirim al:

```sablon
Aşağıdaki ödev metnini ben yazdım. Metni yeniden yazma. Bunun yerine:
1. Yazım ve noktalama hatalarını listele.
2. Anlaşılması zor olan üç cümleyi göster ve neden zor olduğunu söyle.
3. Ana fikrimi destekleyen bir kanıt eksikse söyle.
Kararı ben vereceğim.

[METİN]
```

Bu, metni senin metnin olarak bırakır ve yazmayı öğrenmeni sağlar. Metnini yapay zekâya baştan yazdırmak ise çoğu okulda akademik dürüstlük ihlali sayılır.

## 5. Yapay zekânın verdiği kaynak gerçek mi? {#kaynak}

Yapay zekâya kaynak sorduğunda, var olmayan kitaplar ve makaleler gelebilir. Ödevine bir kaynak koymadan önce Google Akademik ya da DergiPark'ta ara; kaynağı aç ve söylediği şeyi gerçekten söyleyip söylemediğine bak. Adım adım yöntem [kontrol rehberinde](rehber:yapay-zeka-cevabini-kontrol-etmek#kaynak-gercekten-var-mi-20-saniyelik-kontrol).

## Okulunda yapay zekâ kullanmak serbest mi? {#kural}

Yapay zekâ kullanımının sınırı okuldan okula, dersten derse değişiyor. Üniversitede genel çerçeveyi YÖK'ün Mayıs 2024'te yayımladığı üretken yapay zekâ etik rehberi çiziyor; ayrıntılı kuralı çoğu zaman üniversitenin kendi yönergesi ve dersin hocası koyuyor. Okullarda ise Millî Eğitim Bakanlığı Haziran 2025'te Eğitimde Yapay Zekâ Politika Belgesi'ni, Ocak 2026'da da eğitimde yapay zekâ uygulamaları için bir etik kılavuz yayımladı. Pratikte:

- Ders izlencesine ya da ödev yönergesine bak; yapay zekâ hakkında bir cümle olabilir.
- Emin değilsen hocana sor: "Konuyu anlamak için yapay zekâ kullanabilir miyim, yazım düzeltme için kullanabilir miyim?"
- Kullandıysan ödevin sonuna bir cümle ekle: hangi aracı, ne için kullandığın.

Ödevin yapay zekâ dedektörüne takıldıysa ne yapacağın [ödev rehberinde](rehber:odev-yapay-zeka-tespiti). Tez yazıyorsan [tez rehberine](rehber:tezde-yapay-zeka-kullanimi) bak.

## Sık yapılan hatalar {#hatalar}

- **Cevabı kopyalamak.** Ödevi geçer, sınavı geçmez.
- **Tek bir açıklamayla yetinmek.** Anlamadıysan "Bunu 12 yaşındaki birine anlatır gibi anlat" ya da "Başka bir örnekle anlat" de.
- **Kaynak uydurmasını fark etmemek.** Bir kaynağı açmadan ödevine koyma.
- **Kişisel bilgi vermek.** Okul numaranı, adını, öğretmeninin adını yazmana gerek yok.
- **Gece boyu sohbet.** Yapay zekâyla çalışmak da yorar; arada kalk, kâğıt kalemle tekrar et.

## Dürüst sınır {#sinir}

Yapay zekâ bir konuyu anlatmakta çok iyi ama her zaman doğru değil; özellikle ileri matematikte, güncel konularda ve Türkiye'ye özgü müfredatta hata yapabilir. Ders kitabın ve öğretmenin hâlâ ana kaynak. Bir de şunu bil: Yapay zekâ seni sınava hazırlayabilir ama sınavda yanında olmayacak; çalışmanın amacı, onsuz da bilebilmek.

## Sonraki adım {#sonraki-adim}

Bu hafta bir ders seç ve iki şeyi dene: Takıldığın bir soruyu "cevabı söyleme" komutuyla sor ve sınav öncesi "kendini sına" komutuyla on soruluk bir tekrar yap. Hangisinin işine yaradığını not et. Komutları daha iyi yazmak için [iyi komut rehberine](rehber:yapay-zekaya-iyi-komut-yazmak) bak.

## Kaynaklar

- YÖK, "Yükseköğretim Kurumları Bilimsel Araştırma ve Yayın Faaliyetlerinde Üretken Yapay Zekâ Kullanımına Dair Etik Rehber", Mayıs 2024: [yok.gov.tr](https://www.yok.gov.tr/Documents/2024/yapay-zeka-kullanimina-dair-etik-rehber.pdf)
- Millî Eğitim Bakanlığı, "Eğitimde Yapay Zekâ Politika Belgesi ve Eylem Planı (2025-2029)", 17 Haziran 2025: [meb.gov.tr](https://www.meb.gov.tr/egitimde-yapay-zek-politika-belgesi-ve-eylem-plani-yururluge-girdi/haber/37531/tr)
- Millî Eğitim Bakanlığı, "Eğitimde Yapay Zekâ Uygulamaları Etik Kılavuzu yayımlandı", 10 Ocak 2026: [meb.gov.tr](https://www.meb.gov.tr/egitimde-yapay-zeka-uygulamalari-etik-kilavuzu-yayimlandi/haber/39496/tr)
