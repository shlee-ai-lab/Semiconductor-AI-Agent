from pathlib import Path
from datetime import datetime


def save_experiment_memory(
    experiment_id: str,
    project_name: str,
    summary: dict,
    electrical_report: dict,
    material_report: dict,
    scientist_report: dict,
    output_dir: str = "memory/experiments",
) -> str:
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = Path(output_dir) / f"{experiment_id}_{timestamp}.md"

    lines = []

    lines.append(f"# Experiment Memory: {experiment_id}")
    lines.append("")
    lines.append(f"- Project: {project_name}")
    lines.append(f"- Created at: {timestamp}")
    lines.append("")

    lines.append("## Dataset Summary")
    lines.append("")
    for key, value in summary.items():
        lines.append(f"- **{key}**: {value}")
    lines.append("")

    lines.append("## Electrical Agent Memory")
    lines.append("")
    lines.append(f"- Status: {electrical_report['status']}")
    lines.append(f"- Columns: {electrical_report.get('available_columns', [])}")
    lines.append("")

    lines.append("## Material Agent Memory")
    lines.append("")
    lines.append(f"- Status: {material_report['status']}")
    lines.append(f"- Columns: {material_report.get('available_columns', [])}")
    lines.append("")

    lines.append("## Scientist Agent Memory")
    lines.append("")
    lines.append(f"- Status: {scientist_report['status']}")
    lines.append("")
    lines.append("### Hypotheses")
    for item in scientist_report.get("hypotheses", []):
        lines.append(f"- {item}")
    lines.append("")

    lines.append("### Cross-Agent Questions")
    for item in scientist_report.get("cross_agent_questions", []):
        lines.append(f"- {item}")
    lines.append("")

    file_path.write_text("\n".join(lines), encoding="utf-8")

    return str(file_path)