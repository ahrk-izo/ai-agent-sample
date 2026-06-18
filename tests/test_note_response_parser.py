import pytest

from app.models.note import OrganizedNote
from app.parsers.note_response_parser import parse_organized_note_response


def test_parse_organized_note_response_returns_organized_note() -> None:
    response = """{
  "summary": "会議メモの要約です。",
  "decisions": ["方針を決定する"],
  "todos": ["資料を確認する"],
  "risks": ["レビュー時間が不足する"],
  "next_actions": ["次回会議の日程を調整する"]
}"""

    result = parse_organized_note_response(response)

    assert isinstance(result, OrganizedNote)
    assert result.summary == "会議メモの要約です。"
    assert result.decisions == ["方針を決定する"]
    assert result.todos == ["資料を確認する"]
    assert result.risks == ["レビュー時間が不足する"]
    assert result.next_actions == ["次回会議の日程を調整する"]


def test_parse_organized_note_response_raises_error_when_json_is_invalid() -> None:
    response = "これはJSONではありません。"

    with pytest.raises(ValueError, match="LLM response is not valid JSON."):
        parse_organized_note_response(response)


def test_parse_organized_note_response_raises_error_when_required_field_is_missing() -> (
    None
):
    response = """{
  "summary": "会議メモの要約です。",
  "decisions": [],
  "todos": [],
  "risks": []
}"""

    with pytest.raises(
        ValueError, match="LLM response does not match OrganizedNote schema."
    ):
        parse_organized_note_response(response)
