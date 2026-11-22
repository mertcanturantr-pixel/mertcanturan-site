---
title: Yapay zekâyı internete göndermeden kendi bilgisayarında çalıştırmak: Ollama ve LM Studio
slug: yerel-model
seo_title: Yapay zekâyı kendi bilgisayarında çalıştırmak: Ollama, LM Studio
description: Yerel yapay zekâ modeli nedir, hangi bilgisayarda çalışır, Ollama ve LM Studio ile kurulum, Türkçe performansı ve gizli belgelerde ne zaman mantıklı olduğu.
summary: Belgelerin hiçbir şirketin sunucusuna gitmeden yapay zekâ kullanmak: hangi bilgisayar yeter, LM Studio ve Ollama kurulumu, model seçimi, Türkçe performansı ve gerçekçi beklenti.
keywords: yerel yapay zeka, ollama kurulumu, ollama nasıl kullanılır, lm studio kurulumu, bilgisayarda yapay zeka çalıştırmak, internetsiz yapay zeka, offline chatgpt alternatifi, açık kaynak yapay zeka modeli, gemma llama qwen türkçe, gizli belge için yapay zeka
type: adim-adim
audience: Meraklılar, Gizli belgeyle çalışanlar
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: Ollama örneği Gemma 4'e güncellendi, Ollama bulut modelleri uyarısı eklendi, Kısaca ve soru biçimli başlıklar, iç bağlantılar
video:
video_title:
draft: true
---

ChatGPT'ye, Claude'a ya da Gemini'ye yazdığın her şey o şirketlerin sunucularına gidiyor. Ayarları ne kadar sıkı yaparsan yap, bu değişmiyor. Gizli bir belgeyle çalışıyorsan bir seçenek daha var: Yapay zekâ modelini kendi bilgisayarına indirip internete hiçbir şey göndermeden çalıştırmak. Bunun adı yerel model. Bedeli de var: Daha yavaş ve çoğu zaman daha zayıf cevaplar.

Kısaca: Yerel model, yapay zekâyı kendi bilgisayarında, yazdıklarını hiçbir şirketin sunucusuna göndermeden çalıştırmak demek. En az 16 GB belleği olan bir bilgisayarda LM Studio'yu kur, küçük bir model indir ve dene; komut satırıyla çalışmayı seviyorsan Ollama daha esnek. Gizli bir belgeyi özetletmek ya da taslak düzeltmek gibi işlerde işe yarar; en zor işlerde bulut modellerinin yerini tutmaz.

## Yerel model için hangi bilgisayar yeter? {#donanim}

Yerel modelin hızını belirleyen şey bellek (RAM) ve varsa ekran kartının belleği.

| Bilgisayar | Ne çalıştırabilirsin? |
| --- | --- |
| 8 GB bellek | Çok küçük modeller; basit işler, yavaş |
| 16 GB bellek | Küçük ve orta modeller; özetleme ve metin düzeltme için kullanılabilir |
| 32 GB ve üzeri ya da güçlü ekran kartı | Daha büyük modeller; daha iyi cevaplar |
| Apple M serisi Mac | Bellek ekran kartıyla ortak kullanıldığı için aynı bellekte daha iyi sonuç verir |

Modeller birkaç gigabayttan onlarca gigabayta kadar yer kaplıyor; diskte boş yer olduğundan emin ol.

## LM Studio nasıl kurulur? (en kolay yol) {#lm-studio}

LM Studio, sohbet penceresi olan bir masaüstü uygulama; kod yazmadan kullanılıyor.

1. lmstudio.ai adresinden işletim sistemine uygun sürümü indir ve kur.
2. Uygulamadaki arama bölümünden bir model ara. LM Studio, bilgisayarının belleğine sığıp sığmayacağını gösteriyor.
3. İndirdiğin modeli seç ve sohbet ekranında yazmaya başla.
4. İndirdikten sonra interneti kapatıp dene: Cevap veriyorsa model gerçekten bilgisayarında çalışıyor.

> SAHA: LM Studio'yu kendi bilgisayarında kur, 16 GB'lık bir makinede bir modelin Türkçe bir paragrafı özetlemesinin ne kadar sürdüğünü ölç ve ekran görüntüsü al.

## Ollama nasıl kurulur? (esnek yol) {#ollama}

Ollama, modelleri komut satırından indirip çalıştıran bir araç. Başka programlarla bağlamak, kendi küçük uygulamalarını yazmak istiyorsan daha uygun.

