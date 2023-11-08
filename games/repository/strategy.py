from abc import ABC, abstractmethod

from games.schemas import Game


class SourceFileStrategy(ABC):
    @abstractmethod
    def get_games(self) -> list[Game]:
        pass

    @abstractmethod
    def get_game(self, name: str) -> Game:
        pass

    @abstractmethod
    def add_game(
        self,
        name: str,
        release_year: int | None = None,
        rating: int | None = None,
        developer: str | None = None,
    ) -> Game:
        pass

    @abstractmethod
    def update_game(
        self,
        name: str,
        new_game_name: str | None = None,
        new_rating: int | None = None,
    ) -> Game:
        pass

    @abstractmethod
    def delete_game(self, game_name: str) -> None:
        pass
