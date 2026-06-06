#!/usr/bin/env python3
"""build_people.py — 모든 에피소드의 '꼭 알아야 할 인물'을 모아 /history/people/ 색인 페이지로 렌더.

사용:  python 40_build/build_people.py
입력:  30_content/<slug>/episode.json (각 섹션 people[] + 최상위 people[] 자동 수집)
출력:  50_app/people/index.html  (자기완결 단일 파일, 허브 사이드바에서 링크)

새 에피소드가 늘어도 이 스크립트만 다시 돌리면 인물 색인이 자동 갱신된다(데이터↔엔진 분리).
"""
import json, pathlib, html as _html

ROOT = pathlib.Path(__file__).resolve().parent.parent
# (slug, 표시용 에피소드 라벨) — 이야기 순서
EPISODES = [
    ("ww2", "에피소드 01 · 세계대전 이야기"),
    ("imperialism", "에피소드 02 · 제국주의와 19세기"),
]

def collect(slug):
    data = json.loads((ROOT / "30_content" / slug / "episode.json").read_text(encoding="utf-8"))
    out = []
    for sec in data.get("sections", []):
        for p in sec.get("people", []):
            out.append((sec.get("label", ""), p))
    for p in data.get("people", []):
        out.append(("", p))
    return out

def esc(s):
    return _html.escape(s or "", quote=True)

def person_card(label, p):
    parts = ['<div class="person">']
    parts.append('<div class="pheader"><div class="pface">' + esc(p.get("face", "👤")) + '</div>')
    parts.append('<div><div class="pname">' + esc(p.get("name", "")) + '</div>')
    who = esc(p.get("who", ""))
    if label:
        who = (who + ' · ' if who else '') + '<span class="ptag">' + esc(label) + '</span>'
    parts.append('<div class="pwho">' + who + '</div></div></div>')
    if p.get("why"):
        parts.append('<div class="pwhy">' + esc(p["why"]) + '</div>')
    if p.get("quote"):
        parts.append('<div class="pquote">"' + esc(p["quote"]) + '"</div>')
    if p.get("shadow"):
        parts.append('<div class="pshadow">빛과 그림자 · ' + esc(p["shadow"]) + '</div>')
    parts.append('</div>')
    return ''.join(parts)

def build():
    groups = []
    total = 0
    for slug, eplabel in EPISODES:
        people = collect(slug)
        if not people:
            continue
        cards = ''.join(person_card(lbl, p) for lbl, p in people)
        groups.append('<h2 class="eph">' + esc(eplabel) + '</h2><div class="people">' + cards + '</div>')
        total += len(people)

    body = '\n'.join(groups)
    page = TEMPLATE.replace("__BODY__", body).replace("__COUNT__", str(total))
    out_dir = ROOT / "50_app" / "people"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(page, encoding="utf-8")
    print("built %s  (%d people)" % (out_dir / "index.html", total))

TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>인물 도감 — 역사 이야기</title>
<meta name="description" content="역사 이야기 에피소드를 가로지르는 '꼭 알아야 할 인물' 색인.">
<style>
  :root{--rose:#C98B8B;--rose-soft:#E8C8C5;--navy:#33406B;--cream:#FBF7F2;--paper:#FFFFFF;--ink:#2E2A28;--muted:#857B74;--line:#EBE0D5;--accent:#B5546A;--gold:#C49A4A;--shadow-sm:0 2px 10px rgba(51,64,107,.06);--shadow:0 6px 22px rgba(51,64,107,.09);}
  *{box-sizing:border-box;margin:0;padding:0;}
  body{font-family:'Pretendard','Apple SD Gothic Neo','Malgun Gothic',sans-serif;background:var(--cream);color:var(--ink);line-height:1.78;word-break:keep-all;-webkit-font-smoothing:antialiased;}
  .hero{padding:54px 28px 40px;background:linear-gradient(140deg,var(--navy) 0%, #6a4a6e 100%);color:#fff;text-align:center;}
  .hero h1{font-size:30px;font-weight:800;}
  .hero .sub{font-size:14.5px;color:var(--rose-soft);margin-top:11px;}
  .back{display:inline-block;margin:18px auto 0;color:#fff;font-size:12.5px;text-decoration:none;border:1px solid rgba(255,255,255,.3);border-radius:9px;padding:6px 13px;}
  .back:hover{background:rgba(255,255,255,.12);}
  .wrap{max-width:820px;margin:0 auto;padding:34px 22px 90px;}
  .intro{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px 22px;box-shadow:var(--shadow-sm);font-size:15.5px;margin-bottom:10px;}
  .intro b{color:var(--accent);}
  .eph{font-size:14px;letter-spacing:.04em;color:var(--accent);font-weight:800;margin:34px 0 14px;text-transform:uppercase;display:flex;align-items:center;gap:9px;}
  .eph::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--accent);}
  .people{display:grid;gap:14px;}
  @media(min-width:640px){.people{grid-template-columns:1fr 1fr;}}
  .person{background:#fff;border:1px solid var(--line);border-radius:15px;padding:18px 20px;box-shadow:var(--shadow-sm);}
  .person .pheader{display:flex;gap:13px;align-items:center;margin-bottom:8px;}
  .person .pface{flex:0 0 46px;height:46px;border-radius:12px;background:linear-gradient(135deg,var(--rose),var(--accent));display:flex;align-items:center;justify-content:center;font-size:22px;color:#fff;}
  .person .pname{font-size:16.5px;font-weight:800;color:var(--navy);}
  .person .pwho{font-size:12px;color:var(--muted);}
  .person .pwho .ptag{background:var(--cream);border:1px solid var(--line);border-radius:6px;padding:1px 6px;font-weight:700;color:var(--navy);}
  .person .pwhy{font-size:14.5px;margin-bottom:8px;}
  .person .pquote{font-size:14px;font-style:italic;color:var(--accent);border-left:3px solid var(--rose-soft);padding-left:10px;margin:8px 0;}
  .person .pshadow{font-size:13.5px;color:var(--muted);background:var(--cream);border-radius:9px;padding:8px 11px;}
</style>
</head>
<body>
  <div class="hero">
    <h1>🖼️ 인물 도감</h1>
    <div class="sub">역사 이야기를 가로지르는 '꼭 알아야 할 사람들' · 모두 __COUNT__명</div>
    <a class="back" href="../index.html">← 역사 이야기 허브</a>
  </div>
  <div class="wrap">
    <div class="intro">역사는 사건이 아니라 <b>사람</b>의 이야기예요. 여러 에피소드에 등장한 인물을 한곳에 모았어요. 누구나 <b>빛과 그림자</b>를 함께 가지고 있다는 걸 기억하며 읽어 보세요. (탐구학습 '인물 조사'에 바로 쓸 수 있어요.)</div>
    __BODY__
  </div>
</body>
</html>
"""

if __name__ == "__main__":
    build()
