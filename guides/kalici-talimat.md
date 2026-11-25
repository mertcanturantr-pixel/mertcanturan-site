---
title: Kalıcı talimat nasıl yazılır: ChatGPT özel talimat, Claude proje ve Gemini Gem ile seni tanıyan asistan
slug: kalici-talimat
seo_title: Kalıcı talimat: ChatGPT özel talimat, Claude proje, Gemini Gem
description: Her sohbette kendini baştan anlatma: ChatGPT özel talimat ve proje, Claude profil tercihi ve proje, Gemini Gem kurulumu; kopyalanabilir talimat şablonu.
summary: Her sohbette kendini baştan anlatmamak için ChatGPT, Claude ve Gemini'de kalıcı talimat, proje ve Gem kurmak: nerede, neyi yazmalı, neyi asla yazmamalı ve hazır şablon.
keywords: chatgpt özel talimat nasıl yazılır, chatgpt custom instructions örnek, chatgpt kişiselleştirme, claude proje nasıl kurulur, claude profil tercihleri, gemini gem oluşturma, kalıcı talimat şablonu, chatgpt hafıza silme
type: adim-adim
topic: baslangic
audience: Herkes
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İlk sürüm; 2026-11-16 dört rollü denetim: doğrulanamayan 5.000 karakter iddiası çıkarıldı, menü yolları ve Gemini kişisel talimat alanı resmî kaynakla güncellendi, örnek talimat ve çıktı eklendi, SAHA notu düzeltildi.
video:
video_title:
draft: true
---

Her sohbette aynı cümleleri yazıyorsan ("Türkçe cevap ver", "kısa yaz", "ben bir avukatım", "madde madde değil, paragrafla"), bunları bir kez kalıcı talimata kaydetmenin zamanı gelmiş. Üç büyük araçta da bunun bir yeri var ve kurulumu on dakika sürüyor. Sonuç: Cevaplar ilk seferde sana uygun geliyor, sen de her seferinde komut yazmakla uğraşmıyorsun.

Kısaca: Hesap genelinde geçerli olacak, değişmeyen bilgileri (kim olduğun, nasıl cevap istediğin) kalıcı talimata yaz. Belirli bir işe ait bilgileri (bir müşteri, bir ders, bir kitap) o işe özel bir projeye ya da Gem'e koy. Ve hiçbirine kimlik numarası, şifre ya da başkasının bilgisini yazma.

## Kalıcı talimat, proje ve hafıza: hangisi ne işe yarar? {#katmanlar}

| Katman | Ne zaman geçerli | Ne yazılır |
| --- | --- | --- |
| Kalıcı talimat (hesap geneli) | Bütün yeni sohbetlerde | Mesleğin, dilin, cevap biçimi, kaçınmasını istediğin şeyler |
| Proje ya da Gem (işe özel) | Yalnızca o projenin ya da Gem'in sohbetlerinde | O işe ait belgeler, kurallar, ton, örnekler |
| Hafıza | Aracın kendiliğinden öğrendikleri | Senin yazmadığın ama sohbetlerden çıkardığı bilgiler; düzenli kontrol etmen gerekir |

En sık hata, her şeyi kalıcı talimata yığmak. "Müşterim X şirketinin sözleşme şablonu şöyle..." gibi bir bilgi kalıcı talimata girerse, alakasız bir tatil planında bile modelin aklına gelebilir. İşe özel bilgiyi projeye koy.

## ChatGPT'de özel talimat ve proje nasıl kurulur? {#chatgpt}

**Kalıcı talimat (Custom Instructions):**

1. Web ya da masaüstünde profil simgene tıkla, Settings'i (Ayarlar) aç.
2. Personalization (Kişiselleştirme) bölümüne gir.
3. Custom Instructions alanına talimatını yaz ve kaydet. Telefonda da aynı bölüm uygulamanın ayarlarında.

Özel talimat bütün planlarda var. OpenAI'ın yardım sayfası alan başına 1.500 karakter sınırından söz ediyor; ekranda farklı bir sayaç görüyorsan onu esas al. Aynı ekranda hafızayı (Memory) da görüp düzenleyebiliyorsun.

**Projeler:** Sol menüde yeni bir proje aç, projeye dosya ekle ve proje talimatını yaz. Proje içindeki her sohbet o dosyaları ve talimatı bilir. Bir müşterinin işi, bir ders ya da bir ev tadilatı için ayrı proje kullan.

