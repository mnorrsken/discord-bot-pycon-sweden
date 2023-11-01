import json
from source.ranking.schemas import PlayerDetails, Players


def open_players_file() -> Players:
    try:
        with open("source/ranking/repository/players.json", "r") as file:
            data = json.load(file)
            converted_data = {
                "players": {
                    str(key): PlayerDetails(**value)
                    for key, value in data["players"].items()
                }
            }
            return Players(**converted_data)
    except FileNotFoundError:
        return Players(players={})


def save_players_file(data: Players) -> None:
    converted_data = {
        "players": {int(key): value.dict() for key, value in data.players.items()}
    }
    with open("source/ranking/repository/players.json", "w") as file:
        json.dump(converted_data, file, indent=4)
