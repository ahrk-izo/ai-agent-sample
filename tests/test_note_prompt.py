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

    assert "要約" in prompt
    assert "決定事項" in prompt
    assert "TODO" in prompt
    assert "リスク" in prompt
    assert "次に確認すべきこと" in prompt
