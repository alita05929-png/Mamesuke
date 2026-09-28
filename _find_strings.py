import pathlib
import re

needles = [
    "人民",
    "People",
    "people",
    "Broccoli",
    "broccoli",
    "BROCCOLI",
    "0x12",
    "0xdb25",
    "firstbroccoli",
]
files = list(pathlib.Path(".").rglob("*.html"))
out = []
for p in files:
    t = p.read_text(encoding="utf-8", errors="ignore")
    for n in needles:
        if n in t:
            out.append(f"{p}: {n} x{t.count(n)}")
pathlib.Path("_strings.txt").write_text("\n".join(out), encoding="utf-8")
print("wrote", len(out))
