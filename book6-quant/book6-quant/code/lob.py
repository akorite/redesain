"""ch03: a price-level limit order book with price-time priority."""
from collections import deque

class Book:
    def __init__(self):
        self.bids, self.asks = {}, {}   # price -> deque of (qty, order_id)
        self.trades = []                # (price, qty, taker_side)
    def _side(self, s): return self.bids if s == "b" else self.asks
    def add(self, side, price, qty):
        """limit order: rest if not marketable, else match."""
        opp = self.asks if side == "b" else self.bids
        while qty > 0 and opp:
            best = max(opp) if side == "s" else min(opp)
            if (side == "b" and best > price) or (side == "s" and best < price):
                break
            q = opp[best]
            take = min(qty, sum(x for x, _ in q))
            while take > 0 and q:
                q0, oid = q[0]
                f = min(take, q0)
                self.trades.append((best, f, side))
                take -= f; qty -= f
                if f == q0: q.popleft()
                else: q[0] = (q0 - f, oid)
            if not q: del opp[best]
        if qty > 0:
            self._side(side).setdefault(price, deque()).append((qty, id(self.trades)))
        return qty
    def market(self, side, qty):
        """market order: walk until filled or book exhausted."""
        self.add(side, float("inf") if side == "b" else -float("inf"), qty)
    def top(self):
        b = max(self.bids) if self.bids else None
        a = min(self.asks) if self.asks else None
        return b, a
    def mid(self):
        b, a = self.top()
        return (a + b) / 2 if b is not None and a is not None else None
    def depth(self, side, n=3):
        d = self._side(side)
        ks = sorted(d, reverse=(side == "b"))[:n]
        return [(k, sum(q for q, _ in d[k])) for k in ks]

if __name__ == "__main__":
    B = Book()
    for p, q in [(99.0, 5), (99.5, 3), (100.0, 4)]:
        B.add("b", p, q)
    for p, q in [(100.5, 2), (101.0, 3), (101.5, 6)]:
        B.add("s", p, q)
    print("top:", B.top(), "mid:", B.mid())
    print("bids:", B.depth("b"), " asks:", B.depth("s"))
    B.add("s", 99.5, 5)      # limit sell crosses into bids
    print("after sell 5@99.5:", B.trades[-2:], "top:", B.top())
