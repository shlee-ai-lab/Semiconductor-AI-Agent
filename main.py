from src.analyzer import (
    load_dataset,
    summarize_dataset,
    calculate_correlations,
)
from src.plotter import create_scatter_plot
from src.profiler import profile_dataset
from src.planner import create_analysis_plan
from src.knowledge import (
    load_knowledge_base,
    extract_keywords_from_profile,
    search_knowledge,
)
from src.report import create_research_context, assemble_final_report


def main():
    print("=" * 60)
    print("SERA v0.9")
    print("Knowledge Search Engine")
    print("=" * 60)

    df = load_dataset("data/tialn_dataset.csv")

    summary = summarize_dataset(df)
    correlations = calculate_correlations(df)
    profile = profile_dataset(df)
    analysis_plan = create_analysis_plan(profile, correlations)

    knowledge_base = load_knowledge_base()
    keywords = extract_keywords_from_profile(profile)
    knowledge_results = search_knowledge(knowledge_base, keywords)

    figure_paths = [
        "outputs/figures/al_ti_vs_rs.png",
        "outputs/figures/c_ti_vs_rs.png",
    ]

    create_scatter_plot(
        df=df,
        x_col="Al_Ti",
        y_col="Rs_ohm_sq",
        output_path=figure_paths[0],
        title="Al/Ti vs Sheet Resistance",
    )

    create_scatter_plot(
        df=df,
        x_col="C_Ti",
        y_col="Rs_ohm_sq",
        output_path=figure_paths[1],
        title="C/Ti vs Sheet Resistance",
    )

    report_path = "outputs/reports/tialn_research_context.md"

    create_research_context(
        summary=summary,
        correlations=correlations,
        profile=profile,
        analysis_plan=analysis_plan,
        knowledge_results=knowledge_results,
        figure_paths=figure_paths,
        output_path=report_path,
    )

    print(f"Saved research context: {report_path}")

    ai_interpretation_path = "outputs/reports/ai_interpretation.md"
    final_report_path = "outputs/reports/final_tialn_report.md"

    assemble_final_report(
        context_path=report_path,
        ai_interpretation_path=ai_interpretation_path,
        output_path=final_report_path,
    )

    print(f"Saved final report: {final_report_path}")


if __name__ == "__main__":
    main()