import json
from typing import Dict, List

from ranking.schemas import PlayerDetails, Ranking

file_path_ranking = 'ranking/repository/players.json'


def open_players_file() -> List[PlayerDetails]:
    try:
        with open(file_path_ranking) as file:
            data = json.load(file)
            ranking = Ranking(**data)
            return ranking.players
    except FileNotFoundError:
        ranking = Ranking(players={})
        return ranking.players


def save_players_file(players: Dict[str, PlayerDetails]) -> None:
    ranking = Ranking(players=players)
    with open(file_path_ranking, 'w') as file:
        json.dump(ranking.model_dump(), file, indent=4)
