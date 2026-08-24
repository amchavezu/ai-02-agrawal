# Proposition 3 and a correlated-skills extension

This note separates three layers: what the paper assumes, what follows algebraically, and
what changes in the extension. The source is Agrawal, Gans, and Goldfarb (2025), Section 4
and Appendix A.3, especially equations (30), (34), and (57)-(94).

## 1. Paper setup and conditions

For the inequality result, the paper adds the following restrictions:

1. The success function and effort cost are
   \[
   p(se;\theta)=\sqrt{se+\theta},\qquad c(e)=e.
   \]
2. The agent has payoff judgment \(\alpha>0\), implementation skill \(s>0\), and gain
   \(\Delta>0\). The parameter restriction is intended to keep the solution interior over
   the tool-quality range being compared.
3. Opportunity probabilities satisfy \(\gamma(0)=\gamma_0\) and
   \(\gamma(t)=\gamma\) for \(t>0\), with \(\delta\gamma<1\).
4. The paper assumes \(\alpha,\gamma_0,\gamma,s\) are mutually independent, have positive
   support, and satisfy \(\mu_i>3\sigma_i\).
5. Tool quality is treated as continuous, \(\theta\geq0\).

Define the opportunity multiplier

\[
\Gamma=\frac{\gamma_0}{1-\delta\gamma}.
\]

## 2. Optimal effort and continuation value

At one opportunity the agent solves

\[
\max_{e\geq0}\;M(e;\theta)
=\alpha\Delta\sqrt{se+\theta}-e.
\]

For an interior solution, differentiate with respect to \(e\):

\[
\frac{\partial M}{\partial e}
=\frac{\alpha\Delta s}{2\sqrt{se+\theta}}-1=0.
\]

Therefore

\[
\sqrt{se^*+\theta}=\frac{\alpha\Delta s}{2},
\]

and, after squaring and solving for effort,

\[
e^*(\theta)=\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s}.
\]

The second derivative is negative,

\[
\frac{\partial^2M}{\partial e^2}
=-\frac{\alpha\Delta s^2}{4(se+\theta)^{3/2}}<0,
\]

so the interior stationary point is the unique maximum whenever \(e^*(\theta)>0\).
Substitution into \(M\) gives

\[
M(\theta)=\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}.
\]

The discounted continuation value is

\[
V(\theta)=\Gamma M(\theta)
=\Gamma\left(\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}\right).
\]

This is equation (34) of the paper.

## 3. A shorter derivation of the variance result

Define

\[
H=\frac{\Delta^2}{4}\Gamma\alpha^2s,
\qquad
Z=\frac{\Gamma}{s}.
\]

Then the entire variance problem is the affine random-variable identity

\[
V(\theta)=H+\theta Z.
\]

Subtract its expectation:

\[
V(\theta)-\mathbb E[V(\theta)]
=(H-\mathbb E[H])+\theta(Z-\mathbb E[Z]).
\]

Square and take expectations:

\[
\boxed{
\operatorname{Var}(V(\theta))
=\operatorname{Var}(H)
+2\theta\operatorname{Cov}(H,Z)
+\theta^2\operatorname{Var}(Z)
}.
\]

Hence

\[
\boxed{
\frac{d\operatorname{Var}(V(\theta))}{d\theta}
=2\operatorname{Cov}(H,Z)+2\theta\operatorname{Var}(Z)
}
\]

and

\[
\frac{d^2\operatorname{Var}(V(\theta))}{d\theta^2}
=2\operatorname{Var}(Z)\geq0.
\]

If \(\operatorname{Var}(Z)>0\), the variance curve is strictly convex. It initially falls
exactly when

\[
\operatorname{Cov}(H,Z)<0,
\]

and its algebraic turning point is

\[
\boxed{
\theta^*=-\frac{\operatorname{Cov}(H,Z)}{\operatorname{Var}(Z)}
}.
\]

The interior-effort condition must still be checked at that value of \(\theta\); otherwise
the constrained corner \(e^*=0\) changes the formula.

## 4. Recovering the paper's independence condition

Let \(k=\Delta^2/4\). If \(\alpha\) is independent of the joint pair \((\Gamma,s)\), then

\[
HZ=k\alpha^2\Gamma^2,
\]

so

\[
\operatorname{Cov}(H,Z)
=k\mathbb E[\alpha^2]
\left(
\mathbb E[\Gamma^2]
-\mathbb E[\Gamma s]\mathbb E[\Gamma/s]
\right).
\]

Under the paper's additional independence of \(\Gamma\) and \(s\),

