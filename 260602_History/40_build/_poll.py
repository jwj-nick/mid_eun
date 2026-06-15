# -*- coding: utf-8 -*-
# Generic live G3 poll.  Usage: python _poll.py <slug> marker1 marker2 ...
import sys, time, urllib.request
slug = sys.argv[1]; markers = sys.argv[2:]
URL = "https://jwj-nick.github.io/history/%s/index.html" % slug
for attempt in range(1, 14):
    try:
        req = urllib.request.Request(URL + "?cb=%d" % (2000+attempt),
              headers={"User-Agent":"poll/1.0","Cache-Control":"no-cache"})
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8","ignore")
        miss = [m for m in markers if m not in html]
        print("attempt %d: status=%d size=%d miss=%s" % (attempt, r.status, len(html), miss))
        if not miss:
            print("G3 PASS — %s all %d markers live" % (slug, len(markers))); break
    except Exception as e:
        print("attempt %d: err %s" % (attempt, e))
    time.sleep(12)
else:
    print("G3 NOT YET — %s still missing after retries" % slug)
