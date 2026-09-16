# DisasterSense Project Report

## 1. Overview

DisasterSense is a disaster-risk monitoring and emergency-response planning project. It is designed to support decision-making during natural and human-made disasters by evaluating incident severity, ranking urgency, and recommending action plans.

## 2. Problem addressed

Disaster response teams often need to quickly understand which incidents are most critical and which communities or regions require immediate response. Without a structured risk model, emergency planning can become reactive, slow, and inconsistent.

## 3. Solution

DisasterSense introduces a lightweight risk engine that calculates risk using several factors:

- hazard type
- severity
- vulnerability
- exposure
- infrastructure impact

The system converts these factors into a normalized score, enabling better prioritization and clear response guidance.

## 4. Methodology

The project uses a weighted scoring approach,

Risk Score = weighted combination of severity, vulnerability, exposure, and infrastructure,

and then normalizes the result into a 0–100 scale. Incidents are ordered by their computed risk, and a hazard-specific action plan is generated for response teams.

## 5. Core functions

- `calculate_risk_score(...)`
- `prioritize_incidents(...)`
- `build_action_plan(...)`

These functions form the basis of the MVP and are covered by automated tests.

## 6. Project impact

This project is useful for:

- disaster monitoring teams,
- local government and emergency coordinators,
- community risk assessment,
- preparedness planning,
- future dashboard and map-based visualization work.

## 7. Future work

The current MVP can be expanded by adding:

- live weather and hazard API ingestion,
- geospatial mapping,
- alert generation,
- a web dashboard,
- reporting and analytics modules,
- data persistence for historical incidents.

## 8. Conclusion

DisasterSense provides a practical and scalable starting point for a disaster-response support system. It demonstrates the value of structured risk scoring and actionable emergency planning in a simple, testable, and expandable repository.
