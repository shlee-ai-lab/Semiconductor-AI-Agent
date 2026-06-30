import pandas as pd

from src.core.message_bus import MessageBus


MATERIAL_COLUMNS = [
    "Al_Ti",
    "C_Ti",
    "N_Ti",
    "O_Ti",
    "Cl_Ti",
    "Ti_at_percent",
    "Al_at_percent",
    "C_at_percent",
    "O_at_percent",
    "N_at_percent",
]


def analyze_material_data(df: pd.DataFrame, bus: MessageBus | None = None) -> dict:
    available_columns = [col for col in MATERIAL_COLUMNS if col in df.columns]

    if not available_columns:
        return {
            "agent": "Material Agent",
            "status": "No material composition data detected",
            "available_columns": [],
            "summary": {},
            "key_findings": [],
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

    key_findings = []

    if "Al_Ti" in available_columns:
        finding = "Al/Ti ratio is available and can be used to evaluate Al incorporation effect."
        key_findings.append(finding)

        if bus:
            bus.send(
                sender="Material Agent",
                receiver="Scientist Agent",
                message_type="evidence",
                content=finding,
                evidence=["Al_Ti detected"],
            )

    if "C_Ti" in available_columns:
        finding = "C/Ti ratio is available and should be checked as a possible impurity-related factor."
        key_findings.append(finding)

        if bus:
            bus.send(
                sender="Material Agent",
                receiver="Scientist Agent",
                message_type="evidence",
                content=finding,
                evidence=["C_Ti detected"],
            )

    if "O_Ti" in available_columns:
        finding = "O/Ti ratio is available and may indicate oxidation or interfacial reaction."
        key_findings.append(finding)

        if bus:
            bus.send(
                sender="Material Agent",
                receiver="Scientist Agent",
                message_type="evidence",
                content=finding,
                evidence=["O_Ti detected"],
            )

    return {
        "agent": "Material Agent",
        "status": "Material composition data analyzed",
        "available_columns": available_columns,
        "summary": summary,
        "key_findings": key_findings,
    }