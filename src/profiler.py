import pandas as pd


COLUMN_RULES = {
    "process": [
        "Temperature_C",
        "Pressure_Torr",
        "TiN_AlN_Ratio",
        "Cycle",
        "Cycles",
        "Thickness_nm",
    ],
    "composition_xps": [
        "Al_Ti",
        "C_Ti",
        "N_Ti",
        "O_Ti",
        "Ti_at_percent",
        "Al_at_percent",
        "C_at_percent",
        "O_at_percent",
        "N_at_percent",
    ],
    "electrical": [
        "Rs_ohm_sq",
        "Resistivity_uohm_cm",
        "Work_Function_eV",
        "Vfb_V",
        "Leakage_A_cm2",
    ],
    "structure": [
        "Crystallinity",
        "Grain_Size_nm",
        "Roughness_nm",
        "Interface_Layer",
        "TEM_Thickness_nm",
    ],
}


def profile_dataset(df: pd.DataFrame) -> dict:
    columns = list(df.columns)

    detected_types = {}
    for data_type, expected_columns in COLUMN_RULES.items():
        matched = [col for col in expected_columns if col in columns]
        detected_types[data_type] = {
            "matched_columns": matched,
            "score": len(matched),
            "detected": len(matched) > 0,
        }

    recommended_analyses = []

    if detected_types["composition_xps"]["detected"] and detected_types["electrical"]["detected"]:
        recommended_analyses.append(
            "Analyze correlation between XPS-derived composition and electrical properties."
        )

    if "TiN_AlN_Ratio" in columns and "Rs_ohm_sq" in columns:
        recommended_analyses.append(
            "Compare sheet resistance as a function of TiN:AlN supercycle ratio."
        )

    if "Work_Function_eV" in columns:
        recommended_analyses.append(
            "Evaluate work function tuning behavior and its trade-off with conductivity."
        )

    if detected_types["structure"]["detected"] and detected_types["electrical"]["detected"]:
        recommended_analyses.append(
            "Analyze relationship between structural properties and electrical properties."
        )

    ai_questions = []

    if detected_types["composition_xps"]["detected"]:
        ai_questions.append(
            "How do composition and impurity changes influence the material properties?"
        )

    if detected_types["electrical"]["detected"]:
        ai_questions.append(
            "What process or material factors may explain the observed electrical properties?"
        )

    if detected_types["structure"]["detected"]:
        ai_questions.append(
            "How do structural features such as crystallinity, thickness, or interface layers affect device-relevant behavior?"
        )

    if "TiN_AlN_Ratio" in columns:
        ai_questions.append(
            "What is the likely effect of TiN:AlN supercycle ratio on TiAlN gate metal performance?"
        )

    return {
        "columns": columns,
        "detected_types": detected_types,
        "recommended_analyses": recommended_analyses,
        "ai_questions": ai_questions,
    }