from pathlib import Path


def load_markdown_files(folder_path: str) -> list[dict]:
    folder = Path(folder_path)

    if not folder.exists():
        return []

    records = []

    for file_path in folder.glob("*.md"):
        records.append(
            {
                "file_name": file_path.name,
                "path": str(file_path),
                "content": file_path.read_text(encoding="utf-8"),
            }
        )

    return records


def load_knowledge_base(base_path: str = "knowledge") -> dict:
    return {
        "literature": load_markdown_files(f"{base_path}/literature"),
        "experiments": load_markdown_files(f"{base_path}/experiments"),
        "mechanisms": load_markdown_files(f"{base_path}/mechanisms"),
    }


def extract_keywords_from_profile(profile: dict) -> list[str]:
    keywords = []

    detected = profile["detected_types"]

    if detected["composition_xps"]["detected"]:
        keywords += ["XPS", "composition", "Al", "carbon", "oxygen", "TiAlN"]

    if detected["electrical"]["detected"]:
        keywords += ["sheet resistance", "work function", "electrical", "gate metal"]

    if detected["structure"]["detected"]:
        keywords += ["crystallinity", "interface", "TEM", "structure"]

    keywords += ["TiAlN", "HfO2", "ALD", "GAA", "CFET"]

    return list(set(keywords))


def search_knowledge(knowledge_base: dict, keywords: list[str]) -> dict:
    results = {}

    for category, records in knowledge_base.items():
        matched_records = []

        for record in records:
            content_lower = record["content"].lower()
            score = 0

            for keyword in keywords:
                if keyword.lower() in content_lower:
                    score += 1

            if score > 0:
                matched_records.append(
                    {
                        "file_name": record["file_name"],
                        "path": record["path"],
                        "score": score,
                        "content": record["content"],
                    }
                )

        matched_records.sort(key=lambda x: x["score"], reverse=True)
        results[category] = matched_records

    return results