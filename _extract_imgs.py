import re
import pathlib

pat = re.compile(r"(?:src|href|data-lazy-src|data-mfp-src|content)=[\"']([^\"']+\.(?:png|jpg|jpeg|webp|gif))")
pat2 = re.compile(r"url\((?:&quot;|\"|')?([^)\"']+\.(?:png|jpg|jpeg|webp|gif))")
for p in ["index.html", "academy/index.html", "holding/index.html"]:
    t = pathlib.Path(p).read_text(encoding="utf-8", errors="ignore")
    urls = set(pat.findall(t)) | set(pat2.findall(t))
    print("===", p, len(urls))
    for u in sorted(urls):
        print(u)
