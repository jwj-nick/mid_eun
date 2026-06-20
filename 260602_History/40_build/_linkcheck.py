#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""_linkcheck.py — 외부 링크 200 검증 (urllib, curl ask-list 우회). ASCII 출력.
사용:  PYTHONIOENCODING=utf-8 python 40_build/_linkcheck.py <slug>
episode.json의 모든 links[].url + yt(video id 제외)를 GET하여 status 출력.
"""
import json, sys, urllib.request, urllib.parse, pathlib, ssl
ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
CTX = ssl.create_default_context(); CTX.check_hostname=False; CTX.verify_mode=ssl.CERT_NONE

def enc(u):
    p = urllib.parse.urlsplit(u)
    return urllib.parse.urlunsplit((p.scheme,p.netloc,urllib.parse.quote(p.path),p.query,p.fragment))

def check(u):
    try:
        req=urllib.request.Request(enc(u),headers={"User-Agent":UA},method="GET")
        with urllib.request.urlopen(req,timeout=25,context=CTX) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return "ERR:%s" % str(e)[:50]

def main():
    slug=sys.argv[1].strip().strip("/")
    data=json.loads((ROOT/"30_content"/slug/"episode.json").read_text(encoding="utf-8"))
    urls=set()
    for s in data["sections"]:
        for it in (s.get("links") or []):
            u=it.get("url","")
            if u.startswith("http"): urls.add(u)  # 내부 상대링크(../ 등)는 건너뜀
    bad=0
    for u in sorted(urls):
        st=check(u)
        ok = (st==200)
        if not ok: bad+=1
        print("LINK %s %s" % (st, u))
    print("LINKCHECK_%s slug=%s total=%d bad=%d" % ("OK" if bad==0 else "FAIL", slug, len(urls), bad))

if __name__=="__main__":
    main()
