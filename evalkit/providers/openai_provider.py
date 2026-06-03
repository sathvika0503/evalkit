import os

from openai import OpenAI

from evalkit.providers.base import BaseProvider


class OpenAIProvider(BaseProvider):
    def __init__(self, model: str):
        self.model = model

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY environment variable not set"
            )

        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text