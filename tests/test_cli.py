from app.cli import format_cli_output, format_list, format_organized_note, main
from app.models.note import BusinessNoteInput, OrganizedNote


def test_format_list_returns_bullet_list() -> None:
    result = format_list(["資料を確認する", "レビュー日程を調整する"])

    assert result == "- 資料を確認する\n- レビュー日程を調整する"


def test_format_list_returns_none_when_empty() -> None:
    result = format_list([])

    assert result == "- なし"


def test_format_organized_note_returns_cli_output() -> None:
    note = OrganizedNote(
        summary="会議メモの要約です。",
        decisions=["方針を決定する"],
        todos=["資料を確認する"],
        risks=["レビュー時間が不足する"],
        next_actions=["次回会議の日程を調整する"],
    )

    result = format_organized_note(note)

    assert "Summary:" in result
    assert "会議メモの要約です。" in result
    assert "Decisions:" in result
    assert "- 方針を決定する" in result
    assert "TODO:" in result
    assert "- 資料を確認する" in result
    assert "Risks:" in result
    assert "- レビュー時間が不足する" in result
    assert "Next Actions:" in result
    assert "- 次回会議の日程を調整する" in result


def test_main_outputs_organized_note(capsys) -> None:
    exit_code = main(["金曜日までに資料を確認する。"])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Input:" in captured.out
    assert "金曜日までに資料を確認する。" in captured.out
    assert "Summary:" in captured.out
    assert "入力された業務メモを整理した要約です。" in captured.out
    assert "TODO:" in captured.out


def test_format_cli_output_includes_input_note() -> None:
    input_note = BusinessNoteInput(content="金曜日までに資料を確認する。")
    organized_note = OrganizedNote(
        summary="会議メモの要約です。",
        decisions=["方針を決定する"],
        todos=["資料を確認する"],
        risks=["レビュー時間が不足する"],
        next_actions=["次回会議の日程を調整する"],
    )

    result = format_cli_output(input_note, organized_note)

    assert "Input:" in result
    assert "金曜日までに資料を確認する。" in result
    assert "Summary:" in result
    assert "会議メモの要約です。" in result
