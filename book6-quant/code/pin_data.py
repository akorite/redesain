"""Snapshot methodology: pin data, record hash + fetch time."""
import hashlib, json, os
p="data/btc_trades.csv"
h=hashlib.sha256(open(p,"rb").read()).hexdigest()
meta={"file":p,"sha256":h,"bytes":os.path.getsize(p)}
print(f"sha256 {h[:16]}...  bytes {meta['bytes']}")
print("rule: every quoted number in the chapter reproduces from the pinned file offline")
