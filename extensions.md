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

## Student-chosen extension: correlated opportunity judgment and implementation skill

### Status and scope

This is **not** a proposition in the paper and **not** an extension assigned by the
professor. The course instructions allow students to choose an extension as above-minimum
work; this repository develops one such extension. We relax only

$$
\Gamma\not\!\perp s,
$$

while maintaining

$$
\alpha\perp(\Gamma,s).
$$

Assume positive support and that every joint moment displayed below is finite.

We retain the paper's interior-value formula

$$
V(\theta)=\Gamma\left(
\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}
\right).
\tag{E1}
$$

Consequently, all results below apply only while the interior effort solution is valid.
If an agent reaches $e^*=0$, the piecewise solution in
`analysis/variance_derivation.md` must replace (E1).

### Notation

Let

$$
k=\frac{\Delta^2}{4},
\qquad
a_2=\mathbb E[\alpha^2],
\qquad
a_4=\mathbb E[\alpha^4],
$$

and define joint moments

$$
m_{q,r}=\mathbb E[\Gamma^q s^r].
\tag{E2}
$$

The moments used below are

$$
\begin{aligned}
m_{1,1}&=\mathbb E[\Gamma s],
&m_{1,-1}&=\mathbb E[\Gamma/s],\\
m_{2,2}&=\mathbb E[\Gamma^2s^2],
&m_{2,0}&=\mathbb E[\Gamma^2],\\
m_{2,-2}&=\mathbb E[\Gamma^2/s^2].
\end{aligned}
\tag{E3}
$$

As in the variance audit, write

$$
H=k\Gamma\alpha^2s,
\qquad
Z=\frac{\Gamma}{s},
\qquad
V(\theta)=H+\theta Z.
\tag{E4}
$$

Economically, $H$ is baseline continuation value and $Z$ is the loading on an incremental
improvement in tool quality.

### 1. New expected value

Start from linearity:

$$
\mathbb E[V(\theta)]
=\mathbb E[H]+\theta\mathbb E[Z].
\tag{E5}
$$

Because $\alpha$ is independent of the pair $(\Gamma,s)$,

$$
\begin{aligned}
\mathbb E[H]
&=k\mathbb E[\alpha^2\Gamma s]\\
&=k\mathbb E[\alpha^2]\mathbb E[\Gamma s]\\
&=ka_2m_{1,1}.
\end{aligned}
\tag{E6}
$$

No independence assumption is needed for the second term:

$$
\mathbb E[Z]=\mathbb E[\Gamma/s]=m_{1,-1}.
\tag{E7}
$$

Therefore,

$$
\boxed{
\mathbb E[V(\theta)]
=ka_2m_{1,1}+\theta m_{1,-1}.
}
\tag{E8}
$$

Since $\Gamma>0$ and $s>0$,

$$
\frac{d\mathbb E[V(\theta)]}{d\theta}
=m_{1,-1}>0.
\tag{E9}
$$

Thus correlation changes the magnitude of the mean effect but not its positive sign in the
interior region.

### 2. New variance

First use the identity that does not require independence:

$$
\operatorname{Var}(V(\theta))
=\operatorname{Var}(H)
+2\theta\operatorname{Cov}(H,Z)
+\theta^2\operatorname{Var}(Z).
\tag{E10}
$$

Compute each coefficient separately.

For the constant term,

$$
H^2=k^2\alpha^4\Gamma^2s^2.
$$

Independence of $\alpha$ from $(\Gamma,s)$ gives

$$
\mathbb E[H^2]=k^2a_4m_{2,2},
$$

and hence

$$
\boxed{
\operatorname{Var}(H)
=k^2\left(a_4m_{2,2}-a_2^2m_{1,1}^2\right).
}
\tag{E11}
$$

For the quadratic term,

$$
\boxed{
\operatorname{Var}(Z)
=m_{2,-2}-m_{1,-1}^2.
}
\tag{E12}
$$

For the cross term, simplify before taking expectations:

$$
HZ
=\left(k\Gamma\alpha^2s\right)\left(\frac{\Gamma}{s}\right)
=k\alpha^2\Gamma^2.
\tag{E13}
$$

Therefore,

$$
\mathbb E[HZ]=ka_2m_{2,0},
$$

while

$$
\mathbb E[H]\mathbb E[Z]
=ka_2m_{1,1}m_{1,-1}.
$$

Thus

$$
\boxed{
\operatorname{Cov}(H,Z)
=ka_2\left(m_{2,0}-m_{1,1}m_{1,-1}\right).
}
\tag{E14}
$$

Substitution into (E10) yields the full result:

$$
\boxed{
\begin{aligned}
\operatorname{Var}(V(\theta))
={}&k^2\left(a_4m_{2,2}-a_2^2m_{1,1}^2\right)\\
&+2\theta ka_2
\left(m_{2,0}-m_{1,1}m_{1,-1}\right)\\
&+\theta^2\left(m_{2,-2}-m_{1,-1}^2\right).
\end{aligned}
}
\tag{E15}
$$

The first two derivatives are

