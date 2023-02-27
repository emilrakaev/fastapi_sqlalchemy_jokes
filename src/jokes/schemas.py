from pydantic import BaseModel


class JokeIn(BaseModel):
    type: str | None = None
    setup: str | None = None
    punchline: str | None = None


class Joke(BaseModel):
    id: int
    type: str | None = None
    setup: str | None = None
    punchline: str | None = None
