---
title: Günlük işlerde yapay zekâ: 8 iş, hazır komutlar ve hangisi için hangi araç
slug: yapay-zeka-gunluk-isler
seo_title: Günlük işlerde yapay zekâ: 8 iş için hazır komutlar
description: E-posta özeti, toplantı notu, haftalık plan, uzun belge, sunum taslağı, çeviri, tablo ve öğrenme için doldurup kullanacağın komutlar ve dikkat edilecekler.
summary: E-posta, toplantı notu, plan, uzun belge, sunum, çeviri, tablo ve öğrenme: günlük işlerde yapay zekâyı verimli kullanmak için doldurup kopyalayacağın komutlar.
keywords: yapay zeka ile günlük işler, yapay zeka nerelerde kullanılır, chatgpt ile e-posta özeti, toplantı notundan görev listesi, chatgpt haftalık plan, pdf özetleme komutu, chatgpt prompt örnekleri türkçe, yapay zeka verimlilik
type: karsilastirma
audience: Herkes, İş yerleri
stage: hazir
published: 2026-11-16
checked: 2026-11-16
change: 2026-11-16 İskeletten tam rehbere çevrildi: sekiz günlük iş, hazır komutlar ve araç önerileri; 2026-11-16 dört rollü denetim: Kısaca paragrafı, ilgili rehberlere bağlantılar ve Copilot lisans notu eklendi.
video:
video_title:
draft: false
---

Yapay zekâyı her gün açıp yine de "bana pek bir şey kazandırmıyor" diyen çok kişi var. Genellikle sorun araçta değil, ona verilen işte: Ya çok büyük ve belirsiz bir iş veriliyor ("bana iş planı yaz"), ya da her seferinde bağlam baştan anlatılıyor. Aşağıdaki sekiz iş, yapay zekânın gerçekten zaman kazandırdığı, sonucunu da kolayca kontrol edebildiğin işler. Her biri için doldurup kullanacağın bir komut var.

Kısaca: Yapay zekânın günlük işte en çok zaman kazandırdığı yerler e-posta zinciri özeti, toplantı notundan görev listesi, haftalık plan, uzun belge okuma, sunum taslağı, çeviri, tablo ve yeni bir konuyu öğrenmek. Kural basit: Ona taslak, özet, düzen ve seçenek işini ver; karar, rakam ve son kontrol sende kalsın. Hepsi ChatGPT, Claude ve Gemini'nin ücretsiz sürümlerinde yapılabiliyor.

## 1. Uzun bir e-posta zincirini özetlemek {#eposta-ozet}

Yirmi mesajlık bir yazışmaya sonradan dahil edildiğinde:

```sablon
Aşağıdaki e-posta yazışmasını özetle. Şu başlıkları kullan:
- Konu ne?
- Kim ne istiyor?
- Karar verilen şeyler
- Açık kalan sorular ve kimden cevap bekleniyor
- Benden beklenen bir şey var mı? (Benim adım: [ADIN YA DA ROLÜN])

Yazışmada olmayan bir şey ekleme.

[YAZIŞMA]
```

