---
title: ChatGPT, Claude ve Gemini sohbetlerinle eğitilmesin: 3 ayarı kapat, şu bilgileri hiç yazma
slug: yapay-zekaya-ne-yazilmaz
seo_title: ChatGPT, Claude ve Gemini'de eğitim ayarını kapat (2026)
description: Üç araçta sohbetlerinin modeli eğitmesini iki dakikada kapat. Ayarın neyi korumadığı ve ayar ne olursa olsun yazmaman gereken bilgiler.
summary: Üç araçta da sohbetlerinin eğitimde kullanılması açık geliyor. İki dakikada kapat; ama kimlik numarası, şifre ve müşteri bilgisini ayar ne olursa olsun yazma.
type: adim-adim
audience: Herkes, İş yerleri
keywords: chatgpt eğitim ayarı kapatma, chatgpt verilerim eğitimde kullanılıyor mu, improve the model for everyone, claude gizlilik ayarı, gemini keep activity kapatma, yapay zekaya ne yazılmaz, chatgpt güvenli mi, chatgpt kişisel veri kvkk, yapay zekaya şirket bilgisi yazmak
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 Baştan yazıldı: ayar adımları, ayarın sınırları ve iş yerleri için bölüm eklendi.
change: 2026-11-16 Ayar yolları ve saklama süreleri şirketlerin kendi yardım sayfalarından yeniden kontrol edildi; Claude'un tarihleri düzeltildi, hızlı kontrol listesi eklendi; 2026-11-16 dört rollü denetim: Kısaca, sık yapılan hatalar ve dürüst sınır bölümleri, kamuya açık Samsung örneği, 72 saatlik ihlal bildirimi, yeni bölüm adresleri ve iç bağlantılar eklendi, SAHA notları düzeltildi. 2026-11-16 gizlilik ayarları rehberiyle rol ayrımı netleştirildi (Mertcan'ın kararı).
video:
video_title:
draft: true
---

ChatGPT'ye bir kira sözleşmesini yapıştırıp "şu maddeler bana karşı mı?" diye sorduğunu düşün. Cevabı alırsın, sekmeyi kapatırsın. O metin ise orada kalır. Ücretsiz ya da ücretli bireysel bir hesap kullanıyorsan, şirket bu sohbeti bir sonraki modelini eğitmek için de kullanabilir. Bu ayar üç büyük araçta da varsayılan olarak açık geliyor.

Bu ayarı kapatmak iki dakika sürüyor. Ama ayar kapalıyken de sohbetlerin bir süre şirketin sunucusunda duruyor; bu yüzden bazı bilgiler, ayar ne olursa olsun, sohbete hiç girmemeli. Bu sayfa iki şeyi anlatıyor: eğitim ayarını kapatmak ve neyi hiç yazmaman gerektiği. Daha önce yazdıklarını görmek, indirmek ve silmek ayrı bir iş; onu [gizlilik ayarları rehberinde](rehber:yapay-zeka-gizlilik-ayarlari) adım adım anlattım.

Kısaca: ChatGPT'de "Improve the model for everyone", Claude'da Gizlilik altındaki model geliştirme ayarını, Gemini'de "Keep Activity" ayarını kapat; üçü de bireysel hesaplarda varsayılan olarak açık. Ayar kapalıyken de sohbetler bir süre saklanıyor (Kasım 2026 itibarıyla Claude'da 30 gün, Gemini'de 72 saate kadar, ChatGPT geçici sohbette 30 güne kadar). Bu yüzden kimlik numarası, IBAN, şifre, API anahtarı, başkasının sağlık bilgisi ve müşteri bilgisini hiçbir ayarda yazma.

## İki dakikalık kontrol {#ayarlar}

- [ ] **ChatGPT:** Settings, Data controls, "Improve the model for everyone" kapalı.
- [ ] **Claude:** Settings, Privacy, model geliştirme ayarı kapalı.
- [ ] **Gemini:** Settings & help, Activity, "Keep Activity" kapalı.
- [ ] **Hassas tek seferlik iş:** Geçici ya da gizli sohbette yapılıyor.
- [ ] **Yapıştırılacak metin:** İsimler, kimlik ve hesap numaraları çıkarıldı.

Adımların ayrıntısı aşağıda. Menü adları İngilizce arayüze göre, 16 Kasım 2026'da üç şirketin kendi yardım sayfalarından kontrol edildi. Türkçe arayüzde başka adla görünebilir; Türkçe karşılıklarını parantez içinde verdim.

## ChatGPT'de eğitim ayarı nasıl kapatılır? {#chatgpt}

Sol alttaki profil adına tıkla, **Settings** (Ayarlar) bölümünü aç, **Data controls** (Veri kontrolleri) sekmesine geç ve **Improve the model for everyone** düğmesini kapat. Kapattıktan sonra yeni sohbetlerin eğitimde kullanılmıyor.

