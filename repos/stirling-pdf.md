---
name: Stirling-PDF
slug: stirling-pdf
repo: Stirling-Tools/Stirling-PDF
category: belge
summary: PDF birleştirme, bölme, sıkıştırma, imzalama, karartma ve metin okuma gibi 50'yi aşkın işi kendi bilgisayarında yapan araç. Belgen bir siteye yüklenmez.
audience: Herkes, Ofisler, Avukatlar, Muhasebeciler
difficulty: orta
cost: Ücretsiz sürümü var; kurumsal özellikler ücretli
license: MIT
license_note: Çekirdek kod MIT lisanslı. Lisans dosyasına göre bazı klasörler (ticari ve kurumsal bölümler) ayrı lisanslara tabi; depo kendini "open-core" olarak tanımlıyor.
stars: 95,4 bin
checked: 2026-11-16
tested: false
draft: true
---

Bir sözleşmeyi sıkıştırmak ya da iki PDF'i birleştirmek için çoğumuz internette bulduğumuz ilk siteye dosyayı yüklüyoruz. O dosyanın içinde müşteri adı, kimlik numarası, banka bilgisi olabilir ve o site dosyayla ne yapıyor bilmiyoruz. Stirling-PDF aynı işleri kendi bilgisayarında ya da kendi sunucunda yapıyor.

## Ne işe yarar

README'ye göre 50'yi aşkın PDF aracı var: birleştirme, bölme, sıkıştırma, imzalama, karartma (gizli bilgiyi silme), dönüştürme ve metin okuma. Tarayıcıdan açılan bir arayüzü, masaüstü sürümü ve toplu iş için bir API'si var. Arayüz 40'tan fazla dilde.

## Kimin işine yarar

- PDF ile her gün çalışan ofisler, avukatlık ve muhasebe büroları.
- Belgelerini rastgele sitelere yüklemek istemeyen herkes.

## Kurulum

README'deki hızlı başlangıç Docker ile:

`docker run -p 8080:8080 docker.stirlingpdf.com/stirlingtools/stirling-pdf`

Ardından tarayıcıda `http://localhost:8080` adresini aç. Masaüstü sürümü ve diğer kurulum yolları için README resmî belgelerine yönlendiriyor.

## Dikkat etmen gerekenler

- Karartma yaparken metnin gerçekten silindiğini kontrol et. PDF'te üstüne siyah kutu koymak bilgiyi silmez; kutunun altındaki metin kopyalanabilir. Karartılmış belgeyi göndermeden önce metni seçip kopyalamayı dene.
- Lisans: Çekirdek MIT, ama bazı bölümler ticari lisanslı. Ücretsiz sürümle neyin geldiğini kurmadan önce kontrol et.

## Dürüst sınır

Yılda birkaç PDF birleştiriyorsan Docker kurmaya değmez; macOS'taki Önizleme ya da Windows'taki "PDF olarak yazdır" çoğu basit işi görür.

## Benzerleri

Taranmış evrak arşivi kuracaksan Paperless-ngx.
