import pytest
from pydantic import ValidationError

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

    result = organize_note(note)

    assert isinstance(result, OrganizedNote)
    assert result.summary == "入力された業務メモを整理した要約です。"
    assert result.decisions == ["現時点ではダミーの決定事項です。"]
    assert result.todos == ["現時点ではダミーのTODOです。"]
    assert result.risks == ["現時点ではダミーのリスクです。"]
    assert result.next_actions == ["現時点ではダミーの次アクションです。"]
