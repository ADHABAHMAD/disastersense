from disastersense.risk_engine import build_action_plan, calculate_risk_score, prioritize_incidents


def test_calculate_risk_score() -> None:
    score = calculate_risk_score(
        hazard="flood",
        severity=8,
        vulnerability=7,
        exposure=6,
        infrastructure=5,
    )

    assert 0 <= score <= 100
    assert score > 50


def test_prioritize_incidents() -> None:
    incidents = [
        {"hazard": "wind", "severity": 5, "vulnerability": 4, "exposure": 5, "infrastructure": 6},
        {"hazard": "earthquake", "severity": 9, "vulnerability": 8, "exposure": 7, "infrastructure": 7},
    ]

    ranked = prioritize_incidents(incidents)

    assert len(ranked) == 2
    assert ranked[0]["hazard"] == "earthquake"
    assert ranked[1]["hazard"] == "wind"


def test_build_action_plan() -> None:
    plan = build_action_plan("flood")

    assert isinstance(plan, list)
    assert len(plan) >= 3
    assert any("evacuation" in item.lower() for item in plan)
