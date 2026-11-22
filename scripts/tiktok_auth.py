"""TikTok hesabını bir kez bağlamak için kendi bilgisayarında çalıştırılan yardımcı.

Kullanım:
  python scripts/tiktok_auth.py --client-key KEY --redirect-uri https://mertcanturan.com/

Adımlar:
 1. Betik bir bağlantı yazar. Bağlantıyı tarayıcıda aç ve TikTok hesabınla izin ver.
 2. TikTok seni redirect-uri adresine geri gönderir. Adres çubuğundaki tam adresi kopyalayıp betiğe yapıştır.
 3. Betik yenileme anahtarını .tiktok_tokens dosyasına yazar (ekrana basmaz).
 4. Anahtarı GitHub'a kaydet ve dosyayı sil:
      gh secret set TIKTOK_REFRESH_TOKEN < .tiktok_tokens
      rm .tiktok_tokens
Uygulama sırrı (client secret) TIKTOK_CLIENT_SECRET ortam değişkeninden okunur; komut satırına yazılmaz.
"""
from __future__ import annotations

import argparse
import getpass
import json
import os
import secrets
import sys
import urllib.parse
import urllib.request

AUTH_URL = "https://www.tiktok.com/v2/auth/authorize/"
TOKEN_URL = "https://open.tiktokapis.com/v2/oauth/token/"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--client-key", required=True)
    ap.add_argument("--redirect-uri", required=True, help="TikTok uygulamasında kayıtlı yönlendirme adresi")
    a = ap.parse_args()
    client_secret = os.environ.get("TIKTOK_CLIENT_SECRET") or getpass.getpass("TikTok client secret: ")

    state = secrets.token_urlsafe(16)
    url = AUTH_URL + "?" + urllib.parse.urlencode({
        "client_key": a.client_key, "scope": "user.info.basic,video.list", "response_type": "code",
        "redirect_uri": a.redirect_uri, "state": state})
    print("\n1) Bu bağlantıyı tarayıcıda aç ve izin ver:\n\n" + url + "\n")
    back = input("2) Yönlendirildiğin sayfanın tam adresini buraya yapıştır: ").strip()
    q = urllib.parse.parse_qs(urllib.parse.urlsplit(back).query)
    if q.get("state", [""])[0] != state:
        print("Güvenlik kontrolü tutmadı (state farklı). Baştan dene.")
        return 1
    if "error" in q:
        print("TikTok izni vermedi:", q.get("error_description", q["error"])[0])
        return 1
    code = q.get("code", [""])[0]
    if not code:
        print("Adreste izin kodu bulunamadı.")
        return 1

    body = urllib.parse.urlencode({"client_key": a.client_key, "client_secret": client_secret, "code": code,
                                   "grant_type": "authorization_code", "redirect_uri": a.redirect_uri}).encode()
    req = urllib.request.Request(TOKEN_URL, data=body, method="POST",
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    rt = data.get("refresh_token")
    if not rt:
        print("Anahtar alınamadı:", data.get("error_description") or data.get("error") or "bilinmeyen hata")
        return 1
    if "video.list" not in data.get("scope", ""):
        print("Uyarı: video.list izni verilmemiş görünüyor. Videolar çekilemez.")
    fd = os.open(".tiktok_tokens", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as fh:
        fh.write(rt)
    print("\n3) Yenileme anahtarı .tiktok_tokens dosyasına yazıldı. Şimdi:\n"
          "   gh secret set TIKTOK_REFRESH_TOKEN < .tiktok_tokens\n   rm .tiktok_tokens")
    return 0


if __name__ == "__main__":
    sys.exit(main())
