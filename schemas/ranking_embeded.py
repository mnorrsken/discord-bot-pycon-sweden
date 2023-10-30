from pydantic import BaseModel
from typing import Dict


class PlayerDetails(BaseModel):
    exp: int
    level: int


class Players(BaseModel):
    players: Dict[str, PlayerDetails]
