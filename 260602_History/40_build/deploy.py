#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""deploy.py — 견고한 멱등 배포 (셸 cp -r 대체).
사용:  python 40_build/deploy.py <slug>     예) tracks/sci-tech
동작:  50_app/<slug>  →  C:/Nick/30_Apps/jwj-nick.github.io/history/<slug>
       shutil로 복사(교차-경계 안전) + 파일 수 자가검증 + ASCII 한 줄 출력.
이유:  셸 cp -r 가 작업디렉토리(C:/Kids) 밖(C:/Nick)으로 복사할 때
       결과 손실·부분복사가 반복됨. shutil은 멱등·검증 가능. run_in_background 권장.
"""
import sys, shutil, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEPLOY_HISTORY = pathlib.Path("C:/Nick/30_Apps/jwj-nick.github.io/history")

def count_files(p):
    return sum(1 for x in p.rglob("*") if x.is_file())

def main():
    if len(sys.argv) < 2:
        print("USAGE deploy.py <slug>"); sys.exit(2)
    slug = sys.argv[1].strip().strip("/")
    src = ROOT / "50_app" / slug
    dst = DEPLOY_HISTORY / slug
    if not src.is_dir():
        print("SRC_MISSING %s" % src); sys.exit(1)
    n_src = count_files(src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    n_dst = count_files(dst)
    ok = "OK" if n_dst == n_src else "MISMATCH"
    print("DEPLOY_%s slug=%s src=%d dst=%d" % (ok, slug, n_src, n_dst))
    sys.exit(0 if ok == "OK" else 1)

if __name__ == "__main__":
    main()
