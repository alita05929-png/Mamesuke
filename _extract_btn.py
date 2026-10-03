import pathlib
t = pathlib.Path("index.html").read_text(encoding="utf-8", errors="ignore")
keys = [
    "et_pb_fullwidth_header_0.et_pb_fullwidth_header",
    "header_overlay",
    ".et_pb_button",
]
# print chunks around button color for header
idx = t.find("et_pb_fullwidth_header_0.et_pb_fullwidth_header .et_pb_button")
print("idx", idx)
print(t[idx:idx+800] if idx>0 else "none")
idx2 = t.find("fullwidth_header_overlay")
print("--- overlay", idx2)
print(t[idx2-100:idx2+300] if idx2>0 else "none")
