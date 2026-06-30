import pandas as pd

from src.core.message_bus import MessageBus


ELECTRICAL_COLUMNS = [
    "Rs_ohm_sq",
    "Resistivity_uohm_cm",
    "Work_Function_eV",
    "Vfb_V",
    "Leakage_A_cm2",
    "Ion_uA_um",
    "Ioff_A_um",
]


def analyze_electrical_data(df: pd.DataFrame, bus: MessageBus | None = None) -> dict:
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
        question = "Check whether composition or impurity changes explain sheet resistance variation."
        questions_for_other_agents.append(f"Material Agent: {question}")

        if bus:
            bus.send(
                sender="Electrical Agent",
                receiver="Material Agent",
                message_type="question",
                content=question,
                evidence=["Rs_ohm_sq detected"],
            )

        question = "Check whether crystallinity, thickness, or interface quality explains sheet resistance variation."
        questions_for_other_agents.append(f"Structure Agent: {question}")

        if bus:
            bus.send(
                sender="Electrical Agent",
                receiver="Structure Agent",
                message_type="question",
                content=question,
                evidence=["Rs_ohm_sq detected"],
            )

    if "Work_Function_eV" in available_columns:
        question = "Check whether Al incorporation or interface dipole can explain work function shift."
        questions_for_other_agents.append(f"Material Agent: {question}")

        if bus:
            bus.send(
                sender="Electrical Agent",
                receiver="Material Agent",
                message_type="question",
                content=question,
                evidence=["Work_Function_eV detected"],
            )

    return {
        "agent": "Electrical Agent",
        "status": "Electrical data analyzed",
        "available_columns": available_columns,
        "summary": summary,
        "questions_for_other_agents": questions_for_other_agents,
    }