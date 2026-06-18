import pytest
from pydantic import ValidationError

from app.llm.mock import MockLLMClient
from app.models.note import BusinessNoteInput, OrganizedNote
from app.services.note_organizer import organize_note


def test_business_note_input_accepts_content() -> None:
    note = BusinessNoteInput(content="会議で次回までに資料を確認することになった。")

    assert note.content == "会議で次回までに資料を確認することになった。"


def test_business_note_input_rejects_empty_content() -> None:
    with pytest.raises(ValidationError):
        BusinessNoteInput(content="")


def test_organize_note_returns_organized_note() -> None:
    note = BusinessNoteInput(content="会議で次回までに資料を確認することになった。")
    llm_client = MockLLMClient(
        response="""{
  "summary": "会議メモの要約です。",
  "decisions": ["方針を決定する"],
  "todos": ["資料を確認する"],
  "risks": ["レビュー時間が不足する"],
  "next_actions": ["次回会議の日程を調整する"]
}"""
    )

    result = organize_note(note, llm_client)

    assert isinstance(result, OrganizedNote)
    assert result.summary == "会議メモの要約です。"
    assert result.decisions == ["方針を決定する"]
    assert result.todos == ["資料を確認する"]
    assert result.risks == ["レビュー時間が不足する"]
    assert result.next_actions == ["次回会議の日程を調整する"]


def test_organize_note_passes_prompt_to_llm_client() -> None:
    note = BusinessNoteInput(content="期限は金曜日。")
    llm_client = MockLLMClient(
        response="""{
  "summary": "整理結果です。",
  "decisions": [],
  "todos": [],
  "risks": [],
  "next_actions": []
}"""
    )

    organize_note(note, llm_client)

    assert llm_client.last_prompt is not None
    assert "期限は金曜日。" in llm_client.last_prompt
