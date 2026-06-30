from src.analysis.analyzer import (
    load_dataset,
    summarize_dataset,
    calculate_correlations,
)
from src.visualization.plotter import create_scatter_plot
from src.profiling.profiler import profile_dataset
from src.planning.planner import create_analysis_plan
from src.knowledge.retrieval import (
    load_knowledge_base,
    extract_keywords_from_profile,
    search_knowledge,
)
from src.reporting.context_builder import (
    create_research_context,
    assemble_final_report,
)


def run_experiment_workflow() -> None:
    print("=" * 60)
    print("SERA v1.0 Alpha")
    print("Experiment Workflow Orchestrator")
    print("=" * 60)

    dataset_path = "data/tialn_dataset.csv"

    df = load_dataset(dataset_path)

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

    context_path = "outputs/reports/tialn_research_context.md"

    create_research_context(
        summary=summary,
        correlations=correlations,
        profile=profile,
        analysis_plan=analysis_plan,
        knowledge_results=knowledge_results,
        figure_paths=figure_paths,
        output_path=context_path,
    )

    print(f"Saved research context: {context_path}")

    ai_interpretation_path = "outputs/reports/ai_interpretation.md"
    final_report_path = "outputs/reports/final_tialn_report.md"

    assemble_final_report(
        context_path=context_path,
        ai_interpretation_path=ai_interpretation_path,
        output_path=final_report_path,
    )

    print(f"Saved final report: {final_report_path}")