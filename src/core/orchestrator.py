from src.core.config import load_config
from src.workflows.experiment_workflow import run as run_experiment_workflow


def run() -> None:
    config = load_config()

    print("=" * 60)
    print("SERA v1.0 Alpha")
    print("Workflow Orchestrator")
    print("=" * 60)

    run_experiment_workflow(config)