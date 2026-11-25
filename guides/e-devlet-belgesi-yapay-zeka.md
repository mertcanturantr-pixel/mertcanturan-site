---
title: e-Devlet belgesini yapay zekâya yüklemeden önce: barkod, kimlik numarası ve güvenli yol
slug: e-devlet-belgesi-yapay-zeka
seo_title: e-Devlet belgesini yapay zekâya yüklemek güvenli mi?
description: e-Devlet belgesini (SGK dökümü, tapu, öğrenci belgesi) yapay zekâya yüklemek güvenli mi? Barkod ve kimlik numarası riski, güvenli yol ve soru şablonları.
summary: e-Devlet'ten aldığın SGK dökümü, tapu ya da adli sicil gibi belgeleri yapay zekâya sorarken barkod ve kimlik numarası riski, belgeyi anonimleştirmek ve işe yarayan soru şablonları.
keywords: e-devlet belgesi chatgpt'ye yüklemek güvenli mi, sgk hizmet dökümü nasıl okunur, hizmet dökümü yapay zeka, barkodlu belge doğrulama, tapu şerhi ne demek, e-devlet şifresi güvenliği, tc kimlik numarası paylaşmak, e-devlet belgesi karekod
type: kontrol-listesi
audience: Herkes
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: karekod riski, veri ayarı adımı ve KVKK kaynakları eklendi, başlıklar soru biçimine çevrildi.
video:
video_title:
draft: false
---

SGK hizmet dökümünde bir boşluk var ve ne anlama geldiğini bilmiyorsun; ya da tapu kaydındaki bir şerhi anlamak istiyorsun. Belgeyi e-Devlet'ten PDF olarak indirip ChatGPT'ye yüklemek en kolayı gibi görünüyor. Ama e-Devlet belgeleri, sıradan bir belgeden daha fazla şey taşıyor: Kimlik numaranı, adresini ve çoğu zaman bir barkod. Barkodlu belgeler, barkod numarasıyla (bazı belgelerde kimlik numarasıyla birlikte) ya da belgedeki karekodu e-Devlet uygulamasıyla okutarak "Barkodlu Belge Doğrulama" hizmetinde başkaları tarafından da görüntülenebiliyor.

Kısaca: e-Devlet belgesini PDF ya da ekran görüntüsü olarak olduğu gibi yükleme; yalnızca sorduğun satırları, kimlik numarası, ad, adres, barkod ve karekodu çıkararak kopyala. e-Devlet şifreni hiçbir yapay zekâya, hiçbir siteye yazma. Hukuki ya da mali sonuç doğuran bir konuda yapay zekânın cevabını ilgili kurumla ya da bir uzmanla doğrula.

## e-Devlet belgesinde hangi hassas bilgiler var? {#neler-var}

| Belge | İçindeki hassas bilgiler |
| --- | --- |
| SGK hizmet dökümü | Kimlik numarası, işveren adları, kazançlar |
| Tapu bilgileri | Kimlik numarası, taşınmaz adresi, ipotek ve şerhler |
| Adli sicil kaydı | Kimlik numarası, varsa sabıka bilgisi |
| Yerleşim yeri (ikametgâh) belgesi | Kimlik numarası, açık adres, aile bilgileri |
| Öğrenci ve mezuniyet belgeleri | Kimlik numarası, okul, numara |
| Barkodlu her belge | Barkod numarası ve karekod (ikisi de belgenin aslını görüntülemeye yarar) |

Bu bilgilerin bir kısmı, kimlik avı ve dolandırıcılık için tam olarak aranan bilgiler.

## Belgeyi yapay zekâya güvenle nasıl sorarsın? {#guvenli-yol}

