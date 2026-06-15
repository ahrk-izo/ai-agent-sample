from app.llm.base import LLMClient


class MockLLMClient:
    """外部APIを呼び出さず、固定レスポンスを返すテスト用LLMクライアント."""

    def __init__(self, response: str) -> None:
        self.response = response
        self.last_prompt: str | None = None

    def generate(self, prompt: str) -> str:
        """受け取ったプロンプトを記録し、固定レスポンスを返す."""
        self.last_prompt = prompt
        return self.response


def create_mock_llm_client(response: str) -> LLMClient:
    return MockLLMClient(response=response)
