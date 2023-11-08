import json

from source.ranking.schemas import PlayerDetails, Ranking

file_path_ranking = 'source/ranking/repository/players.json'


def open_players_file() -> Ranking:
    try:
        with open('source/ranking/repository/players.json') as file:
            data = json.load(file)
            converted_data = {'players': {str(key): PlayerDetails(**value) for key, value in data['players'].items()}}
            return Ranking(**converted_data)
    except FileNotFoundError:
        return Ranking(players={})


def save_players_file(data: Ranking) -> None:
    converted_data = {'players': {int(key): value.dict() for key, value in data.players.items()}}
    with open('source/ranking/repository/players.json', 'w') as file:
        json.dump(converted_data, file, indent=4)
