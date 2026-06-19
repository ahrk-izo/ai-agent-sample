from app.llm.factory import create_llm_client
from app.llm.mock import MockLLMClient
from app.llm.openai_client import OpenAILLMClient


def test_create_llm_client_returns_mock_by_default(monkeypatch) -> None:
    monkeypatch.delenv("LLM_PROVIDER", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    llm_client = create_llm_client()

    assert isinstance(llm_client, MockLLMClient)


def test_create_llm_client_returns_mock_when_openai_api_key_is_missing(
    monkeypatch,
) -> None:
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    llm_client = create_llm_client()

    assert isinstance(llm_client, MockLLMClient)


def test_create_llm_client_returns_openai_when_provider_is_openai_and_api_key_exists(
    monkeypatch,
) -> None:
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "dummy-api-key")
    monkeypatch.setenv("OPENAI_MODEL", "test-model")

    llm_client = create_llm_client()

    assert isinstance(llm_client, OpenAILLMClient)
    assert llm_client.model == "test-model"


def test_create_llm_client_uses_provider_argument(monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "dummy-api-key")
    monkeypatch.setenv("OPENAI_MODEL", "test-model")

    llm_client = create_llm_client(provider="openai")

    assert isinstance(llm_client, OpenAILLMClient)
