"""Load power and efficiency vs R_L for EMF=12 V, r=2 ohm: the max-power trade."""
emf, r = 12.0, 2.0
print(" R_L (ohm)   P_L (W)   efficiency")
for RL in [0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 18.0, 50.0]:
    P = emf**2 * RL / (RL + r)**2
    print(f"{RL:9.1f}   {P:7.2f}   {RL/(RL+r)*100:9.1f}%")
print(f"analytic max: EMF^2/4r = {emf**2/(4*r):.1f} W at R_L = r = {r:.0f} ohm")
