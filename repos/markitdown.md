---
name: MarkItDown
slug: markitdown
repo: microsoft/markitdown
category: belge
summary: Microsoft'un PDF, Word, Excel ve PowerPoint dosyalarını yapay zekânın en iyi anladığı düz metin biçimine (Markdown) çeviren aracı.
audience: Yazılımcılar, Çok belgeyle çalışanlar
difficulty: orta
cost: Ücretsiz; bilgisayarında çalışır
license: MIT
stars: 194,2 bin
checked: 2026-11-16
tested: false
draft: true
---

Bir PDF'i yapay zekâya yüklediğinde tablolar karışıyor, başlıklar kayboluyor, bazen sayfa numaraları metnin ortasına giriyor. MarkItDown, dosyayı önce başlıkları ve tabloları koruyan düz bir metne çeviriyor. Yapay zekâya bu metni verdiğinde hem daha iyi cevap alıyorsun hem de daha az yer tutuyor.

## Ne işe yarar

Microsoft'un geliştirdiği bir Python aracı. README'ye göre PDF, PowerPoint, Word, Excel, resim (metin okuma ile), ses (yazıya dökme ile), HTML, CSV, JSON, XML, ZIP, YouTube bağlantıları ve EPub dosyalarını Markdown'a çeviriyor.

## Kimin işine yarar

- Çok sayıda belgeyi yapay zekâyla işleyen ofisler ve yazılımcılar.
- Belgeyle sohbet uygulamalarına (AnythingLLM gibi) daha temiz metin vermek isteyenler.

## Kurulum

Bilgisayarında Python kurulu olmalı. README'deki komutlar:

- Kurulum: `pip install 'markitdown[all]'`
- Kullanım: `markitdown dosya.pdf -o belge.md`

Çıkan `belge.md` dosyasını yapay zekâ aracına yükleyebilir ya da içeriğini kopyalayabilirsin.

## Dikkat etmen gerekenler

- Çeviri bilgisayarında yapılıyor; dosya bir yere gönderilmiyor. Ama ses ve görsel çevirme gibi bazı özellikler ek ayar ya da harici servis isteyebilir; README'deki ayrıntıya bak.
- Taranmış belgelerde sonuç metin okumanın kalitesine bağlı; çıktıya göz at.

## Dürüst sınır

Terminalden kullanılan bir araç; pencereli bir uygulaması yok. Ayda birkaç belge çeviriyorsan zahmetine değmeyebilir, belgeyi doğrudan yüklemek yeter.

## Benzerleri

IBM'in Docling'i de benzer işi yapıyor ve karmaşık tablolarda güçlü.
