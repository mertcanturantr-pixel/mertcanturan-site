---
title: Yapay zekâyla uygulama yaparken: başlamadan, çalışırken ve yayına almadan önce
seo_title: Yapay zekâyla yaptığın uygulama güvenli mi? Yayın öncesi kontrol
description: Lovable, Replit ya da Claude Code ile uygulama yapıyorsan: veri tabanı, anahtar ve kullanıcı verisi için kontroller, iki gerçek olay ve komut şablonu.
slug: yapay-zekayla-uygulama
summary: Yapay zekâ araçlarıyla uygulama ya da otomasyon yaparken veri tabanını, anahtarları ve kullanıcı verisini korumak için adım adım kontroller, iki gerçek olay ve komut şablonu.
keywords: yapay zeka ile uygulama yapmak, vibe coding nedir, lovable güvenli mi, replit veri tabanı silindi, supabase rls nasıl açılır, api anahtarı sızdı ne yapmalı, yapay zeka ile yapılan uygulama kvkk, slopsquatting
type: adim-adim
topic: uretim
audience: Herkes, Yazılımcılar
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm.
change: 2026-11-16 Yeni yazı standardına göre yeniden yazılmak üzere iskelete alındı.
change: 2026-11-16 Tam rehbere çevrildi: Lovable ve paket uydurma olayları, araç seçimi, sık hatalar, dürüst sınır; 2026-11-16 dört rollü denetim: KVKK yurt dışı aktarım ve aydınlatma maddeleri, ilgili rehberlere bağlantılar ve soru başlıkları eklendi.
change: 2026-11-27 Arama başlığı güvenlik niyetine göre değişti; kişisel uygulama isteyenler için Claude ile uygulama yapmak rehberine yönlendirme eklendi.
video:
video_title:
draft: false
---

Yapay zekâ araçlarıyla, yazılım bilmeden bile çalışan bir uygulama yapmak artık mümkün. Lovable, Bolt ya da Replit gibi araçlara ne istediğini yazıyorsun, birkaç dakikada giriş ekranı, veri tabanı ve sayfaları olan bir uygulama çıkıyor. Ama "çalışıyor" ile "güvenle kullanılabilir" arasında büyük bir fark var ve bu fark, uygulamaya ilk gerçek kullanıcı girdiğinde ortaya çıkıyor.

Yalnızca kendin kullanacağın bir spor, bütçe ya da ders uygulaması istiyorsan bu rehber fazla gelir; [Claude ile uygulama yapmak rehberindeki](rehber:claude-ile-uygulama-yapmak) hazır komutlarla başla.

Kısaca: Yapay zekâyla yaptığın bir uygulamayı güvenle yayına almak için denemeyi gerçek veriden ayır, her adımı geri alınabilir yap, yapay zekânın silme ve canlıya gönderme yetkisini kendi onayına bağla. Yayından önce bir hesapla başka bir hesabın verisine ulaşılıp ulaşılamadığını kendin dene ve veri tabanı kurallarını kontrol et. Kişisel veri topluyorsan KVKK'ya göre aydınlatma metni hazırla. Aşağıda bunları üç aşamada, iki gerçek olayla anlattım.

## Yapay zekâyla yapılan uygulamalarda ne yanlış gitti? İki gerçek olay {#olaylar}

