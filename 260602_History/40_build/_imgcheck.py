# -*- coding: utf-8 -*-
import urllib.request
base = "https://jwj-nick.github.io/history/korea/modern/img/"
imgs = ["incheon_port.jpg","independence_gate.jpg","hague_emissaries.png","declaration_1919.jpg",
        "provisional_gov.jpg","liberation_1945.jpg"]
ok = 0
for f in imgs:
    try:
        req = urllib.request.Request(base+f+"?cb=1", headers={"User-Agent":"chk/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            print("%d %7d %s" % (r.status, len(r.read()), f)); ok += (r.status==200)
    except Exception as e:
        print("ERR %s %s" % (f, e))
print("IMG_LIVE %d/%d" % (ok, len(imgs)))
