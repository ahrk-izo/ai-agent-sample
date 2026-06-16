import argparse

from app.llm.mock import MockLLMClient
from app.models.note import BusinessNoteInput, OrganizedNote
from app.services.note_organizer import organize_note


def format_cli_output(
    input_note: BusinessNoteInput, organized_note: OrganizedNote
) -> str:
    """入力メモと整理結果をCLI表示用の文字列に変換する."""
    return f"""Input:
{input_note.content}

{format_organized_note(organized_note)}"""


def format_organized_note(note: OrganizedNote) -> str:
    """整理結果をCLI表示用の文字列に変換する."""
    return f"""Summary:
{note.summary}

Decisions:
{format_list(note.decisions)}

TODO:
{format_list(note.todos)}

Risks:
{format_list(note.risks)}

Next Actions:
{format_list(note.next_actions)}
"""


def format_list(items: list[str]) -> str:
    """文字列のリストを箇条書き形式に変換する."""
    if not items:
        return "- なし"

    return "\n".join(f"- {item}" for item in items)


def create_parser() -> argparse.ArgumentParser:
    """CLI引数を解析するためのパーサーを作成する."""
    parser = argparse.ArgumentParser(
        description="業務メモを整理するCLI",
    )
    parser.add_argument(
        "content",
        help="整理したい業務メモ",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """CLIのエントリーポイント."""
    parser = create_parser()
    args = parser.parse_args(argv)

    note = BusinessNoteInput(content=args.content)
    llm_client = MockLLMClient(response="入力された業務メモを整理した要約です。")
    organized_note = organize_note(note, llm_client)

    print(format_cli_output(note, organized_note))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
