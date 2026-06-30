from pathlib import Path
import json


def build_experiment_graph(
    experiment_id: str,
    material_report: dict,
    electrical_report: dict,
    scientist_report: dict,
) -> dict:
    nodes = []
    edges = []

    nodes.append({"id": experiment_id, "type": "experiment"})

    for col in material_report.get("available_columns", []):
        node_id = f"material_metric:{col}"
        nodes.append({"id": node_id, "type": "material_metric"})
        edges.append({
            "source": experiment_id,
            "target": node_id,
            "relationship": "has_material_metric",
        })

    for col in electrical_report.get("available_columns", []):
        node_id = f"electrical_metric:{col}"
        nodes.append({"id": node_id, "type": "electrical_metric"})
        edges.append({
            "source": experiment_id,
            "target": node_id,
            "relationship": "has_electrical_metric",
        })

    for i, hypothesis in enumerate(scientist_report.get("hypotheses", []), start=1):
        node_id = f"{experiment_id}:hypothesis:{i}"
        nodes.append({
            "id": node_id,
            "type": "hypothesis",
            "text": hypothesis,
        })
        edges.append({
            "source": experiment_id,
            "target": node_id,
            "relationship": "generates_hypothesis",
        })

    return {
        "experiment_id": experiment_id,
        "nodes": nodes,
        "edges": edges,
    }


def save_experiment_graph(
    graph: dict,
    output_dir: str = "memory/graph",
) -> str:
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    experiment_id = graph["experiment_id"]
    output_path = Path(output_dir) / f"{experiment_id}_graph.json"

    output_path.write_text(
        json.dumps(graph, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return str(output_path)