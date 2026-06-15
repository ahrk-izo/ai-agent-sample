from pydantic import BaseModel, Field


class BusinessNoteInput(BaseModel):
    content: str = Field(..., min_length=1)


class OrganizedNote(BaseModel):
    summary: str
    decisions: list[str]
    todos: list[str]
    risks: list[str]
    next_actions: list[str]
