# Repository 2 - Agrawal, Gans & Goldfarb (2025)

[*The Economics of Bicycles for the Mind*](https://www.nber.org/papers/w34034),
NBER Working Paper 34034 (unrefereed). Repository:
[github.com/amchavezu/ai-02-agrawal](https://github.com/amchavezu/ai-02-agrawal).

## Question and mechanism

The paper asks how cognitive tools such as computers and AI change effort, productivity,
and the value of human skills. Its single mechanism is that a tool improves implementation
directly, reducing the marginal return to human implementation effort, while judgment still
determines which actions are valuable and when opportunities arise. The tool therefore
substitutes for **implementation skill** and can complement **payoff judgment** and
**opportunity judgment**.

## Agent problem

Conditional on noticing an opportunity in round \(t\), the agent chooses effort
\(e_t\geq0\) to maximize net expected value:

\[
e_t^*(\theta)\in\arg\max_{e_t\geq0}
\left\{M(e_t;\theta)\equiv
p(se_t;\theta)\alpha\Delta-c(e_t;\theta)\right\}.
\]

Here \(s>0\) is implementation skill, \(\alpha\Delta>0\) scales the payoff from a
successful action, and \(\theta\) is tool quality. Opportunity judgment is the sequence
\(\{\gamma(t)\}\), which controls how often the problem is reached. At an interior optimum,

\[
p'(se_t^*;\theta)s\alpha\Delta=c'(e_t^*;\theta).
\]

## Main result: Proposition 1

Assume \(p\) is increasing and weakly concave in implementation, \(c\) is increasing and
weakly convex in effort, \(s>0\), \(\alpha\Delta>0\), and the opportunity sequence and
discount factor produce a finite positive multiplier \(\Gamma\). A cognitive tool moving
from \(\theta=0\) to \(1\) satisfies, for every feasible \(e\),

\[
p(se;1)\geq p(se;0),\qquad c(e;1)\leq c(e;0),\qquad
\frac{p'(se;1)}{c'(e;1)}<\frac{p'(se;0)}{c'(e;0)}\quad(e>0).
\]

With interior, unique optima and a strict relevant improvement for the strict value claim,
the paper's result is

\[
e_t^*(1)<e_t^*(0),\qquad e_t^*(\theta)=e^*(\theta)\ \forall t,\qquad
V_0(1)>V_0(0).
\]

Thus the agent creates more continuation value with less direct implementation effort.
Without interiority or strictness, the corresponding safe conclusions are weak.

## Extension and handwritten check

Our student-chosen extension keeps \(\alpha\perp(\Gamma,s)\) but allows
\(\Gamma\) and \(s\) to be dependent. Initial variance falls exactly when
\(\mathbb E[\Gamma^2]<\mathbb E[\Gamma s]\mathbb E[\Gamma/s]\); two joint
distributions with identical marginals produce opposite signs. The standard-library script
**code/variance_extension.py** verifies 75 grid points and reproduces the paper's endpoint
counterexample: condition (30) holds, but \(\theta^*=1.792>1\).

**Handwritten evidence:** the four genuine pages in **hand/** verify the mean and variance
decomposition, condition (30), the missing endpoint condition \(\theta^*<1\), the exact
counterexample, and the piecewise solution when effort reaches \(e^*=0\).
