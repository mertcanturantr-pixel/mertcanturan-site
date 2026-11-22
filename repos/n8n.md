---
name: n8n
slug: n8n
repo: n8n-io/n8n
category: otomasyon
summary: Uygulamalarını birbirine bağlayıp tekrarlayan işleri otomatikleştiren, yapay zekâ adımları da eklenebilen görsel otomasyon aracı. Zapier'in kendine kurulan rakibi.
audience: Küçük işletmeler, Serbest çalışanlar, Yazılımcılar
difficulty: orta
cost: Kendi bilgisayarına ya da sunucuna kurarsan ücretsiz; bulut sürümü ücretli
license: Sustainable-Use-License
license_note: Açık kaynak değil, "fair-code" olarak dağıtılıyor (Sustainable Use License ve n8n Enterprise License). Kendi işinde kullanmak serbest; n8n'in kendisini başkalarına ücretli hizmet olarak sunmak lisansla sınırlı. Ayrıntısı deponun lisans dosyasında.
stars: 208,2 bin
checked: 2026-11-16
tested: false
draft: true
---

Her sabah gelen siparişleri tabloya kopyalıyor, müşteriye onay e-postası atıyor, sonra kargo firmasının sitesine giriyorsun. n8n bu adımları kutucuklarla birbirine bağlayıp senin yerine yapıyor. Arada bir yapay zekâ adımı da koyabiliyorsun: gelen e-postayı özetlet, sınıflandır, taslak cevap yaz.

## Ne işe yarar

Görsel bir otomasyon aracı. "Şu olunca şunu yap" zincirlerini sürükle bırakla kuruyorsun. Depo sayfasına göre 400'ü aşkın uygulamaya hazır bağlantısı var ve yapay zekâ adımları yerleşik geliyor.

## Kimin işine yarar

- Her gün aynı kopyala yapıştır işini yapan küçük işletmeler ve serbest çalışanlar.
- Müşterilerine otomasyon kurarak iş yapmak isteyenler (bu durumda lisans bölümünü mutlaka oku).

## Kurulum

README'deki resmî yollar:

- Kurulum betiği: `curl -fsSL https://get.n8n.io | sh`
- Docker ile: önce `docker volume create n8n_data`, sonra `docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n`

Ardından tarayıcıda `http://localhost:5678` adresini aç.

## Dikkat etmen gerekenler

- Lisans: n8n açık kaynak değil. Kendi işlerini otomatikleştirmek için kullanabilirsin; ama n8n'i kurup müşterine "otomasyon platformu" diye satmak ya da barındırıp kiralamak lisansın sınırına giriyor. Müşterine bir iş akışı kurup teslim etmekle n8n'in kendisini hizmet olarak satmak aynı şey değil; ticari bir model kuracaksan lisans metnini oku.
- Otomasyonlar e-posta, müşteri listesi gibi kişisel verilere erişir. Hangi akışın neye eriştiğini not et, gereksiz yetki verme.
- Bilgisayarın kapanınca otomasyonlar da durur. Sürekli çalışması gereken işler için küçük bir sunucu gerekir.

## Dürüst sınır

Basit iki adımlı işler için fazla güçlü ve öğrenmesi zaman alır. İlk hafta "bunu elle yapsam daha hızlıydı" diyeceksin; kazanç, aynı iş haftada onlarca kez tekrar ediyorsa geliyor.

## Benzerleri

Flowise ve Dify yapay zekâ akışlarına daha çok odaklanıyor. Kurulum istemeyen ücretli seçenekler Zapier ve Make.
