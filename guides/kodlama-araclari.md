---
title: Yapay zekâ kodlama araçları: Codex, Claude Code, Copilot ve Cursor'u güvenli kullanmak
slug: kodlama-araclari
seo_title: Yapay zekâ kodlama araçları: Codex, Claude Code, Copilot, Cursor
description: Codex, Claude Code, Copilot ve Cursor: hangisi ne işe yarar, görev tanımı, kod incelemesi, testler, gizli anahtarlar ve şirket kodunda dikkat.
summary: Codex, Claude Code, GitHub Copilot ve Cursor gibi kodlama araçları: hangi işe hangisi, iyi görev tanımı, üretilen kodu incelemek, testler, gizli anahtar ve şirket kodunda kurallar.
keywords: yapay zeka kodlama araçları, claude code nedir, openai codex nasıl kullanılır, github copilot ajan modu, cursor editör, codex mi claude code mu, yapay zeka ile kod yazma güvenliği, api anahtarı sızdı ne yapmalı, vibe coding riskleri, yapay zeka kod incelemesi
type: kontrol-listesi
topic: uretim
audience: Yazılımcılar
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: Codex'in ChatGPT masaüstü uygulamasına katılması kaynakla netleştirildi, Claude Code belgeleri adresi güncellendi, komut enjeksiyonu ve talimat dosyası (CLAUDE.md/AGENTS.md) eklendi, Kısaca ve başlıklar
video:
video_title:
draft: true
---

Yapay zekâ kodlama araçları artık bir satırı tamamlamanın ötesine geçti: Bir hata kaydını okuyup kodu düzeltiyor, testleri çalıştırıyor, birkaç dosyayı birden değiştiriyor ve bir çekme isteği (pull request) açıyor. Hız gerçek; ama hızla birlikte gelen riskler de. İncelenmeden birleştirilen kod, sızdırılmış bir API anahtarı ya da "testleri geçsin diye" gevşetilmiş bir kontrol, haftalar sonra bir üretim hatası olarak geri dönüyor.

Kısaca: Codex, Claude Code, GitHub Copilot ve Cursor aynı işi farklı arayüzlerle yapıyor; seçimi editörüne, ekibinin planına ve şirketinin veri kurallarına göre yap. Hangisini seçersen seç, görevi dar tanımla ve kabul ölçütünü yaz, aracın değişikliğini bir ekip arkadaşının kodu gibi incele, testleri kendin çalıştır. Gizli anahtarları depodan ve sohbetten uzak tut; şirket kodunda yalnızca şirketin izin verdiği araç ve planı kullan.

Kod bilmiyorsan ve yapay zekâyla uygulama yapmak istiyorsan, önce [uygulama rehberine](rehber:yapay-zekayla-uygulama) bak; bu sayfa kod yazan kişiler için.

## Hangi kodlama aracı ne işe yarar? {#araclar}

Kasım 2026 itibarıyla en yaygın dört araç:

| Araç | Nasıl çalışıyor |
| --- | --- |
| GitHub Copilot | Editörde satır ve fonksiyon tamamlama, sohbet ve görev üstlenen ajan kipi |
| Cursor | Yapay zekâ odaklı editör; dosyalar arası değişiklik |
| Claude Code | Terminalde, editörde, masaüstü uygulamasında ve web'de çalışan ajan; depoyu okuyup komut çalıştırıyor |
| OpenAI Codex | Bulutta ya da yerelde görev üstlenen ajan; 9 Temmuz 2026'dan beri ChatGPT masaüstü uygulamasının içinde, orada ücretsiz dahil her planda |

Hepsi aynı işi farklı arayüzlerle yapıyor. Seçimi; editör alışkanlığına, ekibinin kullandığı plana ve şirketinin veri kurallarına göre yap. Ürün adları ve planlar sık değişiyor.

> SAHA: Kendi projelerinden birinde aynı küçük hatayı iki farklı araçla düzelttir; süreyi, değişiklik sayısını ve inceleme sırasında bulduğun sorunları not et.

## Araca görev nasıl tanımlanır? {#gorev}

```sablon
Bağlam: [PROJE, İLGİLİ DOSYALAR, KULLANILAN SÜRÜMLER]
Sorun: [NE OLUYOR, NASIL TEKRARLANIYOR, HATA MESAJI]
Beklenen davranış: [NE OLMALI]
Kabul ölçütü:
- [ÖRNEĞİN "ŞU TEST GEÇMELİ", "ŞU ENDPOINT 400 DÖNMELİ"]
- Mevcut testler bozulmamalı.
Sınırlar:
- Görev dışındaki dosyalara dokunma.
- Yeni bağımlılık ekleme; gerekiyorsa önce sor.
- Testleri geçirmek için doğrulamaları kaldırma ya da beklentileri değiştirme.
Önce kök nedeni açıkla, sonra değişikliği yap.
```

"Testleri geçirmek için doğrulamaları kaldırma" satırı, bu araçların bilinen bir eğilimine karşı.

## Aracın yazdığı kod nasıl incelenir? {#inceleme}

Aracın değişikliğini, bir ekip arkadaşının çekme isteği gibi oku:

