import re
import pathlib

t = pathlib.Path("index.html").read_text(encoding="utf-8", errors="ignore")
# find background urls
for m in re.finditer(r".{80}(bone_bg|cyberpunk-city|fullwidth_header_0).{200}", t):
    s = m.group(0)
    if "et_pb_fullwidth_header_0{" in s or "bone_bg" in s or "cyberpunk" in s:
        print("---")
        print(s[:400])
        print()