Tek seferlik hassas bir iş için **Temporary Chat** (geçici sohbet) aç: Geçmişine kaydedilmez ve eğitimde kullanılmaz. OpenAI yine de güvenlik için bir kopyasını 30 güne kadar tutabiliyor.

> SAHA: ChatGPT'yi Türkçe arayüzde aç, bu ayarın Türkçe adını ve yerini kontrol et, ekran görüntüsünü al. Senin hesabında varsayılan olarak açık mıydı?

## Claude'da eğitim ayarı nasıl kapatılır? {#claude}

Profil adına tıkla, **Settings** bölümünde **Privacy** (Gizlilik) sekmesini aç ve modelin geliştirilmesine yardım etme düğmesini kapat. Anthropic'in kendi sayfalarında bu düğme "Help improve Claude" ve "Help improve our AI models" gibi farklı adlarla geçiyor; yeri aynı.

Anthropic, 28 Ağustos 2025'te bireysel planlarda (Free, Pro ve Max) sohbetleri eğitimde kullanmaya başlayacağını duyurdu; mevcut kullanıcılardan 8 Ekim 2025'e kadar seçim yapmaları istendi. Ayar açıksa sohbetlerin beş yıla kadar saklanabiliyor; kapalıysa bu süre 30 gün. Tek seferlik işler için Claude'da da gizli sohbet seçeneği var; gizli sohbetler eğitimde kullanılmıyor.

> SAHA: Claude'un Türkçe arayüzünde bu ayarın adını ve gizli sohbetin nerede olduğunu kontrol et; ekran görüntüsü al.

## Gemini'de etkinlik nasıl kapatılır? {#gemini}

Gemini'de sol alttaki **Settings & help** (Ayarlar ve yardım) menüsünden **Activity** (Etkinlik) sayfasını aç ya da [myactivity.google.com/product/gemini](https://myactivity.google.com/product/gemini) adresine git. Üstteki **On** düğmesine tıkla ve **Turn off** seçeneğini seç. Bu sayfa eski yazılarda "Gemini Apps Activity" diye geçiyor; aynı yer.

Kapatınca yeni sohbetlerin eğitimde kullanılmaz ve geçmişinde görünmez. Google onları hizmetin çalışması ve senin geri bildirimin için yine 72 saate kadar tutuyor.

> SAHA: Gemini'de Türkçe arayüzde bu ayarın adını kontrol et. Kapattığında Gemini sana nasıl bir uyarı gösterdi?

## Ayarı kapatmak neyi korumaz? {#korumaz}

Ayar yalnızca bundan sonraki sohbetleri kapsıyor. Daha önce bir eğitim turuna girmiş bir sohbet modelden geri çıkarılamaz.

Ayar kapalıyken de şirketler sohbetlerini kötüye kullanımı denetlemek ve yasal yükümlülükleri için bir süre saklıyor. Yukarıda gördüğün gibi Claude'da ayar kapalıyken bu süre 30 gün, Gemini'de etkinlik kapalıyken 72 saate kadar, ChatGPT'nin geçici sohbetinde 30 güne kadar. ChatGPT'de normal sohbetler ise sen silene kadar geçmişinde duruyor. Süreler her hizmetin gizlilik politikasında yazıyor ve zaman zaman değişiyor.

Geri bildirime de dikkat et. Google, etkinlik kapalıyken bile bir cevaba geri bildirim gönderirsen o içeriğin kullanılabildiğini kendi sayfasında açıkça yazıyor. ChatGPT için de benzer bir istisnadan söz eden haberler var, ama OpenAI'ın yardım sayfalarında açıkça yazmıyor. Hassas bir sohbette beğen ya da beğenme düğmesine hiç basma.

Para ödemek de tek başına güvence değil. Ayda 20 dolar ödediğin bireysel planlarda bu ayar yine açık geliyor. Varsayılan olarak eğitimde kullanılmayan sürümler, şirketlerin satın aldığı kurumsal planlar.

## Yapay zekâya hangi bilgiler hiç yazılmaz? {#yazma}

Ayar kapalı olsa da sohbet bir yerde saklanıyor. Saklanan şey sızabilir, yanlış kişinin eline geçebilir ya da yanlışlıkla paylaşılabilir. Bu yüzden bazı bilgiler hiç yazılmaz:

