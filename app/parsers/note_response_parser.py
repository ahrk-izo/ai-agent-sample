import json
from json import JSONDecodeError

from pydantic import ValidationError

from app.models.note import OrganizedNote


def parse_organized_note_response(response: str) -> OrganizedNote:
    """LLMレスポンスのJSON文字列を整理結果モデルに変換する."""
    try:
        data = json.loads(response)
    except JSONDecodeError as exc:
        raise ValueError("LLM response is not valid JSON.") from exc

    try:
        return OrganizedNote.model_validate(data)
    except ValidationError as exc:
        raise ValueError("LLM response does not match OrganizedNote schema.") from exc
