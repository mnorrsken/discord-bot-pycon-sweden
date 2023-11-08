from abc import ABC, abstractmethod
from typing import List, Optional

from games.schemas import Game


class SourceFileStrategy(ABC):
    @abstractmethod
    def get_games(self) -> List[Game]:
        pass

    @abstractmethod
    def get_game(self, name: str) -> Game:
        pass

    @abstractmethod
    def add_game(
        self,
        name: str,
        release_year: Optional[int] = None,
        rating: Optional[int] = None,
        developer: Optional[str] = None,
    ) -> Game:
        pass

    @abstractmethod
    def update_game(
        self,
        name: str,
        new_game_name: Optional[str] = None,
        new_rating: Optional[int] = None,
    ) -> Game:
        pass

    @abstractmethod
    def delete_game(self, game_name: str) -> None:
        pass
