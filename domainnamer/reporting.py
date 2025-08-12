def generate_markdown_block(entry: dict, n: int) -> str:
    """Return a formatted markdown block for a single example entry."""
    block = (f"## Example {n}\n"
             f"Business description: {entry['business_description']}\n\n"
             f"Output:\n"
             f"```\n"
             f"{entry['output']}\n"
             f"```\n")
    return block


def generate_markdown_report(model_name: str, prompt: str,
                             outputs: list[dict]) -> str:
    """Return a complete markdown report for a model's prompt and outputs."""
    body = (f"# {model_name}\n"
            f"Prompt:\n"
            f"```\n"
            f"{prompt}\n"
            f"```\n")
    for i, entry in enumerate(outputs):
        body += generate_markdown_block(entry, i + 1)
    return body


def write_reports(outputs: dict, prompt_system: str, dir_path: str) -> None:
    """Write markdown reports for each model's outputs to a given directory."""
    for output in outputs:
        model = output["model"].split('/')[-1]
        entries = output["examples"]
        with open(f'{dir_path}/{model}.md', 'w') as f:
            f.write(generate_markdown_report(model, prompt_system, entries))
    return None
