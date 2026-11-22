"""GitHub depolarının lisans, yıldız, arşiv ve son güncelleme bilgisini GitHub API'den tazeler.

GitHub Actions'ta GITHUB_TOKEN ile çalışır ve data/repos_meta.json dosyasını yazar. Bir depo okunamazsa
önceki bilgisi korunur; hata yalnızca uyarı olarak basılır. Lisans değişirse ya da depo arşivlenirse
site derlemesi (scripts/repos.py) bunu yakalar ve durur.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402
import guides as G  # noqa: E402
import repos as R  # noqa: E402


def tr_stars(n: int) -> str:
    if n < 1000:
        return str(n)
    s = f"{n / 1000:.1f}".rstrip("0").rstrip(".").replace(".", ",")
    return f"{s} bin"


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    old = json.loads(R.META_FILE.read_text(encoding="utf-8")) if R.META_FILE.exists() else {}
    new, errors = dict(old), 0
    names = []
    for f in sorted(R.REPOS_DIR.glob("*.md")):
        if not f.name.startswith("_"):
            m, _ = G.parse_front_matter(f.read_text(encoding="utf-8"))
            if m.get("repo"):
                names.append(m["repo"])
    for repo in names:
        try:
            d = C.http_json(f"https://api.github.com/repos/{repo}", headers=headers)
        except C.FetchError as err:
            errors += 1
            print(f"UYARI: {repo} okunamadı: {err}", file=sys.stderr)
            continue
        new[repo] = {
            "stars": tr_stars(int(d.get("stargazers_count", 0))),
            "license": ((d.get("license") or {}).get("spdx_id")) or "YOK",
            "archived": bool(d.get("archived")),
            "pushed_at": (d.get("pushed_at") or "")[:10],
            "fetched_at": datetime.now(C.TZ).date().isoformat(),
        }
    for gone in set(new) - set(names):
        del new[gone]
    R.META_FILE.write_text(json.dumps(new, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{len(names)} depo kontrol edildi, {errors} hata.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
