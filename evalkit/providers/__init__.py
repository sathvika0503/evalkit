from evalkit.providers.mock import MockProvider
from evalkit.providers.openai_provider import OpenAIProvider

PROVIDERS = {
    "mock": MockProvider,
    "openai": OpenAIProvider,
}