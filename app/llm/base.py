from typing import Protocol


class LLMClient(Protocol):
    """LLM呼び出しを抽象化するためのインターフェース."""

    def generate(self, prompt: str) -> str:
        """プロンプトを受け取り、LLMの生成結果を返す."""
        ...