> SAHA: ChatGPT'nin Türkçe arayüzünde Personalization ve Custom Instructions alanlarının Türkçe adlarını ve karakter sayacını kontrol et; ekran görüntüsü al. Kendi kalıcı talimatından, kişisel ya da iş bilgisi içermeyen iki üç satırı örnek olarak ekleyebilirsin.

## Claude'da profil tercihi ve proje nasıl kurulur? {#claude}

**Profil tercihleri:** Ayarlar > Profil bölümünde, Claude'un bütün sohbetlerde dikkate almasını istediğin kişisel tercihleri yazabileceğin bir alan var. Mesleğin, dilin ve cevap biçimin buraya. Claude'un hafızası açıksa, sohbetlerden çıkardığı bilgileri de ayarlardan görüp düzenleyebilirsin.

**Projeler:** Yeni bir proje aç, proje bilgisine belgelerini yükle ve proje talimatını yaz. Uzun belgelerle çalışıyorsan Claude'un projeleri özellikle işe yarıyor; aynı sözleşme setini ya da raporları her sohbette yeniden yüklemen gerekmiyor.

**Stiller:** Cevapların uzunluğunu ve tonunu bir kez seçtiğin stille ayarlayabilirsin. Kendi yazı örneğini vererek özel bir stil de oluşturabilirsin.

## Gemini'de Gem ve kişisel talimat nasıl kurulur? {#gemini}

**Gem:** Gemini'de belirli bir iş için kendi asistanını kurmanın yolu Gem. Gem yöneticisinden yeni bir Gem oluştur, ona bir ad ver, talimatını yaz ve gerekiyorsa dosya ekle. Örneğin "E-posta yazarı" adlı bir Gem, senin tonunda kısa ve resmî e-postalar yazacak şekilde kurulabilir.

**Kalıcı talimat:** Gemini'nin ayarlarındaki kişisel bağlam (İngilizce arayüzde Personal context) bölümünde, bütün sohbetlerde dikkate alınacak bilgilerini ve tercihlerini yazabileceğin bir alan var. Google Workspace hesaplarında Eylül 2026'dan beri kaydedilen talimatlar Gmail, Dokümanlar, E-Tablolar, Slaytlar, Drive ve Chat'teki Gemini'de de kullanılıyor; yönetimi Ayarlar > Kişiselleştirme altında.

> SAHA: Gemini'nin Türkçe arayüzünde Gem oluşturma ve kalıcı talimat bölümlerinin adlarını ve yerlerini kontrol et; ekran görüntüsü al.

## Kopyalanabilir kalıcı talimat şablonu {#sablon}

```sablon
Hakkımda:
- Mesleğim: [MESLEK VE ALAN]
- Genelde şu işler için kullanıyorum: [İŞLER]
- Bilgi düzeyim: [ÖRNEĞİN "HUKUKU BİLİYORUM, YAZILIMDA YENİYİM"]

Cevaplarken:
- Türkçe yaz; teknik terimleri gerektiğinde kısaca açıkla.
- Önce kısa cevabı ver, sonra gerekirse ayrıntıya gir.
- Emin olmadığın yerde "emin değilim" de; tahmini kesin bilgi gibi sunma.
- Rakam, tarih, kanun maddesi ya da kaynak verirsen nereden kontrol edebileceğimi söyle.
- Bana hak vermeye çalışma; karşı görüş varsa söyle.
- [ÖRNEĞİN "MADDE İŞARETİNİ YALNIZCA LİSTE GEREKTİĞİNDE KULLAN"]

Asla:
- [ÖRNEĞİN "UYDURMA KAYNAK VERME", "TIBBİ TEŞHİS KOYMA"]
```

Temsili örnek: Bir muhasebe bürosunda çalışan biri "Mesleğim: Mali müşavir yardımcısı; KDV ve bordro işleri. Bilgi düzeyim: Mevzuatı biliyorum, Excel formüllerinde yeniyim" yazıp "Öncelik farkı ne?" diye sorduğunda, talimatsız sohbette gelen genel tanım yerine şuna benzer bir cevap bekler: "Kısaca: ... Excel'de bunu şu formülle hesaplarsın: ... Bu oranın güncel hâlini GİB'in sayfasından kontrol et." Talimat, cevabın düzeyini ve biçimini ilk sorudan ayarlar.

