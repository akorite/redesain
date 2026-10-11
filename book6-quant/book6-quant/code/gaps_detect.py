"""Find missing bars by timestamp arithmetic, not by eyeballing."""
import csv, numpy as np
# build 1m bars then delete some to simulate a feed outage
tr=[]
with open("data/btc_trades.csv") as fh:
    reader=csv.reader(fh); next(reader,None)
    for row in reader: tr.append((float(row[2]),float(row[0])))
bars=sorted({int(t//60*60) for t,p in tr})
# simulate dropped feed: drop a 3-minute window
i=len(bars)//2
gone=set(bars[i-1:i+2])
have=[b for b in bars if b not in gone]
full=list(range(bars[0],bars[-1]+60,60))
missing=sorted(set(full)-set(have))
print(f"expected {len(full)} 1m slots, have {len(have)}, missing {len(missing)}")
print(f"outage window: {missing[0]} .. {missing[-1]} ({len(missing)} bars)")
print("rule: forward-fill l>c? never fill price; mark bar as gap and exclude from returns")
