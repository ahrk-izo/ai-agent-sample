from app.llm.base import LLMClient
from app.models.note import BusinessNoteInput, OrganizedNote


def build_prompt(note: BusinessNoteInput) -> str:
    """業務メモ整理用のプロンプトを生成する."""
    return f"""以下の業務メモを整理してください。

業務メモ:
{note.content}

出力項目:
- 要約
- 決定事項
- TODO
- リスク
- 次に確認すべきこと
"""


def organize_note(note: BusinessNoteInput, llm_client: LLMClient) -> OrganizedNote:
    """業務メモをLLMクライアント経由で整理する."""
    prompt = build_prompt(note)
    response = llm_client.generate(prompt)

    return OrganizedNote(
        summary=response,
        decisions=["現時点ではLLMレスポンスの構造化は未実装です。"],
        todos=["現時点ではLLMレスポンスの構造化は未実装です。"],
        risks=["現時点ではLLMレスポンスの構造化は未実装です。"],
        next_actions=["現時点ではLLMレスポンスの構造化は未実装です。"],
    )
