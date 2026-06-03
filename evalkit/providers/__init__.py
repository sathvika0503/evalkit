from .mock import MockProvider
from .openai_provider import OpenAIProvider
from .openrouter_provider import OpenRouterProvider

PROVIDERS = {
    "mock": MockProvider,
    "openai": OpenAIProvider,
    "openrouter": OpenRouterProvider,
}