- Kimlik numarası, IBAN, kart numarası. Bir belgeyi araca vermen gerekiyorsa önce bu satırları sil; belgenin anlamı değişmez.
- Şifreler ve API anahtarları. Koda yardım isterken anahtarı `***` ile değiştir. Yanlışlıkla yapıştırdıysan anahtarı hemen iptal edip yenisini al; sohbeti silmek yetmez.
- Başkasının sağlık bilgisi. 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) sağlık verisini "özel nitelikli" sayıyor (m.6) ve daha sıkı kurallara bağlıyor. Annenin tahlil sonucunu yorumlatmak istiyorsan adını, doğum tarihini ve hastane bilgisini çıkararak yapıştır; ayrıntısı [tahlil sonucu rehberinde](rehber:tahlil-sonucu-yapay-zeka).
- Müşterinin ya da çalışanın bilgileri. Bunu aşağıda ayrıca anlatıyorum.
- Gizlilik sözleşmesi imzaladığın her şey. Sözleşmen bilgiyi "üçüncü kişilerle paylaşma" diyorsa, bir yapay zekâ şirketi de üçüncü kişidir.

İsimleri ve numaraları etiketle değiştirmek işe yarayan bir alışkanlık: "Ahmet Yılmaz" yerine "Kiracı", "0532..." yerine "[TELEFON]". Yapay zekânın cevabı çoğu zaman hiç değişmez.

Temsili bir örnek: "Ahmet Yılmaz'ın 12 Mart tarihli kira sözleşmesinin 7. maddesi..." yerine "Kiracının kira sözleşmesinin 7. maddesi şöyle: [madde metni]. Bu madde kiracı aleyhine mi?" yazarsın. Sorunun cevabı için kiracının adına gerek yok.

## İş yerinde yapay zekâya şirket bilgisi yazılır mı? {#is-yerinde}

Burada iş kişisel tercih olmaktan çıkıyor. Bir şirket adına müşteri ya da çalışan bilgisi işliyorsan, o bilgiyi bir yapay zekâ aracına yapıştırmak da bir veri işleme faaliyeti. Sorumluluk şirkette; şirketin kuralını çiğnediysen sana da dönebilir. Aracın sunucuları yurt dışındaysa bir de KVKK'nın yurt dışına aktarım kuralları (m.9) devreye giriyor.

Kamuya açık bir örnek: Nisan 2023'te Samsung'un yarı iletken biriminde çalışanlar, hata ayıklamak ve toplantı notu çıkarmak için şirketin gizli kaynak kodunu ve iç belgelerini ChatGPT'ye yapıştırdı. Samsung, Mayıs 2023'te şirket cihazlarında üretken yapay zekâ kullanımını yasakladı. Kötü niyet yoktu; sadece "kişisel hesaba yapıştırılan bilgi şirketin dışına çıkmış olur" düşünülmemişti.

Şirket verisini yüklemeden önce kendine üç soru sor:

1. Şirketin bu araç için bir kuralı var mı? Yoksa yöneticine sor. "Herkes kullanıyor" bir kural değil.
2. Kişisel hesabını mı, şirketin anlaştığı kurumsal sürümü mü kullanıyorsun? OpenAI'ın iş planlarında olduğu gibi kurumsal sürümlerde veriler varsayılan olarak eğitimde kullanılmıyor ve sözleşmeyle korunuyor; kişisel hesabında bu güvence yok.
3. Aynı işi isimleri ve numaraları çıkararak yapabilir misin? Çoğu iş için cevap evet.

Temsili örnek: Bir muhasebe bürosunda çalışan biri ay sonu yetişsin diye müşterilerin adını, T.C. kimlik numarasını ve borç tutarını içeren tabloyu kendi ücretsiz yapay zekâ hesabına yapıştırıyor ve "bunu düzenle" diyor. İş on dakikada bitiyor. Ama o tablo artık büronun kontrolünde değil: Büro, hangi müşterinin bilgisinin nereye gittiğini bilmiyor; hesabın eğitim ayarı açıksa sohbet modelin geliştirilmesinde de kullanılabiliyor. Aynı iş, isimler ve kimlik numaraları çıkarılıp yerine "Müşteri 1, Müşteri 2" yazılarak da aynı sürede yapılabilirdi.

## Yanlışlıkla hassas bilgi yazdıysan ne yapmalı? {#yanlislikla}

Panik yapma, sırayla şunları yap:

