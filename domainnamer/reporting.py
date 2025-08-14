def _md_code_block(text: str) -> str:
    """Wrap text in a fenced code block."""
    return f"```\n{text}\n```\n"


def generate_md_example_block(entry: dict, n: int) -> str:
    """Return a formatted markdown block for a single user example."""
    return (
        f"### Example {n}\n"
        f"**User prompt:** {entry['user_prompt']}\n\n"
        f"**Output:**\n"
        f"{_md_code_block(entry['output'])}\n"
    )


def generate_md_system_section(prompt_system: str, examples: list[dict], idx: int) -> str:
    """Return a markdown section for one system prompt with its examples."""
    section = (
        f"## System Prompt {idx}\n\n"
        f"{_md_code_block(prompt_system)}\n"
    )
    for i, ex in enumerate(examples, start=1):
        section += generate_md_example_block(ex, i)
    return section


def generate_markdown_report_new(model_name: str, systems: list[dict]) -> str:
    """Return a complete markdown report grouped by system prompts
    for a model."""
    body = f"# {model_name}\n\n"
    for s_idx, sys_block in enumerate(systems, start=1):
        body += generate_md_system_section(
            prompt_system=sys_block["prompt_system"],
            examples=sys_block["examples"],
            idx=s_idx
        )
    return body


def write_reports(outputs: list[dict], dir_path: str) -> None:
    """Write one markdown file per model with sections per system prompt."""
    import os
    os.makedirs(dir_path, exist_ok=True)
    for model_block in outputs:
        model = model_block["model"].split("/")[-1]
        systems = model_block["systems"]
        md = generate_markdown_report_new(model, systems)
        with open(f"{dir_path}/{model}.md", "w", encoding="utf-8") as f:
            f.write(md)
