#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""_validate.py — order 토큰 ↔ 데이터 필드 정적 검사 (blank-page 크래시 예방).
사용:  PYTHONIOENCODING=utf-8 python 40_build/_validate.py <slug>
각 섹션의 order 토큰마다 해당 데이터 필드가 실재하는지 확인. ASCII 한 줄 출력.
"""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
# 토큰 base -> 실제 필드명 (대부분 동일, 예외만 매핑)
FIELD = {"battlemap": "battlemaps"}

def main():
    slug = sys.argv[1].strip().strip("/")
    data = json.loads((ROOT/"30_content"/slug/"episode.json").read_text(encoding="utf-8"))
    issues = 0
    for s in data["sections"]:
        sid = s.get("id", "?")
        order = s.get("order") or []
        for tok in order:
            base = tok[:-1] if tok.endswith("*") else tok.split(":")[0]
            idx = None
            if ":" in tok:
                try: idx = int(tok.split(":")[1])
                except: pass
            field = FIELD.get(base, base)
            val = s.get(field)
            if val is None:
                print("MISSING slug=%s sec=%s token=%s field=%s" % (slug, sid, tok, field)); issues += 1
            elif idx is not None:
                if not isinstance(val, list) or idx >= len(val):
                    print("BADIDX slug=%s sec=%s token=%s len=%s" % (slug, sid, tok, (len(val) if isinstance(val, list) else "notlist"))); issues += 1
    print("VALIDATE_%s slug=%s sections=%d issues=%d" % ("OK" if issues == 0 else "FAIL", slug, len(data["sections"]), issues))
    sys.exit(0 if issues == 0 else 1)

if __name__ == "__main__":
    main()