1. ollama.com adresinden indir ve kur.
2. Terminali (Windows'ta PowerShell) aç ve bir model çalıştır:

```sablon
ollama run [MODEL ADI]
```

Örneğin `ollama run gemma4:e4b`, Google'ın Gemma 4 ailesinden küçük bir modeli indirip sohbeti başlatır. Güncel model listesi ve boyutları ollama.com/library adresinde.

Dikkat: Ollama'da adında `cloud` geçen modeller (ör. `gemma4:cloud`) senin bilgisayarında değil, Ollama'nın sunucularında çalışıyor. Gizli bir belgeyle çalışacaksan bu modelleri seçme.

3. Sohbetten çıkmak için `/bye` yaz.

Ollama'yı sohbet penceresiyle kullanmak istersen, Ollama'nın kendi masaüstü uygulaması ya da Open WebUI gibi arayüzler var.

## Hangi yerel modeli seçmelisin? {#model}

Açık modeller her ay değişiyor; isim ezberlemek yerine şu ölçütlere bak:

- **Boyut:** Model adındaki "4b", "8b", "20b" gibi ifadeler milyar parametre sayısı ("e4b" gibi adlarda "e", etkin parametre sayısını gösteriyor). Büyüdükçe daha iyi ama daha yavaş ve daha çok bellek istiyor. 16 GB'lık bir bilgisayar için 4-8 milyar parametre iyi bir başlangıç.
- **Türkçe:** Bazı modeller Türkçede belirgin biçimde daha iyi. Aynı Türkçe metni iki üç modele özetletip karşılaştır; nasıl yapılacağı [test yöntemi rehberinde](rehber:test-yontemi#kendi-testin).
- **Lisans:** Ticari kullanım düşünüyorsan modelin lisansını oku; hepsi her kullanıma açık değil.

Bilinen aileler: Meta'nın Llama'sı, Google'ın Gemma'sı, Alibaba'nın Qwen'i, Mistral ve OpenAI'ın açık ağırlıklı gpt-oss modelleri.

## Gizli belgeyle yerel model kullanmak güvenli mi? {#gizli-belge}

Yerel modelin asıl değeri burada. Model bilgisayarında çalıştığı için yazdıkların dışarı gitmiyor. Yine de:

- **Uygulamanın ayarlarına bak.** Bazı uygulamalar kullanım istatistiği gönderebiliyor ya da internetten model indirmek için bağlantı kuruyor. Modeli indirdikten sonra, gizli işte interneti kapatmak en kesin yol.
- **Bilgisayarının kendisi güvenli olmalı.** Disk şifrelemesi, güçlü bir giriş şifresi ve güncel işletim sistemi.
- **Model yine yanılabilir.** Yerel model de uydurur; hatta küçük modeller daha çok uydurur. Çıktıyı [kontrol rehberindeki](rehber:yapay-zeka-cevabini-kontrol-etmek) gibi kontrol et.

Hukuk, sağlık ve finans gibi mesleki sır taşıyan işlerde yerel model, bulut araçlarına göre gizlilik açısından daha savunulabilir bir seçenek; ama mesleki kuralların ve işvereninin politikası yine geçerli; avukatlar için ayrıntı [avukatlar rehberinde](rehber:avukatlar-icin-yapay-zeka). Hangi bilgilerin hiç yazılmaması gerektiği [ne yazılmaz rehberinde](rehber:yapay-zekaya-ne-yazilmaz).

## Yerel modelden ne beklemelisin? {#beklenti}

- **İşe yarar:** Bir belgeyi özetlemek, metni düzeltmek, taslak yazmak, basit sorular, kod açıklamak.
- **Zorlanır:** Uzun ve karmaşık akıl yürütme, güncel bilgi (internete bağlanmadığı için), çok uzun belgeler, Türkçede ince üslup.
- **Hız:** Ortalama bir dizüstü bilgisayarda cevaplar, bulut servislerine göre belirgin biçimde yavaş gelebilir.

## Sık yapılan hatalar {#hatalar}

- **Belleğe sığmayan model indirmek.** Bilgisayar kilitlenir ya da çok yavaşlar; küçük modelle başla.
- **Bulut modeliyle aynı kaliteyi beklemek.** Küçük bir yerel model, en iyi bulut modellerinin yerini tutmaz.
- **Güvenilmeyen kaynaktan model indirmek.** Modelleri uygulamanın kendi kütüphanesinden ya da bilinen depolardan indir.
- **"Yerel" diye kontrolü bırakmak.** Gizlilik sorununu çözer, doğruluk sorununu çözmez.

## Dürüst sınır {#sinir}

Yerel model herkes için değil. Gizli belgeyle çalışmıyorsan ve bilgisayarın güçlü değilse, ayarları doğru yapılmış bir bulut aracı çoğu iş için daha verimli; ayarlar [gizlilik ayarları rehberinde](rehber:yapay-zeka-gizlilik-ayarlari). Teknik terimler takılırsa [sözlüğe](rehber:yapay-zeka-sozlugu) bak.

## Sonraki adım {#sonraki-adim}

Bilgisayarının belleğine bak (Windows'ta Görev Yöneticisi, Mac'te Bu Mac Hakkında). 16 GB ya da üzerindeyse LM Studio'yu kur, küçük bir model indir ve gizli olmayan bir belgeyle dene; sonucu ChatGPT'nin cevabıyla karşılaştır.

## Kaynaklar

- Ollama: [ollama.com](https://ollama.com/) · model kütüphanesi: [ollama.com/library](https://ollama.com/library) · Gemma 4 sayfası (yerel ve `cloud` etiketleri): [ollama.com/library/gemma4](https://ollama.com/library/gemma4)
- LM Studio: [lmstudio.ai](https://lmstudio.ai/)
- OpenAI, gpt-oss açık ağırlıklı modeller, 5 Ağustos 2025: [openai.com](https://openai.com/index/introducing-gpt-oss/)
