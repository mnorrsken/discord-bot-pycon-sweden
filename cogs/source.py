from abc import ABC, abstractmethod
import json
from typing import Optional


class SourceFileStrategy(ABC):
    @abstractmethod
    def get_game(self, game_name: str):
        pass

    @abstractmethod
    def add_game(
        self,
        game_name: str,
        release_year: int,
        rating: Optional[int] = None,
        developer: Optional[str] = None,
    ):
        pass

    @abstractmethod
    def update_game(self, game_name: str, rating: int):
        pass
