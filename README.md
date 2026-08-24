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

This is an initial verified map, not the final submission. The final version still needs
the exact proposition selected for the oral exam, its complete conditions, the hand check,
and the variance analysis in Proposition 3.

## Repository map

| Path | Purpose |
|---|---|
| `README.md` | One-page paper and model summary (this file) |
| `prompts.md` | Raw prompts and answers used for the assignment |
| `extensions.md` | Questions, checks, and possible extensions |
| `hand/` | The student's own photographed derivation |
| `presentation.tex` / `presentation.pdf` | Five-minute Beamer deck |
| `paper/` | Citation and local-paper instructions |
| `course/` | Syllabus, course materials, and a concise course map |
| `AGENTS.md` | Durable instructions for Codex in this repository |
| `scripts/check_environment.ps1` | Repeatable readiness check |

## Submission checklist

- [ ] Replace every `TODO` after checking the paper directly.
- [ ] Add at least one genuine handwritten derivation to `hand/`.
- [ ] Record the relevant AI conversation in `prompts.md` without polishing it.
- [ ] Compile `presentation.tex` and visually inspect `presentation.pdf`.
- [ ] Commit small changes on `analysis`, push the branch, open a PR, and merge it.
- [ ] Confirm `main` contains the final files.
- [ ] Comment only the repository URL on the course issue before Tuesday 22:00.
