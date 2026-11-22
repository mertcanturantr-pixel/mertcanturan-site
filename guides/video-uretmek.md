---
title: Yapay zekâyla video üretmek: hangi araç, nasıl komut ve kullanmadan önce bilmen gerekenler
slug: video-uretmek
seo_title: Yapay zekâyla video üretmek: araçlar, komut ve kurallar
description: Yapay zekâyla kısa video üretmek: Gemini ve Google Flow'da Veo, sahne komutu şablonu, Sora'nın kapanması, gerçek kişi ve ses riskleri, etiket kuralı.
summary: Yapay zekâyla kısa video üretmek: hangi araç hangi planda, sahne komutunun parçaları, beklenti ve sınırlar, gerçek kişi ve ses kullanımında riskler ve paylaşmadan önce etiket.
keywords: yapay zeka ile video oluşturma, gemini veo nasıl kullanılır, google flow nedir, sora kapandı mı, yapay zeka video prompt örnekleri, yapay zeka reklam videosu, ücretsiz yapay zeka video
type: adim-adim
audience: İçerik üreticileri, Esnaf
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm.
change: 2026-11-16 dört rollü denetim: Gemini'de video üretmenin hangi planlarda olduğu Google'ın sınırlar sayfasına göre düzeltildi, dijital kopya kuralı yönetmelik diline çekildi, kaynak ve iç bağlantılar eklendi.
video:
video_title:
draft: true
---

Bir cümle yazıyorsun ve birkaç dakika sonra sekiz saniyelik, sesli, sinematik bir video çıkıyor. Yapay zekâyla video üretmek artık gerçek bir şey; sosyal medyada gördüğün garip ama etkileyici kısa videoların bir kısmı böyle yapıldı. Ama bu araçlar hâlâ kısa klipler üretiyor, ücretli ve sınırlı, ve aynı karakteri sahneden sahneye tutarlı tutmakta zorlanıyor. Bir reklam filmi değil, bir fikir taslağı ya da kısa bir sosyal medya klibi bekle.

Kısaca: Kasım 2026 itibarıyla yapay zekâyla video üretmenin Türkiye'den en kolay yolu, Google AI Plus ve üstü planlarda Gemini'deki Veo ya da Google Flow; ücretsiz Gemini planında video üretme yok. OpenAI'ın Sora uygulaması 26 Nisan 2026'da kapandı. Komutta sahneyi, kamera hareketini ve sesi ayrı ayrı tarif et; gerçek kişileri ve sesleri izinsiz kullanma, gerçek sanılabilecek videoyu etiketle.

## Yapay zekâyla video hangi araçta üretilir? {#arac}

| Araç | Durum (Kasım 2026) |
| --- | --- |
| Gemini uygulaması (Veo) | Google AI Plus, Pro ve Ultra planlarında; kullanım sınırı plana göre artıyor. Ücretsiz planda video üretme yok |
| Google Flow | Google'ın film yapım aracı; kredi sistemiyle çalışıyor (Google AI Pro'da aylık 1.000 kredi) |
| OpenAI Sora | Uygulama ve web sitesi 26 Nisan 2026'da kapandı |
| Diğer araçlar (Runway, Kling ve benzerleri) | Çoğu ücretli; kullanım koşulları ve verinin nereye gittiği araçtan araca değişiyor |

Planlar ve sınırlar sık değişiyor; güncel durumu aracın kendi sayfasından kontrol et. Google planlarının Türkiye fiyatları [hangi yapay zekâ rehberinde](rehber:hangi-yapay-zeka).

> SAHA: Gemini'de bir Veo videosu üret; komutu, bekleme süresini ve sonucun kısa bir parçasını ekle. Türkçe konuşma içeren bir video denediysen dudak senkronunun nasıl olduğunu yaz.

## Video komutu (prompt) nasıl yazılır? {#komut}

Video komutu, görsel komutuna zaman ve ses ekliyor:

```sablon
Sahne: [NE OLUYOR, ÖRNEĞİN "BİR FIRINCI SABAHIN ERKEN SAATİNDE TEPSİYİ FIRINDAN ÇIKARIYOR"]
Ortam ve ışık: [MEKÂN, SAAT, HAVA]
Kamera: [SABİT / YAVAŞÇA YAKLAŞAN / KONUNUN ETRAFINDA DÖNEN / ELDEN ÇEKİM]
Üslup: [GERÇEKÇİ / ANİMASYON / ESKİ FİLM]
Ses: [ORTAM SESİ, MÜZİK, KONUŞMA VARSA TAM CÜMLE VE KİMİN SÖYLEDİĞİ]
Süre ve format: [SANİYE, DİKEY 9:16 / YATAY 16:9]
Olmasın: [YAZI, LOGO, TANINMIŞ KİŞİ]
```

İpuçları:

