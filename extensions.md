# Research checks and possible extensions

This file is deliberately a work log, not a list of established results. Every claim must
be checked against the paper, especially its appendices.

## Immediate checks for this week

1. Reproduce the first-order condition
   $p'(se^*;\theta)s\alpha\Delta=c'(e^*;\theta)$ and state exactly when it is
   valid (interior versus corner solution).
2. Re-derive the envelope-theorem step in Proposition 2. Explain why the indirect
   effect through $e^*(\theta)$ drops out at the optimum.
3. Verify the geometric sum that yields $V_0=\gamma_0M(e^*;\theta)/(1-\delta\gamma)$.
4. Reproduce the derivative of $\operatorname{Var}(V(\theta))$ and check the
   inequality that makes its intercept negative.
5. Distinguish absolute inequality $\operatorname{Var}(V)$ from relative inequality
   measured by the coefficient of variation.

## The variance trap

Do not write "variance is U-shaped in AI" without qualifications. The paper's Proposition 3
uses a specific functional form, independence assumptions, positive-support restrictions,
and the heterogeneity condition

$$
\frac{\mathbb{E}[\Gamma^2]}{\mathbb{E}[\Gamma]^2}
< \mu_s\mathbb{E}[1/s].
$$

The object is the cross-sectional variance of continuation value $V(\theta)$. The
individual tool benefit and the coefficient of variation are different objects.

## Candidate extensions (not yet adjudicated)

- Correlation between implementation skill and opportunity judgment instead of independence.
- Corner solutions when optimal effort reaches zero.
- Alternative success and cost functions beyond the square-root specification.
- Endogenous opportunity discovery effort rather than exogenous $\gamma(t)$.

Before calling any item an extension, search the appendices and related literature.
