import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from disastersense.risk_engine import (
    build_action_plan,
    calculate_risk_score,
    prioritize_incidents,
)


incidents = [
    {"hazard": "flood", "severity": 8, "vulnerability": 7, "exposure": 6, "infrastructure": 5},
    {"hazard": "earthquake", "severity": 9, "vulnerability": 8, "exposure": 7, "infrastructure": 7},
    {"hazard": "wind", "severity": 5, "vulnerability": 4, "exposure": 5, "infrastructure": 6},
]

print("Flood risk score:", calculate_risk_score("flood", 8, 7, 6, 5))
print("Prioritized incidents:")
for incident in prioritize_incidents(incidents):
    print(incident)

print("Flood action plan:")
for step in build_action_plan("flood"):
    print("-", step)