$$
\boxed{
\frac{d\operatorname{Var}(V(\theta))}{d\theta}
=2ka_2\left(m_{2,0}-m_{1,1}m_{1,-1}\right)
+2\theta\left(m_{2,-2}-m_{1,-1}^2\right)
}
\tag{E16}
$$

and

$$
\boxed{
\frac{d^2\operatorname{Var}(V(\theta))}{d\theta^2}
=2\left(m_{2,-2}-m_{1,-1}^2\right)
=2\operatorname{Var}(\Gamma/s)\geq0.
}
\tag{E17}
$$

Strict convexity requires $\operatorname{Var}(\Gamma/s)>0$.

### 3. Joint condition for an initial variance decline

At $\theta=0$, equation (E16) becomes

$$
\left.
\frac{d\operatorname{Var}(V(\theta))}{d\theta}
\right|_{\theta=0}
=2ka_2\left(m_{2,0}-m_{1,1}m_{1,-1}\right).
\tag{E18}
$$

Because $k>0$ and $a_2>0$, the slope is negative if and only if

$$
\boxed{
\mathbb E[\Gamma^2]
<\mathbb E[\Gamma s]\mathbb E[\Gamma/s].
}
\tag{E19}
$$

This is a condition on the **joint distribution** of $(\Gamma,s)$.

### 4. New turning point

Suppose that (E19) holds and

$$
\operatorname{Var}(\Gamma/s)>0.
$$

Set (E16) equal to zero and solve for $\theta$:

$$
\boxed{
\theta^*_{\mathrm{corr}}
=\frac{ka_2
\left[
\mathbb E[\Gamma s]\mathbb E[\Gamma/s]
-\mathbb E[\Gamma^2]
\right]}
{\operatorname{Var}(\Gamma/s)}.
}
\tag{E20}
$$

The numerator is positive under (E19), so $\theta^*_{\mathrm{corr}}>0$. Within the
common interior region,

$$
\frac{d\operatorname{Var}(V(\theta))}{d\theta}
=2\operatorname{Var}(\Gamma/s)
\left(\theta-\theta^*_{\mathrm{corr}}\right).
\tag{E21}
$$

The variance falls before the turning point and rises after it. This statement does not show
that $\theta^*_{\mathrm{corr}}<1$, nor that the turning point occurs before an effort corner.

### 5. Comparison with condition (30) and why marginals are insufficient

Under the paper's independence assumption $\Gamma\perp s$,

$$
\mathbb E[\Gamma s]
=\mathbb E[\Gamma]\mathbb E[s]
$$

and

$$
\mathbb E[\Gamma/s]
=\mathbb E[\Gamma]\mathbb E[1/s].
$$

Then (E19) becomes

$$
\mathbb E[\Gamma^2]
<\mathbb E[\Gamma]^2\mathbb E[s]\mathbb E[1/s].
$$

Dividing by $\mathbb E[\Gamma]^2>0$ gives

$$
\boxed{
\frac{\mathbb E[\Gamma^2]}{\mathbb E[\Gamma]^2}
<\mu_s\mathbb E[1/s],
}
$$

which is exactly condition (30). Therefore, condition (30) is the independence special
case of (E19); it is not the correct general condition after independence is relaxed.

To see what dependence adds, define

$$
C_s=\operatorname{Cov}(\Gamma,s),
\qquad
C_{-1}=\operatorname{Cov}(\Gamma,1/s).
$$

Then

$$
\mathbb E[\Gamma s]
=\mathbb E[\Gamma]\mathbb E[s]+C_s
$$

and

$$
\mathbb E[\Gamma/s]
=\mathbb E[\Gamma]\mathbb E[1/s]+C_{-1}.
$$

Relative to independence, the product on the right side of (E19) changes by

$$
\boxed{
\mathbb E[\Gamma]\mathbb E[s]C_{-1}
+\mathbb E[\Gamma]\mathbb E[1/s]C_s
+C_sC_{-1}.
}
\tag{E22}
$$

Neither $C_s$ nor $C_{-1}$ is determined by the two marginal distributions. Their values
depend on how ranks of $\Gamma$ and $s$ are matched. Thus two populations can have the
same marginal distribution of opportunity judgment and the same marginal distribution of
implementation skill, yet have opposite initial variance effects.

#### Exact same-marginals example

Let each of three types have probability $1/3$, and fix the marginal distributions

$$
s\in\left\{\frac12,\frac34,1\right\},
\qquad
\Gamma\in\left\{\frac7{10},1,\frac32\right\}.
$$

Only the pairing changes:

| Joint distribution | $\operatorname{Cov}(\Gamma,s)$ | $\mathbb E[\Gamma^2]-\mathbb E[\Gamma s]\mathbb E[\Gamma/s]$ | Initial effect |
|---|---:|---:|---|
| $(s,\Gamma)=(1/2,3/2),(3/4,7/10),(1,1)$ | $-1/24$ | $-1/2700$ | variance falls |
| $(s,\Gamma)=(1/2,7/10),(3/4,3/2),(1,1)$ | $1/40$ | $11/300$ | variance rises |

The two rows have exactly the same marginals for both variables. Their different signs
therefore come only from the dependence structure. This is a direct counterexample to any
claim that marginal means and variances alone determine the initial inequality effect.

