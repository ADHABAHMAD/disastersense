"""Small command-line interface for DisasterSense."""

from __future__ import annotations

from disastersense.risk_engine import build_action_plan, calculate_risk_score, prioritize_incidents


def main() -> None:
    sample_incidents = [
        {"hazard": "flood", "severity": 8, "vulnerability": 7, "exposure": 6, "infrastructure": 5},
        {"hazard": "earthquake", "severity": 9, "vulnerability": 8, "exposure": 7, "infrastructure": 7},
        {"hazard": "wind", "severity": 5, "vulnerability": 4, "exposure": 5, "infrastructure": 6},
    ]

    print("DisasterSense risk assessment demo")
    print("Top priority incident:")
    for item in prioritize_incidents(sample_incidents)[:1]:
        print(item)

    print("\nFlood risk score:")
    print(calculate_risk_score("flood", 8, 7, 6, 5))

    print("\nEmergency action plan for flood:")
    for step in build_action_plan("flood"):
        print(f"- {step}")


if __name__ == "__main__":
    main()
