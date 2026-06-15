from app.models.note import BusinessNoteInput, OrganizedNote


def organize_note(note: BusinessNoteInput) -> OrganizedNote:
    _ = note.content

    return OrganizedNote(
        summary="入力された業務メモを整理した要約です。",
        decisions=["現時点ではダミーの決定事項です。"],
        todos=["現時点ではダミーのTODOです。"],
        risks=["現時点ではダミーのリスクです。"],
        next_actions=["現時点ではダミーの次アクションです。"],
    )
