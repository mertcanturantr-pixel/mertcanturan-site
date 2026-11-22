---
name: Paperless-ngx
slug: paperless-ngx
repo: paperless-ngx/paperless-ngx
category: belge
summary: Taradığın kâğıtları metnine kadar aranabilir bir arşive çeviren, etiketleyen ve düzenleyen belge yönetim sistemi. Ofis ve ev evrakı için.
audience: Küçük işletmeler, Avukatlar, Muhasebeciler, Ev evrakıyla boğuşanlar
difficulty: zor
cost: Ücretsiz; kendi bilgisayarında ya da küçük bir sunucuda çalışır
license: GPL-3.0
stars: 47,7 bin
checked: 2026-11-16
tested: false
draft: true
---

Faturalar, sözleşmeler, tapu, kira kontratı, vergi levhası. Hepsi bir klasörde ama lazım olduğunda bulmak yarım saat. Paperless-ngx taradığın her belgenin metnini okuyup aranabilir yapıyor, belgeleri etiketleyip türüne göre ayırıyor. "2024 elektrik faturası" yazınca karşına geliyor.

## Ne işe yarar

Taranmış belgeleri ve PDF'leri alır, metnini okur (OCR), arşive ekler. Etiket, belge türü ve muhatap gibi bilgileri zamanla öğrenip yeni belgelere kendisi önerebiliyor. Topluluk tarafından geliştirilen, uzun süredir yaşayan bir proje.

## Kimin işine yarar

- Kâğıt arşivi dijitale geçirmek isteyen küçük ofisler, avukatlık ve muhasebe büroları.
- Evrakını düzene sokmak isteyen ama belgelerini bir bulut şirketine vermek istemeyen herkes.

## Kurulum

README'ye göre en kolay yol Docker Compose. Depo bir kurulum betiği de veriyor:

`bash -c "$(curl -L https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/install-paperless-ngx.sh)"`

Betik sana birkaç soru sorup kurulumu yapıyor. Docker ve biraz terminal bilgisi gerekiyor; bu yüzden zorluğu "zor" olarak işaretledim.

## Dikkat etmen gerekenler

- Türkçe belgelerde metin okumanın düzgün çalışması için OCR dilini Türkçe olarak ayarlaman gerekiyor; ayarın adı ve nasıl yapılacağı resmî belgelerinde.
- Arşivinde kişisel veri ve ticari sır olacak. Sunucuyu internete açma; açacaksan güçlü şifre, HTTPS ve düzenli yedek şart.
- Yedeği unutma. Arşivin tek kopyası bir diskteyse, o disk bozulduğunda bütün evrak gider.
- Lisans GPL-3.0: kendi işinde kullanmak serbest. Yazılımı değiştirip başkalarına dağıtırsan kaynak kodunu aynı lisansla paylaşman gerekir.

## Dürüst sınır

Kurulumu ve bakımı biraz emek istiyor. Ayda birkaç belge tarıyorsan telefonundaki tarama uygulaması ve düzenli bir klasör yapısı daha mantıklı olabilir.

## Benzerleri

Yalnızca PDF düzenleme ihtiyacın varsa Stirling-PDF daha basit.
