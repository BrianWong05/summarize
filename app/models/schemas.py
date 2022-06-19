from pydantic import BaseModel


class summarize_text(BaseModel):
    text: str
    precent: int