- [ ] Değişiklik sorunun kök nedenini mi çözüyor, yoksa belirtiyi mi gizliyor?
- [ ] Görev dışı dosyalarda değişiklik var mı?
- [ ] Yeni bağımlılık eklendi mi? Gerçekten var mı, güvenilir mi, lisansı uygun mu? (Araçlar bazen var olmayan paket adları uyduruyor; bu adlarla zararlı paket yayınlayanlar var.)
- [ ] Hata yakalama doğru mu, yoksa hatalar sessizce yutuluyor mu?
- [ ] Yetkilendirme ve girdi doğrulama kontrolleri yerinde mi?
- [ ] Testler gerçekten davranışı test ediyor mu, yoksa sadece geçmek için mi yazıldı?

## Doğrulamayı gerçekten çalıştır {#dogrulama}

Aracın "testler geçti" demesi yetmez; testleri, tip kontrolünü ve lint'i kendin ya da CI'da çalıştır. Kullanıcı arayüzü değişikliklerinde ilgili ekranı aç ve akışı dene. Veritabanı değişikliklerinde (migration) mevcut veriyi, geri dönüşü ve kilitlenme riskini ayrıca değerlendir; bu tür değişiklikleri araca onaysız çalıştırtma.

## API anahtarları ve şifreler nasıl korunur? {#gizli}

- API anahtarlarını, şifreleri ve bağlantı dizelerini koda yazma; ortam değişkeni ya da bir gizli bilgi yöneticisi kullan.
- `.env` dosyalarının depoya girmediğini kontrol et (.gitignore).
- Araca hata ayıklatırken log ya da yapılandırma dosyası yapıştırıyorsan, içindeki anahtarları önce sil.
- Bir anahtar yanlışlıkla sohbete, bir commit'e ya da herkese açık bir depoya girdiyse silmek yetmez; anahtarı hemen iptal et ve yenisini oluştur.
- Ajan kipinde aracın hangi komutları onaysız çalıştırabileceğini ayarlardan sınırla; özellikle silme, dağıtım ve ağ komutları için onay iste.
- Aracın okuduğu README, issue, bağımlılık belgesi ya da web sayfasındaki metin ona talimat gibi gelebilir (komut enjeksiyonu, prompt injection). Tanımadığın bir depoda ajanı onaysız çalıştırma; riskin genel anlatımı [ajanlar rehberinde](rehber:yapay-zeka-ajanlari#gizli-talimat).

## Şirket kodunda nelere dikkat etmeli? {#sirket}

- Şirketin izin verdiği araçları ve kurumsal planları kullan; kişisel hesaba şirket kodu yükleme. Gerekçesi [iş yeri rehberinde](rehber:isyerinde-yapay-zeka-kullanmak#gizlilik).
- Kurumsal planlarda kodun eğitimde kullanılmadığını ve saklama süresini kontrol et.
- Müşteri verisi içeren veritabanı dökümlerini ve logları araca verme; örnek ya da anonimleştirilmiş veri kullan.
- Üretilen kodun lisans durumuna dikkat: GitHub Copilot'ta kamuya açık kodla eşleşen önerileri engelleyen ya da kaynağını gösteren bir ayar var; şirket kodunda bunu açık tut.

## Sık yapılan hatalar {#hatalar}

- **İncelemeden birleştirmek.** Hız, hatanın da hızlı yayılması demek.
- **Belirsiz görev.** "Şunu düzelt" yerine sorun, beklenti ve kabul ölçütü.
- **Bütün depoyu her seferinde baştan taratmak.** Proje için kısa bir kod haritası ve talimat dosyası tut (Claude Code `CLAUDE.md` okuyor; Codex ve birçok araç `AGENTS.md` okuyor); araç neye nereden bakacağını bilsin.
- **Ajana üretim ortamında yetki vermek.** Dağıtım ve veri silme insanda kalsın.

## Dürüst sınır {#sinir}

Bu araçlar tekrar eden kodda, testlerde, hata ayıklamada ve tanımadığın bir kod tabanını anlamada çok zaman kazandırıyor. Mimari kararlar, güvenlik tasarımı, iş kurallarının doğruluğu ve "bu özellik gerçekten gerekli mi" sorusu hâlâ senin işin. Kodun sorumluluğu, onu kim yazmış olursa olsun, birleştirene ait.

## Sonraki adım {#sonraki-adim}

Projendeki küçük ve iyi tanımlı bir hatayı şablonla araca ver. Değişikliği inceleme listesinden geçir ve testleri kendin çalıştır. Projen için talimat dosyan yoksa bir tane yaz: komutlar, klasör yapısı, dokunulmaması gereken yerler.

## Kaynaklar

- GitHub Copilot belgeleri: [docs.github.com/copilot](https://docs.github.com/copilot)
- Anthropic, Claude Code belgeleri: [code.claude.com/docs](https://code.claude.com/docs)
- OpenAI, ChatGPT Work ve Codex uygulamasının ChatGPT masaüstü uygulamasına katılması, 9 Temmuz 2026: [openai.com](https://openai.com/index/chatgpt-for-your-most-ambitious-work)
- Cursor belgeleri: [docs.cursor.com](https://docs.cursor.com/)
- OWASP, büyük dil modeli uygulamaları için en önemli 10 risk: [owasp.org](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
