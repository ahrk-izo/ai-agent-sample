from app.llm.openai_client import OpenAILLMClient


class FakeOpenAIResponse:
    output_text = '{"summary": "要約です。"}'


class FakeResponses:
    def __init__(self) -> None:
        self.called_model: str | None = None
        self.called_input: str | None = None

    def create(self, *, model: str, input: str) -> FakeOpenAIResponse:
        self.called_model = model
        self.called_input = input
        return FakeOpenAIResponse()


class FakeOpenAIClient:
    def __init__(self) -> None:
        self.responses = FakeResponses()


def test_openai_llm_client_generate_returns_output_text() -> None:
    fake_client = FakeOpenAIClient()
    llm_client = OpenAILLMClient(model="test-model", client=fake_client)

    result = llm_client.generate("test prompt")

    assert result == '{"summary": "要約です。"}'


def test_openai_llm_client_passes_model_and_prompt() -> None:
    fake_client = FakeOpenAIClient()
    llm_client = OpenAILLMClient(model="test-model", client=fake_client)

    llm_client.generate("test prompt")

    assert fake_client.responses.called_model == "test-model"
    assert fake_client.responses.called_input == "test prompt"
