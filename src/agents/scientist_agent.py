def synthesize_agent_reports(
    electrical_report: dict,
    material_report: dict,
) -> dict:
    hypotheses = []
    cross_agent_questions = []

    electrical_cols = electrical_report.get("available_columns", [])
    material_cols = material_report.get("available_columns", [])

    if "Rs_ohm_sq" in electrical_cols and "C_Ti" in material_cols:
        hypotheses.append(
            "Sheet resistance variation may be related to carbon impurity incorporation."
        )

    if "Rs_ohm_sq" in electrical_cols and "O_Ti" in material_cols:
        hypotheses.append(
            "Sheet resistance variation may be influenced by oxygen incorporation or interfacial oxidation."
        )

    if "Work_Function_eV" in electrical_cols and "Al_Ti" in material_cols:
        hypotheses.append(
            "Work function shift may be related to Al incorporation in TiAlN."
        )

    if "Rs_ohm_sq" in electrical_cols and "Al_Ti" in material_cols:
        cross_agent_questions.append(
            "Does increasing Al/Ti improve work-function tuning while degrading or improving sheet resistance?"
        )

    if "C_Ti" in material_cols or "O_Ti" in material_cols:
        cross_agent_questions.append(
            "Are impurity trends consistent with the observed electrical behavior?"
        )

    if not hypotheses:
        hypotheses.append(
            "Current dataset is insufficient for strong cross-agent mechanism inference."
        )

    return {
        "agent": "Scientist Agent",
        "status": "Cross-agent synthesis completed",
        "hypotheses": hypotheses,
        "cross_agent_questions": cross_agent_questions,
    }