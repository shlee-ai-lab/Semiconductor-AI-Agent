from src.analyzer import load_dataset, summarize_dataset


def main():
    print("=" * 60)
    print("SERA v0.2")
    print("Semiconductor Experiment Analyzer")
    print("=" * 60)

    df = load_dataset("data/tialn_dataset.csv")
    summary = summarize_dataset(df)

    print("\n[Experiment Summary]\n")
    for key, value in summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()