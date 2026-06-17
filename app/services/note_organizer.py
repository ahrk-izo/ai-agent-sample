from app.llm.base import LLMClient
from app.models.note import BusinessNoteInput, OrganizedNote
from app.prompts.note_prompt import build_note_organization_prompt


def organize_note(note: BusinessNoteInput, llm_client: LLMClient) -> OrganizedNote:
    """業務メモをLLMクライアント経由で整理する."""
    prompt = build_note_organization_prompt(note)
    response = llm_client.generate(prompt)

    return OrganizedNote(
        summary=response,
        decisions=["現時点ではLLMレスポンスの構造化は未実装です。"],
        todos=["現時点ではLLMレスポンスの構造化は未実装です。"],
        risks=["現時点ではLLMレスポンスの構造化は未実装です。"],
        next_actions=["現時点ではLLMレスポンスの構造化は未実装です。"],
    )
