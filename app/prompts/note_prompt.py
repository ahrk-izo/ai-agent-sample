from app.models.note import BusinessNoteInput


def build_note_organization_prompt(note: BusinessNoteInput) -> str:
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
