#!/usr/bin/env python3
"""build_people.py — 인물 도감 v2 빌더.

단일 소스(SSOT) = 30_content/people/people.json (에피소드에서 분리·승격).
출력:
  50_app/people/index.html            ← 색인(초상 카드, 인물별 페이지로 링크)
  50_app/people/<slug>/index.html     ← 인물별 상세 페이지(사진·다국어 이름·생애·연표·역링크·공식 링크·편지)
  50_app/people/img/<slug>.jpg        ← 초상 자산 복사(30_content/people/img/ 원본)

데이터↔엔진 분리: 인물을 늘리려면 people.json + img 만 추가하고 이 스크립트를 다시 돌린다.
역링크: 상세 페이지 related[] → /history/<ep>/#<section> (에피소드 SPA가 hash로 해당 섹션을 연다).
"""
import json, pathlib, shutil, sys, html as _html

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "30_content" / "people"
OUT = ROOT / "50_app" / "people"

# 에피소드 표시 순서(시대 사슬 순). related[].ep 로 그룹핑.
# 목록에 없는 ep 의 인물은 build_index 의 fallback 그룹으로 — 조용한 누락 금지.
EP_ORDER = ["exploration", "powers", "imperialism", "ww2",
            "americas/north-america", "americas/latin-america"]


def esc(s):
    return _html.escape(s or "", quote=True)


def load():
    data = json.loads((SRC / "people.json").read_text(encoding="utf-8"))
    return data.get("people", [])


