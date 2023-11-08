import json

from games.repository.strategy import SourceFileStrategy
from games.schemas import Game


class JsonFileStrategy(SourceFileStrategy):
    def __init__(self) -> None:
        self.file = 'games/repository/data.json'

    def get_games(self) -> list[Game]:
        with open(self.file) as file:
            data = json.load(file)
        return [game['name'] for game in data]

    def get_game(self, name: str) -> Game:
        with open(self.file) as file:
            data = json.load(file)

        for item in data:
            if item['name'] == name:
                return item
            return None

    def add_game(
        self,
        name: str,
        release_year: int | None = None,
        rating: int | None = None,
        developer: str | None = None,
    ):
        with open(self.file) as file:
            data = json.load(file)

        new_game = {
            'name': name,
            'release_year': release_year,
            'rating': rating,
            'developer': developer,
        }
        data.append(new_game)

        with open(self.file, 'w') as file:
            json.dump(data, file)

    def update_game(
        self,
        name: str,
        new_game_name: str | None = None,
        new_rating: int | None = None,
    ):
        with open(self.file) as file:
            data = json.load(file)

        for item in data:
            if item['name'] == name:
                if new_game_name is not None:
                    item['name'] = new_game_name
                if new_rating is not None:
                    item['rating'] = new_rating
                break

        with open(self.file, 'w') as file:
            json.dump(data, file)

    def delete_game(self, name: str):
        with open(self.file) as file:
            data = json.load(file)

        data = [item for item in data if item['name'] != name]

        with open(self.file, 'w') as file:
            json.dump(data, file)
