def read_prompt(filepath: str) -> str:
    with open(filepath, 'r') as f:
        prompt_lines = f.readlines()
    return ''.join(prompt_lines)
