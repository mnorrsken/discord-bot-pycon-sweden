import json
from source.source import SourceFileStrategy


class JsonFileStrategy(SourceFileStrategy):
    def __init__(self):
        self.file = "source/data.json"

    def get_games(self):
        with open(self.file, "r") as file:
            data = json.load(file)
        return [game["game_name"] for game in data]

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
