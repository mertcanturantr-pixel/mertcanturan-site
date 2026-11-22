---
title: Gemini'yle fotoğraf düzenlemek: ne yapılır, ne yapılmaz ve vesikalığı neden düzenlememelisin?
slug: gemini-fotograf-duzenleme
seo_title: Gemini (Nano Banana) ile fotoğraf düzenleme: yöntem ve sınırlar
description: Gemini'nin Nano Banana modeliyle fotoğraf düzenlemek: arka plan, nesne silme, eski fotoğraf onarma; başkasının fotoğrafı, vesikalık ve görünmez filigran.
summary: Gemini'yle fotoğraf düzenleme: arka planı değiştirmek, nesne silmek, eski fotoğrafı onarmak için komutlar; başkasının fotoğrafında izin, resmî vesikalık ve SynthID filigranı.
keywords: gemini fotoğraf düzenleme, nano banana nasıl kullanılır, yapay zeka ile arka plan değiştirme, fotoğraftan nesne silme, eski fotoğraf onarma yapay zeka, gemini fotoğraf promptları, vesikalık yapay zeka, synthid nedir
type: sablon
audience: Herkes
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm.
change: 2026-11-16 dört rollü denetim: ücretsiz ve ücretli plandaki model adları (Nano Banana 2, Nano Banana Pro), Kısaca paragrafı, soru biçimli başlıklar ve kaynaklar güncellendi.
video:
video_title:
draft: true
---

Tatil fotoğrafının arka planındaki yabancıyı silmek, dedenin solmuş siyah beyaz fotoğrafını canlandırmak, ürün fotoğrafına düz beyaz bir zemin koymak. Bunlar eskiden Photoshop bilgisi gerektiriyordu; şimdi Gemini'ye bir fotoğraf yükleyip ne istediğini yazmak yetiyor. Google'ın bu iş için kullandığı görsel modellerinin ailesine Nano Banana deniyor; özellikle "fotoğrafın geri kalanını bozmadan tek bir şeyi değiştirme" konusunda iyiler.

Kısaca: Gemini'de fotoğraf düzenlemek için fotoğrafı yükle, tek bir değişiklik iste, sonucu orijinalle karşılaştır, sonra bir sonrakine geç. Ücretsiz planda da çalışıyor; sınırlar ücretli planlarda daha yüksek. Başkasının yüzü olan fotoğraflarda izin al ve resmî belgelerde kullanılacak vesikalık fotoğrafı yapay zekâyla düzenleme.

## Gemini'de fotoğraf nasıl düzenlenir? {#kullanim}

1. Gemini uygulamasını ya da gemini.google.com'u aç.
2. Fotoğrafı yükle (artı simgesi ya da ataç).
3. Değişikliği net bir cümleyle yaz.
4. Sonucu indir; beğenmediysen aynı sohbette düzeltme iste.

