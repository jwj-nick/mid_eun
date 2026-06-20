#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""_imgfetch.py — Wikimedia Commons 이미지 후보 수집 (PD/CC만). ASCII 매니페스트 출력.
스펙은 코드 하단 TARGETS에. 다운로드는 _stage/img_cand/<target>__<i>.<ext>. 검수 후 수동 채택.
"""
import json, sys, time, urllib.request, urllib.parse, pathlib, ssl
ROOT = pathlib.Path(__file__).resolve().parent.parent
STAGE = ROOT/"40_build"/"_stage"/"img_cand"
STAGE.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
CTX = ssl.create_default_context()
OK_LIC = ("public domain","pd-","cc0","cc by","cc-by","attribution","share")
BAD_EXT = (".svg",".pdf",".tif",".tiff",".gif",".webp")

def api(query):
    params = {"action":"query","format":"json","generator":"search","gsrsearch":query,
              "gsrnamespace":"6","gsrlimit":"8","prop":"imageinfo",
              "iiprop":"url|extmetadata|mime","iiurlwidth":"1000"}
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent":UA})
    with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
        return json.loads(r.read().decode("utf-8"))

def lic_of(em):
    for k in ("LicenseShortName","License","UsageTerms","Copyrighted"):
        v = em.get(k,{}).get("value","") if isinstance(em.get(k),dict) else ""
        if v:
            low=v.lower()
            if any(t in low for t in OK_LIC): return v
    # fallback: any field mentioning PD/CC
    for k,vd in em.items():
        v = vd.get("value","") if isinstance(vd,dict) else ""
        low = str(v).lower()
        if any(t in low for t in OK_LIC): return str(v)[:60]
    return ""

def fetch(target, queries):
    seen=set(); n=0
    for q in queries:
        try: d=api(q)
        except Exception as e:
            print("ERR target=%s q=%r %s" % (target,q,e)); continue
        pages=(d.get("query",{}) or {}).get("pages",{}) or {}
        for p in pages.values():
            ii=(p.get("imageinfo") or [{}])[0]
            mime=ii.get("mime",""); thumb=ii.get("thumburl") or ii.get("url","");
            title=p.get("title","")
            if not thumb or title in seen: continue
            seen.add(title)
            em=ii.get("extmetadata",{}) or {}
            lic=lic_of(em)
            ext="."+thumb.rsplit(".",1)[-1].lower().split("?")[0]
            if ext in BAD_EXT or "image" not in mime:
                print("SKIP target=%s mime=%s ext=%s title=%s" % (target,mime,ext,title[:50])); continue
            if not lic:
                print("NOLIC target=%s title=%s" % (target,title[:50])); continue
            local=STAGE/("%s__%d%s" % (target,n,ext if ext in (".jpg",".jpeg",".png") else ".jpg"))
            try:
                req=urllib.request.Request(thumb, headers={"User-Agent":UA})
                with urllib.request.urlopen(req,timeout=40,context=CTX) as r: blob=r.read()
                local.write_bytes(blob)
                print("CAND target=%s idx=%d file=%s bytes=%d mime=%s lic=%s title=%s" %
                      (target,n,local.name,len(blob),mime,lic[:30],title[:55]))
                n+=1
                time.sleep(1.5)
            except Exception as e:
                print("DLERR target=%s title=%s %s" % (target,title[:40],e))
                time.sleep(1.5)
            if n>=3: break
        time.sleep(1.0)
        if n>=3: break
    print("DONE target=%s candidates=%d" % (target,n))

TARGETS = [
 ("osanfortress", ["Wunü Mountain City", "오녀산성", "Five Maiden Peak fortress Goguryeo", "Wunu Shan Goguryeo"]),
 ("janggun",      ["Janggun-chong", "General's Tomb Goguryeo", "장군총", "Tomb of the General Ji'an"]),
 ("tangmap",      ["Tang dynasty map 700", "Tang dynasty greatest extent", "당나라 지도", "Tang Empire 660 map"]),
]
for t,qs in TARGETS:
    fetch(t,qs)
print("ALLDONE stage=%s" % STAGE)
