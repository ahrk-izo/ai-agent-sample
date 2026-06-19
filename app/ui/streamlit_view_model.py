from app.llm.base import LLMClient
from app.llm.factory import create_llm_client
from app.models.note import BusinessNoteInput, OrganizedNote
from app.services.note_organizer import organize_note


def organize_note_text(
    content: str,
    llm_client: LLMClient | None = None,
    provider: str | None = None,
) -> OrganizedNote:
    """入力テキストを業務メモとして整理する."""
    note = BusinessNoteInput(content=content)
    client = llm_client or create_llm_client(provider=provider)

    return organize_note(note, client)
