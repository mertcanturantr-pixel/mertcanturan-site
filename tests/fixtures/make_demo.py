"""Önizleme için örnek video verisi ve kapak görselleri üretir. Canlı siteye çıkmaz."""
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
MEDIA = HERE / "demo_media"
FONT = "/home/claude/fonts/BricolageGrotesque[opsz,wdth,wght].ttf"
INK, PAPER, RED, YEL, WHITE = "#16224F", "#F6F7FB", "#E23B2E", "#FFE04A", "#FFFFFF"
STYLES = [(INK, WHITE, YEL), (YEL, INK, RED), (PAPER, INK, RED), (RED, WHITE, YEL)]


def font(size):
    try:
        f = ImageFont.truetype(FONT, size)
    except OSError:  # yazı tipi yoksa Pillow'un varsayılanı
        return ImageFont.load_default(size)
    try:
        f.set_variation_by_axes([96, 780, 92])
    except Exception:
        pass
    return f


def wrap(draw, text, f, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    return lines


def thumb(name, text, size, style):
    bg, fg, acc = STYLES[style % len(STYLES)]
    W, H = size[0] * 2, size[1] * 2
    im = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(im)
    tall = H > W
    f = font(96 if tall else 92)
    lines = wrap(d, text, f, W - 120)
    y = H * (0.30 if tall else 0.22)
    for ln in lines:
        d.text((60, y), ln, font=f, fill=fg); y += f.size * 1.08
    d.rectangle([60, y + 24, 60 + 160, y + 40], fill=acc)
    small = font(34)
    d.rounded_rectangle([W - 210, 40, W - 40, 100], radius=14, fill=WHITE, outline=INK, width=4)
    d.text((W - 190, 50), "ÖRNEK", font=small, fill=INK)
    im.resize(size, Image.Resampling.LANCZOS).save(MEDIA / name, "JPEG", quality=84)


def main():
    MEDIA.mkdir(exist_ok=True)
    now = datetime(2026, 11, 16, 9, tzinfo=timezone.utc)
    yt = ["Bir hafta boyunca bütün kararlarımı yapay zekâya verdim",
          "Dört yapay zekâya aynı sözleşmeyi okuttum",
          "ChatGPT'ye yazdıkların nereye gidiyor?",
          "Yapay zekâyla bir günde uygulama yaptım"]
    shorts = ["Yapay zekâ kaynak uydurursa nasıl anlarsın?",
              "Bu ayarı kapatmadan ChatGPT'ye müşteri bilgisi yazma",
              "1 dolarlık araba: bir sohbet robotunun hatası",
              "Aynı soruyu dört araca sordum",
              "Yapay zekâ sözleşmemdeki hatayı buldu mu?",
              "Ücretsiz sürüm mü, ücretli sürüm mü?",
              "Bir müşterinin sorusunu yapay zekâya sordum",
              "Yapay zekâ ile CV hazırlarken dikkat"]
    content = {"generated_at": now.isoformat(), "platforms": {}}
    items = []
    for i, t in enumerate(yt):
        n = f"youtube-demo{i}.jpg"; thumb(n, t, (640, 360), i)
        items.append({"platform": "youtube", "id": f"demo{i}", "kind": "video", "title": t,
                      "url": "https://www.youtube.com/", "published": (now - timedelta(days=14 * i)).isoformat(),
                      "ad": False, "guides": ["kontrol-listesi"] if i == 1 else [], "thumb": n})
    content["platforms"]["youtube"] = {"status": "ok", "items": items}
    for p in ("instagram", "tiktok"):
        items = []
        for i, t in enumerate(shorts):
            n = f"{p}-demo{i}.jpg"; thumb(n, t, (360, 640), i + (1 if p == "tiktok" else 0))
            items.append({"platform": p, "id": f"demo{i}", "kind": "reel" if p == "instagram" else "video",
                          "title": t, "url": f"https://www.{p}.com/", "published": (now - timedelta(days=2 * i)).isoformat(),
                          "ad": i == 5, "guides": ["kontrol-listesi"] if i == 0 else [], "thumb": n})
        content["platforms"][p] = {"status": "ok", "items": items}
    (HERE / "demo_content.json").write_text(json.dumps(content, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
