---
name: Open WebUI
slug: open-webui
repo: open-webui/open-webui
category: yerel
summary: Kendi bilgisayarında çalışan modellere ChatGPT'ye benzeyen bir sohbet ekranı verir. Ekip içinde kullanıcı açma ve belge yükleme de var.
audience: Küçük işletmeler, Ekipler, Yazılımcılar
difficulty: orta
cost: Ücretsiz; kendi bilgisayarında ya da sunucunda çalışır
license: Open-WebUI
license_note: Kendi lisansı var ve açık kaynak lisansları listesinde değil. Depo sayfası, lisansta Open WebUI adını ve logosunu korumayı isteyen bir marka koşulu olduğunu söylüyor; istisnaları ve ayrıntısı deponun LICENSE dosyasında.
stars: 157,5 bin
checked: 2026-11-16
tested: false
draft: true
---

Ollama'yı kurdun ama terminalde sohbet etmek kimsenin hoşuna gitmiyor. Open WebUI, yerel modellere tarayıcıdan açılan, sohbet geçmişi, belge yükleme ve kullanıcı hesapları olan bir arayüz ekliyor. İstersen OpenAI uyumlu ücretli bir servise de bağlayabiliyorsun.

## Ne işe yarar

Tarayıcıda açılan bir sohbet ekranı. Ollama'daki modelleri otomatik görüyor. Belgeyi yükleyip ona soru sorabiliyor, sohbetleri saklayabiliyor, birden fazla kullanıcı açabiliyorsun.

## Kimin işine yarar

- Ofiste birkaç kişinin aynı yerel modeli ChatGPT gibi kullanmasını isteyen küçük işletmeler.
- Ollama kurup terminalle uğraşmak istemeyenler.

## Kurulum

Deponun README dosyasındaki iki resmî yol:

1. Python ile (README Python 3.12 öneriyor): `pip install open-webui`, ardından `open-webui serve`. Tarayıcıda `http://localhost:8080` adresini aç.
2. Docker ile: `docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main`. Tarayıcıda `http://localhost:3000` adresini aç.

İlk açılışta oluşturduğun hesap yönetici hesabı olur.

## Dikkat etmen gerekenler

- Lisans: Açık kaynak lisansı değil, kendi lisansı var. Kendi işinde kullanmak için genellikle sorun yok; ama arayüzü kendi markanla müşterine satmayı düşünüyorsan lisans metnini oku.
- Ekip içinde kullanacaksan çalışanların sohbetleri bu sunucuda tutulur. Kim erişebiliyor, ne kadar saklanıyor; KVKK açısından bunu baştan belirle ve çalışanlarına söyle.
- Sunucuyu internete açacaksan güçlü bir şifre ve HTTPS kullan; varsayılan kurulum yalnız kendi bilgisayarın için.

## Dürüst sınır

Arayüz ne kadar iyi olursa olsun cevabın kalitesi arkadaki modele bağlı. Zayıf bir yerel modelle ChatGPT deneyimi beklemeyin.

## Benzerleri

AnythingLLM masaüstü uygulaması olarak kurulumu daha kolay. Belgelerle sohbet ana işinse ona da bak.
