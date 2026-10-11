"""Where a car's joules go: KE, a 100 m climb, and one second of highway drag."""
m, v, g = 1200.0, 27.0, 9.81        # kg, m/s (~60 mph)
Cd, A, rho = 0.30, 2.2, 1.2
KE = 0.5 * m * v**2
PE_100m = m * g * 100
F_drag = 0.5 * rho * Cd * A * v**2
P_drag = F_drag * v
print(f"KE at 60 mph            : {KE/1e3:8.1f} kJ")
print(f"PE climbing 100 m       : {PE_100m/1e3:8.1f} kJ")
print(f"drag force              : {F_drag:8.0f} N")
print(f"drag power at 60 mph    : {P_drag/1e3:8.1f} kW")
print(f"1 min of drag work      : {P_drag*60/1e3:8.1f} kJ = {P_drag*60/KE:.2f} x KE")
print(f"double the speed: drag power x{2**3}")
