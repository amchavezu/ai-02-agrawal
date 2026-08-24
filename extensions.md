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

## Completed extension: correlated opportunity judgment and skill

The paper assumes the opportunity multiplier $\Gamma$ is independent of implementation
skill $s$. The repository now relaxes that assumption while retaining
$\alpha\perp(\Gamma,s)$. Writing

$$
H=\frac{\Delta^2}{4}\Gamma\alpha^2s,
\qquad Z=\frac{\Gamma}{s},
\qquad V(\theta)=H+\theta Z,
$$

gives the general identity

$$
\operatorname{Var}(V(\theta))
=\operatorname{Var}(H)+2\theta\operatorname{Cov}(H,Z)
+\theta^2\operatorname{Var}(Z).
$$

Initial equalisation therefore requires

$$
\mathbb E[\Gamma^2]
<\mathbb E[\Gamma s]\mathbb E[\Gamma/s],
$$

not condition (30), which uses the extra independence restriction. The code contains two
correlated examples with the same skill marginal distribution: one has an initially falling
variance curve and the other an initially rising curve.

See `analysis/variance_derivation.md` for every algebraic step and
`output/variance_summary.txt` for the numerical results.

## Internal slip found

The appendix derives a negative intercept and positive slope for
$d\operatorname{Var}(V)/d\theta$. That proves a unique positive turning point, but it does
not prove that the derivative is positive specifically at $\theta=1$. The extra condition is
$\theta^*<1$. The repository's independent counterexample satisfies condition (30) while
$\theta^*=1.792$ and the derivative at one remains negative.

## Remaining candidates

- Treat the effort constraint explicitly when tool quality makes the interior solution hit
  the corner $e^*=0$.
- Allow payoff judgment $\alpha$ to correlate with $(\Gamma,s)$.
- Endogenise opportunity discovery effort instead of taking $\gamma(t)$ as given.
