from abc import ABC, abstractmethod
import json


class Source(ABC):
    @abstractmethod
    def get_games():
        file = open("src/data.json")
        data = json.load(file)
        for game in data:
            print(game)

    @abstractmethod
    def add_games(game_name: str):
        file = open("src/data.json")
        data = json.load(file)
        data.update(game_name)
        print(f"{game_name} added into file")

    @abstractmethod
    def update_game(game_name: str, new_name: str):
        file = open("src/data.json")
        data = json.load(file)
        file[game_name] = new_name

        file.seek(0)
        json.dump(data, file)
        file.truncate()
