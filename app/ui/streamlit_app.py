import os
import streamlit as st
from pydantic import ValidationError

from app.models.note import OrganizedNote
from app.ui.streamlit_view_model import organize_note_text
from app.llm.factory import OPENAI_API_KEY_ENV, OPENAI_PROVIDER, MOCK_PROVIDER

DEFAULT_NOTE = "金曜日までに資料を確認する。レビュー時間が不足する可能性がある。"


def render_items(title: str, items: list[str]) -> None:  # pragma: no cover
    st.subheader(title)

    if not items:
        st.info("該当なし")
        return

    for item in items:
        st.markdown(f"- {item}")


def render_result(result: OrganizedNote) -> None:  # pragma: no cover
    st.divider()

    st.subheader("Summary")
    st.write(result.summary)

    render_items("Decisions", result.decisions)
    render_items("TODO", result.todos)
    render_items("Risks", result.risks)
    render_items("Next Actions", result.next_actions)


def main() -> None:  # pragma: no cover
    st.set_page_config(page_title="AI Agent Sample", page_icon="📝")

    st.title("AI Agent Sample")
    st.write("業務メモをAIで整理するサンプルUIです。")
    st.caption("現時点では外部LLM APIは呼び出さず、モックLLMクライアントを使用します。")

    provider = st.radio(
        "LLM Provider",
        options=[MOCK_PROVIDER, OPENAI_PROVIDER],
        horizontal=True,
        help="OpenAIを選択する場合は OPENAI_API_KEY が必要です。",
    )

    if provider == OPENAI_PROVIDER and not os.getenv(OPENAI_API_KEY_ENV):
        st.warning("OPENAI_API_KEY が未設定のため、MockLLMClientを使用します。")

    content = st.text_area(
        "業務メモ",
        value=DEFAULT_NOTE,
        height=180,
        placeholder="会議メモや作業メモを入力してください。",
    )

    if st.button("整理する"):
        if not content.strip():
            st.warning("業務メモを入力してください。")
            return

        try:
            result = organize_note_text(content, provider=provider)
        except ValidationError:
            st.error("入力内容を確認してください。")
            return
        except ValueError:
            st.error("LLMレスポンスの解析に失敗しました。")
            return

        render_result(result)


if __name__ == "__main__":
    main()