1. Ne paylaştığını not al: hangi araç, hangi gün, hangi bilgi.
2. Şifre ya da anahtar paylaştıysan önce onu değiştir. En acil adım bu.
3. Sohbeti sil; adımları [gizlilik ayarları rehberinin silme bölümünde](rehber:yapay-zeka-gizlilik-ayarlari#sil). Silmenin, bilginin şirketin kayıtlarından aynı anda silindiği anlamına gelmediğini bil.
4. Şirket verisiyse yöneticine ya da şirketin kişisel verilerden sorumlu kişisine söyle. Hukuki sonucu olaya göre değişir ve bunu şirket değerlendirecek. Ne kadar erken söylersen şirketin o kadar zamanı olur; saklarsan o zamanı elinden alırsın. Olay bir veri ihlali sayılırsa, KVKK m.12/5 ve Kurul'un 2019/10 sayılı kararına göre şirket bunu öğrendiği andan itibaren en geç 72 saat içinde Kurul'a bildirmek zorunda.

> SAHA: Yukarıdaki 72 saat cümlesini avukat gözüyle oku; bir çalışanın kişisel hesabına müşteri verisi yapıştırmasının ihlal sayılıp sayılmayacağına dair genel bir not eklemek ister misin? Kesin hüküm kurmadan bir iki cümle.

## Sık yapılan hatalar {#hatalar}

- **Ücretli plana geçince verinin korunduğunu sanmak.** Plus, Pro ya da Max gibi bireysel ücretli planlarda da eğitim ayarı açık geliyor; kendin kapatmalısın.
- **Ayarı kapatıp eski sohbetlerin de çıktığını sanmak.** Ayar geriye dönük çalışmıyor.
- **Sohbeti silip anahtarı değiştirmemek.** Sızan şifre ya da API anahtarı, sohbet silinse de geçerli kalır.
- **Belgenin adını değiştirip içeriği bırakmak.** Dosya adı "sözlesme_son.pdf" olsa da içindeki ad, adres ve kimlik numarası olduğu gibi gider.
- **Beğen ya da beğenme düğmesine basmak.** Bazı araçlarda bu, ayar kapalıyken bile sohbetin incelenmesine yol açabiliyor.

## Dürüst sınır {#sinir}

Bu sayfa, şirketlerin kendi yardım sayfalarında yazanlara dayanıyor; sunucuda gerçekte ne olduğunu dışarıdan doğrulamanın yolu yok. Ayar adları ve saklama süreleri sık değişiyor; ayda bir ayarlarına bakmak ve hassas işlerde bilgiyi baştan çıkarmak, herhangi bir ayardan daha güvenilir. Kişisel Verileri Koruma Kurulu da konunun üzerinde: 24 Kasım 2025'te üretken yapay zekâ rehberini yayımladı, Şubat 2026'da da Grok hakkında re'sen inceleme başlattığını duyurdu.

## Sonraki adım {#sonraki-adim}

Şimdi iki dakika ayır ve yukarıdaki kontrol listesini kendi hesabında tamamla. Paylaşılan bağlantılar, hafıza ve hesap silme gibi diğer ayarlar [gizlilik ayarları rehberinde](rehber:yapay-zeka-gizlilik-ayarlari). Hangi aracı kullanacağına henüz karar vermediysen [hangi yapay zekâ rehberine](rehber:hangi-yapay-zeka) bak; cevaplarını bir yere koymadan önce de [kontrol listesinden](rehber:yapay-zeka-cevabini-kontrol-etmek) geçir.

## Kaynaklar

Ayar yolları ve süreler 16 Kasım 2026'da şirketlerin kendi yardım sayfalarından kontrol edildi. Her şirketin gizlilik politikası esastır ve değişebilir.

- OpenAI: [Data Controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq) · [Temporary Chat FAQ](https://help.openai.com/en/articles/8914046-temporary-chat-faq) · [Verilerin model geliştirmede kullanımı](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)
- Anthropic: [Tüketici koşulları güncellemesi, 28 Ağustos 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms) · [Model geliştirme ayarı](https://privacy.claude.com/en/articles/12109829) · [Claude veri gizliliği SSS](https://support.claude.com/en/articles/8325621-claude-data-privacy-faq)
- Google: [Gemini Apps etkinliğini yönetme](https://support.google.com/gemini/answer/13278892?hl=en) · [Gemini Apps Gizlilik Merkezi](https://support.google.com/gemini/answer/13594961?hl=en)
- Kişisel Verileri Koruma Kurumu, [Üretken Yapay Zekâ ve Kişisel Verilerin Korunması Rehberi (15 Soruda)](https://www.kvkk.gov.tr/Icerik/8547/uretken-yapay-zeka-ve-kisisel-verilerin-korunmasi-rehberi-15-soruda), 24 Kasım 2025
- 6698 sayılı Kişisel Verilerin Korunması Kanunu, özel nitelikli veriler (m.6), yurt dışına aktarım (m.9) ve ihlal bildirimi (m.12/5): [Mevzuat Bilgi Sistemi](https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5)
- Kişisel Verileri Koruma Kurulu, 24.01.2019 tarihli ve 2019/10 sayılı karar (veri ihlali bildirim süresi): [kvkk.gov.tr](https://www.kvkk.gov.tr/)
- Kişisel Verileri Koruma Kurumu, Grok hakkında re'sen inceleme duyurusu, 11 Şubat 2026: [kvkk.gov.tr](https://www.kvkk.gov.tr/Icerik/8614)
- Samsung'un üretken yapay zekâ yasağı, 2 Mayıs 2023: [Bloomberg](https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak) · [The Register](https://www.theregister.com/2023/05/02/samsung_generative_ai_ban/)
