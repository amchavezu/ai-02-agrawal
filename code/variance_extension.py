"""Reproduce Proposition 3 and relax independence between Gamma and skill.

The script uses only Python's standard library. It writes a numerical table, a
plain-text summary, and an SVG figure to ../output/.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
import csv
import math


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


@dataclass(frozen=True)
class Scenario:
    name: str
    probabilities: tuple[float, ...]
    skill: tuple[float, ...]
    gamma: tuple[float, ...]
    alpha: float = 0.8
    delta_value: float = 4.0

    def validate(self) -> None:
        if not (len(self.probabilities) == len(self.skill) == len(self.gamma)):
            raise ValueError(f"{self.name}: vectors must have the same length")
        if not math.isclose(sum(self.probabilities), 1.0):
            raise ValueError(f"{self.name}: probabilities must sum to one")
        if min(self.probabilities + self.skill + self.gamma) <= 0:
            raise ValueError(f"{self.name}: probabilities and types must be positive")


SCENARIOS = (
    Scenario(
        name="independent_counterexample",
        probabilities=(0.5, 0.5),
        skill=(0.7, 1.0),
        gamma=(1.0, 1.0),
    ),
    Scenario(
        name="correlated_initial_decline",
        probabilities=(0.2, 0.3, 0.5),
        skill=(0.7, 0.85, 1.0),
        gamma=(1.2, 0.8, 1.0),
    ),
    Scenario(
        name="correlated_initial_increase",
        probabilities=(0.2, 0.3, 0.5),
        skill=(0.7, 0.85, 1.0),
        gamma=(1.0, 1.2, 0.8),
    ),
)


def expectation(probabilities: tuple[float, ...], values: tuple[float, ...]) -> float:
    return sum(probability * value for probability, value in zip(probabilities, values))


def variance(probabilities: tuple[float, ...], values: tuple[float, ...]) -> float:
    mean = expectation(probabilities, values)
    return expectation(probabilities, tuple((value - mean) ** 2 for value in values))


def covariance(
    probabilities: tuple[float, ...],
    first: tuple[float, ...],
    second: tuple[float, ...],
) -> float:
    first_mean = expectation(probabilities, first)
    second_mean = expectation(probabilities, second)
    products = tuple(x * y for x, y in zip(first, second))
    return expectation(probabilities, products) - first_mean * second_mean


def components(scenario: Scenario) -> dict[str, float | tuple[float, ...]]:
    scenario.validate()
    probability = scenario.probabilities
    skill = scenario.skill
    gamma = scenario.gamma
    scale = scenario.delta_value**2 / 4

    baseline = tuple(
        scale * scenario.alpha**2 * gamma_i * skill_i
        for gamma_i, skill_i in zip(gamma, skill)
    )
    tool_loading = tuple(gamma_i / skill_i for gamma_i, skill_i in zip(gamma, skill))
    cov_hz = covariance(probability, baseline, tool_loading)
    var_z = variance(probability, tool_loading)
    turning_point = -cov_hz / var_z if cov_hz < 0 and var_z > 0 else math.nan

    e_gamma_squared = expectation(probability, tuple(value**2 for value in gamma))
    e_gamma_skill = expectation(
        probability, tuple(gamma_i * skill_i for gamma_i, skill_i in zip(gamma, skill))
    )
    e_gamma_over_skill = expectation(probability, tool_loading)

    return {
        "baseline": baseline,
        "tool_loading": tool_loading,
        "mean_h": expectation(probability, baseline),
        "mean_z": expectation(probability, tool_loading),
        "var_h": variance(probability, baseline),
        "var_z": var_z,
        "cov_hz": cov_hz,
        "turning_point": turning_point,
        "joint_moment_gap": e_gamma_squared - e_gamma_skill * e_gamma_over_skill,
        "paper_ratio_left": e_gamma_squared / expectation(probability, gamma) ** 2,
        "paper_ratio_right": expectation(probability, skill)
        * expectation(probability, tuple(1 / value for value in skill)),
    }


def evaluate(scenario: Scenario, theta: float) -> dict[str, float]:
    info = components(scenario)
    probability = scenario.probabilities
    baseline = info["baseline"]
    tool_loading = info["tool_loading"]
    assert isinstance(baseline, tuple) and isinstance(tool_loading, tuple)

    value = tuple(h + theta * z for h, z in zip(baseline, tool_loading))
    direct_variance = variance(probability, value)
    quadratic_variance = (
        float(info["var_h"])
        + 2 * theta * float(info["cov_hz"])
        + theta**2 * float(info["var_z"])
    )
    derivative = 2 * float(info["cov_hz"]) + 2 * theta * float(info["var_z"])
    return {
        "mean": expectation(probability, value),
        "direct_variance": direct_variance,
        "quadratic_variance": quadratic_variance,
        "derivative": derivative,
    }


def write_csv() -> dict[str, list[tuple[float, float]]]:
    # The paper's interior-effort formula is valid for every type in these examples
    # on 0 <= theta <= 1.2. We do not extrapolate it past the corner e*=0.
    theta_grid = tuple(index / 20 for index in range(25))
    curves: dict[str, list[tuple[float, float]]] = {}
    destination = OUTPUT_DIR / "variance_results.csv"
    with destination.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(
            (
                "scenario",
                "theta",
                "mean_value",
                "variance_direct",
                "variance_quadratic",
                "variance_derivative",
            )
        )
        for scenario in SCENARIOS:
            curves[scenario.name] = []
            for theta in theta_grid:
                result = evaluate(scenario, theta)
                if not math.isclose(
                    result["direct_variance"],
                    result["quadratic_variance"],
                    rel_tol=1e-12,
                    abs_tol=1e-12,
                ):
                    raise AssertionError("Direct and quadratic variance calculations disagree")
                curves[scenario.name].append((theta, result["direct_variance"]))
                writer.writerow(
                    (
                        scenario.name,
                        f"{theta:.2f}",
                        f"{result['mean']:.10f}",
                        f"{result['direct_variance']:.10f}",
                        f"{result['quadratic_variance']:.10f}",
                        f"{result['derivative']:.10f}",
                    )
                )
    return curves


def write_summary() -> None:
    lines = [
        "Variance extension: reproducible results",
        "========================================",
        "",
        "Identity checked: Var(H + theta Z) = Var(H) + 2 theta Cov(H,Z) + theta^2 Var(Z).",
        "Here H=(Delta^2/4) Gamma alpha^2 s and Z=Gamma/s.",
        "",
    ]
    for scenario in SCENARIOS:
        info = components(scenario)
        at_zero = evaluate(scenario, 0.0)
        at_one = evaluate(scenario, 1.0)
        turning = info["turning_point"]
        turning_text = f"{turning:.6f}" if math.isfinite(float(turning)) else "none (initial slope is non-negative)"
        lines.extend(
            (
                f"Scenario: {scenario.name}",
                f"  probabilities = {scenario.probabilities}",
                f"  skill s       = {scenario.skill}",
                f"  Gamma         = {scenario.gamma}",
                f"  Cov(H,Z)      = {float(info['cov_hz']): .10f}",
                f"  Var(Z)        = {float(info['var_z']): .10f}",
                f"  dVar/dtheta|0 = {at_zero['derivative']: .10f}",
                f"  dVar/dtheta|1 = {at_one['derivative']: .10f}",
                f"  theta*        = {turning_text}",
                f"  joint gap     = {float(info['joint_moment_gap']): .10f}",
                f"  paper ratio L = {float(info['paper_ratio_left']):.10f}",
                f"  paper ratio R = {float(info['paper_ratio_right']):.10f}",
                "  note           = condition (30) uses these ratios only under independence",
                "",
            )
        )

    lines.extend(
        (
            "Key verdict",
            "-----------",
            "The independent counterexample satisfies condition (30), but theta*=1.792000 > 1",
            "and dVar/dtheta at theta=1 is negative. Condition (30) alone therefore does not",
            "imply the paper's displayed claim dVar/dtheta|theta=1 > 0.",
        )
    )
    (OUTPUT_DIR / "variance_summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_svg(curves: dict[str, list[tuple[float, float]]]) -> None:
    width, height = 960, 600
    left, right, top, bottom = 90, 35, 70, 80
    plot_width = width - left - right
    plot_height = height - top - bottom
    all_values = [value for curve in curves.values() for _, value in curve]
    y_min, y_max = min(all_values), max(all_values)
    y_padding = 0.08 * (y_max - y_min)
    y_min -= y_padding
    y_max += y_padding

    def x_pixel(theta: float) -> float:
        return left + theta / 1.2 * plot_width

    def y_pixel(value: float) -> float:
        return top + (y_max - value) / (y_max - y_min) * plot_height

    colors = ("#1769aa", "#2e7d32", "#c62828")
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="480" y="34" text-anchor="middle" font-family="Arial" font-size="24" font-weight="bold">Variance of continuation value under three joint distributions</text>',
    ]

    for index in range(7):
        value = y_min + index / 6 * (y_max - y_min)
        y = y_pixel(value)
        svg.append(f'<line x1="{left}" y1="{y:.2f}" x2="{width-right}" y2="{y:.2f}" stroke="#dddddd"/>')
        svg.append(f'<text x="{left-12}" y="{y+5:.2f}" text-anchor="end" font-family="Arial" font-size="13">{value:.3f}</text>')
    for theta in (0, 0.2, 0.4, 0.6, 0.8, 1, 1.2):
        x = x_pixel(theta)
        svg.append(f'<line x1="{x:.2f}" y1="{top}" x2="{x:.2f}" y2="{height-bottom}" stroke="#eeeeee"/>')
        svg.append(f'<text x="{x:.2f}" y="{height-bottom+25}" text-anchor="middle" font-family="Arial" font-size="13">{theta:g}</text>')

    svg.extend(
        (
            f'<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" stroke="black" stroke-width="2"/>',
            f'<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" stroke="black" stroke-width="2"/>',
            f'<text x="{left + plot_width/2:.2f}" y="{height-28}" text-anchor="middle" font-family="Arial" font-size="18">Tool quality theta</text>',
            f'<text x="24" y="{top + plot_height/2:.2f}" text-anchor="middle" transform="rotate(-90 24 {top + plot_height/2:.2f})" font-family="Arial" font-size="18">Var(V(theta))</text>',
        )
    )

    for color, (name, points) in zip(colors, curves.items()):
        coordinates = " ".join(f"{x_pixel(theta):.2f},{y_pixel(value):.2f}" for theta, value in points)
        svg.append(f'<polyline points="{coordinates}" fill="none" stroke="{color}" stroke-width="4"/>')

    legend_y = top + 10
    for index, (color, name) in enumerate(zip(colors, curves)):
        y = legend_y + index * 27
        svg.append(f'<line x1="{left+20}" y1="{y}" x2="{left+55}" y2="{y}" stroke="{color}" stroke-width="4"/>')
        svg.append(f'<text x="{left+65}" y="{y+5}" font-family="Arial" font-size="14">{escape(name.replace("_", " "))}</text>')

    svg.append("</svg>")
    (OUTPUT_DIR / "variance_curve.svg").write_text("\n".join(svg), encoding="utf-8")


def main() -> None:
    curves = write_csv()
    write_summary()
    write_svg(curves)
    print((OUTPUT_DIR / "variance_summary.txt").read_text(encoding="utf-8"), end="")
    print(f"Wrote {OUTPUT_DIR / 'variance_results.csv'}")
    print(f"Wrote {OUTPUT_DIR / 'variance_curve.svg'}")


if __name__ == "__main__":
    main()
