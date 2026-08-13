# -*- coding: utf-8 -*-
"""get_empty_siteshot.py - 输出 siteshot 为空的可达友链（逗号分隔，供增量截图用）"""

import json
import sys

try:
    with open("result.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except Exception:
    sys.exit(0)

links = [
    e.get("link", "")
    for e in data.get("link_status", [])
    if e.get("latency", -1) > 0 and not (e.get("siteshot") or "").strip()
]
print(",".join(links))
