---
name: Ollama
slug: ollama
repo: ollama/ollama
category: yerel
summary: Açık yapay zekâ modellerini internete göndermeden kendi bilgisayarında çalıştırmanın en kolay yolu. Tek komutla kurulur.
audience: Herkes, Gizliliğe önem verenler, Yazılımcılar
difficulty: kolay
cost: Ücretsiz; modeller kendi bilgisayarında çalışır
license: MIT
stars: 184,7 bin
checked: 2026-11-16
tested: false
draft: true
---

ChatGPT'ye yazdığın her şey OpenAI'ın sunucularına gidiyor. Bir müşteri sözleşmesini ya da şirket içi bir belgeyi özetletmek istediğinde bu bir sorun. Ollama, Gemma, Qwen, DeepSeek ya da gpt-oss gibi açık modelleri kendi bilgisayarına indirip orada çalıştırmanı sağlıyor. Yazdıkların bilgisayarından çıkmıyor.

## Ne işe yarar

Ollama bir model yöneticisi. Modeli indirir, bilgisayarının gücüne göre çalıştırır ve sana terminalde bir sohbet penceresi açar. Arka planda bir de yerel bir arayüz (API) sunar; Open WebUI ya da AnythingLLM gibi uygulamalar bu arayüze bağlanıp sana ChatGPT'ye benzeyen bir ekran verir.

## Kimin işine yarar

- Gizli belgelerle çalışan herkes: avukat, muhasebeci, insan kaynakları, sağlık çalışanı.
- İnternet bağlantısı olmadan yapay zekâ kullanmak isteyenler.
- Kendi uygulamasına ücretsiz bir model bağlamak isteyen yazılımcılar.

## Kurulum

Deponun README dosyasındaki resmî komutlar:

- macOS ve Linux: `curl -fsSL https://ollama.com/install.sh | sh`
- Windows (PowerShell): `irm https://ollama.com/install.ps1 | iex`

Kurulumdan sonra terminale `ollama run` ve ardından bir model adı yazarsın. Hangi modellerin olduğunu ve boyutlarını ollama.com/library sayfasında görebilirsin. İlk çalıştırmada model indirildiği için birkaç dakika sürebilir.

## Dikkat etmen gerekenler

- Model boyutu bilgisayarına uymalı. Küçük modeller sıradan bir dizüstünde çalışır; büyük modeller güçlü bir ekran kartı ya da bol bellek ister. Bilgisayarın yetmezse cevaplar çok yavaş gelir.
- Yerel modeller ChatGPT ya da Claude'un ücretli sürümleri kadar iyi değil. Türkçe cevap kalitesi modelden modele çok değişiyor; kendi işinle birkaç modeli dene.
- Kurulum komutu internetten bir betik indirip çalıştırıyor. Yalnızca ollama.com adresindeki resmî komutu kullan.

## Dürüst sınır

Uzun ve karmaşık hukuki ya da teknik metinlerde yerel modellerin hata oranı yüksek. Gizlilik kazanırsın ama kaliteden bir miktar verirsin. Kişisel veriyi dışarı göndermemen gereken işlerde bu takas çoğu zaman değer.

## Benzerleri

LM Studio da aynı işi pencereli bir uygulamayla yapıyor ama açık kaynak değil. Arayüz istiyorsan Ollama'yı Open WebUI ya da AnythingLLM ile birlikte kullan.