"Bana hak vermeye çalışma" satırı küçük görünüyor ama işe yarıyor: Yapay zekâ modelleri kullanıcıya katılma eğiliminde; nedeni [karar rehberinde](rehber:yapay-zekaya-karar-verdirmek#dalkavukluk).

## Kalıcı talimata neyi yazmamalısın? {#yazma}

Kalıcı talimat ve proje bilgisi, her sohbette modele gönderiliyor ve şirketin sunucusunda saklanıyor. Bu yüzden:

- Kimlik numarası, adres, telefon, banka bilgisi yazma.
- Şifre, API anahtarı ya da erişim bilgisi yazma.
- Başkasının (ailenin, müşterinin, çalışanının) kişisel bilgisini yazma.
- Sağlık durumunu yazacaksan, bunun her sohbette kullanılacağını bil; 6698 sayılı Kişisel Verilerin Korunması Kanunu'na (KVKK) göre sağlık verisi özel nitelikli kişisel veri, gerçekten gerekmiyorsa yazma.
- İş yerine ait gizli bilgileri kişisel hesabındaki talimata koyma.

Neyin hiç yazılmaması gerektiği [ne yazılmaz rehberinde](rehber:yapay-zekaya-ne-yazilmaz).

## Hafızayı ara ara kontrol et {#hafiza}

Kalıcı talimattan farklı olarak hafıza, senin yazmadığın ama araçların sohbetlerden çıkardığı bilgileri tutuyor. Bir sohbette "kızım üniversiteye başladı" dediysen, bu bilgi hafızaya girmiş olabilir. Ayda bir hafızaya bak ve istemediğin bilgileri sil. Nasıl yapılacağı [gizlilik rehberinde](rehber:yapay-zeka-gizlilik-ayarlari#hafiza).

## Sık yapılan hatalar {#hatalar}

- **Çelişen talimatlar.** Kalıcı talimatta "kısa yaz", projede "ayrıntılı yaz" diyorsan, model ikisinin ortasını bulmaya çalışır. Bir yerde tek kural olsun.
- **Çok uzun talimat.** Uzun talimat, asıl kuralları sulandırır. Vazgeçemeyeceğin beş altı kuralı yaz; gerisini gerektiğinde komutta söyle.
- **Talimatı unutmak.** Mesleğin ya da ihtiyacın değiştiğinde talimat eski kalır ve cevaplar tuhaflaşır. Üç ayda bir gözden geçir.
- **Kişisel ve iş talimatını karıştırmak.** İş için ayrı bir proje ya da Gem kur; kişisel talimat iş sohbetlerine taşınmasın.

## Dürüst sınır {#sinir}

Kalıcı talimat modelin davranışını yönlendirir ama her zaman uymasını garanti etmez; özellikle uzun sohbetlerde talimatın etkisi azalabilir. Ciddi bir işte kuralı komutta bir kez daha söylemek hâlâ en güvenli yol. Menü adları ve karakter sınırları da sık değişiyor; bu sayfa 16 Kasım 2026'da kontrol edildi.

## Sonraki adım {#sonraki-adim}

Bugün şablonu kendine göre doldur ve en çok kullandığın araca kaydet. Bir hafta sonra cevapların değişip değişmediğine bak; değişmediyse talimatı kısaltıp netleştir. Komutları daha iyi yazmak için [iyi komut rehberine](rehber:yapay-zekaya-iyi-komut-yazmak) bak.

## Kaynaklar

- OpenAI Yardım Merkezi, "ChatGPT Custom Instructions": [help.openai.com](https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt)
- OpenAI Academy, "Personalizing ChatGPT", Nisan 2026: [openai.com](https://openai.com/academy/personalization)
- Anthropic Yardım Merkezi, profil tercihleri ve projeler: [support.claude.com](https://support.claude.com/)
- Google Gemini Yardım, Gem'ler ve kişisel talimatlar: [support.google.com/gemini](https://support.google.com/gemini/)
- Google, Gemini'de kişisel bağlam ayarları, 13 Ağustos 2025: [blog.google](https://blog.google/products-and-platforms/products/gemini/temporary-chats-privacy-controls/)
- Google Workspace Updates, Gemini özel talimatlarının diğer uygulamalara gelmesi, 2 Eylül 2026: [workspaceupdates.googleblog.com](https://workspaceupdates.googleblog.com/2026/09/custom-instructions-for-gemini-in-Workspace-now-available-in-more-apps.html)
