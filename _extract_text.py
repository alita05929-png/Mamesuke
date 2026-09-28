import re
import pathlib

for p in [
    pathlib.Path("index.html"),
    pathlib.Path("academy/index.html"),
    pathlib.Path("holding/index.html"),
    pathlib.Path("ecosystem/index.html"),
]:
    t = p.read_text(encoding="utf-8", errors="ignore")
    texts = re.findall(r'et_pb_text_inner">(.*?)</div>', t, flags=re.S)
    print("========", p)
    for i, x in enumerate(texts):
        x = re.sub(r"<[^>]+>", " ", x)
        x = re.sub(r"\s+", " ", x).strip()
        if x:
            print(f"[{i}] {x[:700]}")
