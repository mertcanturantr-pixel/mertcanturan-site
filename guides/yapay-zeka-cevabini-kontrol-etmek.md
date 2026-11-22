---
title: Yapay zekânın cevabı doğru mu? Kullanmadan önce 10 dakikalık kontrol
slug: yapay-zeka-cevabini-kontrol-etmek
seo_title: Yapay zekânın cevabını doğrulamak: 10 dakikalık kontrol
description: Yapay zekânın verdiği kaynağı, rakamı, tarihi ve kanun maddesini kullanmadan önce kontrol et: Google Akademik, DergiPark ve Mevzuat ile adım adım.
summary: ChatGPT'nin verdiği kaynak, rakam, tarih ya da kanun maddesi gerçek mi? Ödevine, raporuna ya da bir karara koymadan önce adım adım kontrol ve yazdırılabilir liste.
keywords: chatgpt kaynak uyduruyor, yapay zekanın verdiği kaynak gerçek mi, yapay zeka cevabı doğru mu nasıl anlaşılır, yapay zeka halüsinasyon nedir, chatgpt yanlış bilgi veriyor, yapay zeka kanun maddesi uyduruyor, google akademik kaynak kontrolü, dergipark makale doğrulama, doi numarası sorgulama, yapay zeka cevabi kontrol
type: kontrol-listesi
audience: Herkes
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm.
change: 2026-11-16 Baştan yazıldı: kaynak, rakam, güncellik ve hukuki iddia kontrolleri ayrıntılandırıldı.
change: 2026-11-16 Adres değişti; Deloitte tutarı ve Mata v. Avianca kaynakları düzeltildi, sonraki adım eklendi; 2026-11-16 dört rollü denetim: Kısaca, sık hatalar ve dürüst sınır eklendi, başlıklar soru biçimine çevrildi, iç bağlantılar artırıldı.
video:
video_title:
draft: true
---

