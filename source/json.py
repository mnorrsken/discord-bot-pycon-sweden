import json
from source.source import SourceFileStrategy


# TODO: refactor, create class for load and save json file
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
        with open(self.file_path, "r") as file:
            data = json.load(file)

        new_game = {
            "game_name": game_name,
            "release_year": release_year,
            "rating": rating,
            "developer": developer,
        }
        data.append(new_game)

        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def update_game(
        self,
        game_name: str,
        new_game_name: str | None = None,
        new_rating: int | None = None,
    ):
        with open(self.file_path, "r") as file:
            data = json.load(file)

        for item in data:
            if item["game_name"] == game_name:
                if new_game_name is not None:
                    item["game_name"] = new_game_name
                if new_rating is not None:
                    item["rating"] = new_rating
                break

        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def delete_game(self, game_name: str):
        with open(self.file_path, "r") as file:
            data = json.load(file)

        data = [item for item in data if item["game_name"] != game_name]

        with open(self.file_path, "w") as file:
            json.dump(data, file)
