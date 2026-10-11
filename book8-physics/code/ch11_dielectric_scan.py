"""Half-dielectric two ways: series stack vs side-by-side, C/C0 for kappa = 1..10."""
def c_series(k):    # slab fills half the gap, perpendicular
    return 2 * k / (k + 1)
def c_parallel(k):  # slab fills half the area
    return (1 + k) / 2

print("kappa   C_series/C0   C_parallel/C0")
for k in [1, 2, 3, 4, 6, 10]:
    print(f"{k:5d}   {c_series(k):11.3f}   {c_parallel(k):13.3f}")
print(f"kappa -> inf limits: series {2.0:.1f} C0, parallel diverges like k/2")
for k in [50, 100, 1000]:
    print(f"  k={k:4d}: series {c_series(k):8.3f}   parallel {c_parallel(k):10.1f}")
