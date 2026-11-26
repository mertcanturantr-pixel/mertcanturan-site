import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from PIL import Image  # noqa: E402

import build  # noqa: E402
import guides as G  # noqa: E402
import plan_check  # noqa: E402
from datetime import date  # noqa: E402
import common as C  # noqa: E402
import feeds  # noqa: E402

CFG = C.load_config()

YT_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns:yt="http://www.youtube.com/xml/schemas/2015" xmlns:media="http://search.yahoo.com/mrss/" xmlns="http://www.w3.org/2005/Atom">
 <entry>
  <yt:videoId>AAA111</yt:videoId><title>Uzun video</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=AAA111"/>
  <published>2026-11-20T16:00:00+00:00</published>
  <media:group><media:description>Rehber: mertcanturan.com/rehber/kontrol-listesi #REKLAM</media:description></media:group>
 </entry>
 <entry>
  <yt:videoId>BBB222</yt:videoId><title>Kisa</title>
  <link rel="alternate" href="https://www.youtube.com/shorts/BBB222"/>
  <published>2026-11-21T16:00:00+00:00</published>
  <media:group><media:description></media:description></media:group>
 </entry>
</feed>"""


def jpeg_bytes(size=(800, 600)):
    buf = io.BytesIO()
    Image.new("RGB", size, "#16224F").save(buf, "JPEG")
    return buf.getvalue()


class TempData(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name)
        self.patches = [mock.patch.object(C, "CONTENT_FILE", d / "content.json"),
                        mock.patch.object(C, "MEDIA_DIR", d / "media"),
                        mock.patch.object(C, "DATA_DIR", d)]
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in self.patches:
            p.stop()
        self.tmp.cleanup()


class TextTests(unittest.TestCase):
    def test_ad_detection_turkish_case(self):
        self.assertTrue(C.is_ad("Yeni video #REKLAM"))
        self.assertTrue(C.is_ad("#İşBirliği ile"))
        self.assertTrue(C.is_ad("#isbirligi"))
        self.assertFalse(C.is_ad("reklam yok burada"))
        self.assertFalse(C.is_ad(None))

    def test_title_from_caption(self):
        self.assertEqual(C.title_from_caption("#ai #test\nAsıl başlık burada #yz\nikinci"), "Asıl başlık burada")
        long = "kelime " * 40
        t = C.title_from_caption(long)
        self.assertTrue(t.endswith("…") and len(t) <= 91)

    def test_redact_hides_tokens(self):
        msg = C.redact("https://x.com/a?access_token=SECRET123&b=1 refresh_token=RT")
        self.assertNotIn("SECRET123", msg)
        self.assertNotIn("RT ", msg + " ")

    def test_host_allowed(self):
        self.assertTrue(C.host_allowed("https://www.instagram.com/p/x", ["instagram.com"]))
        self.assertFalse(C.host_allowed("javascript:alert(1)", ["instagram.com"]))
        self.assertFalse(C.host_allowed("http://www.instagram.com/p/x", ["instagram.com"]))
        self.assertFalse(C.host_allowed("https://instagram.com.evil.net/", ["instagram.com"]))

    def test_instagram_timestamp(self):
        self.assertEqual(C.parse_time("2026-11-16T09:00:00+0000").isoformat(), "2026-11-16T09:00:00+00:00")


class FeedTests(TempData):
    def test_youtube_parse(self):
        items = feeds.parse_youtube_feed(YT_XML)
        self.assertEqual([i["kind"] for i in items], ["video", "short"])
        self.assertTrue(items[0]["ad"])
        self.assertEqual(items[0]["guides"], ["kontrol-listesi"])

    def test_instagram_normalize(self):
        data = {"data": [
            {"id": "1", "caption": "Başlık\n#reklam", "media_type": "VIDEO", "media_product_type": "REELS",
             "thumbnail_url": "https://scontent.cdninstagram.com/t.jpg", "permalink": "https://www.instagram.com/reel/1/",
             "timestamp": "2026-11-16T09:00:00+0000"},
            {"id": "2", "caption": "telifli", "media_type": "IMAGE", "timestamp": "2026-11-16T09:00:00+0000"}]}
        items = feeds.normalize_instagram(data)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["kind"], "reel")
        self.assertEqual(items[0]["title"], "Başlık")
        self.assertTrue(items[0]["ad"])

    def test_tiktok_error_raises(self):
        with self.assertRaises(C.FetchError):
            feeds.normalize_tiktok({"error": {"code": "access_token_invalid"}})

    def test_finalize_drops_bad_links_sorts_and_limits(self):
        base = {"platform": "tiktok", "kind": "video", "title": "t", "ad": False, "guides": [], "_thumb_src": []}
        items = [dict(base, id=str(i), url="https://www.tiktok.com/@m/video/%d" % i,
                      published="2026-11-%02dT00:00:00+00:00" % (i + 1)) for i in range(12)]
        items.append(dict(base, id="x", url="javascript:alert(1)", published="2026-12-01T00:00:00+00:00"))
        out = feeds.finalize(items, CFG)
        self.assertEqual(len(out), CFG["max_items_per_platform"])
        self.assertNotIn("x", [i["id"] for i in out])
        self.assertEqual(out[0]["id"], "11")
        self.assertIsNone(out[0]["thumb"])

    def test_store_thumb_rejects_foreign_host_without_request(self):
        with mock.patch.object(C, "http_request") as req:
            self.assertIsNone(feeds.store_thumb("instagram", "1", ["https://evil.example/x.jpg"], (360, 640),
                                                CFG["allowed_image_hosts"]))
            req.assert_not_called()

    def test_store_thumb_resizes_and_skips_broken(self):
        responses = [b"not an image", jpeg_bytes()]
        with mock.patch.object(C, "http_request", side_effect=lambda *a, **k: responses.pop(0)):
            name = feeds.store_thumb("youtube", "AAA", ["https://i.ytimg.com/a.jpg", "https://i.ytimg.com/b.jpg"],
                                     (640, 360), CFG["allowed_image_hosts"])
        self.assertEqual(name, "youtube-AAA.jpg")
        with Image.open(C.MEDIA_DIR / name) as im:
            self.assertEqual(im.size, (640, 360))

    def test_error_keeps_previous_items_and_reports(self):
        cfg = json.loads(json.dumps(CFG))
        cfg["platforms"]["instagram"]["profile_url"] = "https://www.instagram.com/x/"
        old_item = {"platform": "instagram", "id": "9", "url": "https://www.instagram.com/p/9/", "title": "eski"}
        C.CONTENT_FILE.write_text(json.dumps({"platforms": {"instagram": {"status": "ok", "items": [old_item]}}}))

        def fake_json(url, **kw):
            if "refresh_access_token" in url:
                return {"access_token": "NEWTOKEN", "expires_in": 5184000}
            raise C.FetchError("HTTP 400")

        with mock.patch.object(C, "http_json", side_effect=fake_json), \
                mock.patch.object(C, "http_request", return_value=YT_XML):
            content, secrets, report = feeds.run(cfg, {"IG_TOKEN": "OLDTOKEN"})
        self.assertEqual(content["platforms"]["instagram"]["status"], "error")
        self.assertEqual(content["platforms"]["instagram"]["items"], [old_item])
        self.assertIn("instagram", report["errors"])
        self.assertEqual(secrets, {"IG_TOKEN": "NEWTOKEN"})
        self.assertEqual(content["platforms"]["youtube"]["status"], "ok")
        self.assertEqual(content["platforms"]["tiktok"]["status"], "not_configured")
        self.assertNotIn("OLDTOKEN", json.dumps(report))

    def test_tiktok_refresh_rotation(self):
        cfg = json.loads(json.dumps(CFG))
        cfg["platforms"]["tiktok"]["profile_url"] = "https://www.tiktok.com/@x"

        def fake_json(url, **kw):
            if url.endswith("/v2/oauth/token/"):
                return {"access_token": "AT", "refresh_token": "RT2", "refresh_expires_in": 31536000}
            self.assertEqual(kw["headers"]["Authorization"], "Bearer AT")
            return {"data": {"videos": [{"id": "7", "title": "Video #reklam", "create_time": 1763280000,
                                         "share_url": "https://www.tiktok.com/@x/video/7",
                                         "cover_image_url": "https://p16.tiktokcdn.com/c.jpg"}]},
                    "error": {"code": "ok"}}
        secrets, report = {}, {}
        with mock.patch.object(C, "http_json", side_effect=fake_json):
            items = feeds.fetch_tiktok(cfg, {"TIKTOK_CLIENT_KEY": "k", "TIKTOK_CLIENT_SECRET": "s",
                                             "TIKTOK_REFRESH_TOKEN": "RT1"}, secrets, report)
        self.assertEqual(secrets, {"TIKTOK_REFRESH_TOKEN": "RT2"})
        self.assertTrue(items[0]["ad"])


def meta(**kw):
    m = {"title": "T", "slug": "a-b", "summary": "Özet", "type": "kontrol-listesi",
         "published": "2026-11-01", "checked": "2026-11-10", "changes": []}
    m.update(kw)
    return m


class GuideTests(unittest.TestCase):
    TODAY = date(2026, 11, 16)

    def test_validation_rules(self):
        self.assertEqual(G.validate(meta(), "x.md", CFG, self.TODAY), [])
        for bad in (meta(type="blog"), meta(checked="2026-12-01"), meta(checked="2026-10-01"),
                    meta(summary="a" * 201), meta(slug="Kötü"), meta(video="https://evil.example/v"),
                    meta(published="16.11.2026")):
            with self.assertRaises(ValueError):
                G.validate(bad, "x.md", CFG, self.TODAY)

    def test_stale_warning(self):
        w = G.validate(meta(published="2026-01-01", checked="2026-01-02"), "x.md", CFG, self.TODAY)
        self.assertTrue(w and "180" in w[0])

    def test_change_lines(self):
        m, _ = G.parse_front_matter("---\ntitle: a\nchange: 2026-11-16 İlk sürüm.\nchange: 2026-12-01 Güncellendi.\n---\nmetin")
        self.assertEqual(len(m["changes"]), 2)
        self.assertEqual(m["changes"][1]["note"], "Güncellendi.")

    def test_template_block(self):
        body = "```sablon\nMerhaba [SÖZLEŞME TÜRÜ] ve [İLGİLİ KİŞİ] <script>x</script>\n[SÖZLEŞME METNİ]\n```\n"
        out, _, has, _ = G.render_body(body)
        self.assertTrue(has)
        self.assertIn('data-tpl', out)
        self.assertEqual(out.count("<input "), 2)
        self.assertEqual(out.count("<textarea"), 1)
        self.assertIn(">İlgili kişi<", out)
        self.assertNotIn("<script>x", out)
        self.assertIn('<mark data-f="SÖZLEŞME TÜRÜ">', out)

    def test_toc_slugs(self):
        out, toc, _, _ = G.render_body("## Başlamadan önce: 6 kural\n\nx\n\n## Kaynaklar\n")
        self.assertEqual(toc[0][0], "baslamadan-once-6-kural")
        self.assertIn('<h2 id="kaynaklar">', out)

    def test_saha_note(self):
        out, _, _, n = G.render_body("Metin.\n\n> SAHA: Ekran görüntüsü ekle.\n")
        self.assertEqual(n, 1)
        self.assertIn('class="saha"', out)

    def test_json_ld_is_escaped(self):
        g = meta(title="</script><b>", summary="s")
        self.assertNotIn("</script><b>", G.json_ld(g, CFG))


KARNE_OK = """Yöntem: <b>Deneme</b> yöntemi
İddia: Ayda 30 bin TL kazandırır.
Başlangıç maliyeti: Sıfır
İlk gelire kadar: 3 ay
Gereken beceri: Kurgu
Türkiye'den yapılabilir mi: Evet
Platform kuralı: Yok
Bunun yerine: Hizmet sat.
Karar: Bu haliyle çalışmıyor"""

class KarneAndTemplateTests(unittest.TestCase):
    def test_karne_renders_and_escapes(self):
        out, *_ = G.render_body("```karne\n" + KARNE_OK + "\n```")
        self.assertIn('data-verdict="no"', out)
        self.assertIn("&lt;b&gt;Deneme&lt;/b&gt;", out)
        self.assertIn("<dt>İlk gelire kadar</dt><dd>3 ay</dd>", out)

    def test_karne_rules(self):
        bad = {
            "eksik alan": KARNE_OK.replace("Gereken beceri: Kurgu\n", ""),
            "bilinmeyen alan": KARNE_OK + "\nSüre: 3 ay",
            "geçersiz karar": KARNE_OK.replace("Bu haliyle çalışmıyor", "Belki"),
            "olumsuzda bunun yerine yok": KARNE_OK.replace("Bunun yerine: Hizmet sat.\n", ""),
            "olumluda ilk adım yok": KARNE_OK.replace("Bu haliyle çalışmıyor", "Çalışıyor"),
            "gelir vaadi": KARNE_OK.replace("İlk gelire kadar: 3 ay", "İlk gelire kadar: ayda 5.000 TL"),
            "kırmızı çizgi": KARNE_OK.replace("<b>Deneme</b> yöntemi", "Kripto botu"),
            "bağlantı": KARNE_OK.replace("Platform kuralı: Yok", "Platform kuralı: https://ornek.com"),
            "iki kez": KARNE_OK + "\nKarar: Çalışıyor",
            "bozuk satır": KARNE_OK + "\nbozuk satır",
            "kullanıcı adı": KARNE_OK.replace("Ayda 30 bin TL kazandırır.", "@birhesap anlatıyor."),
        }
        for name, text in bad.items():
            with self.subTest(name), self.assertRaises(ValueError):
                G.parse_karne(text)
        # iddianın kendisi rakam içerebilir
        self.assertEqual(G.parse_karne(KARNE_OK)["verdict"], "no")

    def test_extract_karnes_anchor(self):
        k = G.extract_karnes("## Yüzsüz kanal\n\n```karne\n" + KARNE_OK + "\n```\n")
        self.assertEqual((len(k), k[0]["anchor"]), (1, "yuzsuz-kanal"))

    def test_duplicate_method_rejected(self):
        k = dict(G.parse_karne(KARNE_OK), anchor="")
        with self.assertRaises(ValueError):
            build.collect_karnes([{"slug": "a", "karnes": [k]}, {"slug": "b", "karnes": [k]}])

    def test_money_threshold(self):
        def k(name, positive=False):
            text = KARNE_OK.replace("<b>Deneme</b> yöntemi", name)
            if positive:
                text = text.replace("Bunun yerine: Hizmet sat.", "İlk adım: Başla.").replace("Bu haliyle çalışmıyor", "Çalışıyor")
            return dict(G.parse_karne(text), anchor="")
        g = {"slug": "x", "karnes": [k("A"), k("B"), k("C")]}
        self.assertFalse(build.money_page_ready(build.collect_karnes([g]), 3))  # hepsi olumsuz
        g["karnes"] = [k("A"), k("B"), k("C", True)]
        self.assertTrue(build.money_page_ready(build.collect_karnes([g]), 3))
        g["karnes"] = [k("C", True)]
        self.assertFalse(build.money_page_ready(build.collect_karnes([g]), 3))


REPO_OK = """---
name: Deneme
slug: deneme
repo: sahip/deneme
category: yerel
summary: Kısa özet.
difficulty: kolay
cost: Ücretsiz
license: MIT
stars: 10 bin
checked: 2026-11-10
draft: false
---