# ---------- 공통 CSS ----------
CSS = """
  :root{--rose:#C98B8B;--rose-soft:#E8C8C5;--navy:#33406B;--cream:#FBF7F2;--paper:#FFFFFF;--ink:#2E2A28;--muted:#857B74;--line:#EBE0D5;--accent:#B5546A;--gold:#C49A4A;--shadow-sm:0 2px 10px rgba(51,64,107,.06);--shadow:0 6px 22px rgba(51,64,107,.09);}
  *{box-sizing:border-box;margin:0;padding:0;}
  body{font-family:'Pretendard','Apple SD Gothic Neo','Malgun Gothic',sans-serif;background:var(--cream);color:var(--ink);line-height:1.78;word-break:keep-all;-webkit-font-smoothing:antialiased;}
  a{color:inherit;}
  .hero{padding:50px 28px 38px;background:linear-gradient(140deg,var(--navy) 0%, #6a4a6e 100%);color:#fff;text-align:center;}
  .hero h1{font-size:29px;font-weight:800;line-height:1.3;}
  .hero .sub{font-size:14.5px;color:var(--rose-soft);margin-top:11px;}
  .backrow{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:18px;}
  .back{display:inline-block;color:#fff;font-size:12.5px;text-decoration:none;border:1px solid rgba(255,255,255,.3);border-radius:9px;padding:6px 13px;}
  .back:hover{background:rgba(255,255,255,.12);}
  .wrap{max-width:820px;margin:0 auto;padding:32px 22px 90px;}
  .intro{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px 22px;box-shadow:var(--shadow-sm);font-size:15.5px;margin-bottom:6px;}
  .intro b{color:var(--accent);}
  .eph{font-size:14px;letter-spacing:.04em;color:var(--accent);font-weight:800;margin:34px 0 14px;text-transform:uppercase;display:flex;align-items:center;gap:9px;}
  .eph::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--accent);}
  /* ---- 색인 카드 ---- */
  .people{display:grid;gap:14px;}
  @media(min-width:640px){.people{grid-template-columns:1fr 1fr;}}
  .pcard{display:flex;gap:14px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:15px;padding:14px 16px;box-shadow:var(--shadow-sm);text-decoration:none;color:inherit;transition:transform .12s,box-shadow .12s;}
  .pcard:hover{transform:translateY(-2px);box-shadow:var(--shadow);}
  .pcard .ph{flex:0 0 62px;width:62px;height:62px;border-radius:12px;object-fit:cover;object-position:top center;background:linear-gradient(135deg,var(--rose),var(--accent));border:1px solid var(--line);}
  .pcard .pname{font-size:16.5px;font-weight:800;color:var(--navy);}
  .pcard .pone{font-size:12.5px;color:var(--muted);margin-top:2px;}
  .pcard .pmeta{font-size:11.5px;color:var(--accent);margin-top:5px;font-weight:700;}
  .pcard .parrow{margin-left:auto;color:var(--rose);font-size:18px;align-self:center;}
  /* ---- 상세 ---- */
  .portrait{text-align:center;margin:4px 0 20px;}
  .portrait img{max-width:260px;width:60%;border-radius:14px;border:1px solid var(--line);box-shadow:var(--shadow);}
  .portrait figcaption{font-size:11.5px;color:var(--muted);margin-top:9px;line-height:1.6;}
  .portrait .note{display:block;color:var(--accent);margin-top:3px;}
  .panel{background:#fff;border:1px solid var(--line);border-radius:15px;padding:18px 20px;box-shadow:var(--shadow-sm);margin-bottom:14px;}
  .panel h2{font-size:14px;color:var(--accent);font-weight:800;margin-bottom:12px;letter-spacing:.02em;}
  .names{display:grid;gap:7px;}
  .names .row{display:flex;gap:10px;font-size:14.5px;align-items:baseline;}
  .names .k{flex:0 0 96px;color:var(--muted);font-size:12.5px;font-weight:700;}
  .names .v{font-weight:600;color:var(--ink);}
  .names .v.big{font-size:18px;color:var(--navy);font-weight:800;}
  .meta{font-size:13.5px;color:var(--muted);margin-bottom:14px;text-align:center;}
  .meta b{color:var(--navy);}
  .bio p{font-size:15.5px;margin-bottom:11px;}
  .bio p:last-child{margin-bottom:0;}
  .tl{list-style:none;border-left:2px solid var(--rose-soft);margin-left:6px;padding-left:16px;}
  .tl li{position:relative;margin-bottom:12px;font-size:14.5px;}
  .tl li::before{content:"";position:absolute;left:-22px;top:7px;width:9px;height:9px;border-radius:50%;background:var(--accent);}
  .tl .yr{font-weight:800;color:var(--navy);margin-right:7px;}
  .shadow{background:var(--cream);border-radius:11px;padding:13px 15px;font-size:14.5px;}
  .shadow .lbl{font-weight:800;color:var(--gold);margin-right:6px;}
  .rel{display:flex;flex-direction:column;gap:9px;}
  .rel a{display:flex;align-items:center;gap:9px;background:var(--cream);border:1px solid var(--line);border-radius:10px;padding:11px 14px;text-decoration:none;font-size:14.5px;font-weight:700;color:var(--navy);}
  .rel a:hover{border-color:var(--accent);}
  .rel .ep{font-size:11px;color:var(--accent);font-weight:800;}
  .rel .go{margin-left:auto;color:var(--rose);}
  .links{display:flex;flex-direction:column;gap:9px;}
  .links a{display:flex;align-items:center;gap:9px;text-decoration:none;font-size:14px;color:var(--navy);border:1px solid var(--line);border-radius:10px;padding:10px 13px;}
  .links a:hover{border-color:var(--accent);background:#fff;}
  .lang{flex:0 0 auto;font-size:10.5px;font-weight:800;letter-spacing:.03em;color:#fff;background:var(--navy);border-radius:6px;padding:2px 7px;}
  .lang.official,.lang.encyclopedia{background:var(--accent);}
  .links .ext{margin-left:auto;color:var(--muted);font-size:11px;}
  .reflect label{display:block;font-size:14.5px;margin-bottom:9px;}
  .reflect textarea{width:100%;min-height:96px;border:1px solid var(--line);border-radius:11px;padding:12px 14px;font-family:inherit;font-size:14.5px;line-height:1.7;resize:vertical;background:var(--cream);}
  .reflect textarea:focus{outline:none;border-color:var(--accent);background:#fff;}
  .saved{font-size:11.5px;color:var(--gold);font-weight:700;height:14px;margin-top:5px;}
"""

INDEX_TMPL = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>인물 도감 — 역사 이야기</title>
<meta name="description" content="역사 이야기 에피소드를 가로지르는 인물 도감. 사진·다국어 이름·생애·공식 링크까지 깊이 탐구.">
<style>__CSS__</style>
</head>
<body>
  <div class="hero">
    <h1>🖼️ 인물 도감</h1>
    <div class="sub">역사를 움직인 사람들 · 모두 __COUNT__명 · 카드를 누르면 깊이 탐구해요</div>
    <div class="backrow"><a class="back" href="../index.html">← 역사 이야기 허브</a></div>
  </div>
  <div class="wrap">
    <div class="intro">역사는 사건이 아니라 <b>사람</b>의 이야기예요. 사진을 보고, 그 나라 말로 이름을 읽어 보고, 한 사람의 삶을 따라가 보세요. 누구나 <b>빛과 그림자</b>를 함께 가지고 있답니다. (탐구학습 '인물 조사'에 바로 쓸 수 있어요.)</div>
    __BODY__
  </div>