- **Tek sahne, tek hareket.** Sekiz saniyede üç olay olmaz.
- **Konuşma kısa olsun.** Uzun cümlelerde dudak hareketleri ve Türkçe telaffuz bozulabiliyor.
- **Yazıyı videoya yazdırma.** Altyazı ve başlıkları kurguda sen ekle.
- **Aynı karakteri birden fazla sahnede istiyorsan,** araçların "referans görsel" özelliğini kullan; yine de tam tutarlılık bekleme.

## Klipleri nasıl birleştirmeli? {#kurgu}

Yapay zekâ videoları en iyi, kısa parçalar olarak kullanıldığında çalışıyor. Birkaç klip üret, en iyilerini seç ve bir kurgu programında (CapCut, telefonun kendi düzenleyicisi gibi) birleştir; sesi, altyazıyı ve geçişleri orada ekle.

## Paylaşmadan önce: hukuki kontrol listesi {#kurallar}

- [ ] **Gerçek kişi:** Gerçek bir kişinin yüzünü ya da sesini, izni olmadan kullanma. 1 Ağustos 2026'dan beri Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği, gerçek bir kişinin yapay zekâyla üretilmiş dijital kopyasının ürünü deneyimlemiş ya da tavsiye ediyormuş gibi gösterildiği gerçeğe aykırı reklamları açıkça yasaklıyor.
- [ ] **Ses:** Kendi sesini klonlatıyorsan aracın sesini nasıl sakladığına bak; başkasının sesini klonlamak için açık izin gerekiyor. Ses klonlama dolandırıcılıkları için [sahte ses rehberine](rehber:sahte-ses-ve-video) bak.
- [ ] **Etiket:** Gerçek sanılabilecek bir videoyu YouTube, Instagram ya da TikTok'ta paylaşırken platformun etiket ayarını aç; reklamsa Türkiye'deki reklam kuralını da uygula. Ayrıntısı [etiket rehberinde](rehber:yapay-zeka-icerik-etiketi).
- [ ] **Telif:** Tanınmış karakterler, markalar ve müzikler; [telif rehberine](rehber:yapay-zeka-ve-telif) bak.
- [ ] **Yanıltıcı içerik:** Haber, afet ya da siyasi olay gibi görünen yapay zekâ videoları, etiketli olsa bile yanlış anlaşılabilir ve yayılabilir.

## Sık yapılan hatalar {#hatalar}

- **Uzun, çok olaylı komut.** Kısa ve tek sahne.
- **İlk sonucu yayınlamak.** Ellere, yüzlere, yazılara ve fizik hatalarına (havada duran nesneler, birbirine geçen eşyalar) dikkatle bak.
- **Videonun tamamını yapay zekâya bırakmak.** Kurgu, ses ve yazı senin elinde olmalı.
- **Etiketi atlamak.** Platform videoyu kaldırabilir ya da kendisi etiketleyebilir.

## Dürüst sınır {#sinir}

Yapay zekâ videosu şimdilik kısa, göz alıcı ama kontrolü zor parçalar üretiyor. Bir ürünü gerçekten tanıtacak, tutarlı bir marka videosu için hâlâ gerçek çekim ve kurgu daha güvenilir. Fiyatlar yüksek ve kotalar düşük; deneme yapmadan büyük bir iş planlama. Sadece "yüzsüz kanal" kurup yapay zekâ videolarıyla para kazanma vaatlerinin gerçeği [yan iş rehberinde](rehber:yapay-zeka-yan-is-gercekleri).

## Sonraki adım {#sonraki-adim}

Bir ürün ya da yer için sekiz saniyelik tek bir sahne yaz ve şablona göre komut hazırla. Erişimin varsa üret; yoksa komutu sakla, bir sonraki denemende kullan. Videonun kapak görseli ya da tek kare için [görsel üretme rehberine](rehber:gorsel-uretmek#komut) bak.

## Kaynaklar

- Google, Gemini uygulaması planları ve sınırları (Veo video üretme dahil): [support.google.com/gemini/answer/16275805](https://support.google.com/gemini/answer/16275805)
- OpenAI'ın Sora uygulamasını kapatması (uygulama 26 Nisan 2026, API 24 Eylül 2026): [MacRumors](https://macrumors.com/2026/03/24/openai-discontinuing-sora-ai-video-app/) · [The Decoder](https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/)
- Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği'nde değişiklik, Resmî Gazete 1 Temmuz 2026 (33297), yürürlük 1 Ağustos 2026: [Resmî Gazete](https://www.resmigazete.gov.tr/eskiler/2026/07/20260701-9.htm) · [Ticaret Bakanlığı duyurusu](https://ticaret.gov.tr/haberler/ticaret-bakanligi-tarafindan-ticari-reklam-ve-haksiz-ticari-uygulamalar-yonetmeliginde-yapilan-degisikliklerle-tuketicilerin-aldatici-reklam-ve-ticari-uygulamalara-karsi-korunmasi-guclendiriliyor)
- Google AI planları (Türkiye), Flow kredisi ve Veo: [gemini.google/tr/subscriptions](https://gemini.google/tr/subscriptions?hl=tr)
