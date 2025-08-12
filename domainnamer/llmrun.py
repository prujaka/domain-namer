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


def generate_multiple_outputs(client: OpenAI, model_names: list[str],
                              prompt_system: str,
                              prompts_user: list[str]) -> list[str]:
    """Generate outputs for multiple models across multiple user prompts."""
    outputs = []
    for model_name in model_names:
        examples = []
        for prompt_user in prompts_user:
            output = generate_output(client, model_name, prompt_system,
                                     prompt_user)
            output_dict = {'business_description': prompt_user,
                           'output': output}
            examples.append(output_dict)
        examples_dict = {'model': model_name, 'examples': examples}
        outputs.append(examples_dict)

    return outputs
