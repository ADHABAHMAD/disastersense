"""Risk analysis utilities for DisasterSense."""

from __future__ import annotations

from typing import Iterable


def calculate_risk_score(
    hazard: str,
    severity: int,
    vulnerability: int,
    exposure: int,
    infrastructure: int,
) -> int:
    """Return a normalized risk score between 0 and 100."""
    weights = {
        "flood": (0.30, 0.25, 0.25, 0.20),
        "earthquake": (0.35, 0.25, 0.20, 0.20),
        "wind": (0.25, 0.20, 0.30, 0.25),
        "fire": (0.30, 0.20, 0.25, 0.25),
        "storm": (0.28, 0.22, 0.28, 0.22),
    }

    hazard_profile = weights.get(hazard.lower(), (0.25, 0.25, 0.25, 0.25))
    weighted_total = (
        severity * hazard_profile[0]
        + vulnerability * hazard_profile[1]
        + exposure * hazard_profile[2]
        + infrastructure * hazard_profile[3]
    )
    score = weighted_total * 10
    return max(0, min(100, int(round(score))))


def prioritize_incidents(incidents: Iterable[dict]) -> list[dict]:
    """Sort incident records by priority from highest to lowest risk."""
    ranked = []
    for item in incidents:
        score = calculate_risk_score(
            hazard=str(item.get("hazard", "unknown")).lower(),
            severity=int(item.get("severity", 0)),
            vulnerability=int(item.get("vulnerability", 0)),
            exposure=int(item.get("exposure", 0)),
            infrastructure=int(item.get("infrastructure", 0)),
        )
        enriched = dict(item)
        enriched["risk_score"] = score
        ranked.append(enriched)

    return sorted(ranked, key=lambda item: item["risk_score"], reverse=True)


def build_action_plan(hazard: str) -> list[str]:
    """Generate a simple action list for a disaster hazard."""
    hazard_name = hazard.lower()
    actions = {
        "flood": [
            "Activate flood warning systems and monitor river levels.",
            "Issue evacuation orders for low-lying areas.",
            "Deploy emergency teams to support drainage and shelter operations.",
            "Inspect road networks and restore access routes.",
        ],
        "earthquake": [
            "Trigger public safety alerts and confirm emergency communications.",
            "Inspect critical infrastructure and prioritize rescue routes.",
            "Coordinate search-and-rescue teams for trapped populations.",
            "Prepare medical triage centers for casualties.",
        ],
        "wind": [
            "Warn residents about high winds and flying debris hazards.",
            "Secure loose structures and utility equipment.",
            "Prepare emergency shelters and power restoration crews.",
            "Monitor damage reports and clear blocked roads.",
        ],
        "fire": [
            "Deploy firefighting units and activate incident command.",
            "Evacuate nearby communities and isolate vulnerable zones.",
            "Coordinate water and smoke management support.",
            "Assess property damage and restore utility services.",
        ],
    }
    return actions.get(hazard_name, [
        "Activate incident command and monitor conditions.",
        "Issue public warnings and coordinate response teams.",
        "Prioritize evacuation and rescue operations.",
        "Assess infrastructure damage and restore essential services.",
    ])
