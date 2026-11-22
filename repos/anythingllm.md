---
name: AnythingLLM
slug: anythingllm
repo: Mintplex-Labs/anything-llm
category: yerel
summary: Kendi belgelerini yükleyip onlarla sohbet ettiğin, varsayılan olarak bilgisayarında çalışan masaüstü uygulaması. Kurulumu indir, aç kadar kolay.
audience: Herkes, Avukatlar, Muhasebeciler, Öğrenciler
difficulty: kolay
cost: Ücretsiz; yerel model ya da kendi API anahtarınla çalışır
license: MIT
stars: 67,5 bin
checked: 2026-11-16
tested: false
draft: true
---

Yüz sayfalık bir şartname, bir yönetmelik, bir ders notu yığını. "Şu konuda ne diyordu?" sorusunun cevabı bir yerde var ama bulmak saatler alıyor. AnythingLLM bu belgeleri bir çalışma alanına yükleyip onlarla sohbet etmeni sağlıyor; README'ye göre varsayılan olarak her şey bilgisayarında kalıyor.

## Ne işe yarar

Belgeleri (PDF, Word, metin, web sayfası) bir "çalışma alanına" eklersin, uygulama onları parçalara ayırıp aranabilir hâle getirir. Sonra soru sorarsın, cevap belgelerinden gelir. Yerel bir modelle (örneğin Ollama) ya da OpenAI, Anthropic gibi bir servisin API anahtarıyla çalışabilir. Ajan özellikleri ve çok kullanıcılı kullanım da var.

## Kimin işine yarar

- Kendi belge arşivinde hızlı arama ve özet isteyen avukatlar, muhasebeciler, danışmanlar.
- Ders notlarıyla çalışan öğrenciler.
- Terminal kullanmadan yerel yapay zekâ denemek isteyenler.

## Kurulum

README'deki en kolay yol masaüstü uygulaması: anythingllm.com/download adresinden Mac, Windows ya da Linux sürümünü indirip kur. Sunucuya kurmak istersen depodaki Docker rehberini (docker/HOW_TO_USE_DOCKER.md) izle.

İlk açılışta hangi modeli kullanacağını sorar. Belgelerin bilgisayarından çıkmasın istiyorsan yerel bir model seç.

## Dikkat etmen gerekenler

- Bulut bir model (OpenAI, Anthropic vb.) seçersen belgelerinin ilgili parçaları o şirkete gider. "Yerel çalışıyor" ifadesi yalnızca yerel model seçtiğinde tam doğru.
- Cevap verirken hangi belge parçasına dayandığını gösteriyor; önemli bir karar vermeden önce o parçayı açıp kendin oku.
- Taranmış (resim) PDF'lerde metin okunamazsa cevap da eksik olur. Önce metin içeren PDF'e çevir.

## Dürüst sınır

Belgeyle sohbet, belgeyi okumanın yerini tutmaz. Arama ve ilk özet için çok iyi; ama soru belgelerde olmayan bir şeyse model yine de cevap uydurabilir.

## Benzerleri

Google'ın NotebookLM'i benzer işi bulutta, kurulum gerektirmeden yapıyor; belgelerin Google'a gider. Arayüzün yalnızca sohbet olmasını istiyorsan Open WebUI.