1. **Aracın veri ayarına bak.** Kullandığın yapay zekânın yazdıklarını modeli eğitmek için kullanmasını kapat; üç araçta nasıl yapıldığı [ne yazılmaz rehberinde](rehber:yapay-zekaya-ne-yazilmaz#ayarlar).
2. **Sadece gereken kısmı al.** Belgenin tamamı yerine sorduğun satırları kopyala ya da yaz.
3. **Kimlik bilgilerini çıkar.** Ad, soyad, kimlik numarası, adres, barkod numarası, işveren unvanı (gerekmiyorsa).
4. **Yerine etiket koy.** "İşveren A", "2019-2021 arası" gibi.
5. **Ekran görüntüsü yüklemen gerekiyorsa** hassas alanları, barkodu ve karekodu önce telefonunun düzenleme aracıyla tamamen kapat (bulanıklaştırma yerine düz siyah kutu). PDF'te siyah kutu çizmek her zaman yetmez; alttaki metin seçilebilir kalabilir. Emin değilsen sayfanın ekran görüntüsünü alıp onu kapat.

## Hangi belge için hangi soru: şablonlar {#sablonlar}

**SGK hizmet dökümü:**

```sablon
SGK hizmet dökümümde şu satırlar var (kimlik bilgilerimi çıkardım):
[SATIRLAR: DÖNEM, GÜN SAYISI, BELGE TÜRÜ, İŞVEREN A/B]
Bu sütunların ne anlama geldiğini ve gün sayısı eksik görünen dönemlerin genelde hangi nedenlerle olabileceğini açıkla. Emekliliğim hakkında kesin bir hesap yapma; SGK'ya hangi soruları sormam gerektiğini listele.
```

**Tapu kaydındaki bir şerh ya da beyan:**

```sablon
Tapu kaydımda şu ifade geçiyor: "[İFADE]". Bunun genel olarak ne anlama geldiğini sade bir dille açıkla ve satış ya da kredi gibi bir işlemde ne tür sonuçları olabileceğini söyle. Kesin bir hukuki değerlendirme yapma; tapu müdürlüğüne ya da bir avukata hangi soruları sormam gerektiğini yaz.
```

**Bir resmî yazıyı anlamak:**

```sablon
Bir kurumdan aldığım yazıda şu paragraf var (isim ve numaraları çıkardım): "[PARAGRAF]". Benden ne istendiğini, bir süre verilip verilmediğini ve ne yapmam gerektiğini maddeler hâlinde yaz. Paragrafta olmayan bir şey ekleme.
```

Resmî yazılardaki süreler (itiraz, ödeme, başvuru) kaçırılırsa hak kaybına yol açabilir. Yapay zekânın söylediği süreyi yazının aslından ve ilgili kurumdan kontrol et; dilekçe gerekiyorsa [dilekçe rehberine](rehber:yapay-zekayla-dilekce) bak.

## e-Devlet şifresi yapay zekâya yazılır mı? {#sifre}

- e-Devlet şifreni, kimlik numaranla birlikte hiçbir yapay zekâya, hiçbir siteye, hiçbir uygulamaya yazma.
- "Yapay zekâ ile e-Devlet işlemlerinizi yapalım", "SGK dökümünüzü analiz edelim, emeklilik tarihinizi hesaplayalım" diyen ve senden e-Devlet girişi isteyen siteler ve uygulamalar kimlik avı olabilir. e-Devlet'e yalnızca turkiye.gov.tr adresinden ya da resmî e-Devlet uygulamasından gir.
- Şifreni bir yere yazdıysan hemen değiştir.

## Adli sicil ve sağlık raporu gibi belgeler {#hassas}

Adli sicil kaydı, sağlık raporları ve engellilik raporları gibi belgeler en hassas bilgileri taşıyor. Sağlık ve ceza mahkûmiyetine ilişkin bilgiler, 6698 sayılı Kişisel Verilerin Korunması Kanunu'nda (KVKK) "özel nitelikli kişisel veri" sayılıyor (m.6). Bunları yapay zekâya sormak yerine ilgili kuruma ya da bir avukata, doktora danışmak daha doğru. Tahlil sonuçları için [tahlil rehberine](rehber:tahlil-sonucu-yapay-zeka) bak.

## Sık yapılan hatalar {#hatalar}

- **PDF'yi olduğu gibi yüklemek.** Barkod ve kimlik numarasıyla birlikte.
- **Yapay zekânın hesapladığı emeklilik tarihine güvenmek.** Emeklilik şartları karmaşık ve kişiye özel; SGK'dan teyit et.
- **Belgeyi başkasıyla paylaşırken barkodu kapatmamak.** Yapay zekâ olmasa bile, barkodlu belgeyi paylaşmak belgeyi görüntüleme imkânı verebilir.
- **e-Devlet girişi isteyen "yardımcı" sitelere güvenmek.**

## Yapay zekâ bu belgelerde nereye kadar yardım eder? {#sinir}

Yapay zekâ resmî bir belgedeki terimleri ve genel kuralları anlatmakta iyi; ama mevzuat değişiyor ve senin durumuna özgü istisnaları bilmiyor. Emeklilik, tapu, vergi ve ceza kayıtları gibi konularda kesin cevabı ilgili kurum ya da bir uzman verir. Neyin hiç yazılmaması gerektiğinin genel listesi [ne yazılmaz rehberinde](rehber:yapay-zekaya-ne-yazilmaz).

## Sonraki adım {#sonraki-adim}

Merak ettiğin bir e-Devlet belgesini aç, sadece sormak istediğin satırları kimlik bilgilerini çıkararak kopyala ve şablonlardan biriyle sor. Cevaptaki "kuruma sorulacak sorular" listesini sakla.

## Kaynaklar

- e-Devlet Kapısı, Barkodlu Belge Doğrulama hizmeti: [turkiye.gov.tr](https://www.turkiye.gov.tr/belge-dogrulama)
- 6698 sayılı Kişisel Verilerin Korunması Kanunu, m.6 (özel nitelikli kişisel veriler): [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/)
- Kişisel Verileri Koruma Kurumu, "Üretken Yapay Zekâ ve Kişisel Verilerin Korunması Rehberi (15 Soruda)", 24 Kasım 2025: [kvkk.gov.tr](https://www.kvkk.gov.tr/Icerik/8547/uretken-yapay-zeka-ve-kisisel-verilerin-korunmasi-rehberi-15-soruda)
