from .base import Provider


class MockProvider(Provider):
    def generate(self, prompt: str) -> str:
        return "The Eiffel Tower was completed in 1889."