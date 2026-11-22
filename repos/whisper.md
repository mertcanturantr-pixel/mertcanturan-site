---
name: Whisper
slug: whisper
repo: openai/whisper
category: ses-video
summary: OpenAI'ın açık ses tanıma modeli. Toplantı, röportaj ya da ders kaydını kendi bilgisayarında Türkçe dahil yazıya döker.
audience: Herkes, Gazeteciler, Öğrenciler, İçerik üreticileri
difficulty: orta
cost: Ücretsiz; kendi bilgisayarında çalışır
license: MIT
stars: 111,9 bin
checked: 2026-11-16
tested: false
draft: true
---

Bir saatlik toplantı kaydını dinleyip not çıkarmak bir saatten fazla sürüyor. Whisper, ses dosyasını kendi bilgisayarında yazıya döküyor. Kayıt bir bulut şirketine gitmiyor; bu da müşteri görüşmeleri ya da iç toplantılar için ciddi bir fark.

## Ne işe yarar

OpenAI'ın yayımladığı açık bir konuşma tanıma modeli. Birçok dilde, Türkçe dahil, sesi metne çeviriyor. Farklı boyutlarda modelleri var: küçük olanlar hızlı ama daha çok hata yapıyor, büyük olanlar daha doğru ama güçlü donanım istiyor.

## Kimin işine yarar

- Toplantı, röportaj ya da ders kaydını yazıya dökmek isteyenler.
- Videolarına altyazı hazırlayan içerik üreticileri.
- Kayıtlarının dışarı çıkmasını istemeyen avukatlar, gazeteciler, araştırmacılar.

## Kurulum

README'deki adımlar:

1. Bilgisayarında `ffmpeg` kurulu olmalı. README, Ubuntu, macOS ve Windows için paket yöneticisi komutlarını listeliyor.
2. Kurulum: `pip install -U openai-whisper`
3. Kullanım: `whisper kayit.mp3 --model turbo`

README'deki model tablosuna göre yaklaşık bellek ihtiyacı: tiny ve base 1 GB, small 2 GB, medium 5 GB, turbo 6 GB, large 10 GB ekran kartı belleği. README, turbo modelinin çeviri için eğitilmediğini de not ediyor.

## Dikkat etmen gerekenler

- Bir kişinin sesini kaydetmeden ve yazıya dökmeden önce haberi olsun. Ses kaydı kişisel veridir; toplantıda kayıt aldığını baştan söyle.
- Ekran kartın yoksa büyük modeller çok yavaş çalışır. Önce küçük bir modelle kısa bir kayıtla dene.
- Özel isimler, rakamlar ve teknik terimler en sık hata yapılan yerler. Önemli bir metni yayınlamadan önce kaydı dinleyerek kontrol et.

## Dürüst sınır

Gürültülü ortam, üst üste konuşma ve kötü mikrofon sonucu ciddi bozuyor. Kimin konuştuğunu ayırmıyor; bunun için ek araç gerekiyor.

## Benzerleri

whisper.cpp aynı modeli ekran kartı olmayan bilgisayarlarda daha hızlı çalıştıran bir uyarlama.
