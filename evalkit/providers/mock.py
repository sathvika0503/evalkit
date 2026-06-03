from .base import BaseProvider


class MockProvider(BaseProvider):
    def generate(self, prompt: str) -> str:
        return "The Eiffel Tower was completed in 1889."