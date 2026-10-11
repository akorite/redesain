"""Wheatstone bridge off-null: detector voltage vs resistor mismatch, theory vs sweep."""
Vs = 10.0
R = 1000.0
def v_d(eps):
    return Vs * ((1 + eps) / (2 + eps) - 0.5)
print("mismatch (%)   V_d measured (mV)   V_d approx Vs*eps/4 (mV)")
for eps in [0.0005, 0.001, 0.005, 0.01, 0.05, 0.10]:
    exact = v_d(eps) * 1000
    approx = Vs * eps / 4 * 1000
    print(f"{eps*100:11.2f}%   {exact:17.2f}   {approx:23.2f}")
print(f"0.1% -> {v_d(0.001)*1000:.2f} mV, still decades above a DMM's uV floor")
