"""Video planındaki her videonun rehberi var mı ve zamanında yayında mı, kontrol eder.

Çıkış kodu: 0 sorun yok · 1 geciken rehber var · 2 planda olmayan bir rehbere bağlanmış video var.
GITHUB_STEP_SUMMARY tanımlıysa tabloyu Actions özetine de yazar.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402
import guides as G  # noqa: E402

LEAD_DAYS = 1      # rehber, videodan en geç bu kadar gün önce yayında olmalı
WARN_DAYS = 7      # bu kadar gün kala uyar


def check(today: date | None = None) -> tuple[int, list[dict]]:
    today = today or datetime.now(C.TZ).date()
    plan = json.loads((C.DATA_DIR / "plan.json").read_text(encoding="utf-8"))
    guides, _ = G.load(C.load_config(), include_drafts=True, today=today)
    by_slug = {g["slug"]: g for g in guides}
    rows, code = [], 0
    for v in plan["videos"]:
        g = by_slug.get(v["guide"])
        deadline = date.fromisoformat(v["date"]) - timedelta(days=LEAD_DAYS)
        if not g:
            state, code = "REHBER YOK", 2
        elif not g["draft"]:
            state = "yayında"
        elif today > deadline:
            state = "GECİKTİ"
            code = max(code, 1)
        elif (deadline - today).days <= WARN_DAYS:
            state = "yaklaşıyor" + (" (iskelet)" if g["stage"] == "iskelet" else " (onay bekliyor)")
        else:
            state = "iskelet" if g and g["stage"] == "iskelet" else "onay bekliyor"
        rows.append({**v, "deadline": deadline.isoformat(), "state": state})
    return code, rows


def main() -> int:
    code, rows = check()
    lines = ["| Video | Tarih | Rehber | Son gün | Durum |", "| --- | --- | --- | --- | --- |"]
    lines += [f"| {r['code']} | {r['date']} | {r['guide']} | {r['deadline']} | {r['state']} |" for r in rows]
    table = "\n".join(lines)
    print(table)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write("## Video ve rehber planı\n\n" + table + "\n")
    late = [r for r in rows if r["state"] in ("GECİKTİ", "REHBER YOK")]
    if late:
        print("\nSorunlu: " + ", ".join(f"{r['code']} → {r['guide']} ({r['state']})" for r in late), file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(main())
