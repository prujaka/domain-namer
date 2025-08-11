def generate_markdown_block(entry: dict, n: int) -> str:
    block = (f"## Example {n}\n"
             f"Business description: {entry['business_description']}\n\n"
             f"Output:\n"
             f"```\n{entry['output']}\n```\n")
    return block


def generate_markdown_report(model_name: str, prompt: str,
                             entries: list[dict]) -> str:
    body = (f"# {model_name}\n"
            f"Prompt:\n{prompt}\n")
    for i, entry in enumerate(entries):
        body += generate_markdown_block(entry, i + 1)
    return body

