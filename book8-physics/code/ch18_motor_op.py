"""DC motor operating point: stall/no-load anchors, torque-speed line vs load."""
import numpy as np
V, R, kv = 12.0, 1.5, 0.02        # V, ohm, N.m/A back-EMF const (Kt=Kv here)
w_free = V / kv                    # ideal no-load speed, rad/s
I_stall = V / R
T_stall = kv * I_stall
def torque(w):
    I = (V - kv * w) / R
    return kv * I
print(f"no-load speed {w_free:.0f} rad/s   stall torque {T_stall:.3f} N.m")
print(" load (N.m)   speed (rad/s)   current (A)   P_out (W)   eff")
for T_load in [0.01, 0.03, 0.06, 0.09, 0.12]:
    # solve torque(w) = T_load -> w = (V - T_load*R/kv)/kv
    w = (V - T_load * R / kv) / kv
    I = (V - kv * w) / R
    p_out = T_load * w
    p_in = V * I
    print(f"{T_load:11.2f}   {w:14.1f}   {I:12.2f}   {p_out:10.1f}   {p_out/p_in*100:4.0f}%")
w_best = V / (2 * kv)
print(f"max mechanical power at w={w_best:.0f} rad/s (half no-load): {kv*(V-kv*w_best)/R*w_best:.1f} W")
