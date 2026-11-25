---
title: Öğretmen için yapay zekâ: ders planı, ölçme sorusu, farklılaştırma ve veli mesajı
slug: ogretmenler-icin-yapay-zeka
seo_title: Öğretmenler için yapay zekâ: ders planı ve soru hazırlama
description: Ders planı, farklı seviyelerde etkinlik, ölçme soruları, rubrik ve veli mesajı için hazır komutlar; öğrenci verisinde dikkat ve MEB'in etik çerçevesi.
summary: Öğretmenler için yapay zekâ: ders planı, farklı seviyede etkinlik, ölçme sorusu, rubrik ve veli mesajı için hazır komutlar; öğrenci verisini korumak ve MEB'in etik çerçevesi.
keywords: öğretmenler için yapay zeka, yapay zeka ile ders planı hazırlama, chatgpt ile soru hazırlama, rubrik hazırlama yapay zeka, farklılaştırılmış etkinlik, veli mesajı örneği, meb yapay zeka etik kılavuzu, yazek nedir
type: sablon
topic: egitim
audience: Öğretmenler
stage: hazir
published: 2026-11-16
checked: 2026-11-25
change: 2026-11-16 İlk sürüm.; 2026-11-25 hukuki doğrulama: YAZEK beyanının hangi durumlarda gerektiği kılavuza göre eklendi
change: 2026-11-16 dört rollü denetim: MEB etik kılavuzu ve YAZEK açıklaması duyuruya göre düzeltildi, KVKK tam adı, Kısaca paragrafı ve iç bağlantılar.
video:
video_title:
draft: false
---

Bir öğretmenin haftasının büyük kısmı öğrenciyle değil kâğıtla geçiyor: ders planı, etkinlik, sınav sorusu, değerlendirme ölçütü, veli mesajı. Yapay zekâ bu işlerin ilk taslağını dakikalar içinde çıkarabilir; böylece zaman, asıl işe, yani öğrenciye kalır. Ama taslak her zaman taslak: Müfredata, sınıfına ve öğrencine uygun olup olmadığına sen karar veriyorsun.

Kısaca: Öğretmen yapay zekâyı ders planı, farklı seviyede etkinlik, ölçme sorusu, rubrik ve veli mesajının ilk taslağı için kullanabilir. Komutta sınıf düzeyini, müfredattaki kazanım metnini, süreyi ve sınıfın genel profilini ver; çıktıyı müfredatla karşılaştır ve soruları sınıfa vermeden önce kendin çöz. Öğrencilerin adlarını, notlarını ve özel durumlarını yazma.

## Öğrenci bilgisi yapay zekâya yazılır mı? {#ogrenci-verisi}

Öğrencilerin adları, notları, sağlık ya da özel eğitim durumları, aile bilgileri kişisel veri; bir kısmı özel nitelikli. Kişisel bir yapay zekâ hesabına bunları yazmak hem 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) hem de meslek etiği açısından risk. Komutlarında "Öğrenci A", "üç öğrenci okumada zorlanıyor" gibi genel ifadeler kullan; yapay zekânın işi görmesi için isme ihtiyacı yok.

Millî Eğitim Bakanlığı (MEB), 17 Haziran 2025'te "Eğitimde Yapay Zekâ Politika Belgesi ve Eylem Planı (2025-2029)"nı yürürlüğe koydu. 10 Ocak 2026'da da "Eğitimde Yapay Zekâ Uygulamaları Etik Kılavuzu"nu yayımladı: Kılavuz il, ilçe ve okul düzeyinde etik kurullar ve ekipler kuruyor, etik ihlal bildirimlerinin nasıl ele alınacağını düzenliyor. Bakanlığın duyurusuna göre öğretmenler ve MEB birimleri etik beyan formunu 2 Şubat 2026'da açılan Yapay Zekâ Uygulamaları Etik Beyan Sistemi (YAZEK) üzerinden dolduruyor.

Kılavuza göre öğrenci verisi girmeden ders planı, etkinlik fikri, sunum ya da materyal hazırlıyorsan beyan gerekmiyor. Öğrenci yapay zekâyı derste kullanacaksa, öğrenci verisi (anonim olsa bile) araca girilecekse ya da sonuç not ve değerlendirmede kullanılacaksa uygulamadan önce beyan doldurman gerekiyor; beyan için onay beklenmiyor.

## Yapay zekâyla ders planı nasıl hazırlanır? {#ders-plani}

```sablon
[SINIF DÜZEYİ] [DERS] dersi için [SÜRE] dakikalık bir ders planı hazırla.
Kazanım: [MÜFREDATTAKİ KAZANIM METNİ]
Sınıf: [ÖĞRENCİ SAYISI, GENEL SEVİYE, VARSA ÖZEL DURUMLAR (İSİMSİZ)]
Elimdeki imkânlar: [AKILLI TAHTA, LABORATUVAR YOK, VB.]

Planda: giriş (dikkat çekme), ana etkinlik, değerlendirme ve kapanış olsun; her bölümün süresi yazsın. Kazanımın dışına çıkma. Bir etkinlik için malzeme gerekiyorsa listele.
```

Kazanım metnini müfredattan aynen yapıştırmak, yapay zekânın konudan sapmasını büyük ölçüde engeller.

## Farklı seviyeler için etkinlik uyarlamak {#farklilastirma}

Aynı sınıfta farklı hızlarda öğrenen öğrenciler için:

```sablon
Aşağıdaki etkinliği üç seviyeye uyarla: desteğe ihtiyacı olan öğrenciler, sınıf düzeyindeki öğrenciler ve ileri düzeydeki öğrenciler. Kazanım aynı kalsın; yalnızca destek miktarı, örnek sayısı ve soru zorluğu değişsin.

Etkinlik: [ETKİNLİK]
Sınıf düzeyi: [SINIF]
```

