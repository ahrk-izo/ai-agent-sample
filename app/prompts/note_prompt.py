from app.models.note import BusinessNoteInput


def build_note_organization_prompt(note: BusinessNoteInput) -> str:
    """業務メモ整理用のプロンプトを生成する."""
    return f"""以下の業務メモを整理してください。

業務メモ:
{note.content}

出力は以下のJSON形式のみで返してください。

{{
  "summary": "要約",
  "decisions": ["決定事項"],
  "todos": ["TODO"],
  "risks": ["リスク"],
  "next_actions": ["次に確認すべきこと"]
}}
"""
