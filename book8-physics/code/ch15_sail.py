"""Solar-sail parameter scan: radiation acceleration vs areal density."""
S, c, M_sun, G = 1360.0, 3e8, 1.989e30, 6.674e-11
r_au = 1.496e11
p = 2 * S / c                     # reflecting sail, N/m^2
g_sun = G * M_sun / r_au**2
print(f"pressure on a reflector at 1 AU: {p*1e6:.2f} uN/m^2")
print(f"solar gravity at 1 AU          : {g_sun*1e3:.2f} mm/s^2")
print(" areal density (g/m^2)   accel (mm/s^2)   vs gravity")
for sm in [0.5, 1.0, 1.5, 2.0, 5.0]:
    a = p / (sm * 1e-3)
    print(f"{sm:18.1f}   {a*1e3:14.2f}   {'outward' if a > g_sun else 'inward':>7s}")
print(f"breakeven density: {p/g_sun*1e3:.2f} g/m^2")