**Silinen veri tabanı (Replit, Temmuz 2025).** Bir yapay zekâ kodlama ajanı, kendisine "izinsiz değişiklik yok" denmesine rağmen bir şirketin canlı veri tabanını sildi. Ayrıntısı [hata dosyasında](rehber:yapay-zeka-hatalari#replit). Ders: Ajanın yapabildiği her şeyi bir gün yapacağını varsay; silme yetkisini baştan verme.

**Herkese açık kalan veri tabanları (Lovable, 2025).** Bir güvenlik araştırmacısı, Lovable'ın vitrinindeki uygulamaları taradı ve 170 projede, 303 ayrı uç noktada veri tabanı tablolarının, uygulamanın sayfasında zaten görünen genel anahtarla dışarıdan okunabildiğini buldu. Açık kalan verilerin arasında e-posta adresleri, borç tutarları ve API anahtarları vardı. Sorun, veri tabanındaki satır düzeyinde güvenlik (Row Level Security) kurallarının eksik olmasıydı ve CVE-2025-48757 numarasıyla kayda geçti. Ders: Uygulamanın giriş ekranı olması, verinin korunduğunu göstermez; koruma veri tabanında ve sunucuda olmalı.

Bu iki olayın ortak noktası, uygulamaların çalışıyor olması. Sorun, kimse kontrol etmeden gerçek veriyle yayına alınmalarıydı.

## Hangi araçla başlamalı? {#arac}

İki tür araç var ve risk profilleri farklı:

- **Tarayıcıda uygulama kuran araçlar** (Lovable, Bolt, Replit gibi): Hızlı başlarsın, sunucuyu ve veri tabanını araç kurar. Kodu görmeden ilerleyebilirsin; risk de tam burada. Neyin nerede açık kaldığını bilmeden yayına alabilirsin.
- **Kendi bilgisayarında kod yazan araçlar** (Claude Code, Cursor, Codex gibi): Kodu ve dosyaları görürsün, her değişikliği onaylayabilirsin. Daha fazla bilgi ister ama kontrol sende kalır.

Yazılım bilmiyorsan ilk türle başlamak mantıklı. Ama kullanıcıdan kişisel veri ya da para alan bir uygulamayı, kodu okuyabilen birine kontrol ettirmeden yayına alma.

## Başlamadan önce ne yapmalısın? {#baslamadan}

- [ ] **Ne yapacağını bir paragrafta yaz.** Uygulama kimin, hangi işini çözecek? Hangi veriyi tutacak? Bu paragraf, yapay zekâya vereceğin ilk komutun da temeli olur.
- [ ] **Geliştirme ve canlı ortamı ayır.** Denemeleri gerçek kullanıcı verisinin olduğu veri tabanında yapma. Ayrı bir geliştirme veri tabanı kullan.
- [ ] **Sürüm kontrolü kur.** Kodu Git gibi bir sürüm kontrol sistemiyle tut. Yapay zekânın her değişikliği böylece geri alınabilir olur. Tarayıcı araçlarının çoğunda GitHub'a bağlama seçeneği var; aç.
- [ ] **Gizli anahtarları ayır.** API anahtarlarını ve şifreleri koda ya da sohbete yazma; ortam değişkenlerinde tut. Yanlışlıkla yapıştırdıysan anahtarı hemen iptal et ve yenisini al; ayrıntısı [kodlama araçları rehberinde](rehber:kodlama-araclari#gizli).

## Yapay zekâyla kod yazdırırken nelere dikkat? {#calisirken}

- [ ] **Küçük adımlarla iste.** Bir seferde tek bir özellik iste. Her adımdan sonra çalıştır ve dene. Beş özelliği tek komutta isteyip beşini birden kontrol etmek, hiçbirini kontrol etmemek demek.
- [ ] **Yetkiyi sınırla.** Kod yazıp kendisi çalıştıran bir ajan kullanıyorsan, silme, veri tabanı şemasını değiştirme ve canlıya gönderme gibi komutları senin onayına bağla. Ajan onay ayarlarının mantığı [yapay zekâ ajanları rehberinde](rehber:yapay-zeka-ajanlari#onay).
- [ ] **Hassas kodu oku.** Özellikle giriş, yetki, ödeme ve silme işlemlerini yapan kodu satır satır oku. Anlamadığın yeri yapay zekâya açıklat; açıklamayı da başka bir sohbette kontrol ettir.
- [ ] **Önerilen paketleri kontrol et.** Yapay zekâ var olmayan paket adları da önerebiliyor. 2025'te yayımlanan bir çalışma, 16 dil modelinin ürettiği 576 bin kod örneğinde önerilen paketlerin yaklaşık beşte birinin gerçekte var olmadığını buldu. Saldırganlar bu uydurma adlarla zararlı paketler yayımlayabiliyor; buna "slopsquatting" deniyor. Bir paketi kurmadan önce paket deposunda (npm, PyPI) gerçekten var olduğunu, kimin yayımladığını ve ne kadar kullanıldığını kontrol et.

## Yayına almadan önce güvenlik kontrolü {#yayindan-once}

- [ ] **Başka birinin verisine erişilebiliyor mu, dene.** İki ayrı hesap aç. Birinin verisine ötekinin hesabıyla ulaşmaya çalış: adres çubuğundaki numarayı değiştir, başka kullanıcının kaydını açmayı dene. Bir düğmeyi gizlemek yetkilendirme değildir; kontrol sunucuda ve veri tabanında yapılmalı.
- [ ] **Veri tabanı kurallarını kontrol et.** Supabase gibi bir veri tabanı kullanıyorsan her tabloda satır düzeyinde güvenliğin açık olduğunu ve kuralların "herkes okuyabilir" olmadığını kontrol et. Tarayıcı araçlarının çoğunda güvenlik taraması var; çalıştır.
- [ ] **Yedeği geri yüklemeyi dene.** Yedek almak yetmez. Yedeği gerçekten geri yükleyebildiğini bir kez dene.
- [ ] **Hata mesajlarına bak.** Kullanıcıya gösterilen hatalarda şifre, anahtar ya da başka kullanıcıların bilgisi görünmemeli.
- [ ] **Kişisel veri topluyorsan KVKK'yı unutma.** 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) m.10'a göre kullanıcıya hangi veriyi neden topladığını anlatan bir aydınlatma metni gerekir. Veriyi ne kadar saklayacağına ve nasıl sileceğine karar ver.
- [ ] **Yapay zekâ servisine kullanıcı verisi gidiyorsa söyle.** Uygulaman kullanıcı verisini bir yapay zekâ servisine gönderiyorsa bunu aydınlatma metninde yaz. Servis yurt dışındaysa bu, KVKK m.9'daki yurt dışına aktarım kurallarını (2024 değişikliğiyle standart sözleşme ve bildirim yükümlülüğü dahil) gündeme getirir. Kullanıcıdan sağlık verisi ya da para alan bir uygulamada bu kısmı bir avukatla netleştir.

## Yapay zekâya özellik ekletirken komut şablonu {#sablon}

```sablon
Uygulamama şu özelliği ekle: [ÖZELLİK]
Kullandığım teknoloji: [TEKNOLOJİ]

Kurallar:
- Önce yapacağın değişikliğin planını yaz ve onayımı bekle.
- Mevcut kodu, ilgisiz dosyaları ve verileri değiştirme.
- Veri silmen, veri tabanı yapısını değiştirmen ya da bir şeyi canlıya göndermen gerekiyorsa önce sor.
- Şifre ve anahtarları koda yazma; ortam değişkeni kullan.
- Yeni bir paket kullanacaksan adını, neden gerektiğini ve paket deposundaki bağlantısını yaz.
- Kullanıcı verisine erişen her yerde, bir kullanıcının başka kullanıcının verisini göremeyeceğini sunucu tarafında kontrol et.
- Değişikliği nasıl test edeceğimi adım adım yaz.
```

Yayından önce aynı uygulamayı başka bir sohbette şu soruyla kontrol ettir: "Bu kodda bir kullanıcının başka bir kullanıcının verisine erişebileceği, kimlik doğrulamadan geçilebilecek ya da gizli anahtarın tarayıcıya sızdığı bir yer var mı? Dosya ve satır göstererek listele." Cevabı körü körüne kabul etme; ama gösterdiği yerleri tek tek kontrol et.

## Sık yapılan hatalar {#hatalar}

- **Demo verisiyle test edip gerçek veriyle yayına almak.** Uygulama test verisiyle çalışıyor diye gerçek kullanıcı verisini koruduğu anlamına gelmez.
- **"Giriş ekranı var, güvenli" sanmak.** Lovable olayındaki uygulamaların çoğunun giriş ekranı vardı; veri tabanı ise dışarıya açıktı.
- **Yapay zekâya canlı ortamda ajan yetkisi vermek.** Replit olayı tam olarak buydu.
- **Hatayı yapay zekâya tekrar tekrar düzelttirmek.** Aynı hatayı üç kez düzeltemeyen bir araç, dördüncüde başka bir şeyi bozar. Durup sorunun ne olduğunu anla ya da bir önceki çalışan sürüme dön.
- **Ödeme ve kimlik doğrulamayı kendin yazdırmak.** Bu işler için hazır, denetlenmiş servisleri kullan; sıfırdan yazdırılmış ödeme kodu en riskli koddur.

## Bu kontroller uygulamayı güvenli yapar mı? {#sinir}

Bu liste, en sık ve en pahalı hataları yakalar; uygulamanın güvenli olduğunu kanıtlamaz. Kendin ve arkadaşların için yaptığın küçük bir araç için bu kontroller yeter. Ama başkalarının kişisel verisini, sağlık bilgisini ya da parasını işleyen bir uygulamayı yayına alacaksan, kodu okuyabilen ve güvenlik bilen birine kontrol ettir. Yapay zekâ uygulamayı yazmayı hızlandırır; uygulamanın sorumluluğu yine sende.

## Sonraki adım {#sonraki-adim}

Elinde yapay zekâyla yaptığın bir uygulama varsa bugün "Yayına almadan önce" bölümündeki ilk maddeyi dene: iki hesap aç ve birinin verisine diğerinden ulaşmaya çalış. Uygulamada kullanıcı verisini yapay zekâ servislerine gönderiyorsan [ne yazılmaz rehberindeki](rehber:yapay-zekaya-ne-yazilmaz#is-yerinde) iş yeri kurallarına da bak.

## Kaynaklar

- Replit olayı: [The Register, 21 Temmuz 2025](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/)
- Lovable ve eksik satır düzeyinde güvenlik, CVE-2025-48757: [Superblocks incelemesi](https://www.superblocks.com/blog/lovable-vulnerabilities)
- Uydurma paket adları ve slopsquatting, Spracklen ve diğerleri, USENIX Security 2025: [The Decoder özeti](https://the-decoder.com/slopsquatting-one-in-five-ai-code-snippets-contains-fake-libraries/) · [TechRepublic, 16 Nisan 2025](https://www.techrepublic.com/article/news-slopsquatting-vibe-coding-ai-cybersecurity-risk/)
- Supabase, Row Level Security belgesi: [supabase.com](https://supabase.com/docs/guides/database/postgres/row-level-security)
- 6698 sayılı Kişisel Verilerin Korunması Kanunu, m.9 (yurt dışına aktarım) ve m.10 (aydınlatma yükümlülüğü): [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/)
- Kişisel Verileri Koruma Kurumu, "Üretken Yapay Zekâ ve Kişisel Verilerin Korunması Rehberi (15 Soruda)", 24 Kasım 2025: [kvkk.gov.tr](https://www.kvkk.gov.tr/Icerik/8547/uretken-yapay-zeka-ve-kisisel-verilerin-korunmasi-rehberi-15-soruda)
