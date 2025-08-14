from openai import OpenAI


def generate_output(client: OpenAI, model_name: str, prompt_system: str,
                    prompt_user: str) -> str:
    """Generate a single model output for a given model and user prompt."""
    # noinspection PyTypeChecker
    chat_completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {'role': 'system', 'content': f'{prompt_system}'},
            {'role': 'user', 'content': f'{prompt_user}'}]
    )
    return chat_completion.choices[0].message.content


def generate_outputs(
        client: OpenAI,
        model_names: list[str],
        system_prompts: list[str],
        user_prompts: list[str]) -> list[dict]:
    """Generate outputs for each model, grouped by system prompt with multiple
    user prompts."""
    results = []
    for model_name in model_names:
        systems_block = []
        for prompt_system in system_prompts:
            examples = []
            for prompt_user in user_prompts:
                output_text = generate_output(client, model_name, prompt_system,
                                              prompt_user)
                examples.append({
                    "user_prompt": prompt_user,
                    "output": output_text,
                })
            systems_block.append({
                "prompt_system": prompt_system,
                "examples": examples,
            })
        results.append({
            "model": model_name,
            "systems": systems_block,
        })

    return results
