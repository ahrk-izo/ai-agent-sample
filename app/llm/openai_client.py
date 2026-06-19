from typing import Any

from openai import OpenAI


class OpenAILLMClient:
    """OpenAI APIを利用するLLMクライアント."""

    def __init__(self, model: str, client: Any | None = None) -> None:
        self.model = model
        self.client = client or OpenAI()

    def generate(self, prompt: str) -> str:
        """プロンプトをOpenAI APIに送信し、生成結果を返す."""
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return str(response.output_text)
