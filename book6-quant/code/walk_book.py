"""ch03 WE1: a market order walking the book -> slippage vs mid."""
from lob import Book

B = Book()
levels_bid = [(99.0, 5), (99.5, 3), (100.0, 4)]
levels_ask = [(100.5, 2), (101.0, 3), (101.5, 6), (102.5, 10)]
for p, q in levels_bid: B.add("b", p, q)
for p, q in levels_ask: B.add("s", p, q)
mid0 = B.mid()
n = len(B.trades)
B.market("b", 9)                     # market buy 9
fills = B.trades[n:]
tot = sum(q for _, q, _ in fills)
cost = sum(p * q for p, q, _ in fills)
avg = cost / tot
print("book: bids", levels_bid, "asks", levels_ask)
print(f"mid before = {mid0}")
print("fills:", fills)
print(f"filled {tot} at avg {avg:.4f}  vs mid {mid0}")
print(f"slippage = {avg - mid0:+.4f}/unit = {100*(avg/mid0-1):+.3f}%")
print(f"posted spread was {100.5-100.0}; paid avg above best ask by {avg-100.5:+.4f}")
