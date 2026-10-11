# Notation — textbook-physics

Conventions for the whole book. Symbol collisions are listed with their local resolution
(project decision 2: never use a colliding symbol in two meanings within one chapter
without redefining it at the point of use). `log` = natural log throughout (decision 1).

## Conventions (chosen, stated once in the preface)

- **Vectors:** bold italic $\mathbf{F}$, $\mathbf{v}$, $\mathbf{E}$. Magnitude $F=|\mathbf F|$.
  Components $F_x,F_y,F_z$; column form $\begin{pmatrix}x\\y\end{pmatrix}$ when a matrix
  acts on it. Unit vectors $\hat{\mathbf x},\hat{\mathbf y},\hat{\mathbf z}$;
  $\hat{\mathbf r},\hat{\boldsymbol\theta}$ in polar; $\hat{\mathbf n}$ surface normal.
- **Derivatives:** Newton's dot for time, $\dot x=dx/dt$, $\ddot x=d^2x/dt^2$, after the
  first introduction of each quantity writes $dx/dt$ out in full. Angular rates
  $\omega=\dot\theta$, $\alpha=\dot\omega$. Partials $\partial f/\partial x$ where needed.
- **Units:** SI throughout, set with `siunitx` (`\qty{9.8}{\meter\per\second\squared}`)
  loaded in `main.tex` after `lifeos` (allowed extra package); fallback manual
  `\,\mathrm{m\,s^{-2}}`. Radians for all angles unless stated. $g=9.8\,\mathrm{m/s^2}$ in
  text; F=ma-styled problems set $g=10\,\mathrm{N/kg}$ like the exam.
- **Difficulty scheme:** `[easy]` ≈ AP-C multiple-choice / lower-half F=ma ·
  `[medium]` ≈ AP-C free-response part / upper F=ma · `[hard]` ≈ USAPhO / APhO short
  problem / Gnädig one-star+. Resemblance tags: `(AP-C)` `(F=ma)` `(USAPhO)`
  `(APhO-style)` `(estimation)` `(engineering)`.
- **Sign conventions:** work–energy in mechanics uses $W=\int\mathbf F\cdot d\mathbf r$
  with $\Delta K=W_\mathrm{net}$; in ch17 only, the first law is written
  $\Delta E_\mathrm{int}=Q-W_\mathrm{by}$ and "work done *by* the gas" is always tagged.
  CCW torque/rotation positive; current is conventional ($+q$ carriers) everywhere —
  electron flow noted only when the distinction matters (ch13 Hall effect).
