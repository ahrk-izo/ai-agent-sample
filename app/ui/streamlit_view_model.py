from app.llm.base import LLMClient
from app.llm.mock import MockLLMClient
from app.llm.sample_responses import MOCK_ORGANIZED_NOTE_RESPONSE
from app.models.note import BusinessNoteInput, OrganizedNote
from app.services.note_organizer import organize_note


def create_mock_note_llm_client() -> LLMClient:
    """Streamlit UIで利用するモックLLMクライアントを生成する."""
    return MockLLMClient(response=MOCK_ORGANIZED_NOTE_RESPONSE)


def organize_note_text(
    content: str, llm_client: LLMClient | None = None
) -> OrganizedNote:
    """入力テキストを業務メモとして整理する."""
    note = BusinessNoteInput(content=content)
    client = llm_client or create_mock_note_llm_client()

    return organize_note(note, client)
