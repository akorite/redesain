import heapq
import numpy as np

freq = {"e": 0.127, "t": 0.091, "a": 0.082, "o": 0.075,
        "i": 0.070, "n": 0.067, "s": 0.063, "r": 0.060,
        "h": 0.043, "d": 0.043, "l": 0.040, "u": 0.028,
        "c": 0.028, "m": 0.024, "f": 0.022, "w": 0.020,
        "y": 0.020, "p": 0.019, "b": 0.015, "g": 0.020,
        "v": 0.010, "k": 0.008, "x": 0.002, "j": 0.002,
        "q": 0.001, "z": 0.001}
tot = sum(freq.values()); freq = {k: v/tot for k, v in freq.items()}

heap = [(p, [s]) for s, p in freq.items()]
heapq.heapify(heap)
lengths = {s: 0 for s in freq}
while len(heap) > 1:
    p1, g1 = heapq.heappop(heap); p2, g2 = heapq.heappop(heap)
    for s in g1 + g2: lengths[s] += 1
    heapq.heappush(heap, (p1 + p2, g1 + g2))

H = -(np.array(list(freq.values()))
      * np.log2(list(freq.values()))).sum()
avg = sum(freq[s] * lengths[s] for s in freq)
print(f"entropy H        = {H:.3f} bits/symbol")
print(f"Huffman avg      = {avg:.3f} bits/symbol")
print(f"fixed 5-bit code = 5.000 bits/symbol")
top = sorted(freq, key=freq.get, reverse=True)[:6]
for s in top:
    print(f"  {s}: p={freq[s]:.3f}  -log2 p={-np.log2(freq[s]):.2f}"
          f"  len={lengths[s]}")
