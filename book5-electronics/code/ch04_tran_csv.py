#!/usr/bin/env python3
"""ch04_tran_csv.py -- Chapter 4 figure data: rescale ngspice wrdata output.

Reads the raw .dat files ngspice wrote (time in seconds, voltage in volts)
and emits pgfplots-ready tables in friendlier units (ms or us).  Run after
`ngspice -b` on the chapter's netlists; the figures plot these files.
"""
import sys

def rescale(src, dst, tscale, thin=1):
    rows = [l.split() for l in open(src) if l.split()]
    with open(dst, "w") as f:
        for t, v in rows[::thin]:
            f.write(f"{float(t) * tscale:.6e}  {float(v):.6e}\n")
    print(f"{src} -> {dst}: {len(rows[::thin])} rows (x{tscale:g})")

rescale("ch04_rc_step.dat",        "../figures/ch04/ch04_rc_step_ms.dat", 1e3, 4)
rescale("ch04_rc_discharge.dat",   "../figures/ch04/ch04_rc_discharge_ms.dat", 1e3, 4)
rescale("ch04_decouple_cap.dat",   "../figures/ch04/ch04_decouple_cap_us.dat", 1e6, 3)
rescale("ch04_decouple_nocap.dat", "../figures/ch04/ch04_decouple_nocap_us.dat", 1e6, 3)
rescale("ch04_flyback.dat",        "../figures/ch04/ch04_flyback_ms.dat", 1e3, 2)
