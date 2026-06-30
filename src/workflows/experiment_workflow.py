from pathlib import Path

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
from src.agents.electrical_agent import analyze_electrical_data
from src.agents.material_agent import analyze_material_data
from src.agents.scientist_agent import synthesize_agent_reports


def run(config: dict) -> None:
    experiment_folder = Path(config["experiment"]["folder"])
    dataset_path = experiment_folder / "data" / "tialn_dataset.csv"

    df = load_dataset(dataset_path)

    summary = summarize_dataset(df)
    correlations = calculate_correlations(df)
    profile = profile_dataset(df)
    analysis_plan = create_analysis_plan(profile, correlations)

    electrical_report = analyze_electrical_data(df)
    material_report = analyze_material_data(df)
    scientist_report = synthesize_agent_reports(
        electrical_report=electrical_report,
        material_report=material_report,
    )

    knowledge_base = load_knowledge_base()
    keywords = extract_keywords_from_profile(profile)
    knowledge_results = search_knowledge(knowledge_base, keywords)

    figure_dir = Path(config["outputs"]["figure_dir"])
    report_dir = Path(config["outputs"]["report_dir"])

    figure_paths = []

    for fig in config["figures"]:
        output_path = figure_dir / fig["filename"]
        figure_paths.append(str(output_path))

        create_scatter_plot(
            df=df,
            x_col=fig["x"],
            y_col=fig["y"],
            output_path=str(output_path),
            title=fig["title"],
        )

    context_path = report_dir / config["outputs"]["context_report"]

    create_research_context(
        summary=summary,
        correlations=correlations,
        profile=profile,
        analysis_plan=analysis_plan,
        electrical_report=electrical_report,
        material_report=material_report,
        scientist_report=scientist_report,
        knowledge_results=knowledge_results,
        figure_paths=figure_paths,
        output_path=str(context_path),
    )

    print(f"Saved research context: {context_path}")

    ai_interpretation_path = report_dir / config["outputs"]["ai_interpretation"]
    final_report_path = report_dir / config["outputs"]["final_report"]

    assemble_final_report(
        context_path=str(context_path),
        ai_interpretation_path=str(ai_interpretation_path),
        output_path=str(final_report_path),
    )

    print(f"Saved final report: {final_report_path}")