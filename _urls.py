import json
import re
from pathlib import Path

t = Path("ecosystem/index.html").read_text(encoding="utf-8")
m = re.search(r"var et_link_options_data = (\[.*?\]);", t)
data = json.loads(m.group(1))
bad = [item["url"] for item in data if re.search(r"broccoli", item["url"], re.I)]
Path("_urls.txt").write_text("\n".join(bad) if bad else "none", encoding="utf-8")
print("cards", len(data), "bad", len(bad))
# sample a few destinations
sample = [data[i]["url"] for i in (2, 3, 4, 20, 21)]
Path("_urls.txt").write_text("\n".join(sample + ["---"] + bad), encoding="utf-8")
