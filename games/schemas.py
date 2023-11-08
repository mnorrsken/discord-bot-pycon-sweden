from pydantic import BaseModel


class Game(BaseModel):
    name: str
    release_year: int | None = None
    rating: int | None = None
    developer: str | None = None