- **Misc:** $i=\sqrt{-1}$ (not $j$ — that's current density here); $\approx$ approximate,
  $\propto$ proportional, $\sim$ order-of-magnitude; $\exp(i\omega t)$ phasors in ch14/18.

## Symbol table

| Symbol / macro | Meaning | First used |
|---|---|---|
| $\mathbf r$, $\Delta\mathbf r$ | position, displacement | ch1 |
| $\mathbf v=\dot{\mathbf r}$, $\mathbf a=\ddot{\mathbf r}$ | velocity, acceleration | ch1 |
| $g$, $\mathbf g$ | gravitational field strength / field | ch2, ch8 |
| $\mathbf F$, $\mathbf N$, $\mathbf T$, $\mathbf f$ | force; normal, tension, friction | ch2 |
| $k$ | spring constant (Hooke) | ch2 |
| $\mu_s$, $\mu_k$ | friction coefficients (static/kinetic) | ch2 |
| $D=\tfrac12\rho_f C_dAv^2$ | quadratic drag force; $C_d$ drag coefficient | ch2 |
| $\mathbf p=m\mathbf v$, $\mathbf J=\int\mathbf F\,dt$ | momentum, impulse | ch3 |
| $\mathbf R$, $M$ | centre-of-mass position, total mass | ch3 |
| $W$, $K$, $U$, $E$, $P$ | work, kinetic energy, potential energy, mechanical energy, power | ch4 |
| $\theta,\omega,\alpha$ | angular position/velocity/acceleration | ch5 |
| $\boldsymbol\tau=\mathbf r\times\mathbf F$ | torque | ch5 |
| $I$ | moment of inertia (see collision note: also current) | ch5 |
| $\mathbf L=\mathbf r\times\mathbf p$ | angular momentum | ch6 |
| $\omega_0$, $\omega_d$, $A$, $\phi$, $T$, $\beta$, $Q$ | natural/driving frequency, amplitude, phase, period, damping parameter, quality factor | ch7 |
| $G$, $U(r)=-GMm/r$ | gravitational constant, potential energy | ch8 |
| $q$, $Q$ | charge; $Q$ also heat in ch17 — resolved below | ch9 |
| $\lambda$, $\sigma$, $\rho$ | line / surface / volume **charge** density | ch9 |
| $\mathbf E$, $\Phi_E$ | electric field, electric flux | ch9–10 |
| $\epsilon_0$, $\kappa$ | vacuum permittivity, dielectric constant | ch10–11 |
| $p$ | electric dipole moment $p=qa$ (italic scalar in ch9 only; momentum stays bold $\mathbf p$) | ch9 |
| $V$, $\Delta V$, $\mathcal E$ | electric potential (volts), potential difference, EMF | ch11–12 |
| $C$ | capacitance (see collision note: also heat capacity ch17) | ch11 |
| $I$, $\mathbf j$ | current, current density | ch12 |
| $R$, $\rho$ (resistivity) | resistance, resistivity — $\rho$ reused locally, redefined in §12.2 | ch12 |
| $r$, $R_\mathrm{int}$ | internal resistance | ch12 |
| $\tau=RC$ | RC time constant (collision: also torque — always spelled "time constant $\tau$" vs $\boldsymbol\tau$) | ch12 |
| $\mathbf B$, $\Phi_B$, $\boldsymbol\mu=IA\hat{\mathbf n}$, $\mu_0$ | magnetic field, flux, dipole moment, vacuum permeability | ch13 |
| $L$ | inductance (collision: also $\mathbf L$ angular momentum — bold vs italic) | ch14 |
| $u_E=\tfrac{\epsilon_0}{2}E^2$, $u_B=\tfrac{1}{2\mu_0}B^2$ | field energy densities | ch14–15 |
| $\mathbf S=\mathbf E\times\mathbf B/\mu_0$ | Poynting vector | ch15 |
| $c$ | speed of light ($c$ never used for drag — see $D$ above) | ch15 |
| $k=2\pi/\lambda$, $\lambda$, $f$ | wavenumber (collision: also spring constant — waves only in ch16, redefined at §16.1), wavelength, frequency | ch16 |
| $n$ | index of refraction | ch16 |
| $T$, $p$, $n_\mathrm{mol}$, $E_\mathrm{int}$, $Q$, $W_\mathrm{by}$, $C_V,C_P$, $\eta$, $S$ | temperature, pressure, moles, internal energy, heat, work by gas, heat capacities, efficiency, entropy | ch17 |
| $N$, $K_v$, $K_t$, $D$ (duty cycle) | transformer turns, motor velocity/torque constants, converter duty | ch18 |
| $\rho_m$, $\rho_f$ | mass density, fluid density (subscripted whenever charge density could appear nearby) | App A |

## Declared collisions and resolutions

- $\mathbf p$: momentum everywhere (bold vector); the electric dipole moment is italic
  scalar $p$ inside ch9 only, where momentum never appears in vector form.
- $\mathbf J$: impulse (mechanics); current density is $\mathbf j$.
- $L$: inductance vs $\mathbf L$ angular momentum — bold/italic distinguishes; in ch14
  $L$ is redefined as inductance at first use.
- $Q$: heat (ch17) vs charge — charge stays lowercase $q$ except enclosed charge
  $Q_\mathrm{encl}$; heat $Q$ only in ch17.
- $U$: potential energy (parts I–II) vs internal energy — internal energy is
  $E_\mathrm{int}$ (ch17), never $U$.
- $T$: period (ch7) vs temperature (ch17) — ch17 redefines $T$ at first use.
- $P$: power vs pressure — pressure is $p$ (lowercase, ch17).
- $k$: spring constant vs wavenumber — wavenumber only in ch16, redefined at §16.1.
- $\rho$: volume charge density vs resistivity vs mass density — resistivity $\rho$
  is redefined locally in §12.2; mass/fluid density always subscripted
  ($\rho_m,\rho_f$).
- $\boldsymbol\mu$: magnetic dipole moment vs $\mu_s,\mu_k$ friction vs $\mu_0$
  permeability — always bold/subscripted as shown.
- $\tau$: RC/RL time constant vs $\boldsymbol\tau$ torque — plain vs bold.
- $C$: capacitance vs heat capacities $C_V,C_P$ (subscripted in ch17).
- $\omega$: angular velocity vs angular frequency vs driving frequency — subscript
  $\omega_0,\omega_d$ whenever ambiguity could arise.