## Ölçme soruları ve rubrik hazırlamak {#olcme}

```sablon
[SINIF] [DERS] dersinde [KAZANIM] kazanımını ölçen [SAYI] soru hazırla: [SAYI] çoktan seçmeli, [SAYI] açık uçlu.
Çoktan seçmeli sorularda çeldiriciler, öğrencilerin bu konudaki yaygın yanlış anlamalarına dayansın. Her sorunun doğru cevabını ve hangi kazanımı ölçtüğünü ayrıca yaz.
```

Ardından açık uçlu sorular için değerlendirme ölçütü:

```sablon
Yukarıdaki açık uçlu soru için dört düzeyli (başlangıç, gelişmekte, yeterli, ileri) bir dereceli puanlama anahtarı hazırla. Her düzeyde öğrencinin cevabında görmem gereken somut davranışı yaz.
```

**Kontrol et:** Yapay zekâ bazen yanlış cevap anahtarı yazar ya da iki doğru cevabı olan bir soru üretir. Soruları sınıfa vermeden önce kendin çöz.

## Veliye zor bir mesaj yazmak {#veli}

Zor bir konuyu veliye iletmek (devamsızlık, davranış, başarı düşüşü) için:

```sablon
Bir veliye göndereceğim kısa bir mesaj yaz. Konu: [KONU, İSİMSİZ]. Amacım: [ÖRNEĞİN "VELİYİ GÖRÜŞMEYE DAVET ETMEK"].
Ton: saygılı, suçlamayan, çözüm odaklı. Önce olumlu bir gözlemle başla. En fazla beş cümle. Öğrencinin adını ve özel bilgilerini ben ekleyeceğim; yerlerini [KÖŞELİ PARANTEZ] ile bırak.
```

Zor yazışmaların genel kuralları [zor e-postalar rehberinde](rehber:zor-e-postalar).

## Öğrencilerin yapay zekâ kullanımına nasıl yaklaşmalı? {#ogrenci-kullanimi}

Öğrencilerin yapay zekâ kullanması kaçınılmaz; asıl soru nasıl kullandıkları. Ödev yönergene yapay zekâ hakkında açık bir cümle ekle ("Konuyu anlamak için kullanabilirsin, metni kendin yazmalısın; kullandıysan bir cümleyle belirt"). Bir ödevin yapay zekâyla yazıldığından şüpheleniyorsan, dedektörlerin neden güvenilir olmadığını ve ne yapabileceğini [ödev rehberinin öğretmen bölümünde](rehber:odev-yapay-zeka-tespiti#ogretmen) anlattım. Öğrencilere verebileceğin kullanım önerileri [öğrenciler rehberinde](rehber:ogrenciler-icin); küçük yaştaki öğrenciler ve veliler için yaşa göre kurallar [çocuklar ve yapay zekâ rehberinde](rehber:cocuklar-ve-yapay-zeka#yas).

## Sık yapılan hatalar {#hatalar}

- **Müfredatı vermemek.** "8. sınıf fen planı" yerine kazanım metnini yapıştır; yoksa plan başka bir ülkenin müfredatına göre çıkabilir.
- **Cevap anahtarını kontrol etmemek.** Yanlış bir anahtar, bütün sınıfın notunu etkiler.
- **Öğrenci adı yazmak.** Hiçbir işte gerekli değil.
- **Her şeyi yapay zekâya hazırlatmak.** Öğrencini en iyi tanıyan sensin; plan senin sınıfına göre şekillenmeli.

## Dürüst sınır {#sinir}

Yapay zekâ genel bir ders planını iyi hazırlar ama senin sınıfındaki öğrencileri tanımaz. Türkiye'ye özgü müfredat ayrıntılarında, yerel örneklerde ve güncel yönetmeliklerde hata yapabilir. Bir de şunu bil: MEB ve okulların yapay zekâ kuralları yeni ve gelişiyor; bu sayfa 16 Kasım 2026'da kontrol edildi.

## Sonraki adım {#sonraki-adim}

Bu hafta bir ders için yalnızca ölçme sorusu şablonunu dene ve soruları sınıfa vermeden önce kendin çöz. Kaç tanesini değiştirmen gerektiği, bu araca ne kadar güvenebileceğini sana gösterir. Şablonları kendi ihtiyacına göre değiştirmek için [iyi komut rehberindeki](rehber:yapay-zekaya-iyi-komut-yazmak#sablon) beş parçalı yapıyı kullan; ders sunumu hazırlıyorsan [sunum rehberine](rehber:sunum-hazirlamak) bak.

## Kaynaklar

- MEB, Eğitimde Yapay Zekâ Uygulamaları Etik Kılavuzu (Ocak 2026), bölüm 4.1 ve Tablo 1: [MEB](https://ttkb.meb.gov.tr/meb_iys_dosyalar/2026_01/09152326_egitimdeyapayzekauygulamalari_etik_kilavuzu.pdf)

- Millî Eğitim Bakanlığı, "Eğitimde Yapay Zekâ Politika Belgesi ve Eylem Planı (2025-2029)", 17 Haziran 2025: [meb.gov.tr](https://www.meb.gov.tr/egitimde-yapay-zek-politika-belgesi-ve-eylem-plani-yururluge-girdi/haber/37531/tr)
- Millî Eğitim Bakanlığı, "Eğitimde Yapay Zekâ Uygulamaları Etik Kılavuzu" ve YAZEK, 10 Ocak 2026: [meb.gov.tr](https://www.meb.gov.tr/egitimde-yapay-zeka-uygulamalari-etik-kilavuzu-yayimlandi/haber/39496/tr)
- 6698 sayılı Kişisel Verilerin Korunması Kanunu: [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/)
