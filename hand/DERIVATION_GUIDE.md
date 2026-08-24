# Guide for the handwritten verification

The professor requires a **real photo of your own handwritten work**. This file is a guide,
not a substitute for that photo. Work through the equations yourself and make sure you can
explain each equality aloud.

## Recommended two-page derivation

### Page 1: derive the variance identity

1. Write
   \[
   V(\theta)=\Gamma\left(\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}\right)
   =H+\theta Z,
   \]
   where \(H=(\Delta^2/4)\Gamma\alpha^2s\) and \(Z=\Gamma/s\).
2. Subtract the mean:
   \[
   V-\mathbb E[V]=(H-\mathbb E[H])+\theta(Z-\mathbb E[Z]).
   \]
3. Square the right-hand side and take expectations.
4. Reach
   \[
   \operatorname{Var}(V)=\operatorname{Var}(H)
   +2\theta\operatorname{Cov}(H,Z)+\theta^2\operatorname{Var}(Z).
   \]
5. Differentiate and obtain
   \[
   \frac{d\operatorname{Var}(V)}{d\theta}
   =2\operatorname{Cov}(H,Z)+2\theta\operatorname{Var}(Z).
   \]

### Page 2: check the counterexample

Use \(\alpha=0.8\), \(\Delta=4\), \(\Gamma=1\), and equal probabilities on
\(s\in\{0.7,1\}\).

1. Compute
   \[
   \mathbb E[s]=17/20,\qquad \mathbb E[1/s]=17/14.
   \]
2. Verify condition (30):
   \[
   1< (17/20)(17/14)=289/280.
   \]
3. Compute
   \[
   \operatorname{Cov}(H,Z)=-72/875,
   \qquad \operatorname{Var}(Z)=9/196.
   \]
4. Compute
   \[
   \theta^*=-(\operatorname{Cov}(H,Z))/\operatorname{Var}(Z)
   =1568/875=1.792.
   \]
5. Conclude that condition (30) holds but \(\theta^*>1\), so the derivative at
   \(\theta=1\) is still negative.

## What to photograph

- Photograph both pages, including any corrections or crossings-out.
- Put the photos in this folder, for example `hand/variance-page-1.jpg` and
  `hand/variance-page-2.jpg`.
- Do not delete this guide; it lets the reader compare the intended check with your work.
- After adding the photos, update the verdict in the presentation and README.