\[
\mathbb E[\Gamma s]=\mathbb E[\Gamma]\mathbb E[s],
\qquad
\mathbb E[\Gamma/s]=\mathbb E[\Gamma]\mathbb E[1/s].
\]

Therefore initial variance reduction is equivalent to

\[
\mathbb E[\Gamma^2]
<(\mathbb E[\Gamma])^2\mathbb E[s]\mathbb E[1/s],
\]

or

\[
\boxed{
\frac{\mathbb E[\Gamma^2]}{(\mathbb E[\Gamma])^2}
<\mu_s\mathbb E[1/s]
},
\]

which is exactly condition (30).

## 5. Extension: allow opportunity judgment and skill to be correlated

The professor does not prescribe one unique extension; the issue says that extensions,
simulations, and limiting cases are possible above-the-floor work. Here we relax only
\(\Gamma\perp s\), retaining \(\alpha\perp(\Gamma,s)\).

The mean effect becomes

\[
\mathbb E[V(\theta)]
=k\mathbb E[\alpha^2]\mathbb E[\Gamma s]
+\theta\mathbb E[\Gamma/s],
\]

so

\[
\frac{d\mathbb E[V(\theta)]}{d\theta}
=\mathbb E[\Gamma/s]>0.
\]

Thus the positive mean effect survives correlation because \(\Gamma/s\) has positive
support.

For variance, the paper's marginal condition must be replaced by the joint-moment condition

\[
\boxed{
\mathbb E[\Gamma^2]
<\mathbb E[\Gamma s]\mathbb E[\Gamma/s]
}.
\]

Correlation matters through both joint expectations. Marginal variances of \(\Gamma\) and
\(s\) alone no longer determine whether tool quality initially raises or lowers inequality.
The turning point becomes

\[
\boxed{
\theta^*=
\frac{k\mathbb E[\alpha^2]
\left(
\mathbb E[\Gamma s]\mathbb E[\Gamma/s]-\mathbb E[\Gamma^2]
\right)}
{\operatorname{Var}(\Gamma/s)}
}
\]

when the numerator is positive and \(\operatorname{Var}(\Gamma/s)>0\).

## 6. The paper's internal slip and a counterexample

Condition (30) implies

\[
\left.\frac{d\operatorname{Var}(V(\theta))}{d\theta}\right|_{\theta=0}<0
\quad\text{and}\quad \theta^*>0.
\]

It does **not** by itself imply the displayed statement in Proposition 3(b)

\[
\left.\frac{d\operatorname{Var}(V(\theta))}{d\theta}\right|_{\theta=1}>0.
\]

That stronger statement also requires

\[
\boxed{\theta^*<1}.
\]

Equivalently,

\[
\operatorname{Cov}(H,Z)+\operatorname{Var}(Z)>0.
\]

Here is a counterexample with independent \(\Gamma\) and \(s\):

\[
\alpha=0.8,\quad \Delta=4,\quad \Gamma=1,
\quad
s=\begin{cases}0.7&\text{with probability }1/2,\\1&\text{with probability }1/2.\end{cases}
\]

Then

\[
\mu_s\mathbb E[1/s]
=\frac{17}{20}\frac{17}{14}
=\frac{289}{280}>1
=\frac{\mathbb E[\Gamma^2]}{(\mathbb E[\Gamma])^2},
\]

so condition (30) holds. But

\[
\operatorname{Cov}(H,Z)=-\frac{72}{875},
\qquad
\operatorname{Var}(Z)=\frac{9}{196},
\]

and therefore

\[
\theta^*=-\frac{\operatorname{Cov}(H,Z)}{\operatorname{Var}(Z)}
=\frac{1568}{875}=1.792>1.
\]

Consequently,

\[
\left.\frac{d\operatorname{Var}(V(\theta))}{d\theta}\right|_{\theta=1}
=2\left(-\frac{72}{875}+\frac{9}{196}\right)<0.
\]

The code in `code/variance_extension.py` reproduces this counterexample and two correlated
distributions. Its direct variance calculation is asserted to equal the quadratic identity
at every grid point.

## 7. Verdict for slide 4

**Verdict: the loose AI claim is incorrect, and the paper's displayed endpoint claim is
under-conditioned.** The variance object is \(\operatorname{Var}(V(\theta))\), the U-shape
requires a negative covariance/heterogeneity condition, and condition (30) only establishes
an initially negative slope and a positive algebraic turning point. A positive slope at
\(\theta=1\) additionally requires \(\theta^*<1\), with the interior solution valid over the
relevant range.
