from openai import OpenAI

from evalkit.providers.base import Provider


class OpenAIProvider(Provider):
    def __init__(self, model: str):
        self.model = model
        self.client = OpenAI()

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text