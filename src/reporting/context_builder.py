from pathlib import Path


def _append_agent_summary(lines: list[str], report: dict) -> None:
    lines.append(f"## {report['agent']} Report")
    lines.append("")
    lines.append(f"- **Status**: {report['status']}")
    lines.append(f"- **Available columns**: {report.get('available_columns', [])}")
    lines.append("")

    if report.get("summary"):
        lines.append("### Summary")
        lines.append("")
        for col, stats in report["summary"].items():
            lines.append(f"- **{col}**")
            for key, value in stats.items():
                lines.append(f"  - {key}: {value}")
        lines.append("")

    if report.get("key_findings"):
        lines.append("### Key Findings")
        lines.append("")
        for item in report["key_findings"]:
            lines.append(f"- {item}")
        lines.append("")

    if report.get("questions_for_other_agents"):
        lines.append("### Questions for Other Agents")
        lines.append("")
        for item in report["questions_for_other_agents"]:
            lines.append(f"- {item}")
        lines.append("")


def create_research_context(
    summary: dict,
    correlations: dict,
    profile: dict,
    analysis_plan: dict,
    electrical_report: dict,
    material_report: dict,
    scientist_report: dict,
    knowledge_results: dict,
    figure_paths: list[str],
    output_path: str,
) -> None:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    lines = []

    lines.append("# SERA Research Context Package")
    lines.append("")
    lines.append("## 1. Project Information")
    lines.append("")
    lines.append("Project: TiAlN gate metal for advanced GAA/CFET devices")
    lines.append("")
    lines.append("Research Goal:")
    lines.append("- Evaluate TiAlN as a gate metal candidate for advanced GAA/CFET devices.")
    lines.append("- Understand the relationship between process variables, composition, structure, and electrical properties.")
    lines.append("")

    lines.append("## 2. Dataset Summary")
    lines.append("")
    for key, value in summary.items():
        lines.append(f"- **{key}**: {value}")
    lines.append("")

    lines.append("## 3. Data Profile")
    lines.append("")
    for data_type, info in profile["detected_types"].items():
        lines.append(f"- **{data_type}**")
        lines.append(f"  - Detected: {info['detected']}")
        lines.append(f"  - Matched columns: {info['matched_columns']}")
    lines.append("")

    lines.append("## 4. Correlation Summary")
    lines.append("")
    for key, value in correlations.items():
        lines.append(f"- **{key}**: {value}")
    lines.append("")

    lines.append("## 5. Research Planner Output")
    lines.append("")
    for item in analysis_plan["planned_analyses"]:
        lines.append(f"- **Analysis**: {item['analysis']}")
        lines.append(f"  - Priority: {item['priority']}")
        lines.append(f"  - Reason: {item['reason']}")
        lines.append("  - Methods:")
        for method in item["methods"]:
            lines.append(f"    - {method}")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("# Multi-Agent Analysis")
    lines.append("")

    _append_agent_summary(lines, electrical_report)
    _append_agent_summary(lines, material_report)

    lines.append("## Scientist Agent Report")
    lines.append("")
    lines.append(f"- **Status**: {scientist_report['status']}")
    lines.append("")

    lines.append("### Cross-Agent Hypotheses")
    lines.append("")
    for item in scientist_report["hypotheses"]:
        lines.append(f"- {item}")
    lines.append("")

    lines.append("### Cross-Agent Questions")
    lines.append("")
    for item in scientist_report["cross_agent_questions"]:
        lines.append(f"- {item}")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Relevant Knowledge")
    lines.append("")
    for category, records in knowledge_results.items():
        lines.append(f"### {category}")
        lines.append("")

        if not records:
            lines.append("- No relevant knowledge found.")
            lines.append("")
            continue

        for record in records[:3]:
            lines.append(f"#### {record['file_name']}")
            lines.append(f"- Path: `{record['path']}`")
            lines.append(f"- Match Score: {record['score']}")
            lines.append("")
            lines.append(record["content"])
            lines.append("")

    lines.append("## Generated Figures")
    lines.append("")
    for i, path in enumerate(figure_paths, start=1):
        lines.append(f"- Figure {i}: `{path}`")
    lines.append("")

    lines.append("## Requested AI Output")
    lines.append("")
    lines.append("Please write the following sections in Korean technical research style:")
    lines.append("")
    lines.append("1. Results summary")
    lines.append("2. Discussion")
    lines.append("3. Possible mechanism")
    lines.append("4. Cross-agent interpretation")
    lines.append("5. How the current result relates to the retrieved knowledge")
    lines.append("6. Limitations of the current dataset")
    lines.append("7. Recommended next experiments")
    lines.append("8. One-slide PPT message")
    lines.append("")
    lines.append("Important rule: Do not invent missing data. Clearly separate observation, interpretation, and hypothesis.")
    lines.append("")

    Path(output_path).write_text("\n".join(lines), encoding="utf-8")


def assemble_final_report(
    context_path: str,
    ai_interpretation_path: str,
    output_path: str,
) -> None:
    context = Path(context_path).read_text(encoding="utf-8")
    interpretation = Path(ai_interpretation_path).read_text(encoding="utf-8")

    lines = []

    lines.append("# Final TiAlN Research Report")
    lines.append("")
    lines.append("## Part 1. Research Context")
    lines.append("")
    lines.append(context)
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Part 2. AI Scientist Interpretation")
    lines.append("")
    lines.append(interpretation)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text("\n".join(lines), encoding="utf-8")