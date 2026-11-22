---
title: Yapay zekâyla sunum hazırlamak: ana mesaj, akış, slayt ve prova için 4 hazır komut
slug: sunum-hazirlamak
seo_title: Yapay zekâyla sunum hazırlama: akış, slayt ve prova komutları
description: Yapay zekâyla sunum hazırlarken önce ana mesaj ve akış, sonra slayt: ChatGPT, Copilot, Gemini ve Canva için kopyalanabilir komutlar ve prova şablonu.
summary: Yapay zekâyla sunum: tek cümlelik ana mesaj, akış, slayt başına bir fikir, konuşmacı notları, PowerPoint ve Canva'da yapay zekâ ve sorulara hazırlık için prova şablonu.
keywords: yapay zeka ile sunum hazırlama, chatgpt ile sunum hazırlama, powerpoint copilot sunum oluşturma, canva yapay zeka sunum, gamma sunum, yapay zeka slayt hazırlama, sunum provası yapay zeka, öğrenci sunumu yapay zeka, sunum komutu
type: sablon
audience: Çalışanlar, Öğrenciler
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: Copilot lisans durumu (Nisan 2026) ve Gemini Notebook slayt özelliği eklendi, yazım hatası düzeltildi, başlıklar soru biçimine çevrildi, iç bağlantılar artırıldı.
video:
video_title:
draft: true
---

Yarın sunum var ve elinde sadece bir yığın not. "Yapay zekâ bana sunum yapsın" dersen, birkaç saniyede on beş slaytlık, maddeli, renkli bir dosya çıkar. Sorun şu: Bu slaytların çoğu bir şey söylemez ve sen sahneye çıktığında ne anlatacağını bilmezsin. Yapay zekâ sunumda en çok slayttan önceki işte, yani ne anlatacağına karar vermekte ve provada işe yarıyor.

Kısaca: Yapay zekâyla sunum hazırlarken slaytla değil, tek cümlelik ana mesajla başla. Sonra yapay zekâya akışı kurdur, her slayta tek fikir koy ve konuşmacı notlarını yazdır; slayt tasarımını en son PowerPoint, Canva ya da Google Slaytlar'da yap. Sunumdan bir gün önce yapay zekâya izleyici rolü verip en zor soruları sordur. Aracın eklediği her rakamı ve grafiği kaynağından kontrol et.

## 1. Sunumun ana mesajı ne? {#mesaj}

İzleyici sunumdan çıkarken tek bir cümleyi hatırlayacak. O cümle ne?

```sablon
[KİME] [KAÇ DAKİKALIK] bir sunum yapacağım. Konu: [KONU]. İzleyicinin sunumdan sonra [NE YAPMASINI / NE DÜŞÜNMESİNİ] istiyorum.
Notlarım: [NOTLAR]
Bu notlardan sunumun ana mesajı olabilecek üç farklı cümle öner. Her biri tek cümle, izleyicinin diliyle olsun. Hangisinin bu izleyici için en güçlü olduğunu gerekçesiyle söyle.
```

Önerilerden birini seç ya da kendin yaz. Bu cümle, sunumun geri kalanının filtresi: Ana mesaja hizmet etmeyen slayt çıkar.

## 2. Sunumun akışı nasıl kurulur? {#akis}

```sablon
Ana mesajım: "[MESAJ]". Süre: [DAKİKA].
Bu sunum için bir akış öner:
- Açılış: İzleyicinin tanıdığı bir sorun ya da somut bir örnek.
- Gövde: Ana mesajı destekleyen en fazla üç bölüm; her biri için bir kanıt (rakam, örnek, karşılaştırma).
- Kapanış: Ana mesajın tekrarı ve izleyiciden beklediğim tek adım.
Her bölüme kaç dakika ayırmam gerektiğini yaz. Toplam slayt sayısı süreye göre makul olsun (kabaca dakikada bir slayt).
Notlarımda olmayan bir rakam ya da örnek uydurma; eksik gördüğün kanıtları "eksik" diye listele.
```

"Eksik" listesi değerli: Sunumda iddia edip kanıtlayamayacağın yerleri gösterir.

## 3. Slayt metinleri nasıl kısaltılır? {#slaytlar}

Kötü slaytın en yaygın sebebi çok fazla yazı. Kural: Her slaytta tek fikir, başlık o fikri söyleyen bir cümle.

```sablon
Bu akışın her slaytı için şunları yaz:
- Başlık: Slaytın ana fikrini söyleyen tam bir cümle (örneğin "Satışlar Mart'ta yüzde 12 düştü", "Satış rakamları" değil).
- Slaytta görünecek metin: En fazla 15 kelime ya da tek bir rakam.
- Görsel önerisi: Grafik, fotoğraf, şema ya da hiçbiri.
- Konuşmacı notu: Bu slaytta söyleyeceklerim, 60-90 saniyelik konuşma dilinde.
```

Konuşmacı notları sahnede okunmak için değil, hazırlanmak için. Bir kez sesli oku, sonra kendi cümlelerinle anlat.