Yapay zekâ yanlış bir bilgiyi doğru bir bilgiyle aynı tonda yazıyor. Cümlenin akıcı olması, düzgün Türkçesi, hatta altına konmuş bir kaynak bile doğru olduğunu göstermiyor. Avustralya'da bir bakanlık için Deloitte'un hazırladığı, yaklaşık 440 bin Avustralya doları bedelli bir raporda hiç yazılmamış kitaplar kaynak gösterildi; ayrıntısı [hata dosyasında](rehber:yapay-zeka-hatalari#deloitte).

Her cevabı baştan sona doğrulamak zorunda değilsin. Ama bir cevabı bir yere koyacaksan, birine göndereceksen ya da ona göre karar vereceksen aşağıdaki kontroller çoğu cevapta on dakikayı geçmez. Ödev için ilk üç bölüm yeter; para, sağlık ya da hukukla ilgili bir kararda hepsini yap.

Kısaca: Yapay zekânın cevabındaki rakam, tarih, alıntı, kaynak ve kanun maddesi içeren cümleleri işaretle; her birini o bilgiyi ilk yayımlayan yerde aç. Kaynağı Google Akademik, DergiPark ya da DOI ile bul; kanun maddesini Mevzuat Bilgi Sistemi'nde oku. Bulamadığın kaynağı ve göremediğin kararı kullanma, neyi nereden doğruladığını iki satırla not et.

## Önce hangi cümleleri kontrol etmelisin? {#riskli-cumleler}

Bütün metni kontrol etmeye çalışma, yorulursun. Önce yapay zekânın en sık yanıldığı cümleleri işaretle:

- Rakam içerenler: tutar, oran, yüzde, nüfus, tarih, süre.
- "İlk", "en", "tek", "rekor" diyenler.
- Bir kişiye, kuruma ya da yayına bir söz ya da bulgu atfedenler: "X'e göre", "Y'nin araştırmasına göre".
- Kanun maddesi, karar numarası, yönetmelik adı geçenler.
- Güncel olması gereken her şey: fiyat, faiz, kur, bir uygulamanın menüsü, bir kuralın bugünkü hâli.

Metindeki cümlelerin çoğu bu gruplara girmiyorsa işin kolay: Kontrol edeceğin yer birkaç cümleden ibaret.

## Kaynak gerçekten var mı? 20 saniyelik kontrol {#kaynak-gercekten-var-mi-20-saniyelik-kontrol}

Yapay zekâ bazen gerçek gibi görünen yazar adları, dergi adları ve yıllarla hiç var olmamış makaleler gösteriyor. Bir kaynağı kullanmadan önce:

1. Kaynağın tam başlığını tırnak işaretleri arasında [Google Akademik](https://scholar.google.com/)'te ara. Türkçe bir yayınsa [DergiPark](https://dergipark.org.tr/)'ta da ara.
2. Bir DOI numarası verilmişse [doi.org](https://www.doi.org/) adresinde aç. Numara gerçekten o makaleye mi gidiyor, yoksa bambaşka bir yayına ya da hiçbir yere mi?
3. Yazarın üniversite sayfasına ya da Google Akademik profiline bak. Böyle bir çalışması var mı?

Birinde bile takılıyorsan o kaynağı yok say. Yapay zekâya "bu kaynak bulunamadı, gerçeğini göster" dersen bir yenisini uydurabilir. Doğru kaynağı kendin bul.

> SAHA: Bir yapay zekâdan dar bir konuda üç akademik kaynak iste ve bu üç adımla kontrol et. Kaçı gerçek çıktı? Aracı, tarihi ve sonucu buraya ekle. Hepsi doğru çıktıysa onu da yaz.

## Kaynak var ama gerçekten o söylüyor mu? {#kaynak-ne-diyor}

Daha sinsi bir hata türü bu: Kaynak gerçek, ama yapay zekânın ona atfettiği cümle orada yok ya da bambaşka bir bağlamda geçiyor.

Kaynağı aç ve iddianın geçtiği yeri bul. Uzun bir belgeyse tarayıcıda Ctrl+F (Mac'te Cmd+F) ile anahtar kelimeyi ara. Rakam aynı mı, cümle aynı anlama mı geliyor? "Yüzde 40'a kadar" ile "yüzde 40" aynı şey değil.

## Rakam ve tarihler nasıl kontrol edilir? {#rakamlar}

Cümlenin tamamı doğruyken içindeki rakam yanlış olabilir. Bunu yakalamak zor, çünkü "yüzde 37" de "yüzde 43" de kulağa aynı derecede makul geliyor.

Rakamı en yakın birincil kaynaktan kontrol et: istatistikse TÜİK, ekonomiyse Merkez Bankası, bir şirketin verisiyse şirketin kendi açıklaması. Haber sitesindeki rakam bile çoğu zaman bir başkasından aktarılmış oluyor.

## Bilgi bugün hâlâ geçerli mi? {#guncellik}

Her modelin bilgisi belli bir tarihte kesilir. Sonrasını bilmez ve bilmediğini her zaman söylemez. İnternette arama yapan araçlar da, Google'ın arama sonuçlarının üstündeki yapay zekâ özetleri de bazen eski bir sayfayı bulup getiriyor; ikincisine nasıl bakacağın [Google Yapay Zekâ Modu rehberinde](rehber:google-yapay-zeka-modu#guvenme).

Fiyat, faiz, vergi oranı, bir uygulamanın ayar menüsü, bir kurumun başvuru şartı gibi değişen bilgileri, onları yayımlayan kurumun sitesinden kontrol et. Bir bilginin tarihini yapay zekâya sormak yerine kaynağın üzerindeki tarihe bak.

## Kanun maddesi ve içtihat doğru mu? {#hukuk}

Yapay zekâ kanun maddesi ve mahkeme kararı uydurmakta da çok rahat. 2023'te New York'taki federal mahkemede (Mata v. Avianca davası), ChatGPT'nin uydurduğu kararları dosyaya koyan iki avukat ve büroları birlikte 5.000 dolar para cezasına çarptırıldı; mahkeme ayrıca uydurma kararların atfedildiği her hâkime ve müvekkillerine kararı ekleyerek mektup göndermelerini istedi. Bu yüzden:

- Kanun ve yönetmelik maddelerini [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/)'nde aç ve oku. Madde numarası doğru mu, maddenin bugünkü metni aynı mı? Kanunlar değişiyor ve eski metin internette dolaşmaya devam ediyor.
- Bir yargı kararından söz ediliyorsa, kararın kendisini bulamıyorsan o karara dayanma.
- Yapay zekânın yorumu bir hukuki görüş değil. Somut bir uyuşmazlıkta, özellikle bir süre işliyorsa (itiraz, dava açma süresi gibi), bir avukata danış.

> SAHA: Bir yapay zekâya Türk hukukuyla ilgili bir soru sor ve verdiği kanun maddelerini kontrol et. Yanlış ya da güncel olmayan bir madde çıktı mı? Örneği kısaca ekle.

## Hangi bilgiyi nereden kontrol edersin? {#nereden}

Türkiye'de çoğu bilginin bir resmî kaynağı var. Yapay zekânın verdiği bilgiyi orada aç:

| Bilgi | Nereden kontrol edersin |
| --- | --- |
| Makale, kitap, tez | [Google Akademik](https://scholar.google.com), [DergiPark](https://dergipark.org.tr), DOI numarası varsa [doi.org](https://www.doi.org) |
| Kanun, yönetmelik, tebliğ | [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr), [Resmî Gazete](https://www.resmigazete.gov.tr) |
| Yargıtay kararı | [Yargıtay karar arama](https://karararama.yargitay.gov.tr) |
| Anayasa Mahkemesi kararı | [AYM kararlar bilgi bankası](https://kararlarbilgibankasi.anayasa.gov.tr) |
| Nüfus, işsizlik, enflasyon | [TÜİK](https://www.tuik.gov.tr) |
| Faiz, kur | [Merkez Bankası](https://www.tcmb.gov.tr) |
| Borsadaki bir şirketin açıklaması | [KAP](https://www.kap.org.tr) |
| Bir aracın fiyatı ya da ayarı | Şirketin kendi fiyat ve yardım sayfası; blog yazısı ya da video değil |

Kaynağı bu tabloda yoksa kendine şunu sor: Bu bilgiyi ilk kim yayımlar? Oraya git.

## Aynı soruyu başka bir yapay zekâya sormak işe yarar mı? {#ikinci-arac}

Hızlı bir ikinci görüş için soruyu başka bir yapay zekâya sor. Cevaplar birbirini tutmuyorsa en az biri yanlış demektir ve nereye bakman gerektiğini öğrenmiş olursun. Tutuyorsa bu da kesin doğru demek değil; aynı yanlış kaynaktan beslenmiş olabilirler. Bu yöntem kontrolün yerine geçmiyor ama neyi kontrol edeceğini gösteriyor.

## Neyi kontrol ettiğini neden not almalısın? {#not-al}

Cevabı kullandıktan sonra hangi bilgiyi hangi kaynaktan doğruladığını iki satırla yaz. Ödevse kaynakçana, iş belgesiyse bir nota. Sonradan "bunu nereden buldun?" diye sorulduğunda elinde dayanak olur. Bir avukat olarak söyleyeyim: "Kontrol ettim" demek yetmez, neyi nereden kontrol ettiğini gösterebilmen gerekir. İki satırlık not bunun için yeter.

## Göndermeden önce hızlı liste {#hizli-liste}

Aceleyle bir şey göndereceksen en azından şunları yap:

- [ ] Rakam, tarih ve "ilk/en" içeren cümleleri işaretledim.
- [ ] Gösterilen kaynakları açtım; var ve aynı şeyi söylüyor.
- [ ] Değişebilecek bilgileri resmî kaynaktan bugün kontrol ettim.
- [ ] Kanun maddesi varsa Mevzuat Bilgi Sistemi'nde okudum.
- [ ] Neyi nereden doğruladığımı not ettim.

## Sık yapılan hatalar {#hatalar}

- **Kaynağı yapay zekâya doğrulatmak.** "Bu kaynak gerçek mi?" sorusuna "evet" cevabı almak kontrol değil; kaynağı kendin aç.
- **Haber sitesindeki rakamla yetinmek.** Rakamı ilk yayımlayan kuruma git; haber çoğu zaman aktarım.
- **İnternette arama yapan aracın cevabına körü körüne güvenmek.** Gösterdiği bağlantıyı aç; bağlantı başka bir şey söylüyor olabilir.
- **Kanun maddesini eski bir blog yazısından kontrol etmek.** Maddenin bugünkü metni Mevzuat Bilgi Sistemi'nde.
- **Uydurma kaynağı tezde ya da ödevde fark etmemek.** Akademik çalışmada neye dikkat edeceğin [tez rehberinde](rehber:tezde-yapay-zeka-kullanimi#uydurma-kaynak).

## Dürüst sınır {#sinir}

Bu kontroller bir bilginin var olup olmadığını ve kaynağın aynı şeyi söyleyip söylemediğini yakalar; bir yorumun ya da değerlendirmenin doğru olup olmadığını her zaman yakalamaz. İki kaynak birbiriyle çelişiyorsa ya da konu senin uzmanlık alanının dışındaysa son sözü o alanın uzmanına bırak. Hukuki bir süre ya da sağlık kararı söz konusuysa kontrol listesi bir avukatın ya da hekimin yerini tutmaz.

## Sonraki adım {#sonraki-adim}

Bu sayfayı yer imlerine ekle ya da hızlı listeyi yazdır. Kontrolü kolaylaştırmanın en iyi yolu, cevabı baştan kaynaklı istemek; nasıl yapılacağı [yapay zekâya iyi komut yazmak](rehber:yapay-zekaya-iyi-komut-yazmak) rehberinde. Uzun bir belgeyi okuturken aynı kontrolü sayfa numarasıyla yapmak için [uzun PDF rehberine](rehber:uzun-pdf-okumak#kontrol), yapay zekâya fazla güvenilen gerçek olaylar için [hata dosyasına](rehber:yapay-zeka-hatalari) bak.

## Kaynaklar

- [Google Akademik](https://scholar.google.com/) · [DergiPark](https://dergipark.org.tr/) · [doi.org](https://www.doi.org/)
- [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/)
- Mata v. Avianca, Inc., No. 22-cv-1461 (PKC), S.D.N.Y., 22 Haziran 2023 tarihli yaptırım kararı: [Justia](https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54) · [ABA Journal, 26 Haziran 2023](https://abajournal.com/web/article/lawyers-who-doubled-down-and-defended-chatgpts-fake-cases-must-pay-5k-judge-says)
- Deloitte raporu: [BNN Bloomberg, 7 Ekim 2025](https://www.bnnbloomberg.ca/business/artificial-intelligence/2025/10/07/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/)
