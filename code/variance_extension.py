"""Numerically verify Proposition 3 and the correlated-skills extension.

Run from the repository root with:

    python code/variance_extension.py

The script uses only the Python standard library. It checks every numerical
identity before replacing the deterministic files in ``output/``. Any failed
condition or discrepancy raises ``AssertionError`` and stops execution.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
import csv
import math


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output"
THETA_GRID = tuple(index / 20 for index in range(25))  # 0.00, ..., 1.20
ABS_TOL = 1e-12
REL_TOL = 1e-12


@dataclass(frozen=True)
class Scenario:
    """A finite cross-sectional joint distribution of (s, Gamma)."""

    name: str
    probabilities: tuple[float, ...]
    skill: tuple[float, ...]
    opportunity_multiplier: tuple[float, ...]
    alpha: float
    delta_gain: float
    independent: bool
    expected_initial_sign: int  # -1 for decline, +1 for increase

    def validate(self) -> None:
        lengths = {
            len(self.probabilities),
            len(self.skill),
            len(self.opportunity_multiplier),
        }
        if len(lengths) != 1:
            raise AssertionError(f"{self.name}: vectors have different lengths")
        if not math.isclose(sum(self.probabilities), 1.0, abs_tol=ABS_TOL):
            raise AssertionError(f"{self.name}: probabilities do not sum to one")
        if min(self.probabilities) <= 0:
            raise AssertionError(f"{self.name}: probabilities must be positive")
        if min(self.skill) <= 0 or min(self.opportunity_multiplier) <= 0:
            raise AssertionError(f"{self.name}: s and Gamma must have positive support")
        if self.alpha <= 0 or self.delta_gain <= 0:
            raise AssertionError(f"{self.name}: alpha and Delta must be positive")
        if self.expected_initial_sign not in (-1, 1):
            raise AssertionError(f"{self.name}: invalid expected slope sign")


# The first scenario is the exact counterexample in analysis/variance_derivation.md.
# The correlated scenarios have identical marginals for both s and Gamma. Only
# their pairing differs, so their opposite signs cannot be attributed to marginals.
SCENARIOS = (
    Scenario(
        name="independent_condition30_counterexample",
        probabilities=(0.5, 0.5),
        skill=(0.7, 1.0),
        opportunity_multiplier=(1.0, 1.0),
        alpha=0.8,
        delta_gain=4.0,
        independent=True,
        expected_initial_sign=-1,
    ),
    Scenario(
        name="correlated_initial_decline",
        probabilities=(1 / 3, 1 / 3, 1 / 3),
        skill=(0.5, 0.75, 1.0),
        opportunity_multiplier=(1.8, 0.84, 1.66),
        alpha=0.8,
        delta_gain=6.0,
        independent=False,
        expected_initial_sign=-1,
    ),
    Scenario(
        name="correlated_initial_increase",
        probabilities=(1 / 3, 1 / 3, 1 / 3),
        skill=(0.5, 0.75, 1.0),
        opportunity_multiplier=(0.84, 1.8, 1.66),
        alpha=0.8,
        delta_gain=6.0,
        independent=False,
        expected_initial_sign=1,
    ),
)


def expectation(probabilities: tuple[float, ...], values: tuple[float, ...]) -> float:
    return math.fsum(p * value for p, value in zip(probabilities, values))


def variance(probabilities: tuple[float, ...], values: tuple[float, ...]) -> float:
    mean = expectation(probabilities, values)
    return expectation(probabilities, tuple((value - mean) ** 2 for value in values))


def covariance(
    probabilities: tuple[float, ...],
    first: tuple[float, ...],
    second: tuple[float, ...],
) -> float:
    mean_first = expectation(probabilities, first)
    mean_second = expectation(probabilities, second)
    centered_products = tuple(
        (x - mean_first) * (y - mean_second) for x, y in zip(first, second)
    )
    return expectation(probabilities, centered_products)


def require_close(actual: float, expected: float, label: str) -> None:
    if not math.isclose(actual, expected, rel_tol=REL_TOL, abs_tol=ABS_TOL):
        raise AssertionError(
            f"{label}: actual={actual:.17g}, expected={expected:.17g}"
        )


def components(scenario: Scenario) -> dict[str, float | tuple[float, ...] | bool]:
    """Compute all moments used by the analytical extension."""

    scenario.validate()
    p = scenario.probabilities
    s = scenario.skill
    gamma = scenario.opportunity_multiplier
    k = scenario.delta_gain**2 / 4
    alpha_second_moment = scenario.alpha**2

    baseline = tuple(
        k * alpha_second_moment * gamma_i * skill_i
        for gamma_i, skill_i in zip(gamma, s)
    )
    tool_loading = tuple(gamma_i / skill_i for gamma_i, skill_i in zip(gamma, s))

    mean_h = expectation(p, baseline)
    mean_z = expectation(p, tool_loading)
    var_h = variance(p, baseline)
    var_z = variance(p, tool_loading)
    cov_hz = covariance(p, baseline, tool_loading)

    e_gamma = expectation(p, gamma)
    e_gamma_squared = expectation(p, tuple(value**2 for value in gamma))
    e_skill = expectation(p, s)
    e_inverse_skill = expectation(p, tuple(1 / value for value in s))
    e_gamma_skill = expectation(
        p, tuple(gamma_i * skill_i for gamma_i, skill_i in zip(gamma, s))
    )
    e_gamma_over_skill = mean_z
    joint_gap = e_gamma_squared - e_gamma_skill * e_gamma_over_skill

    # From Cov(H,Z)=k E[alpha^2] times the joint gap.
    require_close(
        cov_hz,
        k * alpha_second_moment * joint_gap,
        f"{scenario.name}: covariance identity",
    )

    if var_z <= ABS_TOL:
        theta_star_formal = math.nan
        theta_min_nonnegative = 0.0
    else:
        theta_star_formal = -cov_hz / var_z
        theta_min_nonnegative = max(0.0, theta_star_formal)

    interior_theta_limit = min(
        alpha_second_moment * scenario.delta_gain**2 * skill_i**2 / 4
        for skill_i in s
    )
    correlation_gamma_skill = covariance(p, gamma, s) / math.sqrt(
        variance(p, gamma) * variance(p, s)
    ) if variance(p, gamma) > ABS_TOL and variance(p, s) > ABS_TOL else 0.0

    return {
        "baseline": baseline,
        "tool_loading": tool_loading,
        "mean_h": mean_h,
        "mean_z": mean_z,
        "var_h": var_h,
        "var_z": var_z,
        "cov_hz": cov_hz,
        "joint_gap": joint_gap,
        "paper_ratio_left": e_gamma_squared / e_gamma**2,
        "paper_ratio_right": e_skill * e_inverse_skill,
        "theta_star_formal": theta_star_formal,
        "theta_min_nonnegative": theta_min_nonnegative,
        "interior_theta_limit": interior_theta_limit,
        "turning_inside_interior": (
            math.isfinite(theta_star_formal)
            and 0 <= theta_star_formal < interior_theta_limit
        ),
        "correlation_gamma_skill": correlation_gamma_skill,
    }


def evaluate(scenario: Scenario, theta: float) -> dict[str, float | bool]:
    """Evaluate direct and formula-based moments at one tool-quality value."""

    info = components(scenario)
    baseline = info["baseline"]
    tool_loading = info["tool_loading"]
    assert isinstance(baseline, tuple)
    assert isinstance(tool_loading, tuple)

    values = tuple(h + theta * z for h, z in zip(baseline, tool_loading))
    direct_mean = expectation(scenario.probabilities, values)
    formula_mean = float(info["mean_h"]) + theta * float(info["mean_z"])
    direct_variance = variance(scenario.probabilities, values)
    quadratic_variance = (
        float(info["var_h"])
        + 2 * theta * float(info["cov_hz"])
        + theta**2 * float(info["var_z"])
    )
    derivative = 2 * float(info["cov_hz"]) + 2 * theta * float(info["var_z"])

    require_close(direct_mean, formula_mean, f"{scenario.name} at theta={theta}: mean")
    require_close(
        direct_variance,
        quadratic_variance,
        f"{scenario.name} at theta={theta}: variance",
    )

    efforts = tuple(
        scenario.alpha**2 * scenario.delta_gain**2 * skill_i / 4
        - theta / skill_i
        for skill_i in scenario.skill
    )
    interior_effort_valid = min(efforts) > 0
    if not interior_effort_valid:
        raise AssertionError(
            f"{scenario.name} at theta={theta}: interior effort formula is invalid"
        )

    return {
        "mean": direct_mean,
        "variance_direct": direct_variance,
        "variance_quadratic": quadratic_variance,
        "derivative": derivative,
        "interior_effort_valid": interior_effort_valid,
    }


def verify_scenario_conditions() -> dict[str, dict[str, float | tuple[float, ...] | bool]]:
    """Assert the economic sign conditions before writing any output."""

    information = {scenario.name: components(scenario) for scenario in SCENARIOS}

    independent = SCENARIOS[0]
    independent_info = information[independent.name]
    if not (
        float(independent_info["paper_ratio_left"])
        < float(independent_info["paper_ratio_right"])
    ):
        raise AssertionError("independent counterexample does not satisfy condition (30)")

    decline = SCENARIOS[1]
    increase = SCENARIOS[2]
    decline_info = information[decline.name]
    increase_info = information[increase.name]

    # Stronger than requested: the correlated scenarios have the same marginals.
    if sorted(decline.skill) != sorted(increase.skill):
        raise AssertionError("correlated scenarios do not share the same s marginal")
    if sorted(decline.opportunity_multiplier) != sorted(
        increase.opportunity_multiplier
    ):
        raise AssertionError("correlated scenarios do not share the same Gamma marginal")
    if decline.probabilities != increase.probabilities:
        raise AssertionError("correlated scenarios use different probability masses")

    for scenario in SCENARIOS:
        info = information[scenario.name]
        initial_derivative = 2 * float(info["cov_hz"])
        if scenario.expected_initial_sign < 0 and not initial_derivative < 0:
            raise AssertionError(f"{scenario.name}: initial slope is not negative")
        if scenario.expected_initial_sign > 0 and not initial_derivative > 0:
            raise AssertionError(f"{scenario.name}: initial slope is not positive")
        if float(info["interior_theta_limit"]) <= max(THETA_GRID):
            raise AssertionError(f"{scenario.name}: grid extends beyond the effort corner")
        for theta in THETA_GRID:
            evaluate(scenario, theta)

    return information


def build_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for scenario in SCENARIOS:
        info = components(scenario)
        for theta in THETA_GRID:
            result = evaluate(scenario, theta)
            rows.append(
                {
                    "scenario": scenario.name,
                    "theta": f"{theta:.2f}",
                    "mean_value": f"{float(result['mean']):.10f}",
                    "variance_direct": f"{float(result['variance_direct']):.10f}",
                    "variance_quadratic": f"{float(result['variance_quadratic']):.10f}",
                    "variance_derivative": f"{float(result['derivative']):.10f}",
                    "theta_star_formal": f"{float(info['theta_star_formal']):.10f}",
                    "theta_min_nonnegative": f"{float(info['theta_min_nonnegative']):.10f}",
                    "interior_effort_valid": str(result["interior_effort_valid"]),
                }
            )
    return rows


def write_csv(rows: list[dict[str, str]]) -> None:
    destination = OUTPUT_DIR / "variance_results.csv"
    with destination.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def make_summary(
    information: dict[str, dict[str, float | tuple[float, ...] | bool]],
) -> str:
    lines = [
        "Variance extension: reproducible verification",
        "============================================",
        "",
        "Identity: Var(H + theta Z) = Var(H) + 2 theta Cov(H,Z) + theta^2 Var(Z)",
        "H=(Delta^2/4) Gamma alpha^2 s; Z=Gamma/s",
        "All assertions and all direct-versus-quadratic checks passed.",
        "",
    ]

    for scenario in SCENARIOS:
        info = information[scenario.name]
        at_zero = evaluate(scenario, 0.0)
        at_one = evaluate(scenario, 1.0)
        formal = float(info["theta_star_formal"])
        formal_text = f"{formal:.10f}" if math.isfinite(formal) else "undefined"
        lines.extend(
            (
                f"Scenario: {scenario.name}",
                f"  probabilities            = {scenario.probabilities}",
                f"  skill s                  = {scenario.skill}",
                f"  Gamma                    = {scenario.opportunity_multiplier}",
                f"  alpha, Delta             = {scenario.alpha:.4f}, {scenario.delta_gain:.4f}",
                f"  Corr(Gamma,s)            = {float(info['correlation_gamma_skill']): .10f}",
                f"  joint gap                = {float(info['joint_gap']): .10f}",
                f"  Cov(H,Z)                 = {float(info['cov_hz']): .10f}",
                f"  Var(Z)                   = {float(info['var_z']): .10f}",
                f"  mean at theta=0          = {float(at_zero['mean']): .10f}",
                f"  mean at theta=1          = {float(at_one['mean']): .10f}",
                f"  variance at theta=0      = {float(at_zero['variance_direct']): .10f}",
                f"  variance at theta=1      = {float(at_one['variance_direct']): .10f}",
                f"  dVar/dtheta at theta=0   = {float(at_zero['derivative']): .10f}",
                f"  dVar/dtheta at theta=1   = {float(at_one['derivative']): .10f}",
                f"  theta* formal            = {formal_text}",
                f"  minimizer on theta>=0    = {float(info['theta_min_nonnegative']):.10f}",
                f"  first effort corner      = {float(info['interior_theta_limit']):.10f}",
                f"  theta* inside interior   = {info['turning_inside_interior']}",
                f"  condition (30) left      = {float(info['paper_ratio_left']):.10f}",
                f"  condition (30) right     = {float(info['paper_ratio_right']):.10f}",
                "",
            )
        )

    lines.extend(
        (
            "Verified conclusions",
            "--------------------",
            "1. The independent counterexample satisfies condition (30), has theta*=1.792,",
            "   and still has a negative derivative at theta=1.",
            "2. The correlated scenarios have identical s and Gamma marginals.",
            "3. Changing only their pairing reverses the sign of the initial variance slope.",
            "4. Every grid point has positive interior effort.",
            "5. Direct variance equals the quadratic formula at every grid point.",
            "",
        )
    )
    return "\n".join(lines)


def write_summary(summary: str) -> None:
    destination = OUTPUT_DIR / "variance_summary.txt"
    with destination.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(summary)


def write_svg(rows: list[dict[str, str]]) -> None:
    curves: dict[str, list[tuple[float, float]]] = {
        scenario.name: [] for scenario in SCENARIOS
    }
    for row in rows:
        curves[row["scenario"]].append(
            (float(row["theta"]), float(row["variance_direct"]))
        )

    width, height = 1000, 620
    left, right, top, bottom = 95, 35, 70, 85
    plot_width = width - left - right
    plot_height = height - top - bottom
    all_values = [value for curve in curves.values() for _, value in curve]
    y_min, y_max = min(all_values), max(all_values)
    padding = 0.06 * (y_max - y_min)
    y_min -= padding
    y_max += padding

    def x_pixel(theta: float) -> float:
        return left + theta / max(THETA_GRID) * plot_width

    def y_pixel(value: float) -> float:
        return top + (y_max - value) / (y_max - y_min) * plot_height

    colors = ("#1769aa", "#2e7d32", "#c62828")
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="500" y="34" text-anchor="middle" font-family="Arial" font-size="24" font-weight="bold">Variance under independent and correlated joint distributions</text>',
    ]

    for index in range(7):
        value = y_min + index / 6 * (y_max - y_min)
        y = y_pixel(value)
        svg.append(
            f'<line x1="{left}" y1="{y:.2f}" x2="{width-right}" y2="{y:.2f}" stroke="#dddddd"/>'
        )
        svg.append(
            f'<text x="{left-12}" y="{y+5:.2f}" text-anchor="end" font-family="Arial" font-size="13">{value:.3f}</text>'
        )
    for theta in (0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2):
        x = x_pixel(theta)
        svg.append(
            f'<line x1="{x:.2f}" y1="{top}" x2="{x:.2f}" y2="{height-bottom}" stroke="#eeeeee"/>'
        )
        svg.append(
            f'<text x="{x:.2f}" y="{height-bottom+25}" text-anchor="middle" font-family="Arial" font-size="13">{theta:g}</text>'
        )

    svg.extend(
        (
            f'<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" stroke="black" stroke-width="2"/>',
            f'<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" stroke="black" stroke-width="2"/>',
            f'<text x="{left + plot_width/2:.2f}" y="{height-30}" text-anchor="middle" font-family="Arial" font-size="18">Tool quality theta</text>',
            f'<text x="25" y="{top + plot_height/2:.2f}" text-anchor="middle" transform="rotate(-90 25 {top + plot_height/2:.2f})" font-family="Arial" font-size="18">Var(V(theta))</text>',
        )
    )

    for color, (name, points) in zip(colors, curves.items()):
        coordinates = " ".join(
            f"{x_pixel(theta):.2f},{y_pixel(value):.2f}" for theta, value in points
        )
        svg.append(
            f'<polyline points="{coordinates}" fill="none" stroke="{color}" stroke-width="4"/>'
        )

    for index, (color, name) in enumerate(zip(colors, curves)):
        y = top + 10 + index * 27
        svg.append(
            f'<line x1="{left+20}" y1="{y}" x2="{left+55}" y2="{y}" stroke="{color}" stroke-width="4"/>'
        )
        label = escape(name.replace("_", " "))
        svg.append(
            f'<text x="{left+65}" y="{y+5}" font-family="Arial" font-size="14">{label}</text>'
        )

    svg.append("</svg>")
    destination = OUTPUT_DIR / "variance_curve.svg"
    with destination.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write("\n".join(svg) + "\n")


def main() -> None:
    information = verify_scenario_conditions()
    rows = build_rows()
    summary = make_summary(information)

    OUTPUT_DIR.mkdir(exist_ok=True)
    write_csv(rows)
    write_summary(summary)
    write_svg(rows)

    print(summary, end="")
    print(f"Wrote {OUTPUT_DIR / 'variance_summary.txt'}")
    print(f"Wrote {OUTPUT_DIR / 'variance_results.csv'}")
    print(f"Wrote {OUTPUT_DIR / 'variance_curve.svg'}")


if __name__ == "__main__":
    main()
