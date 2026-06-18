from app.models.note import BusinessNoteInput
from app.prompts.note_prompt import build_note_organization_prompt


def test_build_note_organization_prompt_includes_note_content() -> None:
    note = BusinessNoteInput(content="金曜日までに資料を確認する。")

    prompt = build_note_organization_prompt(note)

    assert "以下の業務メモを整理してください。" in prompt
    assert "金曜日までに資料を確認する。" in prompt


def test_build_note_organization_prompt_includes_output_items() -> None:
    note = BusinessNoteInput(content="会議メモです。")

    prompt = build_note_organization_prompt(note)

    assert "summary" in prompt
    assert "decisions" in prompt
    assert "todos" in prompt
    assert "risks" in prompt
    assert "next_actions" in prompt


def test_build_note_organization_prompt_requests_json_only() -> None:
    note = BusinessNoteInput(content="会議メモです。")

    prompt = build_note_organization_prompt(note)

    assert "JSON形式のみ" in prompt
