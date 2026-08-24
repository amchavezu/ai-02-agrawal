# Repository 2 - Agrawal, Gans & Goldfarb (2025)

*The Economics of Bicycles for the Mind*

[NBER Working Paper 34034](https://www.nber.org/papers/w34034) - [DOI](https://doi.org/10.3386/w34034)

> Work in progress for *Artificial Intelligence and Economic Modeling* (UP 2026-II).
> The final repository must be merged into `main` through a pull request and its URL
> posted in [course issue #1](https://github.com/alexanderquispe/AI-Econ-Modeling/issues/1).

## What question the paper answers

How do cognitive tools such as computers and AI change effort, productivity, and the
value of different human skills? The paper separates three human inputs:

- **Implementation skill**: how effectively effort becomes a successful implementation.
- **Payoff judgment**: the ability to choose or recognise the valuable action.
- **Opportunity judgment**: the ability to notice further opportunities for improvement.

The central mechanism is that a cognitive tool can be a substitute for implementation
effort while remaining a complement to judgment.

## The agent's problem

Conditional on noticing an improvement opportunity in round $t$, the agent chooses
effort $e_t\geq 0$ to maximise expected net benefit

$$
e_t^*(\theta)=\arg\max_{e_t\geq 0}
M(e_t;\theta), \qquad
M(e_t;\theta)=p(se_t;\theta)\alpha\Delta-c(e_t;\theta).
$$

Here $s\in(0,1]$ is implementation skill, $\alpha\in[0,1]$ is payoff judgment,
$\Delta>0$ is the value of a successful improvement, and $\theta\geq0$ is tool
quality. Opportunity judgment enters through the probability sequence $\{\gamma(t)\}$.
For an interior optimum,

$$
p'(se_t^*(\theta);\theta)s\alpha\Delta=c'(e_t^*(\theta);\theta).
$$

## Initial main result: Proposition 1

The paper defines a cognitive tool by two conditions. When $\theta'>\theta$, it weakly
raises the success function $p(se;\theta)$ and weakly lowers the effort cost
$c(e;\theta)$ for every $e$; moreover, the marginal-benefit-to-marginal-cost ratio
$p'(se;\theta)/c'(e;\theta)$ is strictly decreasing in tool quality for $e>0$.
Together with increasing/concave $p$, increasing/convex $c$, and an interior optimum,
Proposition 1 states that adoption lowers optimal effort, makes effort time-invariant,
and raises expected task quality:

$$
e_t^*(1)<e_t^*(0),\qquad e_t^*(\theta)=e^*(\theta),\qquad V_0(\theta)>V_0(0).
$$

*Intuition in one sentence:* the tool shifts net benefit upward but makes another unit
of human implementation effort less attractive at the margin, so the agent produces
more value with less direct effort.

This repository states Proposition 1 as the main result and develops Proposition 3 as the
above-the-floor extension. The mathematical and numerical checks are complete; the one
remaining academic-integrity requirement is the student's own handwritten verification.

## Repository map

| Path | Purpose |
|---|---|
| `README.md` | One-page paper and model summary (this file) |
| `prompts.md` | Raw prompts and answers used for the assignment |
| `extensions.md` | Questions, checks, and possible extensions |
| `analysis/variance_derivation.md` | Full Proposition 3 derivation, extension, and counterexample |
| `code/variance_extension.py` | Reproducible standard-library Python analysis |
| `output/` | Console summary, numerical CSV, and variance figure |
| `hand/` | The student's own photographed derivation |
| `presentation.tex` / `presentation.pdf` | Five-minute Beamer deck |
| `paper/` | Citation and local-paper instructions |
| `course/` | Syllabus, course materials, and a concise course map |
| `AGENTS.md` | Durable instructions for Codex in this repository |
| `scripts/check_environment.ps1` | Repeatable readiness check |

## Reproducible extension and output

The above-the-floor extension relaxes independence between the opportunity multiplier
\(\Gamma\) and implementation skill \(s\). It shows that the paper's marginal condition is
replaced by the joint-moment inequality

$$
\mathbb E[\Gamma^2]<\mathbb E[\Gamma s]\mathbb E[\Gamma/s].
$$

The derivation also documents an internal slip: condition (30) guarantees an initially
negative variance slope and \(\theta^*>0\), but a positive slope specifically at
\(\theta=1\) additionally requires \(\theta^*<1\). The included independent counterexample
satisfies condition (30) yet has \(\theta^*=1.792\), so the derivative remains negative at
\(\theta=1\).

Run the analysis from the repository root:

```powershell
python code\variance_extension.py
```

The command prints the results and regenerates `output/variance_summary.txt`,
`output/variance_results.csv`, and `output/variance_curve.svg`. The complete algebra is in
`analysis/variance_derivation.md`; `hand/DERIVATION_GUIDE.md` gives a two-page sequence for
the student's own handwritten verification.

## Submission checklist

- [x] Check every mathematical claim against the paper and its appendix.
- [ ] Add at least one genuine handwritten derivation to `hand/`.
- [x] Record the relevant AI conversation in `prompts.md` without polishing it.
- [x] Compile `presentation.tex` and visually inspect `presentation.pdf`.
- [x] Commit the work in small changes on `analysis`.
- [ ] Push `analysis`, open a PR, and merge it into `main`.
- [ ] Confirm `main` contains the final files.
- [ ] Comment only the repository URL on the course issue before Tuesday 22:00.
