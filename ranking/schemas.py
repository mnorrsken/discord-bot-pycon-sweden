from pydantic import BaseModel


class PlayerDetails(BaseModel):
    exp: int
    level: int


class Ranking(BaseModel):
    players: dict[str, PlayerDetails]
