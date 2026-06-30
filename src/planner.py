def create_analysis_plan(profile: dict, correlations: dict) -> dict:
    detected = profile["detected_types"]

    planned_analyses = []
    priority_questions = []

    if detected["composition_xps"]["detected"] and detected["electrical"]["detected"]:
        planned_analyses.append({
            "analysis": "Composition vs Electrical Property Analysis",
            "priority": "High",
            "reason": "XPS-derived composition and electrical data are both available.",
            "methods": [
                "Al/Ti vs Rs correlation",
                "C/Ti vs Rs correlation",
                "O/Ti vs Rs correlation",
                "N/Ti vs Rs correlation",
            ],
        })
        priority_questions.append(
            "Which compositional factor most strongly affects sheet resistance?"
        )

    if "Al_Ti_vs_Rs_ohm_sq" in correlations:
        planned_analyses.append({
            "analysis": "Al incorporation effect",
            "priority": "High",
            "reason": "Al/Ti ratio and Rs data are available.",
            "methods": [
                "Check whether Al incorporation improves or degrades conductivity.",
                "Evaluate trade-off between work function tuning and resistance.",
            ],
        })

    if "C_Ti_vs_Rs_ohm_sq" in correlations:
        planned_analyses.append({
            "analysis": "Carbon impurity effect",
            "priority": "High",
            "reason": "C/Ti ratio and Rs data are available.",
            "methods": [
                "Assess whether carbon impurity increases resistance.",
                "Connect precursor chemistry to electrical degradation.",
            ],
        })

    if detected["structure"]["detected"]:
        planned_analyses.append({
            "analysis": "Structure-property relationship",
            "priority": "Medium",
            "reason": "Structural data are available.",
            "methods": [
                "Compare crystallinity, roughness, or interface layer with electrical properties.",
            ],
        })

    if not planned_analyses:
        planned_analyses.append({
            "analysis": "Basic dataset inspection",
            "priority": "Medium",
            "reason": "No specialized data combination was detected.",
            "methods": [
                "Check available columns.",
                "Summarize numerical trends.",
                "Identify missing data.",
            ],
        })

    return {
        "planned_analyses": planned_analyses,
        "priority_questions": priority_questions,
    }