</body>
</html>
"""

DETAIL_TMPL = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__NAME__ — 인물 도감</title>
<meta name="description" content="__ONELINE__">
<style>__CSS__</style>
</head>
<body>
  <div class="hero">
    <h1>__FACE__ __NAME__</h1>
    <div class="sub">__ALIAS____ONELINE__</div>
    <div class="backrow">
      <a class="back" href="../index.html">← 인물 도감</a>
      <a class="back" href="../../index.html">역사 허브</a>
    </div>
  </div>
  <div class="wrap">
__BODY__
  </div>
  <script>
  // '편지' 메모 자동 저장(앱 전체의 '빈칸 남기기' 원칙)
  (function(){var ta=document.getElementById('rf');if(!ta)return;var k='people_reflect___SLUG__';
   try{ta.value=localStorage.getItem(k)||'';}catch(e){}
   var tag=document.getElementById('rfsaved'),t;
   ta.addEventListener('input',function(){try{localStorage.setItem(k,ta.value);}catch(e){}
     tag.textContent='저장됨 ✓';clearTimeout(t);t=setTimeout(function(){tag.textContent='';},1300);});})();
  </script>
</body>
</html>
"""


def index_card(p):
    src = esc(p["portrait"]["src"])
    name = esc(p["names"]["ko"])
    one = esc(p.get("oneLine", ""))
    meta = esc(p.get("nationality", "")) + " · " + esc(p.get("lifespan", ""))
    return (
        '<a class="pcard" href="%s/index.html">' % esc(p["slug"])
        + '<img class="ph" src="%s" alt="%s" loading="lazy">' % (src, esc(p["portrait"].get("alt", name)))
        + '<div><div class="pname">%s</div><div class="pone">%s</div><div class="pmeta">%s</div></div>' % (name, one, meta)
        + '<div class="parrow">→</div></a>'
    )


def build_index(people):
    groups = []
    shown = set()
    for ep in EP_ORDER:
        grp = [p for p in people if p.get("related") and p["related"][0].get("ep") == ep]
        if not grp:
            continue
        shown.update(p["slug"] for p in grp)
        eplabel = grp[0]["related"][0].get("epLabel", ep)
        cards = "".join(index_card(p) for p in grp)
        groups.append('<h2 class="eph">에피소드 · %s</h2><div class="people">%s</div>' % (esc(eplabel), cards))
    rest = [p for p in people if p["slug"] not in shown]
    if rest:
        cards = "".join(index_card(p) for p in rest)
        groups.append('<h2 class="eph">그 밖의 인물</h2><div class="people">%s</div>' % cards)
        sys.stdout.write("  [warn] EP_ORDER fallback group: %d people\n" % len(rest))
    body = "\n".join(groups)
    page = INDEX_TMPL.replace("__CSS__", CSS).replace("__BODY__", body).replace("__COUNT__", str(len(people)))
    (OUT / "index.html").write_text(page, encoding="utf-8")


