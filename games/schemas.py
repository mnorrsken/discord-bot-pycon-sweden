from typing import Optional

from pydantic import BaseModel


class Game(BaseModel):
    name: str
    release_year: Optional[int] = None
    rating: Optional[int] = None
    developer: Optional[str] = None
