from abc import ABC, abstractmethod
from typing import Optional


class SourceFileStrategy(ABC):
    @abstractmethod
    def get_games(self):
        pass

    @abstractmethod
    def get_game(self, game_name: str):
        pass

    @abstractmethod
    def add_game(
        self,
        game_name: str,
        release_year: Optional[int] = None,
        rating: Optional[int] = None,
        developer: Optional[str] = None,
    ):
        pass

    @abstractmethod
    def update_game(
        self,
        game_name: str,
        new_game_name: Optional[str] = None,
        new_rating: Optional[int] = None,
    ):
        pass

    @abstractmethod
    def delete_game(self, game_name: str):
        pass
