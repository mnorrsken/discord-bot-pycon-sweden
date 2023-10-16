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
        release_year: Optional[int] = None,
        rating: Optional[int] = None,
        developer: Optional[str] = None,
    ):
        pass

    @abstractmethod
    def update_game(self, game_name: str, rating: int):
        pass


class JsonFileStrategy(SourceFileStrategy):
    def __init__(self, file):
        self.file = "data.json"

    def get_game(self, game_name: str):
        with open(self.file, "r") as file:
            data = json.load(file)

        for item in data:
            if item["game_name"] == game_name:
                return item
            return None

    def add_game(
        self,
        game_name: str,
        release_year: int | None = None,
        rating: int | None = None,
        developer: str | None = None,
    ):
        return super().add_game(game_name, release_year, rating, developer)

    def update_game(self, game_name: str, rating: int):
        return super().update_game(game_name, rating)


data_source = JsonFileStrategy("data.json")
print(data_source.get_game("FIFA"))