## Ne işe yarar

Bir şey yapar.

## Kurulum

`pip install deneme`

## Dikkat etmen gerekenler

Dikkat.
"""


class RepoTests(unittest.TestCase):
    def _load(self, files, meta=None):
        import repos as R
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            for name, text in files.items():
                (p / name).write_text(text, encoding="utf-8")
            mf = p / "meta.json"
            mf.write_text(json.dumps(meta or {}), encoding="utf-8")
            with mock.patch.object(R, "REPOS_DIR", p), mock.patch.object(R, "META_FILE", mf):
                return R.load(include_drafts=True, today=date(2026, 11, 16))

    def test_valid_repo_loads(self):
        repos, warn = self._load({"a.md": REPO_OK})
        self.assertEqual((len(repos), repos[0]["license"], warn), (1, "MIT", []))

    def test_repo_rules(self):
        bad = {
            "lisans yok": REPO_OK.replace("license: MIT", "license: YOK"),
            "açık olmayan lisans notsuz": REPO_OK.replace("license: MIT", "license: SSPL-1.0"),
            "eksik bölüm": REPO_OK.replace("## Kurulum", "## Başka"),
            "yanlış depo biçimi": REPO_OK.replace("repo: sahip/deneme", "repo: deneme"),
            "bilinmeyen kategori": REPO_OK.replace("category: yerel", "category: kripto"),
            "ileri tarih": REPO_OK.replace("checked: 2026-11-10", "checked: 2026-12-10"),
        }
        for name, text in bad.items():
            with self.subTest(name), self.assertRaises(ValueError):
                self._load({"a.md": text})

    def test_meta_overrides_and_guards(self):
        repos, _ = self._load({"a.md": REPO_OK}, {"sahip/deneme": {"stars": "12 bin", "license": "MIT"}})
        self.assertEqual(repos[0]["stars"], "12 bin")
        with self.assertRaises(ValueError):  # GitHub'da lisans değişmiş
            self._load({"a.md": REPO_OK}, {"sahip/deneme": {"license": "GPL-3.0"}})
        with self.assertRaises(ValueError):  # arşivlenmiş depo yayınlanamaz
            self._load({"a.md": REPO_OK}, {"sahip/deneme": {"archived": True}})
        repos, _ = self._load({"a.md": REPO_OK.replace("draft: false", "draft: true")}, {"sahip/deneme": {"archived": True}})
        self.assertTrue(repos[0]["archived"])

    def test_unrecognized_github_license_does_not_stop_build(self):
        text = REPO_OK.replace("license: MIT", "license: Sustainable-Use-License\nlicense_note: Açık kaynak değil.")
        repos, _ = self._load({"a.md": text}, {"sahip/deneme": {"license": "NOASSERTION", "stars": "5 bin"}})
        self.assertEqual((repos[0]["license"], repos[0]["stars"]), ("Sustainable-Use-License", "5 bin"))

    def test_license_note_allows_custom_license(self):
        text = REPO_OK.replace("license: MIT", "license: Sustainable-Use-License\nlicense_note: Açık kaynak değil.")
        repos, _ = self._load({"a.md": text})
        import repos as R
        self.assertIn("açık kaynak lisansı değil", R.license_text(repos[0]))

    def test_tr_stars(self):
        import repo_meta
        self.assertEqual([repo_meta.tr_stars(n) for n in (950, 1000, 184712, 95400)], ["950", "1 bin", "184,7 bin", "95,4 bin"])


class TopicTests(unittest.TestCase):
    def test_every_real_guide_has_a_known_topic(self):
        guides, _ = G.load(C.load_config(), include_drafts=True, today=date(2026, 11, 26))
        self.assertEqual([g["slug"] for g in guides if g["topic"] not in G.TOPICS or g["topic"] == "diger"], [])

    def test_unknown_topic_is_rejected(self):
        meta = {"title": "a", "slug": "a", "summary": "a", "type": "sablon", "published": "2026-01-01",
                "checked": "2026-01-01", "topic": "yok", "changes": []}
        with self.assertRaises(ValueError):
            G.validate(meta, "a.md", C.load_config(), date(2026, 11, 26))


class ShortLinkTests(unittest.TestCase):
    def test_short_links_point_to_published_or_fall_back(self):
        with tempfile.TemporaryDirectory() as d:
            made = build.write_short_links(Path(d), C.load_config(), {"cv-ve-mulakat"}, True)
            self.assertEqual(made["cv"], "rehber/cv-ve-mulakat/")
            self.assertEqual(made["ayar"], "rehber/")  # rehber yayında değil: listeye gider
            html = (Path(d) / "cv" / "index.html").read_text(encoding="utf-8")
            self.assertIn("https://mertcanturan.com/rehber/cv-ve-mulakat/", html)
            self.assertIn("noindex", html)


class PlanTests(unittest.TestCase):
    def test_every_video_has_an_existing_guide(self):
        code, rows = plan_check.check(today=date(2026, 11, 26))
        self.assertEqual([r for r in rows if r["state"] == "REHBER YOK"], [])
        self.assertEqual(len(rows), 15)

    def test_late_guide_is_reported(self):
        code, rows = plan_check.check(today=date(2026, 12, 9))
        self.assertEqual(code, 1)
        late = {r["code"] for r in rows if r["state"] == "GECİKTİ"}
        self.assertIn("S1", late)  # taslak hâlâ yayında değil
        self.assertNotIn("U1", late)  # yayındaki rehber gecikmiş sayılmaz


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.links = build.Links(0, False)
        self._g = mock.patch.object(G, "GUIDES_DIR", ROOT / "tests" / "fixtures" / "guides")
        self._g.start()

    def tearDown(self):
        self._g.stop()

    def test_card_escapes_and_labels(self):
        item = {"platform": "instagram", "id": "1", "title": '<script>alert("x")</script>',
                "url": "https://www.instagram.com/p/1/?a=1&b=2", "published": "2026-11-16T09:00:00+00:00",
                "ad": True, "guides": ["kontrol-listesi", "yok-boyle"], "thumb": "instagram-1.jpg"}
        html = build.render_card(item, self.links, {"kontrol-listesi"})
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertIn('href="https://www.instagram.com/p/1/?a=1&amp;b=2"', html)
        self.assertIn(">Reklam<", html)
        self.assertIn("rehber/kontrol-listesi/", html)
        self.assertNotIn("yok-boyle", html)

    def test_feed_hides_unconfigured_platforms(self):
        content = {"platforms": {"youtube": {"status": "ok", "items": []},
                                 "instagram": {"status": "not_configured", "items": []}}}
        html = build.render_feed(content, CFG, self.links, set())
        self.assertIn("panel-youtube", html)
        self.assertNotIn("tab-instagram", html)
        self.assertNotIn('role="tablist"', html)  # tek platformda sekme gösterilmez
        self.assertIn("İlk videolar yakında", html)
        self.assertIn("sub_confirmation=1", html)

    def test_youtube_prefers_long_videos_and_full_rows(self):
        items = [{"platform": "youtube", "id": str(i), "kind": "video", "title": str(i),
                  "url": "https://www.youtube.com/watch?v=%d" % i, "published": "2026-11-16T09:00:00+00:00",
                  "thumb": None} for i in range(4)]
        items.append(dict(items[0], id="s", kind="short", url="https://www.youtube.com/shorts/s"))
        html = build.render_feed({"platforms": {"youtube": {"status": "ok", "items": items}}}, CFG, self.links, set())
        self.assertEqual(html.count('class="card"'), 3)
        self.assertIn("grid wide", html)

    def test_guide_front_matter_validation(self):
        with self.assertRaises(ValueError):
            G.parse_front_matter("baslik yok")
        self.assertIsNone(build.SLUG_RE.match("Kötü Adres"))

    def test_checklist_rendering(self):
        out, _, _, _ = G.render_body("- [ ] **Bir.** açıklama\n- [ ] **İki.** açıklama\n")
        self.assertIn('<ul class="checklist">', out)
        self.assertEqual(out.count('type="checkbox"'), 2)
        self.assertEqual(out.count("</label></li>"), 2)

    def test_full_build_live_has_no_demo_and_valid_pages(self):
        with tempfile.TemporaryDirectory() as d:
            out = build.build(preview=False, demo=False, out_dir=Path(d) / "dist")
            index = (out / "index.html").read_text(encoding="utf-8")
            self.assertNotIn("Önizleme", index)
            self.assertNotIn("{{", index)
            self.assertTrue((out / "rehber" / "ornek-yayinda" / "index.html").exists())
            self.assertTrue((out / "CNAME").exists())
            self.assertIn("/rehber/ornek-yayinda/", (out / "sitemap.xml").read_text())
            # SEO ve yardımcı dosyalar
            self.assertIn('"@type": "Person"', index)
            self.assertIn('href="#ust">İçeriğe geç', index)
            for name in ("favicon.svg", "apple-touch-icon.png", "404.html", "llms.txt", "robots.txt"):
                self.assertTrue((out / name).exists(), name)
            nf = (out / "404.html").read_text(encoding="utf-8")
            self.assertIn('content="noindex"', nf)
            self.assertIn('href="/site.css"', nf)
            llms = (out / "llms.txt").read_text(encoding="utf-8")
            self.assertIn("/rehber/ornek-yayinda/", llms)
            self.assertNotIn("ornek-taslak", llms)
            tpl = (out / "rehber" / "sablonlar" / "index.html").read_text(encoding="utf-8")
            self.assertIn("Örnek şablon", tpl)
            self.assertIn('href="../../rehber/ornek-yayinda/#ikinci-bolum"', tpl)
            self.assertIn("/rehber/sablonlar/", (out / "sitemap.xml").read_text())
            page_html = (out / "rehber" / "ornek-yayinda" / "index.html").read_text(encoding="utf-8")
            self.assertIn('data-verdict="maybe"', page_html)
            # tek karne eşiğin altında: para sayfası ve bağlantıları yok
            self.assertFalse((out / "yapay-zekayla-para-kazanmak").exists())
            self.assertNotIn("money-cta", index)
            self.assertNotIn("yapay-zekayla-para-kazanmak", (out / "sitemap.xml").read_text())

    def test_money_page_when_threshold_met(self):
        cfg = json.loads(json.dumps(CFG))
        cfg["money_page_min"] = 1
        with tempfile.TemporaryDirectory() as d, mock.patch.object(C, "load_config", return_value=cfg):
            out = build.build(preview=False, demo=False, out_dir=Path(d) / "dist")
            money = (out / "yapay-zekayla-para-kazanmak" / "index.html").read_text(encoding="utf-8")
            self.assertIn("Örnek yöntem", money)
            self.assertNotIn("örnektir", money)  # demo notu canlıda yok
            self.assertIn('href="../rehber/ornek-yayinda/#ikinci-bolum"', money)
            self.assertNotIn("ornek-taslak", money)
            self.assertIn("money-cta", (out / "index.html").read_text(encoding="utf-8"))
            self.assertIn("yapay-zekayla-para-kazanmak", (out / "rehber" / "index.html").read_text(encoding="utf-8"))
            self.assertIn("money-link", (out / "rehber" / "ornek-yayinda" / "index.html").read_text(encoding="utf-8"))
            self.assertIn("/yapay-zekayla-para-kazanmak/", (out / "sitemap.xml").read_text())
            self.assertIn("/yapay-zekayla-para-kazanmak/", (out / "llms.txt").read_text(encoding="utf-8"))
            self.assertTrue((out / "og" / "para-kazanmak.png").exists())

    def test_money_demo_only_in_preview(self):
        with tempfile.TemporaryDirectory() as d:
            out = build.build(preview=True, demo=True, out_dir=Path(d) / "dist")
            money = (out / "yapay-zekayla-para-kazanmak" / "index.html").read_text(encoding="utf-8")
            self.assertIn("karneler örnektir", money)
            for page in out.rglob("*.html"):
                text = page.read_text(encoding="utf-8")
                self.assertNotRegex(text, r'(src|href)="//', page.name)
                self.assertNotRegex(text, r'<(script|img)[^>]+src="https?://', page.name)
                self.assertNotRegex(text, r'<link(?![^>]*rel="(canonical|alternate)")[^>]+href="https?://', page.name)

    def test_archor_hidden_by_default_and_shown_when_enabled(self):
        self.assertEqual(build.render_archor(CFG), ("", ""))
        cfg = dict(CFG, archor={"show": True, "url": "https://archor.com.tr"})
        collab, about = build.render_archor(cfg)
        self.assertIn('href="https://archor.com.tr"', collab)
        self.assertIn("kurucusuyum", about)
        with self.assertRaises(ValueError):
            build.render_archor(dict(CFG, archor={"show": True, "url": "javascript:alert(1)"}))

    def test_follow_lists_only_configured_accounts(self):
        html = build.render_follow(CFG)
        self.assertIn(">YouTube<", html)
        self.assertNotIn("Instagram", html)
        cfg = json.loads(json.dumps(CFG))
        cfg["platforms"]["tiktok"]["profile_url"] = "https://www.tiktok.com/@mertcanturan"
        self.assertIn('href="https://www.tiktok.com/@mertcanturan" rel="me"', build.render_follow(cfg))

    def test_live_build_hides_archor_and_has_follow(self):
        with tempfile.TemporaryDirectory() as d:
            out = build.build(out_dir=Path(d) / "dist")
            index = (out / "index.html").read_text(encoding="utf-8")
            self.assertNotIn("Archor", index)
            self.assertIn('class="follow"', index)
            self.assertIn("Ürünle bir ticari bağım varsa", index)
            guide = (out / "rehber" / "ornek-yayinda" / "index.html").read_text(encoding="utf-8")
            self.assertIn('class="follow"', guide)

    def test_drafts_only_in_preview(self):
        with tempfile.TemporaryDirectory() as d:
            live = build.build(out_dir=Path(d) / "live")
            self.assertFalse((live / "rehber" / "ornek-taslak").exists())
            self.assertNotIn("ornek-taslak", (live / "rehber" / "feed.xml").read_text())
            self.assertNotIn("ornek-taslak", (live / "sitemap.xml").read_text())
            yayinda = (live / "rehber" / "ornek-yayinda" / "index.html").read_text(encoding="utf-8")
            self.assertNotIn("rehber:ornek-taslak", yayinda)  # taslağa bağlantı düz metin
            self.assertTrue((live / "og" / "ornek-yayinda.png").exists())
            with Image.open(live / "og" / "ornek-yayinda.png") as im:
                self.assertEqual(im.size, (1200, 630))
            prev = build.build(preview=True, out_dir=Path(d) / "prev")
            draft = (prev / "rehber" / "ornek-taslak" / "index.html").read_text(encoding="utf-8")
            self.assertIn('class="saha"', draft)
            self.assertIn('content="noindex"', draft)
            self.assertIn("Taslak: Onayından sonra", draft)

    def test_internal_links(self):
        known = {"a": {"bolum"}, "b": set()}
        L = build.Links(2, False)
        html = build.resolve_internal('<a href="rehber:a#bolum">x</a> <a href="rehber:b">y</a>', L, known, "t.md", {"b"})
        self.assertIn('href="../../rehber/a/#bolum"', html)
        self.assertNotIn("rehber:b", html)
        with self.assertRaises(ValueError):
            build.resolve_internal('<a href="rehber:yok">x</a>', L, known, "t.md")
        with self.assertRaises(ValueError):
            build.resolve_internal('<a href="rehber:a#olmayan">x</a>', L, known, "t.md")

    def test_skeleton_cannot_be_published(self):
        with self.assertRaises(ValueError):
            G.validate(meta(stage="iskelet", draft="false"), "x.md", CFG, date(2026, 11, 16))

    def test_real_guides_build_in_preview(self):
        self._g.stop()
        try:
            with tempfile.TemporaryDirectory() as d:
                build.build(preview=True, out_dir=Path(d) / "p")
        finally:
            self._g.start()

    def test_demo_requires_preview(self):
        with mock.patch.object(sys, "argv", ["build.py", "--demo"]), self.assertRaises(SystemExit):
            build.main()


if __name__ == "__main__":
    unittest.main()


class SeoAndAnchorTests(unittest.TestCase):
    def test_fixed_anchor_survives_heading_change(self):
        out, toc, _, _ = G.render_body("## Eski başlık {#sabit}\n\nMetin.\n")
        self.assertIn('<h2 id="sabit">Eski başlık</h2>', out)
        self.assertEqual(toc, [("sabit", "Eski başlık")])

    def test_duplicate_fixed_anchor_fails(self):
        with self.assertRaises(ValueError):
            G.render_body("## A {#ayni}\n\nx\n\n## B {#ayni}\n\ny\n")

    def test_fixed_anchor_in_template_links(self):
        body = "## Şablon bölümü {#sablon}\n\n```sablon\nMetin [ALAN]\n```\n"
        self.assertEqual(G.extract_templates(body)[0]["anchor"], "sablon")

    def test_title_tag_drops_brand_when_long(self):
        self.assertEqual(build.guide_title_tag({"title": "Kısa başlık"}), "Kısa başlık · Mertcan Turan")
        long = "x" * 58
        self.assertEqual(build.guide_title_tag({"title": "Çok uzun", "seo_title": long}), long)

    def test_red_line_checked_in_every_karne_field(self):
        text = KARNE_OK.replace("Bunun yerine: Hizmet sat.", "Bunun yerine: Kazancı kripto hesabına aktar.")
        self.assertNotEqual(text, KARNE_OK)
        with self.assertRaises(ValueError):
            G.parse_karne(text)



class JobToolTests(unittest.TestCase):
    """Mesleğine göre yapay zekâ aracı: veri bütünlüğü, yayın eşiği ve gizlilik."""

    def setUp(self):
        import meslek as M
        self.M = M
        self.data = M.load()

    def test_every_reference_points_to_a_real_guide_and_anchor(self):
        gdir = ROOT / "guides"
        for src, target in self.M.refs(self.data):
            slug, _, anchor = target.partition("#")
            path = gdir / f"{slug}.md"
            self.assertTrue(path.exists(), f"{src}: {slug} rehberi yok")
            if anchor:
                self.assertIn("{#" + anchor + "}", path.read_text(encoding="utf-8"), f"{src}: #{anchor} yok")

    def test_prompts_have_fillable_fields_only(self):
        import re
        for m in self.data["meslekler"]:
            self.assertGreaterEqual(len(m["isler"]), self.M.MIN_TASKS, m["slug"])
            self.assertEqual(len(m["kirmizi"]), 3, m["slug"])
            self.assertIn(m["veri"], self.data["veri"])
            for t in m["isler"]:
                for br in re.findall(r"\[[^\]]*\]", t["komut"]):
                    self.assertRegex(br, G.PLACEHOLDER_RE.pattern, f'{m["slug"]}/{t["id"]}: {br}')

    def test_unpublished_guides_are_dropped_and_threshold_applies(self):
        fake = [{"slug": "zor-e-postalar", "toc": [], "title": "x"}]
        self.assertEqual(self.M.available(self.data, fake), [])
        self.assertFalse(self.M.ready(self.data, fake))
        self.assertFalse(self.M.ready(None, fake))

    def test_page_sends_nothing(self):
        for bad in ("fetch(", "XMLHttpRequest", "sendBeacon", "localStorage", "document.cookie"):
            self.assertNotIn(bad, self.M.JS)

    def test_llms_full_cleans_internal_markup(self):
        g = {"slug": "a", "title": "A", "checked": "2026-11-16",
             "body_md": "## Başlık {#adres}\n\nBak: [x](rehber:b#c)\n\n> SAHA: doldur\n\n```sablon\n[ALAN]\n```"}
        out = G.llms_full([g], CFG)
        self.assertNotIn("{#", out)
        self.assertNotIn("SAHA", out)
        self.assertNotIn("rehber:", out)
        self.assertIn("/rehber/b/#c", out)
        self.assertNotIn("```sablon", out)
