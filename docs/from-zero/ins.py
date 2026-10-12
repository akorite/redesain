"""insert(path, anchor, tag, text): idempotently insert `text` before the first line starting with `anchor`."""
import re, pathlib
def insert(path, anchor, tag, text):
    p = pathlib.Path(path); s = p.read_text()
    b, e = f"% from-zero:{tag}:begin", f"% from-zero:{tag}:end"
    s = re.sub(re.escape(b) + r".*?" + re.escape(e) + r"\n\n?", "", s, flags=re.S)
    i = s.find("\n" + anchor)
    if i < 0:
        raise SystemExit(f"anchor not found in {path}: {anchor}")
    i += 1
    s = s[:i] + b + "\n" + text.strip("\n") + "\n" + e + "\n\n" + s[i:]
    p.write_text(s)