def detail_body(p):
    n = p["names"]
    parts = []
    # 초상
    src = "../" + p["portrait"]["src"]
    cap = esc(p["portrait"].get("source", ""))
    lic = esc(p["portrait"].get("license", ""))
    note = p["portrait"].get("note", "")
    fig = '<figure class="portrait"><img src="%s" alt="%s">' % (esc(src), esc(p["portrait"].get("alt", n["ko"])))
    capline = cap + (" · " + lic if lic else "")
    fig += '<figcaption>출처: %s' % capline
    if note:
        fig += '<span class="note">%s</span>' % esc(note)
    fig += '</figcaption></figure>'
    parts.append(fig)

    # 이름 블록
    rows = ['<div class="row"><span class="k">한국어</span><span class="v big">%s</span></div>' % esc(n["ko"])]
    if n.get("native"):
        rows.append('<div class="row"><span class="k">원어</span><span class="v">%s</span></div>' % esc(n["native"]))
    if n.get("pronun_ko"):
        rows.append('<div class="row"><span class="k">실제 발음</span><span class="v">%s</span></div>' % esc(n["pronun_ko"]))
    if n.get("roman"):
        rows.append('<div class="row"><span class="k">로마자</span><span class="v">%s</span></div>' % esc(n["roman"]))
    if n.get("en"):
        rows.append('<div class="row"><span class="k">영어권</span><span class="v">%s</span></div>' % esc(n["en"]))
    if n.get("alias"):
        rows.append('<div class="row"><span class="k">별칭</span><span class="v">%s</span></div>' % esc(n["alias"]))
    parts.append('<div class="panel"><h2>이름</h2><div class="names">%s</div></div>' % "".join(rows))

    # 메타
    parts.append('<div class="meta"><b>%s</b> · %s</div>' % (esc(p.get("nationality", "")), esc(p.get("lifespan", ""))))

    # 생애
    bio = "".join("<p>%s</p>" % esc(par) for par in p.get("bio", []))
    parts.append('<div class="panel bio"><h2>생애</h2>%s</div>' % bio)

    # 연표
    if p.get("personTimeline"):
        items = "".join('<li><span class="yr">%s</span>%s</li>' % (esc(e.get("yr", "")), esc(e.get("t", ""))) for e in p["personTimeline"])
        parts.append('<div class="panel"><h2>연표</h2><ul class="tl">%s</ul></div>' % items)

    # 빛과 그림자
    if p.get("lightShadow"):
        parts.append('<div class="panel"><div class="shadow"><span class="lbl">빛과 그림자</span>%s</div></div>' % esc(p["lightShadow"]))

    # 관련 에피소드 역링크
    if p.get("related"):
        rl = []
        for r in p["related"]:
            href = "../../%s/index.html#%s" % (esc(r.get("ep", "")), esc(r.get("section", "")))
            rl.append('<a href="%s"><span><span class="ep">%s</span><br>%s</span><span class="go">→ 이야기로</span></a>'
                      % (href, esc(r.get("epLabel", "")), esc(r.get("label", ""))))
        parts.append('<div class="panel"><h2>이 인물이 나오는 이야기</h2><div class="rel">%s</div></div>' % "".join(rl))

    # 더 알아보기 링크
    if p.get("links"):
        ll = []
        for l in p["links"]:
            badge = esc(l.get("lang", ""))
            ll.append('<a href="%s" target="_blank" rel="noopener"><span class="lang %s">%s</span>%s<span class="ext">↗</span></a>'
                      % (esc(l.get("url", "")), esc(l.get("type", "")), badge, esc(l.get("label", ""))))
        parts.append('<div class="panel"><h2>더 알아보기 (공식·신뢰할 수 있는 링크)</h2><div class="links">%s</div></div>' % "".join(ll))

    # 편지(reflect)
    if p.get("reflect"):
        parts.append('<div class="panel reflect"><h2>이 인물에게 편지</h2><label>%s</label>'
                     '<textarea id="rf" placeholder="여기에 네 생각을 적어 보세요. 자동으로 저장돼요."></textarea>'
                     '<div class="saved" id="rfsaved"></div></div>' % esc(p["reflect"]))
    return "\n".join(parts)


def build_detail(p):
    d = OUT / p["slug"]
    d.mkdir(parents=True, exist_ok=True)
    alias = p["names"].get("alias", "")
    alias_html = ('“%s” · ' % esc(alias)) if alias else ""
    page = (DETAIL_TMPL
            .replace("__CSS__", CSS)
            .replace("__NAME__", esc(p["names"]["ko"]))
            .replace("__FACE__", esc(p.get("face", "👤")))
            .replace("__ALIAS__", alias_html)
            .replace("__ONELINE__", esc(p.get("oneLine", "")))
            .replace("__SLUG__", esc(p["slug"]))
            .replace("__BODY__", detail_body(p)))
    (d / "index.html").write_text(page, encoding="utf-8")


def copy_assets():
    img_src = SRC / "img"
    if img_src.is_dir():
        img_dst = OUT / "img"
        if img_dst.exists():
            shutil.rmtree(img_dst)
        shutil.copytree(img_src, img_dst)


def build():
    people = load()
    OUT.mkdir(parents=True, exist_ok=True)
    copy_assets()
    build_index(people)
    for p in people:
        build_detail(p)
    print("built people gallery: index + %d detail pages -> %s" % (len(people), OUT))
    for p in people:
        print("  /history/people/%s/" % p["slug"])


if __name__ == "__main__":
    build()
