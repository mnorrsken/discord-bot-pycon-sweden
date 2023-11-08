import json

from ranking.schemas import PlayerDetails, Ranking

file_path_ranking = 'ranking/repository/players.json'


def open_players_file() -> list[PlayerDetails]:
    try:
        with open(file_path_ranking) as file:
            ranking = Ranking(**json.load(file))
            return ranking.players
    except FileNotFoundError:
        ranking = Ranking(players={})
        return ranking.players


def save_players_file(players: dict[str, PlayerDetails]) -> None:
    with open(file_path_ranking, 'w') as file:
        json.dump(Ranking(players=players).model_dump(), file, indent=4)