## 4. Slaytları hangi araçla yapmalı? {#arac}

İçerik hazır olduktan sonra:

- **PowerPoint:** Copilot'a hazırladığın içeriği verip taslak sunum oluşturtabilirsin. Kişisel hesapta bu, Microsoft 365 Bireysel ya da Aile aboneliğinde kullanım sınırıyla geliyor. İş hesabında 15 Nisan 2026'dan beri PowerPoint'in içindeki Copilot için Microsoft 365 Copilot lisansı gerekiyor. Lisans yoksa Tasarımcı (Designer) özelliği slayt düzeni önerir. Kısayollar [Copilot kısayolları rehberinde](rehber:copilot-kisayollari#office).
- **Canva:** Canva'nın yapay zekâ özellikleriyle bir metinden sunum taslağı çıkarabilirsin; ayrıntısı [Canva rehberinde](rehber:canva-yapay-zeka).
- **Google Slaytlar:** Google Workspace'te ve Google AI planlarında Gemini, slayt ve görsel önerebiliyor.
- **Gemini Notebook (eski adıyla NotebookLM):** Kaynak belgelerinden slayt destesi üretebiliyor; rapor ya da ders notundan sunum çıkarırken işe yarar, çünkü her bilgi senin kaynağına dayanıyor. Kurulumu [NotebookLM rehberinde](rehber:notebooklm).
- **Sunuma özel araçlar:** Gamma gibi araçlar metinden doğrudan sunum üretiyor; hızlı ama kurumsal şablona uymayabilir ve içeriğin o şirkete gider.

Hangi aracı kullanırsan kullan, aracın eklediği rakamları, grafikleri ve görselleri kontrol et. Grafikler için verinin aslından çiz; yapay zekânın "örnek" diye uydurduğu bir grafik sunumda gerçek veri gibi görünür.

Şirket verisi içeren bir sunumu dışarıdaki bir araca yüklemeden önce [iş yeri rehberine](rehber:isyerinde-yapay-zeka-kullanmak#uc-soru) bak.

## 5. Prova {#prova}

Sunumdan bir gün önce:

```sablon
Sen bu sunumun izleyicisisin: [İZLEYİCİ, ÖRNEĞİN "BÜTÇEYİ ONAYLAYACAK ÜÇ YÖNETİCİ"]. Sunumumun metni aşağıda.
1. Hangi slaytta sıkılır ya da koparsın? Neden?
2. Bana sorabileceğin en zor beş soru ne? Her birine iyi bir cevabın nasıl olacağını kısaca yaz.
3. Ana mesajımı sunumdan sonra tek cümleyle nasıl özetlersin? Benim istediğim cümleyle aynı mı?
Sunum: [SUNUM METNİ]
```

Üçüncü soru en iyi test: İzleyicinin özeti senin ana mesajınla aynı değilse, sunum mesajını iletmiyor demek.

Telefonda sesli sohbetle prova da yapabilirsin: Sunumu yüksek sesle anlat, sonra yapay zekâdan süreyi ve tekrar ettiğin kelimeleri sor. Sesli modun nasıl açılacağı [telefon rehberinde](rehber:telefonda-yapay-zeka).

## Sık yapılan hatalar {#hatalar}

- **Slaytlarla başlamak.** Önce mesaj ve akış.
- **Yapay zekânın maddeli listesini aynen koymak.** Madde madde yazı okuyan izleyici seni dinlemez.
- **Uydurma rakam ve grafik.** Her rakamın kaynağını bil.
- **Telifli görseli kullanmak.** İnternetten bulunan görseller ve yapay zekâ görselleri için [telif rehberine](rehber:yapay-zeka-ve-telif) bak.

## Dürüst sınır {#sinir}

Yapay zekâ akışı ve metni toparlar; konuyu bilmeni, izleyiciyi tanımanı ve sahnede rahat olmanı sağlamaz. Bir sunumu en çok iyileştiren şey hâlâ gerçek bir insana yapılan bir provadır. Öğrenciysen, sunumda yapay zekâ kullanımı için okulunun kuralına bak; [öğrenciler rehberinde](rehber:ogrenciler-icin) ayrıntısı var.

## Sonraki adım {#sonraki-adim}

Bir sonraki sunumun için bugün sadece ana mesaj cümlesini yaz ve ilk şablonu dene. Slaytları açmadan önce akışı bitir. Komutlarını daha iyi yazmak için [iyi komut rehberine](rehber:yapay-zekaya-iyi-komut-yazmak) bak.

## Kaynaklar

Bu sayfadaki şablonlar bu site için yazıldı.

- Microsoft Destek, PowerPoint'te Copilot: [support.microsoft.com](https://support.microsoft.com/tr-tr)
- İş hesaplarında 15 Nisan 2026 Copilot lisans değişikliği: [Windows Central, 17 Mart 2026](https://www.windowscentral.com/microsoft/microsoft-office/microsoft-365-is-paywalling-most-of-copilot-in-office-apps-whats-changing)
- Google Workspace, Slaytlar'da Gemini: [support.google.com/docs](https://support.google.com/docs/)
