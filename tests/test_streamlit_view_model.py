from app.llm.mock import MockLLMClient
from app.models.note import OrganizedNote
from app.ui.streamlit_view_model import organize_note_text


def test_organize_note_text_returns_organized_note() -> None:
    result = organize_note_text("金曜日までに資料を確認する。")

    assert isinstance(result, OrganizedNote)
    assert result.summary == "入力された業務メモを整理した要約です。"
    assert result.todos == ["資料を確認する"]


def test_organize_note_text_accepts_custom_llm_client() -> None:
    llm_client = MockLLMClient(
        response="""{
  "summary": "カスタム要約です。",
  "decisions": ["方針を決定する"],
  "todos": ["資料を確認する"],
  "risks": ["レビュー時間が不足する"],
  "next_actions": ["日程を確認する"]
}"""
    )

    result = organize_note_text("会議メモです。", llm_client=llm_client)

    assert result.summary == "カスタム要約です。"
    assert result.decisions == ["方針を決定する"]
    assert result.next_actions == ["日程を確認する"]
