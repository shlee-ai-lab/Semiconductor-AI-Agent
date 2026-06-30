from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def create_scatter_plot(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    output_path: str,
    title: str,
) -> None:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    plt.figure()
    plt.scatter(df[x_col], df[y_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()