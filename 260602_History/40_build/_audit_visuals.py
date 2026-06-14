# -*- coding: utf-8 -*-
# Measure representative-image coverage across all episodes. Writes ASCII report to file.
import io, os, json

ROOT = os.path.join(os.path.dirname(__file__), "..", "30_content")
SKIP = {"people"}  # people gallery is separate subsystem

def img_count(s):
    """count representative images in an image block (single dict=1, array=len)"""
    v = s.get("image")
    if v is None: return 0
    if isinstance(v, list): return len([x for x in v if isinstance(x, dict) and x.get("src")])
    if isinstance(v, dict): return 1 if v.get("src") else 0
    return 0

def has(s, key):
    v = s.get(key)
    if v is None: return 0
    if isinstance(v, list): return len(v)
    return 1

lines = []
order = ["ww2","imperialism","renaissance","exploration","powers","revolutions",
         "north-america","latin-america","coldwar","globalization","new-order"]
# discover any not in order
all_eps = [d for d in sorted(os.listdir(ROOT)) if os.path.isdir(os.path.join(ROOT,d)) and d not in SKIP]
for d in all_eps:
    if d not in order: order.append(d)

total_sec=0; under=0
for slug in order:
    p = os.path.join(ROOT, slug, "episode.json")
    if not os.path.exists(p): continue
    doc = json.load(io.open(p, encoding="utf-8"))
    secs = doc.get("sections", [])
    lines.append("\n### %s  (%d sections)" % (slug, len(secs)))
    for s in secs:
        total_sec += 1
        ic = img_count(s)
        om = has(s,"oldmap")
        bm = has(s,"battlemaps")
        mp = has(s,"map")
        ch = has(s,"chart")
        rep = ic + om  # representative-image-ish (photo/artwork + old map)
        flag = ""
        if rep < 2:
            under += 1
            flag = "  <-- NEEDS +%d" % (2-rep)
        lines.append("  - %-20s img=%d oldmap=%d | (map=%d battlemap=%d chart=%d)%s"
                     % (s.get("id","?"), ic, om, mp, bm, ch, flag))

head = "VISUAL COVERAGE AUDIT — representative images (image + oldmap) per section\n"
head += "total sections=%d | sections with <2 representative images=%d\n" % (total_sec, under)
out = os.path.join(os.path.dirname(__file__), "_visual_audit.txt")
io.open(out,"w",encoding="utf-8").write(head + "\n".join(lines) + "\n")
print("wrote", out)
print(head)
