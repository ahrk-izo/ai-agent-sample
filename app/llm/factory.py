import os

from app.llm.base import LLMClient
from app.llm.mock import MockLLMClient
from app.llm.openai_client import OpenAILLMClient
from app.llm.sample_responses import MOCK_ORGANIZED_NOTE_RESPONSE

LLM_PROVIDER_ENV = "LLM_PROVIDER"
OPENAI_API_KEY_ENV = "OPENAI_API_KEY"
OPENAI_MODEL_ENV = "OPENAI_MODEL"

MOCK_PROVIDER = "mock"
OPENAI_PROVIDER = "openai"

DEFAULT_OPENAI_MODEL = "gpt-5.5"


def create_llm_client(provider: str | None = None) -> LLMClient:
    """指定されたプロバイダーに応じてLLMクライアントを生成する."""
    resolved_provider = (provider or os.getenv(LLM_PROVIDER_ENV, MOCK_PROVIDER)).lower()

    if resolved_provider == OPENAI_PROVIDER and os.getenv(OPENAI_API_KEY_ENV):
        model = os.getenv(OPENAI_MODEL_ENV, DEFAULT_OPENAI_MODEL)
        return OpenAILLMClient(model=model)

    return MockLLMClient(response=MOCK_ORGANIZED_NOTE_RESPONSE)
