from pydantic import BaseModel


class JokeIn(BaseModel):
    type: str | None = None
    setup: str | None = None
    punchline: str | None = None


class JokeId(BaseModel):
    joke_id: int


class Joke(BaseModel):
    id: int
    type: str | None = None
    setup: str | None = None
    punchline: str | None = None
