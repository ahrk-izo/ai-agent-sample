from app.llm.base import LLMClient
from app.models.note import BusinessNoteInput, OrganizedNote
from app.parsers.note_response_parser import parse_organized_note_response
from app.prompts.note_prompt import build_note_organization_prompt


def organize_note(note: BusinessNoteInput, llm_client: LLMClient) -> OrganizedNote:
    """業務メモをLLMクライアント経由で整理する."""
    prompt = build_note_organization_prompt(note)
    response = llm_client.generate(prompt)

    return parse_organized_note_response(response)
