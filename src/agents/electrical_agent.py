import pandas as pd


ELECTRICAL_COLUMNS = [
    "Rs_ohm_sq",
    "Resistivity_uohm_cm",
    "Work_Function_eV",
    "Vfb_V",
    "Leakage_A_cm2",
    "Ion_uA_um",
    "Ioff_A_um",
]


def analyze_electrical_data(df: pd.DataFrame) -> dict:
    available_columns = [col for col in ELECTRICAL_COLUMNS if col in df.columns]

    if not available_columns:
        return {
            "agent": "Electrical Agent",
            "status": "No electrical data detected",
            "available_columns": [],
            "summary": {},
            "questions_for_other_agents": [],
        }

    summary = {}

    for col in available_columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            summary[col] = {
                "mean": round(df[col].mean(), 4),
                "min": round(df[col].min(), 4),
                "max": round(df[col].max(), 4),
                "std": round(df[col].std(), 4),
            }

    questions_for_other_agents = []

    if "Rs_ohm_sq" in available_columns:
        questions_for_other_agents.append(
            "Material Agent: Check whether composition or impurity changes explain sheet resistance variation."
        )
        questions_for_other_agents.append(
            "Structure Agent: Check whether crystallinity, thickness, or interface quality explains sheet resistance variation."
        )

    if "Work_Function_eV" in available_columns:
        questions_for_other_agents.append(
            "Material Agent: Check whether Al incorporation or interface dipole can explain work function shift."
        )

    if "Leakage_A_cm2" in available_columns:
        questions_for_other_agents.append(
            "Structure Agent: Check whether interface defects or film non-uniformity explain leakage behavior."
        )

    return {
        "agent": "Electrical Agent",
        "status": "Electrical data analyzed",
        "available_columns": available_columns,
        "summary": summary,
        "questions_for_other_agents": questions_for_other_agents,
    }