Yapıştırmadan önce müşteri ve çalışan bilgilerini çıkar ya da iş hesabındaki kurumsal aracı kullan; neden olduğu [ne yazılmaz rehberinde](rehber:yapay-zekaya-ne-yazilmaz#is-yerinde). Zor bir e-postaya cevap yazacaksan [zor e-postalar rehberine](rehber:zor-e-postalar) geç.

## 2. Toplantı notundan görev listesi {#toplanti}

Toplantıda aldığın dağınık notları ya da otomatik transkripti düzenlemek için:

```sablon
Aşağıdaki toplantı notlarından şunları çıkar:
1. Alınan kararlar (madde madde)
2. Görevler: Görev | Sorumlu | Son tarih (notlarda yoksa "belirtilmedi" yaz)
3. Bir sonraki toplantıya kalan konular

Kimseye notlarda olmayan bir görev atama. Belirsiz yerleri sonunda soru olarak listele.

[NOTLAR]
```

Çıkan listeyi toplantıdaki herkese göndermeden önce bir kez oku; yapay zekâ "belki Ahmet bakar" cümlesini kesin bir görev gibi yazabilir. Toplantıyı kaydedip özetletmenin kuralları ve izin konusu [toplantı özeti rehberinde](rehber:toplanti-ozeti).

## 3. Haftalık plan {#plan}

```sablon
Bu hafta yapmam gereken işler şunlar: [İŞLER, VARSA SON TARİHLERİYLE]
Sabit randevularım: [GÜN VE SAATLER]
Günde gerçekçi olarak odaklanabildiğim süre: [SAAT]

Bunları güne böl. Önce son tarihi yakın ve uzun süren işleri yerleştir. Her güne en fazla iki büyük iş koy. Bir güne sığmayan işi söyle; sığdırmaya çalışma. Planın sonunda, bu hafta yapılamayacak gibi duran işleri ayrıca listele.
```

Yapay zekânın planı, ne kadar zaman ayırabileceğini bildiğin kadar gerçekçi olur. "Günde 8 saat odaklanırım" yazarsan plan da tutmaz.

## 4. Uzun bir belgeyi okumak {#uzun-belge}

Bir rapor, yönetmelik ya da sözleşme için:

```sablon
Ekteki belgeyi [AMACIM, ÖRNEĞİN "YARINKİ TOPLANTIYA HAZIRLANMAK"] için okuyacağım. Benim için şunları çıkar:
1. Belgenin bir paragraflık özeti
2. Benim işimi doğrudan etkileyen bölümler (bölüm ya da sayfa numarasıyla)
3. Belgede geçen tarihler, tutarlar ve yükümlülükler (bulunduğu yerle)
4. Belgeyi okuyunca sorulması gereken üç soru

Her bilgi için belgenin neresinde geçtiğini yaz. Belgede olmayan bilgi ekleme.
```

Rakamları ve tarihleri belgenin kendisinden kontrol et; yapay zekâ uzun belgelerde sayfa numarası ve rakam karıştırabiliyor. Yüzlerce sayfalık belgeler için yol [uzun PDF rehberinde](rehber:uzun-pdf-okumak), sözleşmeler için ayrı şablonlar [sözleşme okutma rehberinde](rehber:sozlesme-sablonu).

## 5. Sunum taslağı {#sunum}

```sablon
[KİME] yapacağım [SÜRE] dakikalık bir sunumun taslağını hazırla. Konu: [KONU].
Dinleyicinin sunumdan sonra yapmasını istediğim şey: [AMAÇ].
Elimdeki malzeme: [RAKAMLAR, NOTLAR, BELGELER]

Her slayt için: başlık (bir cümlelik mesaj olarak), en fazla üç madde ve konuşurken söyleyeceğim iki üç cümle. Rakam uydurma; malzemede olmayan rakam gerekiyorsa [RAKAM] diye boş bırak.
```

Slayt başlığını "Satışlar" gibi bir kelime değil, "Satışlar üçüncü çeyrekte düştü, nedeni stok" gibi bir cümle yapmak, sunumu çok daha anlaşılır yapar; yapay zekâya bunu açıkça iste. Taslaktan slayta geçiş [sunum rehberinde](rehber:sunum-hazirlamak).

## 6. Çeviri ve yazı düzeltme {#ceviri}

```sablon
Aşağıdaki metni [DİL] diline çevir. Metin [KİME] gidecek ve tonu [RESMÎ / SAMİMİ] olmalı.
Özel isimleri, rakamları ve teknik terimleri değiştirme. Emin olmadığın bir terimi çeviride köşeli parantez içinde orijinaliyle bırak.

[METİN]
```

Önemli bir yazışmada çeviriyi, ana dili o dil olan birine ya da başka bir araca tersinden çevirterek kontrol et. Hukuki ya da tıbbi bir metnin çevirisini resmî iş için kullanacaksan yeminli tercümana git.

## 7. Tablo ve Excel {#tablo}

Dağınık bir listeyi tabloya çevirmek, formül yazdırmak ya da veriyi temizlemek yapay zekânın iyi yaptığı işler; ama hesap sonucunu sohbetten değil, tablodaki formülden kontrol et. Türkçe Excel'deki tuzaklar ve hazır komutlar [Excel rehberinde](rehber:excel-yapay-zeka).

## 8. Yeni bir şey öğrenmek {#ogrenme}

```sablon
[KONU] hakkında hiçbir şey bilmiyorum. Bana bu konuyu öğret ama şöyle:
- Önce konunun neden önemli olduğunu iki cümleyle anlat.
- Sonra en temel beş kavramı, her birine günlük hayattan bir örnek vererek açıkla.
- Her kavramdan sonra beni sınayan bir soru sor ve cevabımı bekle.
- Yanlış cevap verirsem nedenini açıkla.
```

Bu şekilde öğrenmek, yapay zekâya özet yazdırmaktan çok daha kalıcı. Öğrendiğin bilginin doğru olup olmadığını önemli konularda bir kaynaktan kontrol et; nasıl yapılacağı [kontrol rehberinde](rehber:yapay-zeka-cevabini-kontrol-etmek).

## Hangi iş için hangi araç? {#arac}

Bu sekiz işin hepsi ChatGPT, Claude ve Gemini'nin ücretsiz sürümlerinde yapılabiliyor. Fark, işin büyüklüğünde ve araçların diğer uygulamalarla bağlantısında çıkıyor:

- **Gmail, Drive ve Takvim kullanıyorsan** e-posta özeti ve haftalık plan için Gemini, verilerine doğrudan erişebildiği için pratik.
- **Uzun belge okutuyorsan** belge boyutu sınırlarına dikkat et; uzun metinlerde araçlar arasında fark büyüyor.
- **Şirketin Microsoft 365 kullanıyorsa** ve Copilot lisansı varsa, Word ve Outlook içindeki Copilot belgeyi başka yere taşımadan çalıştığı için veri açısından daha güvenli olabilir.

Araçların fiyatları ve farkları [hangi yapay zekâ rehberinde](rehber:hangi-yapay-zeka). Aynı işi iki araçla nasıl karşılaştıracağın [test yöntemi rehberinde](rehber:test-yontemi#kendi-testin).

## Sık yapılan hatalar {#hatalar}

- **Her işi yapay zekâya vermek.** İki dakikalık bir e-postayı yapay zekâya yazdırmak, komut yazmak ve kontrol etmek dahil beş dakika sürer. Kısa işleri kendin yap.
- **Bağlamı her seferinde baştan anlatmak.** Sık tekrar ettiğin bilgileri (rolün, şirketin, yazım tarzın) kalıcı talimata kaydet. Nasıl yapılacağı [kalıcı talimat rehberinde](rehber:kalici-talimat); iyi komutun genel kuralları [komut rehberinde](rehber:yapay-zekaya-iyi-komut-yazmak).
- **Özeti okuyup belgeyi hiç açmamak.** Özet bir harita; önemli kararı haritaya göre değil, araziye bakarak ver.
- **Rakamları kontrol etmemek.** Tarih, tutar ve isim, yapay zekânın en kolay karıştırdığı bilgiler.

## Yapay zekâ her zaman zaman kazandırır mı? {#sinir}

Bu işlerin hepsinde yapay zekâ zaman kazandırır ama her seferinde değil. Ne istediğini net bilmediğin işlerde komut yazmak ve sonucu düzeltmek, işi kendin yapmaktan uzun sürebilir. Bir işte yapay zekânın sana gerçekten zaman kazandırıp kazandırmadığını anlamanın tek yolu, bir hafta boyunca o işi yapay zekâyla ve yapay zekâsız yapıp süreyi karşılaştırmak.

## Sonraki adım {#sonraki-adim}

Bu sekiz işten senin haftanda en çok tekrar edeni seç ve şablonunu bir hafta boyunca her seferinde kullan. Hafta sonunda kendine sor: Bana zaman kazandırdı mı, kaybettirdi mi?

## Kaynaklar

Bu sayfadaki komutlar ve öneriler araçların 16 Kasım 2026'daki ücretsiz sürümlerine göre yazıldı. Araç özellikleri ve sınırları için:

- OpenAI Yardım Merkezi: [help.openai.com](https://help.openai.com/)
- Anthropic Yardım Merkezi: [support.claude.com](https://support.claude.com/)
- Google Gemini Yardım: [support.google.com/gemini](https://support.google.com/gemini/)
