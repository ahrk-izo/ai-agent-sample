from app.llm.mock import MockLLMClient, create_mock_llm_client


def test_mock_llm_client_returns_fixed_response() -> None:
    client = MockLLMClient(response="固定レスポンスです。")

    result = client.generate("テストプロンプト")

    assert result == "固定レスポンスです。"


def test_mock_llm_client_stores_last_prompt() -> None:
    client = MockLLMClient(response="固定レスポンスです。")

    client.generate("テストプロンプト")

    assert client.last_prompt == "テストプロンプト"


def test_create_mock_llm_client_returns_client() -> None:
    client = create_mock_llm_client(response="固定レスポンスです。")

    assert client.generate("テストプロンプト") == "固定レスポンスです。"
