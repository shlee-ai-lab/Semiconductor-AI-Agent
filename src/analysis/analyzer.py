import pandas as pd


def load_dataset(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)


def summarize_dataset(df: pd.DataFrame) -> dict:
    summary = {
        "sample_count": len(df),
        "columns": list(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "substrates": df["Substrate"].dropna().unique().tolist(),
        "temperatures_C": df["Temperature_C"].dropna().unique().tolist(),
        "ratios": df["TiN_AlN_Ratio"].dropna().unique().tolist(),
        "average_rs_ohm_sq": round(df["Rs_ohm_sq"].mean(), 2),
        "min_rs_ohm_sq": round(df["Rs_ohm_sq"].min(), 2),
        "max_rs_ohm_sq": round(df["Rs_ohm_sq"].max(), 2),
        "average_al_ti": round(df["Al_Ti"].mean(), 3),
        "average_c_ti": round(df["C_Ti"].mean(), 3),
        "average_n_ti": round(df["N_Ti"].mean(), 3),
        "average_o_ti": round(df["O_Ti"].mean(), 3),
    }

    if "Work_Function_eV" in df.columns:
        summary["average_work_function_eV"] = round(df["Work_Function_eV"].mean(), 2)

    return summary


def calculate_correlations(df: pd.DataFrame) -> dict:
    target = "Rs_ohm_sq"
    variables = ["Al_Ti", "C_Ti", "N_Ti", "O_Ti"]

    correlations = {}

    for var in variables:
        if var in df.columns and target in df.columns:
            correlations[f"{var}_vs_{target}"] = round(df[var].corr(df[target]), 3)

    if "Work_Function_eV" in df.columns:
        for var in variables:
            if var in df.columns:
                correlations[f"{var}_vs_Work_Function_eV"] = round(
                    df[var].corr(df["Work_Function_eV"]), 3
                )

    return correlations