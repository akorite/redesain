# Outline — Physics for engineers (`textbook-physics`)

*For approval before any chapter is written. Prepared 2026-10-10 after the §3B research
logged in `docs/sources.md`.*

**Reader:** Calculus I; vectors. Self-study, five-year horizon.
**Outcomes targeted:** solves F=ma-level and AP Physics C problems; derives standard results
from the stated laws; connects mechanics and electromagnetism to engineering practice
(bridge into Book 5 electronics).
**Shape:** 18 chapters in 4 parts + a capstone part. ~236 pages total (in the 150–250
window, with a named compression order below).
**Chapter standard (per §3/§3A):** opening paragraph; motivation before definitions;
≥3 worked examples (Strategy → Solution → Significance); ≥4 figures; ≥1 Python simulation
listing with real captured output; inline checkpoint exercises; ≥10 additional graded
exercises `[easy]/[medium]/[hard]` each carrying a contest-resemblance tag; a "common
mistakes" section; a one-page summary table; a "Notes" section with numbered citations.

## Global design decisions (deviations from the seed are marked ◆)

1. **Order: momentum before energy.** Adopted from MIT 8.01SC (impulse/momentum right
   after Newton's laws; collisions revisited after \(K\) exists) against the OpenStax/AP
   order. Consequence: ch3 covers impulse, systems, CM, conservation and *inelastic/2D*
   collisions; **fully elastic collisions are worked in §4.7** once the work–energy theorem
   is available — flagged as a deliberate two-pass treatment. ◆
2. **Seed "circuits and RC dynamics"** = one chapter (ch12) covering Kirchhoff through RC
   transients. Seed "magnetic fields and forces" = one chapter (ch13) that also covers
   *sources* of B (Biot–Savart, Ampère) — matches AP-C unit 12 and 8.02SC. ◆
3. **Maxwell's equations** = integral form only. Divergence and curl are *named* and drawn
   (the reader has Calc I; full vector calculus is Book 3's job), the wave equation is
   derived heuristically, and the numeric \(c\) check is done by simulation. ◆
4. **"Waves and optics"** is one chapter after EM waves (light as the running example);
   geometric optics is out of scope (not AP C, not F=ma). ◆
5. **Thermodynamics** = one chapter (seed says "essentials"). ◆
6. **Fluids**: F=ma includes fluids, AP C does not. Compact optional appendix (App A, ~5 pp)
   covers pressure, buoyancy, continuity, Bernoulli — flagged for approval. ◆
7. **Capstone lives as its own part** (Part V, "The workshop"): 20 original contest-style
   problems with full solutions, deliberately multi-topic — contest sets mix topics, and
   chapter exercises stay chapter-scoped. Structured problems→(hints)→solutions like
   Gnädig/Krotov. ~12 mechanics, ~6 E&M, ~2 waves/thermo.
8. **Engineering thread** ("In engineering practice" end-sections): FBDs→loads (ch2),
   drag→ballistics/aero (ch2, ch17), momentum→rockets (ch3), energy→power budgets (ch4),
   rotation→flywheels/motors (ch5–6), resonance→filters/antennas (ch7, ch14), orbits→GPS
   (ch8), E-field→deflection/sensors (ch9), capacitance→decoupling (ch11), circuits→Book 5
   (ch12–14, named cross-refs), Maxwell→RF/links (ch15), waves→imaging/antennas (ch16),
   thermo→engines/heat sinks (ch17), all unified in ch18 power conversion.
9. **Every derivation is a "From the laws" box**: the law(s) it starts from are stated at
   the top; no result appears without its assumption set. (Brief "Special".)
10. **Each chapter ends with one numbered Python simulation** (`code/chNN_*.py`,
    NumPy+matplotlib only, ≤40 inline lines, real output printed and discussed; "predict
    before you run" checkpoint precedes the output). Deeper dives go in `code/` referenced.
11. **Difficulty scheme** (defined in `notation.md`): `[easy]` ≈ AP-C MC / lower F=ma;
    `[medium]` ≈ AP-C free-response part / upper F=ma; `[hard]` ≈ USAPhO/APhO short
    problem / Gnädig-star. Every exercise also carries a resemblance tag `(AP-C)`,
    `(F=ma)`, `(USAPhO)`, `(APhO-style)`, `(estimation)`.
12. **Compression order** (if the book runs long; never cut figures/code outputs/worked
    examples/common-mistakes per approved rules): (a) merge ch5+ch6 into one 15 pp
    rotation chapter → −9 pp; (b) capstone solutions to compact two-column format → −4 pp;
    (c) App A fluids → drop to a 2-page note → −3 pp; (d) ch16 diffraction/lens tail cut →
    −2 pp. **Expansion order** (if under ~190): split rotation back into two chapters;
    second code listing per chapter; restore fluids appendix.

## Page budget

| Block | Pages |
|---|---|
| Front matter (title, preface, how-to-use/ratings, contents) | 10 |
| Part I Mechanics (ch1–8) | 92 |
| Part II Fields and circuits (ch9–14) | 70 |
| Part III Maxwell, waves, heat (ch15–17) | 32 |
| Part IV Engineering synthesis (ch18) | 9 |
| Part V The workshop (capstone, 20 problems + solutions) | 15 |
| Back matter (hints to all `[hard]`; solutions to ≥half of all exercises; bibliography; index) | 18 |
| **Total** | **~246 → trim to ~236 via per-chapter estimates below** |

Per-chapter estimates were set to land ~236 pp; the compression order covers overshoot.

---

# Part I — Mechanics

## Chapter 1 — Kinematics: describing motion (~11 pp)

**Prerequisites:** Calculus I (derivative, chain rule, definite integral); vector components
(cross-ref Book 3). **Sections:** 1.1 Position, displacement, average vs instantaneous
velocity · 1.2 Acceleration; the calculus loop \(x\to v\to a\) and back by integration ·
1.3 Constant acceleration (the three formulas derived, not quoted) · 1.4 Projectile motion
as independent components · 1.5 Circular motion: \(a_c=v^2/r\) derived by the velocity
difference argument · 1.6 Relative velocity and Galilean frames.
**Worked examples:** (1) extracting \(v(t)\) and \(a(t)\) from a measured \(x(t)\) plot;
(2) projectile landing on an elevated target — range equation generalised; (3) river/boat
crossing in a current (relative frames).
**Figures (6):** aligned \(x(t),v(t),a(t)\) triple plot; position vs velocity sign map;
projectile trajectory with velocity components at 3 instants; \(\Delta\mathbf v\) geometry
for centripetal acceleration; relative-velocity vector triangle; summary table (end).
**Code:** `ch01_projectile.py` — Euler integrator vs analytic solution, same axes; then add
quadratic drag term and show the shortened range. Output: trajectory plot + printed
range error for \(h\to0\) step convergence.
**Exercises:** 4 inline checkpoints + 11 additional. Plan: 4[easy] (reading \(v\)-\(t\)
graphs (AP-C); unit conversions of acceleration (AP-C); two-object meeting time (F=ma-style);
free-fall timing (F=ma)) · 5[medium] (max range on an incline (AP-C FR-style); crossing
time vs drift trade (F=ma); acceleration from a displacement table — data-analysis
(F=ma); centripetal acceleration of a turning car (AP-C); ball thrown off a cliff —
direction of \(\mathbf a\) reasoning (F=ma)) · 2[hard] (range as a function of launch angle
on uneven ground — optimisation (USAPhO-style); pursuit with acceleration caps
(APhO-style)).
**Common mistakes:** confusing speed with velocity and distance with displacement; treating
\(a=v^2/r\) as a new force; sign of \(g\) inconsistent within one solution; using
constant-\(a\) formulas when \(a(t)\) varies.
**Sources:** MIT 8.01SC weeks 1,3; AP-C U1; OpenStax v1 ch3–4; Feynman I §8.

## Chapter 2 — Newton's laws and applications (~12 pp)

**Prerequisites:** ch1. **Sections:** 2.1 The three laws; inertial frames stated as an
assumption · 2.2 The force inventory (gravity, normal, tension, spring, friction, drag) ·
2.3 Free-body diagrams (the discipline) · 2.4 Constraint problems: inclines, pulleys,
contact forces · 2.5 Circular dynamics: centripetal *net force*, not a force · 2.6 Friction:
static vs kinetic, angle of repose · 2.7 Drag: linear and quadratic models, terminal
velocity as an ODE fixed point.
**Worked examples:** (1) Atwood machine with massive-free string — full FBD method;
(2) banked curve with friction — two boundary cases; (3) block on an accelerating incline
(apparent weight); (4) quadratic drag: derive \(v(t)\) and \(v_\mathrm{t}\).
**Figures (7):** FBD gallery (5 canonical cases); incline decomposition; pulley constraint
labelling; banked-curve diagram; \(f_s\) vs applied force plot; drag force vs \(v\) with
\(v_\mathrm{t}\); summary table.
**Code:** `ch02_drag_fall.py` — Euler-Cromer integration of \(\dot v=g-(c_d/m)v^2\), prints
\(v_\mathrm{t}\) vs analytic, plots convergence of Euler vs exact \(v(t)\).
**Exercises:** 4 inline + 12 additional. Plan: 4[easy] (FBD selection MC-style (AP-C);
\(N=mg\cos\theta\) when it holds (AP-C); weight vs mass numeric (AP-C); tension in static
rope (F=ma)) · 5[medium] (two stacked blocks, friction-limited acceleration (F=ma); conical
pendulum (AP-C); Atwood with table friction (AP-C); elevator apparent weight (F=ma);
critical speed on banked vs flat curve (AP-C)) · 3[hard] (rope sliding off a frictionless
table — variable mass element (USAPhO-style); wedge free to slide (APhO-style); drag-limited
projectile max range estimate (USAPhO-style)).
**Common mistakes:** drawing \(mv^2/r\) as an extra force; assuming \(N=mg\) on
accelerating surfaces; guessing friction direction instead of deriving it; dropping the
third-law pair on the wrong object; premature coordinate choice before the FBD.
**Sources:** MIT 8.01SC weeks 2–4; AP-C U2; Morin ch1–3; OpenStax v1 ch5–6.

## Chapter 3 — Momentum, impulse and collisions (~12 pp)

**Prerequisites:** ch2. **Sections:** 3.1 \(\mathbf p\), impulse \(\mathbf J=\int\mathbf F\,dt\)
· 3.2 Systems of particles: internal vs external forces · 3.3 Conservation of momentum —
when it applies (the boundary rule) · 3.4 Centre of mass: definition, motion, \(M\mathbf A
=\mathbf F_\mathrm{ext}\) · 3.5 1-D collisions: perfectly inelastic; elastic *stated* —
full solution deferred to §4.7 (needs \(K\)) · 3.6 2-D collisions, explosions, recoil ·
3.7 Continuous mass transfer: the rocket equation derived.
**Worked examples:** (1) impulse from a real \(F(t)\) force–time curve (area method);
(2) person jumping off a movable cart — CM stays put; (3) rocket \(\Delta v\) with staging
estimate; (4) glancing 2-D collision via component conservation.
**Figures (6):** impulse as area under \(F(t)\); system-boundary cartoon (the *choose-your-
system* figure); CM of two bodies and of an extended object; collision sequence small-
multiple; rocket mass-loss schematic; summary table.
**Code:** `ch03_collision_chain.py` — event-stepped simulation of N blocks on a rail
exchanging momentum; prints \(\sum p\) and \(\sum K\) before/after each collision; shows
\(K\) loss in inelastic events (feeds §4.7).
**Exercises:** 4 inline + 11 additional. Plan: 4[easy] (impulse from constant \(F\) (AP-C);
recoil velocity (F=ma); CM of a 2-mass system (AP-C); momentum conservation MC reasoning
(AP-C)) · 5[medium] (ballistic-pendulum momentum stage only (AP-C); explosion into 3
fragments (F=ma); CM frame reasoning (F=ma); impulse from graph area (F=ma); thrust of a
water jet (USAPhO-lite)) · 2[hard] (chain falling off a table — continuous flux
(APhO-style); two-stage rocket optimisation sketch (USAPhO-style)).
**Common mistakes:** conserving momentum when an external impulse exists; wrong system
boundary (excluding the fragment you need); sign errors in 1-D momentum; believing \(K\)
survives inelastic collisions; forgetting the CM keeps moving through an explosion.
**Sources:** MIT 8.01SC weeks 3,5–6; AP-C U4; Morin ch5; OpenStax v1 ch9.

## Chapter 4 — Work, energy and power (~12 pp)

**Prerequisites:** ch3. **Sections:** 4.1 Work \(W=\int\mathbf F\cdot d\mathbf r\), variable
forces · 4.2 Work–kinetic-energy theorem (derived from \(\mathbf F=m\mathbf a\)) ·
4.3 Potential energy: conservative forces, gravity, spring — *From the laws* · 4.4
Conservation of mechanical energy and its failure modes · 4.5 Energy diagrams: \(U(x)\),
turning points, equilibrium · 4.6 Power \(P=\dot W=\mathbf F\cdot\mathbf v\) · 4.7 Elastic
collisions — the deferred full treatment (energy + momentum systems) · 4.8 Non-conservative
work: friction, heating, energy audits.
**Worked examples:** (1) minimum release height for the loop-the-loop (energy + circular
dynamics); (2) spring-launched block up a rough incline — full energy audit; (3) 1-D
elastic collision solved three ways (lab, CM, \(v_\mathrm{rel}\) flip).
**Figures (7):** work as area under \(F(x)\); spring \(U(x)\) parabola with turning points;
energy bar charts along a trajectory; loop-the-loop annotated track; elastic-collision
\(p\)-\(K\) bookkeeping figure; power force–velocity plot; summary table.
**Code:** `ch04_energy_check.py` — integrates a block-spring with plain Euler vs
symplectic Euler; prints energy drift of each → motivates symplectic integrators used
henceforth. *Predict-before-you-run checkpoint included.*
**Exercises:** 4 inline + 12 additional. Plan: 4[easy] (work sign reasoning (AP-C);
\(P=Fv\) numeric (AP-C); spring energy (AP-C); energy bar-chart reading (F=ma)) ·
6[medium] (loop minimum speed (F=ma classic); spring + friction incline (AP-C FR-style);
power to climb stairs — measurement style (F=ma data); pendulum speed at bottom (AP-C);
two-block elastic result (AP-C); conveyor-belt heating estimate (F=ma)) · 2[hard]
(particle in \(U(x)=ax^4-bx^2\) — turning points (USAPhO-style); elastic collision with
unequal masses — limiting cases (USAPhO-style)).
**Common mistakes:** sign of work vs \(\Delta U\) (work done *by* vs *on*); mixing PE zero
points inside one problem; conserving mechanical energy across friction; \(P=Fv\) with the
wrong velocity; assuming contact forces do no work on deformable systems.
**Sources:** MIT 8.01SC weeks 7–9; AP-C U3; Morin ch5; OpenStax v1 ch7–8.

## Chapter 5 — Rotation I: kinematics, torque and statics (~12 pp)

**Prerequisites:** ch1, ch2, ch4. **Sections:** 5.1 Angular variables \(\theta,\omega,\alpha\);
the linear–angular dictionary (derived, not memorised) · 5.2 No-slip rolling *kinematics*
preview (velocity of rim points) · 5.3 Torque \(\boldsymbol\tau=\mathbf r\times\mathbf F\);
lever arm · 5.4 Moment of inertia as an integral; perpendicular/parallel-axis theorems ·
5.5 \(\tau=I\alpha\): pulleys with mass, falling unwinding objects · 5.6 Static equilibrium:
\(\sum\mathbf F=0,\sum\tau=0\); ladders and hinges · 5.7 Rotational kinetic energy.
**Worked examples:** (1) Atwood machine *with* massive pulley — where the old solution
breaks; (2) ladder minimum friction angle — torque about the smart pivot; (3) \(I\) of a
rod and a disk by direct integration (and check vs table).
**Figures (7):** angular kinematics analogy table (figure-as-table); torque/lever-arm
geometry; massive-pulley three-FBD set; ladder free-body; \(I\) of six standard shapes
with derivations sketched; rolling wheel velocity field; summary table.
**Code:** `ch05_inertia_integrator.py` — numerical moment of inertia of a lamina by grid
quadrature vs analytic; prints relative error, shows why the parallel-axis term matters.
**Exercises:** 3 inline + 11 additional. Plan: 4[easy] (angular–linear conversion (AP-C);
lever-arm identification (AP-C); \(I\) units/table use (AP-C); static beam tension (F=ma))
· 5[medium] (massive-pulley Atwood (F=ma classic); ladder angle bound (AP-C FR-style);
yo-yo acceleration (F=ma); \(I\) of composite body (AP-C); sign-of-torque reasoning (AP-C))
· 2[hard] (rod falling off a frictionless edge (USAPhO-style); non-uniform rod balance
with torque integral (APhO-style)).
**Common mistakes:** lever arm vs point distance; forgetting the pulley's inertia; wrong
parallel-axis shift; choosing the torque origin badly (pick it to kill unknowns);
translational-only force balance in statics.
**Sources:** MIT 8.01SC weeks 6,10–11; AP-C U5; OpenStax v1 ch10, ch12; Morin ch7–8.

## Chapter 6 — Rotation II: angular momentum and rolling (~11 pp)

**Prerequisites:** ch5. **Sections:** 6.1 \(\mathbf L=\mathbf r\times\mathbf p\) for a
particle · 6.2 \(L=I\omega\) for a rigid body; when it holds · 6.3
\(\boldsymbol\tau=d\mathbf L/dt\) — valid origins (inertial point vs CM) · 6.4 Conservation
of angular momentum · 6.5 Rolling dynamics three ways: forces, energy, instantaneous axis ·
6.6 Gyroscopic precession — qualitative + order-of-magnitude law.
**Worked examples:** (1) skater pulling in arms — \(\omega\) ratio and energy audit
(\(K\) increases — why?); (2) bullet embedding in a pivoted rod — conserve \(L\), not \(p\);
(3) race down the incline: hoop vs disk vs sphere — who wins and why.
**Figures (6):** \(\mathbf r\times\mathbf p\) geometry; turntable before/after sequence;
rolling-constraint velocity field revisited; incline-race energy split bars; gyroscope
vector diagram; summary table.
**Code:** `ch06_rolling_race.py` — integrates rolling down an incline for several shape
factors \(\beta\); prints finish order and energy partition \(K_\mathrm{tr}/K_\mathrm{rot}\).
**Exercises:** 3 inline + 10 additional. Plan: 4[easy] (units and direction of \(\mathbf L\)
(AP-C); \(L\) conservation recognition (AP-C); rolling constraint \(v=\omega r\) (AP-C);
skater reasoning (F=ma)) · 4[medium] (child walking on turntable (AP-C FR-style);
rolling-race ranking (F=ma); bullet-rod system (AP-C); angular collision of two disks
(F=ma)) · 2[hard] (ball transitions sliding→rolling — friction-limited dynamics
(USAPhO-style); spool pulled by a thread — rolls which way? (APhO-style classic)).
**Common mistakes:** applying \(L=I\omega\) about the wrong axis; conserving \(L\) while
external torque acts; forgetting translational \(K\) in rolling; \(\tau=dL/dt\) about a
non-inertial origin; cross-product sign.
**Sources:** MIT 8.01SC weeks 11–12 + gyroscope deep dive; AP-C U6; Morin ch8–9; OpenStax
v1 ch11.

## Chapter 7 — Oscillations (~11 pp)

**Prerequisites:** ch4, ch6 (energy diagrams, physical pendulum needs \(I\)).
**Sections:** 7.1 SHM: \(\ddot x+\omega_0^2x=0\), solution family, initial conditions ·
7.2 Spring–mass: period derived; energy in SHM · 7.3 Simple and physical pendulums ·
7.4 The small-angle approximation — stated, bounded, and when it fails · 7.5 Damped
oscillations: under/critical/over as regimes of one equation · 7.6 Driven oscillations:
amplitude response, resonance, \(Q\) · 7.7 Phase space; first look at nonlinear
oscillations.
**Worked examples:** (1) physical pendulum (meter stick pivot) — \(I\omega\) method;
(2) damped oscillator: extract \(\gamma,\omega_0,\omega_d\) from a decaying trace;
(3) resonance-curve half-power bandwidth → \(Q\).
**Figures (7):** \(x(t)\) for three damping regimes; phase portrait spiral; \(U(x)\) and the
SHM parabola; pendulum small-angle geometry; driven-oscillator amplitude vs \(\omega_d\);
tuning-fork/engineering resonance photo-substitute (drawn); summary table.
**Code:** `ch07_resonance_sweep.py` — RK4 driven damped oscillator; sweeps \(\omega_d\),
prints measured resonance peak vs theory; output curve shown beside the analytic formula.
**Exercises:** 4 inline + 11 additional. Plan: 4[easy] (period scaling \(T\propto\sqrt{m/k}\)
(AP-C); amplitude vs energy (AP-C); frequency–period conversion (AP-C); pendulum on the
Moon (F=ma)) · 5[medium] (springs in series/parallel effective \(k\) (F=ma); physical
pendulum period (AP-C FR-style); SHM phase reasoning (AP-C); critical damping recognition
(AP-C); energy decay per cycle (F=ma)) · 2[hard] (finite-amplitude pendulum correction
\(T\approx T_0(1+\theta_0^2/16)\) use (USAPhO-style); oscillator with position-dependent
force — linearise about equilibrium (APhO-style)).
**Common mistakes:** applying small-angle where \(\theta\) isn't small; \(\omega\) vs \(f\)
confusion; amplitude vs energy relation (\(E\propto A^2\)); driving at \(\omega_0\) vs
damped \(\omega_d\); damping "slows" period assumption checked.
**Sources:** MIT 8.01SC/8.03 heritage via OCW; AP-C U7; Morin ch4; OpenStax v1 ch15;
Feynman I §21–24.

## Chapter 8 — Gravitation and orbits (~11 pp)

**Prerequisites:** ch1 (circular motion), ch4, ch6. **Sections:** 8.1 Newton's law; the
field picture \(\mathbf g(\mathbf r)\) · 8.2 Shell theorem: \(g\) inside and outside a
planet — *From the laws* · 8.3 Gravitational potential energy \(U=-GMm/r\); escape velocity
· 8.4 Circular orbits: \(v_\mathrm{orb}\), period, energy · 8.5 Ellipses and Kepler's three
laws derived (1st stated+sketched, 2nd from \(L\) conservation, 3rd in full) · 8.6 Energy
and \(L\) as the orbit's conserved labels; effective potential · 8.7 Satellites, station-
keeping cost, GPS timing note, tides in two paragraphs.
**Worked examples:** (1) escape velocity and why it's the same from any direction;
(2) Hohmann-style transfer energy bookkeeping between two circular orbits; (3) \(g(r)\)
profile inside the Earth for uniform density.
**Figures (7):** \(g(r)\) inside/outside Earth; \(U(r)\) and \(U_\mathrm{eff}(r)\) with
orbit types; Kepler equal-areas figure; orbit \(E\) vs semi-major axis; satellite/transfer
geometry; summary table.
**Code:** `ch08_orbit_verlet.py` — leapfrog/velocity-Verlet orbit integrator; prints \(E,L\)
drift (<0.1%), recovers \(T^2\propto a^3\) numerically from three orbits.
**Exercises:** 3 inline + 11 additional. Plan: 4[easy] (circular-orbit \(v\) (AP-C);
geostationary radius reasoning (AP-C); escape-vs-orbital speed ratio (F=ma); surface \(g\)
scaling (F=ma)) · 5[medium] (transfer-energy estimate (F=ma); weight inside a mine shaft
(AP-C); two-satellite period comparison (F=ma); energy to raise an orbit (AP-C); tidal
bulge reasoning (F=ma-lite)) · 2[hard] (reduced-mass two-body correction (USAPhO-style);
launch-angle-independent escape proof — energy argument (APhO-style)).
**Common mistakes:** treating \(g\) as constant at altitude; escape-velocity direction
myth; \(U\)'s negative sign dropped; confusing orbital speed and period scaling;
forgetting rotational contribution to apparent \(g\).
**Sources:** MIT 8.01SC weeks 3,11–12 + course notes ch9; AP-C U1/U3 links; Morin ch7;
OpenStax v1 ch13; Feynman I §7.

---

# Part II — Fields and circuits

## Chapter 9 — Electric charge and field (~11 pp)

**Prerequisites:** vectors; ch2 force discipline. **Sections:** 9.1 Charge, quantisation,
conductors vs insulators · 9.2 Coulomb's law — superposition is the real law · 9.3 The
field concept \(\mathbf E=\mathbf F/q\) · 9.4 Field lines: rules and reading · 9.5
Continuous distributions: line, ring, disk by integration — *From the laws* · 9.6 Motion of
a charge in uniform \(\mathbf E\) (kinematics returns).
**Worked examples:** (1) \(\mathbf E\) on the axis of a charged ring — full integral;
(2) dipole far-field pattern derived; (3) electron beam deflection in a capacitor
(links to oscilloscopes).
**Figures (7):** field-line maps of point charge, dipole, two like charges; geometry for
ring/disk integrals; field-line rules infographic; deflection trajectory; conductor vs
insulator cartoon; summary table.
**Code:** `ch09_field_lines.py` — traces \(\mathbf E\) of arbitrary point-charge sets;
produces the field-line map; prints a numeric check vs Coulomb at sample points.
**Exercises:** 4 inline + 11 additional. Plan: 4[easy] (superposition of two charges
(AP-C); field vs force direction (AP-C); units of \(\mathbf E\) (AP-C); field-line reading
(F=ma)) · 5[medium] (on-axis field of a rod (AP-C FR-style); semicircle centre field
(AP-C); equilibrium of three charges — unstable? (F=ma); dipole torque in uniform \(\mathbf E\)
(AP-C); charge-deflection plate design (engineering)) · 2[hard] (field of an arc with
charge density varying (USAPhO-style); dipole oscillation frequency estimate (APhO-style)).
**Common mistakes:** field vs force conflation; scalar superposition instead of vector;
\(dq\) element setup errors (linear density); sign of test charge in direction questions;
field "used up" by the test charge.
**Sources:** 8.02SC modules 1–4; AP-C U8; OpenStax v2 ch5; Purcell–Morin ch1; Feynman II §1.

## Chapter 10 — Gauss's law (~11 pp)

**Prerequisites:** ch9. **Sections:** 10.1 Flux \(\Phi_E=\int\mathbf E\cdot d\mathbf A\) ·
10.2 Gauss's law from Coulomb — solid-angle intuition stated · 10.3 Spherical symmetry:
insulating sphere, shells · 10.4 Cylindrical symmetry: line charge, coaxial · 10.5 Planar
symmetry: sheets and plates · 10.6 Conductors in electrostatics: \(E=0\) inside, shielding,
\(E=\sigma/\epsilon_0\) at the surface.
**Worked examples:** (1) uniform-volume-charge sphere \(E(r)\) both regions; (2) coaxial
cable field — engineering case; (3) induced surface charge on a conductor with a cavity.
**Figures (7):** flux through open/closed surfaces; the three Gaussian-surface archetypes;
\(E(r)\) plots for sphere/cylinder/sheet; conductor cavity induction sequence; field at a
charged surface pillbox; summary table.
**Code:** `ch10_flux_check.py` — numerically integrates \(\mathbf E\cdot d\mathbf A\) over
a cube around a point charge; prints \(\Phi\to Q/\epsilon_0\) convergence vs grid.
**Exercises:** 4 inline + 10 additional. Plan: 4[easy] (flux through simple surfaces (AP-C);
enclosed-charge reasoning (AP-C); \(E\) inside conductor (AP-C); field of an infinite sheet
(F=ma)) · 4[medium] (uniform sphere both regions (AP-C FR-style); line of charge by Gauss
(AP-C); charged shell + point inside (F=ma); coaxial field profile (engineering)) ·
2[hard] (charge inside a conductor cavity — induced distributions (USAPhO-style); non-
uniform \(\rho(r)\) sphere inversion problem (APhO-style)).
**Common mistakes:** applying Gauss without symmetry; wrong enclosed charge; confusing the
Gaussian area with the charge's area; \(E=0\) inside a *conductor* vs inside a *cavity*;
adding a surface term that symmetry doesn't kill.
**Sources:** 8.02SC modules 5,8; AP-C U8; OpenStax v2 ch6; Purcell–Morin ch1–2; Griffiths
§2 (anchor, print).

## Chapter 11 — Electric potential, conductors and capacitance (~12 pp)

**Prerequisites:** ch4 (energy), ch9–10. **Sections:** 11.1 Potential energy of charges;
sign discipline · 11.2 \(V\), equipotentials, field↔potential maps · 11.3 \(V\) of
distributions by integration · 11.4 \(\mathbf E=-\nabla V\) in one dimension and what the
gradient means · 11.5 Conductors: equipotential bodies, shielding, method of images named
(not developed) · 11.6 Capacitance: parallel plate derived, cylinders/spheres · 11.7
Dielectrics: polarisation, \(\kappa\), effect on \(C\) · 11.8 Energy stored
\(U=\tfrac12CV^2=\tfrac{\epsilon_0}{2}E^2\cdot\text{vol}\).
**Worked examples:** (1) \(V\) on axis of a charged disk — integral + \(E\) check via
gradient; (2) spherical capacitor derivation end-to-end; (3) assembling a charge
configuration — work vs stored energy audit.
**Figures (7):** equipotential + field-line maps (dipole, plates); \(V(x)\)/\(E(x)\) paired
plots; parallel-plate cross-section with fringing sketch; cylindrical/spherical capacitor
geometries; dielectric bound-charge picture; summary table.
**Code:** `ch11_potential_map.py` — evaluates \(V\) on a grid from a charge set, draws
equipotential contours; prints a numeric check of \(-\partial V/\partial x\approx E_x\).
**Exercises:** 4 inline + 11 additional. Plan: 4[easy] (potential from two charges (AP-C);
equipotential reading (AP-C); capacitor series/parallel (AP-C); energy in a charged
capacitor (F=ma)) · 5[medium] (ring-axis \(V\) then \(E\) (AP-C FR-style); work to move a
charge between two points (AP-C); dielectric slab insertion — what changes and why
(AP-C); energy density of a field (F=ma); shielded conductor reasoning (F=ma)) ·
2[hard] (self-energy of a charge configuration (USAPhO-style); capacitor half-filled with
dielectric — two geometries (APhO-style)).
**Common mistakes:** treating \(V\) as a vector; sign errors for unlike charges;
series/parallel rules swapped; believing \(Q\) stays fixed when a dielectric is inserted
with the battery attached; field "inside" conductor vs "just outside" (\(\sigma/\epsilon_0\)).
**Sources:** 8.02SC modules 6–11; AP-C U9–U10; OpenStax v2 ch7–8; Purcell–Morin ch2–3;
Griffiths §2–3 (anchor).

## Chapter 12 — Current and DC circuits; RC dynamics (~12 pp)

**Prerequisites:** ch11. **Sections:** 12.1 Current \(I=dq/dt\), current density
\(\mathbf j\), drift velocity (microscopic picture) · 12.2 Ohm's law: \(V=IR\),
\(\rho\) resistivity, temperature · 12.3 EMF \(\mathcal E\), internal resistance, real
batteries · 12.4 Kirchhoff's two rules — stated as conservation laws · 12.5 Equivalent
resistance; solving multi-loop circuits · 12.6 Power dissipation \(P=IV=I^2R=V^2/R\) ·
12.7 RC circuits: charge/discharge ODE derived and solved; energy audit (the \(\tfrac12\)
paradox) · 12.8 Meters and loading; Wheatstone bridge — *In engineering practice*.
**Worked examples:** (1) two-loop circuit solved by Kirchhoff — sign discipline shown;
(2) terminal voltage vs internal resistance from two measurements (data style);
(3) RC transient: derive \(q(t),i(t)\), find when the capacitor has half its final charge;
(4) energy audit of charging — where did half the battery's energy go?
**Figures (8):** drift-velocity microscopic picture; resistor \(I\)-\(V\) plot; battery +
internal resistance model; two-loop circuit with labelled loops; series/parallel reduction
small-multiple; RC \(q(t),i(t)\) curves; energy-flow diagram for charging; summary table.
**Code:** `ch12_rc_transient.py` — integrates RC charging numerically vs analytic, prints
measured \(\tau\); extension: square-wave response showing charging/discharging cycles.
**Exercises:** 4 inline + 12 additional. Plan: 4[easy] (Ohm's law + power (AP-C); series/
parallel reduction (AP-C); drift-velocity reasoning (AP-C); RC time-constant reading (F=ma))
· 6[medium] (multi-loop Kirchhoff solve (AP-C FR-style); internal resistance extraction
from data (F=ma data-style); bulb brightness ordering (F=ma classic); RC energy audit
(AP-C); Wheatstone balance condition (engineering); switch-throw reasoning at \(t=0,\infty\)
(AP-C)) · 2[hard] (infinite resistor ladder (USAPhO classic); cube of resistors across a
diagonal (APhO-style classic)).
**Common mistakes:** current vs voltage roles in branches; forgetting internal resistance;
power formula chosen wrongly for series vs parallel; \(Q\)-vs-\(\Delta V\) state at
\(t=0\) after long time; believing the capacitor "stores" all battery energy (audit!).
**Sources:** 8.02SC modules 12–15; AP-C U11; OpenStax v2 ch9–10; All About Circuits
(Book 5 cross-ref); PhET Circuit Construction Kit (visual anchor).

## Chapter 13 — Magnetic field: forces and sources (~12 pp)

**Prerequisites:** ch9, ch12. **Sections:** 13.1 Lorentz force \(\mathbf F=q\mathbf v\times
\mathbf B\); \(\mathbf B\) does no work — proof · 13.2 Circular and helical motion in uniform
\(\mathbf B\): \(r=mv/qB\), period independent of \(v\) · 13.3 Force and torque on currents;
magnetic moment \(\boldsymbol\mu=IA\hat{\mathbf n}\) · 13.4 Hall effect — the sign of the
charge carrier (engineering sensor note) · 13.5 Biot–Savart: the wire integral — *From the
laws* · 13.6 Ampère's law and its symmetry limits · 13.7 Solenoid and toroid fields.
**Worked examples:** (1) cyclotron radius/frequency + a mass-spectrometer design;
(2) torque on a rectangular loop — first step toward motors; (3) \(\mathbf B\) on the axis
of a current loop via Biot–Savart; (4) long solenoid via Ampère.
**Figures (8):** \(\mathbf v\times\mathbf B\) handedness figure; circular/helical
trajectories; current-loop torque diagram + \(\boldsymbol\mu\); Hall-voltage setup;
Biot–Savart geometry; field around a straight wire; Ampèrian loops gallery; solenoid field
map; summary table.
**Code:** `ch13_lorentz_orbit.py` — integrates \(q\mathbf v\times\mathbf B\) motion; shows
orbit radius vs theory and the energy drift of naive Euler (motivates Boris-style update,
noted honestly).
**Exercises:** 4 inline + 11 additional. Plan: 4[easy] (force direction MC (AP-C); cyclotron
scaling (AP-C); wire-segment force (AP-C); field of long wire (F=ma)) · 5[medium] (velocity
selector design (AP-C FR-style); loop torque/max \(\tau\) (AP-C); two-wire attraction/
repulsion (F=ma); mass-spectrometer reasoning (F=ma); Ampère for a coax cable
(engineering)) · 2[hard] (crossed-field trajectory — cycloid path (USAPhO-style); field of
a finite wire segment — limiting cases (APhO-style)).
**Common mistakes:** left- vs right-hand slip (negative charges!); believing \(\mathbf B\)
does work on a point charge; Ampère's law applied off-symmetry; \(\mu_0\) vs material
permeability; helix pitch ignored.
**Sources:** 8.02SC modules 16–20; AP-C U12; OpenStax v2 ch11–12; Purcell–Morin ch5–6;
Feynman II §13.

## Chapter 14 — Faraday's law, inductance, RL and RLC (~12 pp)

**Prerequisites:** ch12–13. **Sections:** 14.1 Flux \(\Phi_B\) and motional EMF — sliding
rod first · 14.2 Faraday's law \(\mathcal E=-d\Phi_B/dt\) · 14.3 Lenz's law — direction by
energy conservation · 14.4 Induced \(\mathbf E\) fields: circulation, non-conservative — the
conceptual leap · 14.5 Self- and mutual inductance; \(L\) of a solenoid derived · 14.6 RL
transients (ODE mirror of RC) · 14.7 Energy stored \(\tfrac12LI^2\) and \(u_B=B^2/2\mu_0\) ·
14.8 LC and driven RLC: the electric harmonic oscillator — resonance returns (ch7 link) ·
14.9 Eddy currents and magnetic braking — *In engineering practice*.
**Worked examples:** (1) sliding rod on rails: motional EMF, force, power audit — electrical
power generated = mechanical power dissipated; (2) RL energisation transient with time
constant; (3) RLC underdamped ringing — measured vs predicted \(\omega_d\); (4) solenoid
\(L\) from Ampère + energy density check.
**Figures (8):** four-way small-multiple of flux changes (move/rotate/grow/change B); Lenz
direction flowchart figure; induced-\(\mathbf E\) loops around a solenoid; RL transient
curves; LC/RLC energy sloshing diagram; eddy-current braking sketch; phasor diagram for
driven RLC; summary table.
**Code:** `ch14_rlc.py` — driven RLC integrator; sweeps drive frequency → resonance curve;
prints measured \(Q\) and compares with ch7 oscillator formula (the same mathematics).
**Exercises:** 4 inline + 11 additional. Plan: 4[easy] (flux sign and change (AP-C); Lenz
direction (AP-C); inductor energy (AP-C); RL time constant (F=ma)) · 5[medium] (sliding-rod
power audit (AP-C FR-style); loop entering a field region (F=ma); mutual inductance of
coaxial loops (AP-C); RLC ringing frequency (AP-C); transformer-primary reasoning preview
(engineering)) · 2[hard] (terminal velocity of a magnet falling in a conducting tube
(USAPhO-style); rotating loop EMF — generator waveform (APhO-style)).
**Common mistakes:** EMF sign/direction vs magnitude conflation; treating induced
\(\mathbf E\) as conservative (potential undefined!); \(\Phi_B\) vs \(B\) confusion;
double counting motional + transformer EMF; inductor "resists current" at all times myth.
**Sources:** 8.02SC modules 21–25; AP-C U13; OpenStax v2 ch13–15; Purcell–Morin ch7–8;
Griffiths §7 (anchor); PhET Faraday's Law (visual anchor).

---

# Part III — Maxwell, waves and heat

## Chapter 15 — Maxwell's equations and electromagnetic waves (~11 pp)

**Prerequisites:** ch10, ch14. **Sections:** 15.1 The four equations assembled — one line of
physical reading each (integral form) · 15.2 The displacement current: the charging-capacitor
paradox and its fix — *From the laws* · 15.3 The wave equation sketch: how changing
\(\mathbf E\) and \(\mathbf B\) sustain each other · 15.4 Plane waves: \(E=cB\), energy
density, Poynting vector \(\mathbf S\) · 15.5 The spectrum and light as the same physics ·
15.6 Radiation pressure and momentum (order-of-magnitude).
**Worked examples:** (1) displacement current between charging capacitor plates — computed
to equal \(I\); (2) evaluating \(1/\sqrt{\mu_0\epsilon_0}\) and recognising \(c\);
(3) Poynting flux into a charging capacitor — where the field energy "enters".
**Figures (7):** the four equations in one diagram; charging-capacitor Amperian paradox
figure; plane-wave snapshot with \(\mathbf E,\mathbf B,\mathbf S\) orthogonal; EM spectrum
log chart; energy-flow-into-resistor field picture; summary table.
**Code:** `ch15_em_pulse.py` — 1-D scalar wave-equation integrator standing in for Maxwell
(simplified, stated honestly); measures propagation speed of a pulse on the discrete
lattice and compares with the analytic wave speed.
**Exercises:** 3 inline + 10 additional. Plan: 4[easy] (identify the equation for each
statement (AP-C); \(E/B\) ratio in a wave (AP-C); spectrum ordering (F=ma); Poynting
direction (AP-C)) · 4[medium] (displacement current magnitude (AP-C FR-style); wave energy
density numeric (AP-C); energy into a capacitor via \(\mathbf S\) (F=ma); polarization
reasoning (AP-C)) · 2[hard] (radiation pressure on a solar sail estimate
(estimation/USAPhO-style); standing EM wave between plates — nodes reasoning (APhO-style)).
**Common mistakes:** displacement current is not charge flow; \(\mathbf B\)-does-no-work
carried wrongly into waves; thinking wires deliver energy (the *fields* do — \(\mathbf S\)
figure); forgetting which equation has no magnetic monopole term.
**Sources:** 8.02SC modules 26–30; OpenStax v2 ch16; Purcell–Morin ch9; Griffiths §7
(anchor); Feynman II §18,§27.

## Chapter 16 — Waves and optics essentials (~11 pp)

**Prerequisites:** ch7, ch15. **Sections:** 16.1 Wave quantities: \(v=\lambda f\), the
travelling wave \(y(x,t)=A\cos(kx-\omega t)\) · 16.2 Waves on strings; reflection at
boundaries · 16.3 Superposition → standing waves, harmonics · 16.4 Sound and the Doppler
shift (compact) · 16.5 Light as an EM wave; interference: two-slit · 16.6 Thin-film and
phase change (compact) · 16.7 Diffraction: single slit, why \(a\sin\theta=\lambda\) matters,
Rayleigh criterion stated · 16.8 Polarisation.
**Worked examples:** (1) string harmonics — which modes a pinned-pinned string supports;
(2) two-slit fringe spacing from geometry; (3) soap-film colour condition derived with the
phase flip.
**Figures (8):** travelling-wave snapshots (3 frames); reflection at fixed/free ends;
standing-wave envelope with nodes; Doppler wavefronts; two-slit geometry + intensity;
single-slit intensity curve; thin-film rays; summary table.
**Code:** `ch16_superposition.py` — sums two counter-propagating sinusoids into a standing
wave (animated frames as a small multiple); extension: beats \(f_1+f_2\).
**Exercises:** 3 inline + 10 additional. Plan: 4[easy] (\(v=\lambda f\) (AP-C); node/antinode
reading (AP-C); harmonic numbering (AP-C); Doppler direction reasoning (F=ma)) ·
4[medium] (string tension from harmonics (AP-C FR-style); two-slit fringe spacing (AP-C);
thin-film order reasoning (APhO-lite); beat frequency (F=ma)) · 2[hard] (diffraction-limited
aperture resolution estimate (estimation); interference from three slits (USAPhO-style)).
**Common mistakes:** \(v=\lambda f\) misused across media (which quantity is invariant);
node vs antinode at a fixed end; interference ≠ diffraction; forgetting the \(\lambda/2\)
phase flip in thin films; Doppler numerator/denominator swap.
**Sources:** OpenStax v1 ch16–17, v3 ch1,3–4; Feynman I §30,§47–51; 8.02SC modules 31–32
(interference/diffraction tail).

## Chapter 17 — Thermodynamics essentials (~10 pp)

**Prerequisites:** ch4. **Sections:** 17.1 Temperature, thermal equilibrium, scales ·
17.2 Ideal gas \(PV=nRT\); microscopic pressure — *From the laws* · 17.3 Internal energy
and equipartition (monatomic: \(\tfrac32k_BT\) per particle) · 17.4 First law
\(\Delta E_\mathrm{int}=Q-W_\mathrm{by}\) — sign convention fixed and repeated · 17.5
Processes: isochoric, isobaric, isothermal, adiabatic on the \(PV\) plane · 17.6 Heat
engines; the Carnot bound \(\eta\le1-T_C/T_H\) derived for the ideal gas cycle · 17.7
Second law and entropy — statistical reading in one page.
**Worked examples:** (1) work integral for isothermal expansion + audit \(Q=W\);
(2) Carnot cycle efficiency derived stepwise on \(PV\); (3) a two-process cycle: net work
from the enclosed area.
**Figures (7):** \(PV\) plane with the four processes; cycle-with-enclosed-area figure;
\(T\)-\(S\) sketch for Carnot; kinetic-theory wall-collision picture; engine schematic
(reservoirs); Maxwell–Boltzmann distribution from code; summary table.
**Code:** `ch17_maxwell_boltzmann.py` — samples 2-D gas speeds (or velocity exchange
micro-sim), histograms the distribution vs theory; prints mean kinetic energy vs
\(\tfrac32k_BT\).
**Exercises:** 3 inline + 10 additional. Plan: 4[easy] (ideal-gas state change (AP-style);
first-law sign reading (AP-C); process recognition on \(PV\) (F=ma); \(C_V\) vs \(C_P\)
concept (AP-C)) · 4[medium] (adiabatic work and \(\Delta T\) (AP-C FR-style); cycle net work
(F=ma); efficiency bound numeric (F=ma); entropy of isothermal expansion (USAPhO-lite)) ·
2[hard] (free expansion reasoning — \(Q=W=0\), \(S\) increases anyway (USAPhO-style);
engine between finite reservoirs — cooling source (APhO-style)).
**Common mistakes:** sign of \(W\) (done *by* gas — our fixed convention); \(Q=0\) ≠
\(\Delta T=0\) (adiabatic ≠ isothermal); \(\eta=1-Q_C/Q_H\) vs Carnot bound conflated;
Celsius/Kelvin slips in ratios; entropy "disorder" mysticism vs counting states.
**Sources:** OpenStax v2 ch1–4; Feynman I §39–45; Krotov heat section (problem style);
F=ma scope note (data analysis).

---

# Part IV — Engineering synthesis

## Chapter 18 — Power conversion: where mechanics meets the grid (~9 pp)

**Prerequisites:** ch14, ch15, ch17. **Sections:** 18.1 Why AC won: \(I^2R\) transmission
losses vs voltage · 18.2 The generator: Faraday → terminal EMF; mechanical input audit ·
18.3 The motor: loop torque → continuous rotation; back-EMF is not optional · 18.4 The
transformer: flux linkage, ideal ratio laws, why it needs AC · 18.5 Switch-mode conversion:
the buck converter as an energy-shuttle (inductor volt-second balance) — *In engineering
practice* anchor · 18.6 Rectification, RMS vs peak, power factor (one page) · 18.7 Safety:
mains and high-current work requires supervision (boxed note).
**Worked examples:** (1) transmission loss vs voltage scaling — why 400 kV; (2) DC motor
no-load speed and stall current from \(K_v,K_t\); (3) ideal transformer turns ratio with a
loaded secondary; (4) buck converter: output voltage and inductor ripple from duty cycle.
**Figures (8):** grid block diagram (plant→transmission→distribution→load); generator/motor
duality figure; transformer circuitikz schematic; motor torque–speed and back-EMF curves;
buck-converter topology + inductor-current waveform; \(I^2R\) vs voltage log plot; RMS/peak
waveform; summary table.
**Code:** `ch18_motor_start.py` — DC motor ODEs (electrical + mechanical with back-EMF);
prints inrush vs steady current, torque–speed operating point; extension cell: buck
converter ripple integration.
**Exercises:** 3 inline + 10 additional. Plan: 4[easy] (loss scaling arithmetic (AP-C);
transformer ratio (AP-C); motor back-EMF direction (engineering); RMS vs peak (F=ma)) ·
4[medium] (transmission-voltage optimisation estimate (F=ma/engineering); motor torque–
speed operating point (engineering); converter duty reasoning (engineering); generator
terminal voltage sag (AP-C)) · 2[hard] (motor + load transient stability estimate
(USAPhO-style); transformer non-idealities — where the ideal model leaks (APhO-style)).
**Common mistakes:** motor modelled as a resistor (back-EMF ignored); ideal transformer
"creating" power; higher voltage = safer/dirtier intuition backwards; RMS/peak mix-ups;
forgetting the inductor's volt-second balance.
**Sources:** 8.02SC modules 21–25 (induction→machines link); OpenStax v2 ch13–15;
Purcell–Morin ch7–8; Book 5 cross-references (named, e.g. "see Book 5 ch. power supplies").

---

# Part V — The workshop: twenty contest problems (~15 pp)

**Placement decision:** gathered at the end as its own part — contests mix topics and the
problems are deliberately multi-chapter (e.g., energy + rolling + friction; Faraday +
mechanics + power audit). Structure borrowed from Gnädig/Krotov: **problems** (with
rating + resemblance tag) → **hints** (one line each, at back) → **full solutions**
(Strategy → Solution → Significance, ~0.7 pp each).

**Planned problem set (all original; resemblance tags, not copies):**

| # | Topic blend | Rating | Resembles |
|---|---|---|---|
| W1 | projectile + drag bound (when does drag matter?) | medium | F=ma data-style |
| W2 | constraint/pulley with friction — boundary cases | medium | F=ma |
| W3 | collision + projectile composite | medium | F=ma |
| W4 | elastic + inelastic chain, energy audit | medium | AP-C FR-style |
| W5 | rolling + statics: spool/thread problem | hard | APhO-style |
| W6 | physical pendulum + measurement design | medium | F=ma data |
| W7 | orbit + energy + transfer bookkeeping | medium | F=ma |
| W8 | orbit + angular momentum: satellite capture | hard | USAPhO |
| W9 | gravitation + oscillation: tunnel through Earth | hard | USAPhO classic |
| W10 | momentum + variable mass: sand hopper | hard | APhO-style |
| W11 | field integration + symmetry shortcut | medium | AP-C FR |
| W12 | Gauss + conductors: induced charges | hard | USAPhO |
| W13 | potential + energy: charge release and speed | medium | F=ma |
| W14 | capacitor + dielectric + work audit | hard | APhO-style |
| W15 | circuit + measurement: non-ideal meter | medium | F=ma data |
| W16 | RC transient + energy audit paradox | hard | USAPhO |
| W17 | B-field motion: crossed fields, design a selector | medium | AP-C FR |
| W18 | Faraday + mechanics: falling rod terminal velocity | hard | USAPhO classic |
| W19 | RLC + oscillation: the same maths twice | medium | AP-C |
| W20 | power conversion: loss-minimising design estimate | hard | estimation |

Plus ~1 pp of contest method up front (units-first checks, limiting cases, estimation
habits, when to integrate vs conserve).

## Back matter (~18 pp)

- **Hints** for every `[hard]` exercise and all W-problems (one–two lines each) ·
- **Solutions** to at least half of all exercises (every odd-numbered, plus all worked
  capstone problems in full) · **Appendix A** — fluids essentials (F=ma scope, ~5 pp,
  optional) · **Appendix B** — integrals and the three vector-calculus facts actually used
  (~2 pp) · numbered **bibliography** · **index**.

## Per-chapter source map (abbreviated)

ch1–8: MIT 8.01SC (Dourmashkin notes) + AP-C Mechanics CED + Morin + OpenStax v1 + Feynman
I; ch9–14: 8.02SC + AP-C E&M CED + Purcell–Morin + OpenStax v2 + Griffiths + Feynman II;
ch15–16: 8.02SC + OpenStax v2/v3 + Feynman II/I; ch17: OpenStax v2 + Feynman I + Krotov;
ch18: 8.02SC + OpenStax v2 + Book 5 cross-refs; Part V: F=ma/USAPhO formats (AAPT),
Gnädig/Krotov problem-register — all problems original.