### 6. Economic interpretation of positive and negative correlation

The sign of the initial effect is best understood through

$$
\operatorname{Cov}(H,Z).
$$

- If this covariance is negative, agents with high baseline value $H$ tend to have a low
  marginal tool loading $Z$. Improvements initially catch lower-value agents up, so
  cross-sectional variance falls.
- If this covariance is positive, agents with high baseline value also receive the larger
  marginal tool gain. Improvements initially reinforce existing differences, so variance
  rises.

Correlation between $\Gamma$ and $s$ affects both objects in opposite algebraic ways:

$$
H\propto\Gamma s,
\qquad
Z=\Gamma/s.
$$

With positive correlation, high-implementation-skill agents also tend to have high
opportunity multipliers. This strongly raises their baseline component $\Gamma s$.
However, high $s$ reduces the tool loading through the denominator of $\Gamma/s$, while
high $\Gamma$ raises it. Which force dominates is not determined by the correlation sign.

With negative correlation, low-implementation-skill agents tend to have high opportunity
multipliers. This can make $\Gamma/s$ especially large precisely for initially disadvantaged
agents and produce a strong equalising force. But the same dependence also changes
$\Gamma s$, so negative correlation is not by itself sufficient for an initial decline.

Therefore, “positive correlation raises inequality” and “negative correlation lowers
inequality” are useful intuitions in some parameterisations, but neither is a theorem. The
theorem-like statement is the joint-moment inequality (E19).

### 7. Important limiting cases

#### 7.1. Independence

If $\Gamma\perp s$, the extension collapses exactly to condition (30) and to the paper's
turning-point formula. This is the benchmark, not a separate result.

#### 7.2. Homogeneous opportunity multiplier

If $\Gamma=\bar\Gamma$ is constant, (E19) reduces to

$$
1<\mathbb E[s]\mathbb E[1/s].
$$

By Cauchy--Schwarz, the weak inequality is always true and is strict when $s$ is
nonconstant. Hence heterogeneous implementation skill generates an initial decline. The
turning point becomes

$$
\boxed{
\theta^*
=ka_2\frac{\mathbb E[s]\mathbb E[1/s]-1}
{\operatorname{Var}(1/s)}.
}
\tag{E23}
$$

#### 7.3. Homogeneous implementation skill

If $s=\bar s$ is constant, the right side of (E19) is

$$
\mathbb E[\Gamma s]\mathbb E[\Gamma/s]
=\mathbb E[\Gamma]^2.
$$

Since $\mathbb E[\Gamma^2]\geq\mathbb E[\Gamma]^2$, an initial decline is impossible.
If $\Gamma$ is nonconstant, the initial slope is strictly positive.

#### 7.4. Proportional dependence: $\Gamma=\lambda s$

Then

$$
Z=\frac{\Gamma}{s}=\lambda
$$

is constant. Consequently,

$$
\operatorname{Var}(Z)=0,
\qquad
\operatorname{Cov}(H,Z)=0,
$$

and $\operatorname{Var}(V(\theta))=\operatorname{Var}(H)$ throughout the interior
region. There is no turning point: the tool adds the same amount to every agent.

#### 7.5. Inverse dependence: $\Gamma=\lambda/s$

Here $\Gamma s=\lambda$, so

$$
H=k\lambda\alpha^2.
$$

Because $\alpha$ is independent of $s$, $H$ is independent of
$Z=\lambda/s^2$. Therefore,

$$
\operatorname{Cov}(H,Z)=0.
$$

The initial slope is zero and

$$
\operatorname{Var}(V(\theta))
=\operatorname{Var}(H)+\theta^2\operatorname{Var}(\lambda/s^2).
$$

Variance rises for every $\theta>0$ when $s$ is nonconstant.

#### 7.6. Equality and degeneracy

If
$$
\mathbb E[\Gamma^2]
=\mathbb E[\Gamma s]\mathbb E[\Gamma/s],
$$

the initial slope is zero. If $\operatorname{Var}(\Gamma/s)>0$, variance rises
quadratically immediately after zero. If $\operatorname{Var}(\Gamma/s)=0$, the variance
is constant in the interior region.

#### 7.7. Role of payoff judgment

Under $\alpha\perp(\Gamma,s)$, heterogeneity in $\alpha$ does not affect the sign of
(E19): $a_2>0$ only scales the initial slope. It does affect the level of variance through
$a_4$ and the location of the turning point through $a_2$. Correlating $\alpha$ with the
pair would require a different extension.

### Extension verdict

Relaxing $\Gamma\perp s$ preserves the affine structure $V=H+\theta Z$ but replaces the
paper's marginal-moment condition with the joint-moment condition (E19). The relevant
economic object is whether baseline value $\Gamma s$ (also scaled by independent
$\alpha^2$) covaries negatively or positively with marginal tool exposure $\Gamma/s$.
Marginals alone cannot answer that question.

The existing script `code/variance_extension.py` verifies the quadratic identity and
illustrates correlated cases numerically. Its output is in `output/variance_summary.txt`.

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
