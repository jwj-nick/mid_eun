#!/usr/bin/env python3
"""build.py — Episode Content Schema(JSON) + 표준 템플릿 → 자기완결형 단일 HTML.

사용:  python 40_build/build.py <slug>     (기본 slug=ww2)
입력:  30_content/<slug>/episode.json , 40_build/templates/episode.html
출력:  50_app/<slug>/index.html  (더블클릭/Pages 모두 동작하는 단일 파일)
"""
import json, sys, pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLACEHOLDER = "/*__EPISODE_DATA__*/ null"

def build(slug):
    data_path = ROOT / "30_content" / slug / "episode.json"
    tpl_path  = ROOT / "40_build" / "templates" / "episode.html"
    out_dir   = ROOT / "50_app" / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    data = json.loads(data_path.read_text(encoding="utf-8"))
    meta = data["meta"]
    tpl  = tpl_path.read_text(encoding="utf-8")

    if PLACEHOLDER not in tpl:
        raise SystemExit("템플릿에 데이터 주입 지점이 없습니다: " + PLACEHOLDER)

    data_js = json.dumps(data, ensure_ascii=False)
    html = (tpl
            .replace("__TITLE__", meta.get("title", ""))
            .replace("__DESC__",  meta.get("description", ""))
            .replace(PLACEHOLDER, data_js))

    out = out_dir / "index.html"
    out.write_text(html, encoding="utf-8")
    print("built %s  (%d sections, %d bytes)" % (out, len(data["sections"]), len(html)))

    # 정적 자산(이미지) 복사: 30_content/<slug>/img → 50_app/<slug>/img
    # (image 블록이 참조하는 PD 역사지도 등. 배포 시 index.html과 함께 옮긴다.)
    img_src = ROOT / "30_content" / slug / "img"
    if img_src.is_dir():
        img_dst = out_dir / "img"
        if img_dst.exists():
            shutil.rmtree(img_dst)
        shutil.copytree(img_src, img_dst)
        print("  copied img/ (%d files)" % sum(1 for _ in img_src.iterdir()))

if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "ww2")