Google'ın plan sayfasına göre (16 Kasım 2026) görsel üretme ve düzenleme her planda Nano Banana 2 modeliyle yapılıyor; Google AI Plus, Pro ve Ultra'da bir sonucu daha gelişmiş Nano Banana Pro ile yeniden yaptırabiliyorsun. Ücretsiz planda kullanım sınırı daha düşük; ücretli planlarda sınır kat kat artıyor. Hangi planın ne kadar olduğu [hangi yapay zekâ rehberinde](rehber:hangi-yapay-zeka#fiyatlar).

## Fotoğraf düzenleme için hazır komutlar {#komutlar}

**Nesne silmek:**

```sablon
Bu fotoğraftaki [NESNE / KİŞİ, ÖRNEĞİN "ARKA PLANDAKİ ÇÖP KUTUSU"] sil; boşalan yeri çevreye uygun doldur. Fotoğrafın geri kalanını, özellikle yüzleri değiştirme.
```

**Arka plan değiştirmek:**

```sablon
Ön plandaki [KONU]'yu olduğu gibi bırak, arka planı [YENİ ARKA PLAN, ÖRNEĞİN "DÜZ AÇIK GRİ STÜDYO ZEMİNİ"] ile değiştir. Işık ve gölge yeni zemine uygun olsun.
```

**Eski fotoğraf onarmak:**

```sablon
Bu eski fotoğraftaki çizikleri, lekeleri ve kırışıklıkları temizle; netliği biraz artır. Yüz hatlarını değiştirme, yeni ayrıntı ekleme. Renklendirme yapma.
```

İstersen ikinci adımda renklendirme iste; ama renklendirilmiş bir aile fotoğrafındaki renklerin tahmin olduğunu unutma, gerçek renkler bu olmayabilir.

**Ürün fotoğrafı:** "Ürünü değiştirmeden, beyaz zemin ve yumuşak gölgeyle e-ticaret fotoğrafı gibi düzenle." Ürünün rengini, şeklini ya da etiketini değiştiren bir düzenleme, satışta müşteriyi yanıltır; e-ticaret kuralları için [satıcılar rehberine](rehber:e-ticaret-saticilari-icin-yapay-zeka) bak.

> SAHA: Kendi fotoğraflarından biriyle (ailenden izin alarak ya da yüzsüz bir fotoğrafla) üç komutu dene; önce ve sonra hâlini ekle, nerede iyi nerede kötü sonuç verdiğini yaz.

## Düzenleme yüzleri değiştirir mi? {#yuzler}

Yapay zekâ bir fotoğrafı düzenlerken, istemesen de yüzleri hafifçe değiştirebiliyor: göz şekli, gülümseme, cilt dokusu. Bir aile fotoğrafında bu, kişinin artık kendisine benzememesi demek. Komutta "yüzleri değiştirme" yaz ve sonucu orijinalle yan yana karşılaştır.

## Vesikalık fotoğraf yapay zekâyla düzenlenir mi? {#vesikalik}

Pasaport, kimlik kartı ve ehliyet gibi belgeler için istenen biyometrik fotoğrafların gerçek ve üzerinde oynanmamış olması gerekiyor. Yapay zekâyla arka planı değiştirilmiş, yüzü düzeltilmiş ya da tamamen üretilmiş bir vesikalık, başvurunun reddine yol açabilir; belgeyi kullanırken kimlik doğrulamasında da sorun çıkarabilir. Resmî belge için fotoğrafı bir fotoğrafçıda çektir.

Aynı şey sınav başvurusu, iş başvurusu ya da resmî bir kuruma verilen her fotoğraf için geçerli: Fotoğraf seni göstermeli, yapay zekânın senin yorumunu değil.

## Başkasının fotoğrafını düzenlemek {#baskasi}

- Başkasının yüzü olan bir fotoğrafı yüklemeden önce o kişinin iznini al; çocuklar söz konusuysa özellikle dikkatli ol.
- Birini olmadığı bir yerde, yapmadığı bir şeyi yaparken gösteren düzenleme, şaka bile olsa ciddi sonuçlar doğurabilir; [sahte ses ve video rehberine](rehber:sahte-ses-ve-video) bak.
- Bir kişinin kıyafetini çıkaran ya da onu cinsel içerikli gösteren düzenleme suç teşkil edebilir; hedef olduysan [mağdur rehberine](rehber:deepfake-magduru) bak.

## Görünmez filigran: SynthID nedir? {#synthid}

Google, Gemini'yle üretilen ve düzenlenen görsellere SynthID adında görünmez bir dijital filigran ekliyor. Bu filigran gözle görülmüyor ama Google'ın araçlarıyla tespit edilebiliyor. Yani düzenlenmiş bir fotoğrafı "hiç dokunulmamış" diye sunmak, teknik olarak da ortaya çıkabilir. Gerçek sanılabilecek bir düzenlemeyi paylaşırken etiketle; kurallar [etiket rehberinde](rehber:yapay-zeka-icerik-etiketi).

## Sık yapılan hatalar {#hatalar}

- **Tek komutta beş değişiklik.** Her seferinde bir şey iste.
- **Yüzleri kontrol etmemek.** Orijinalle yan yana bak.
- **Orijinali silmek.** Düzenlenmiş hâlini ayrı kaydet, orijinali sakla.
- **Hassas fotoğraf yüklemek.** Kimlik kartı, çocukların banyo fotoğrafları, özel anlar; yükleme.

## Dürüst sınır {#sinir}

Gemini basit düzenlemelerde çok hızlı ve çoğu zaman yeterli. Hassas rötuş, baskıya gidecek yüksek çözünürlüklü işler ve tutarlı bir ürün kataloğu için profesyonel bir araç ya da bir fotoğrafçı hâlâ daha güvenilir. Sıfırdan görsel üretmek için [görsel üretme rehberine](rehber:gorsel-uretmek) bak.

## Sonraki adım {#sonraki-adim}

Telefonundaki, içinde insan yüzü olmayan bir fotoğrafla (bir manzara, bir ürün) nesne silme komutunu dene. Sonucu orijinalle karşılaştır ve neyin değiştiğine dikkat et.

## Kaynaklar

- Google, Gemini uygulaması planları ve sınırları (Nano Banana 2 ve Nano Banana Pro dahil): [support.google.com/gemini/answer/16275805](https://support.google.com/gemini/answer/16275805)
- Google DeepMind, SynthID: [deepmind.google/models/synthid](https://deepmind.google/models/synthid/)
- Nüfus ve Vatandaşlık İşleri Genel Müdürlüğü (biyometrik fotoğraf şartları): [nvi.gov.tr](https://www.nvi.gov.tr/)
