from typing import Dict, List

from ranking.repository.repository import open_players_file, save_players_file
from ranking.schemas import PlayerDetails


def add_xp(user_id: int) -> None:
    user_id: str = str(user_id)
    players: Dict[str, PlayerDetails] = open_players_file()
    if user_id in players:
        players[user_id].exp = players[user_id].exp + 50
        if players[user_id].exp == 100:
            players[user_id].exp = 0
            players[user_id].level = players[user_id].level + 1
    else:
        players[user_id] = PlayerDetails(exp=50, level=1)

    save_players_file(players)


def get_ranking(user_id) -> [str, int]:
    players: List[PlayerDetails] = open_players_file()
    user_id = str(user_id)
    if user_id in players:
        xp: int = players[user_id].exp
    else:
        players[user_id] = PlayerDetails(exp=0, level=1)
        xp = 0
    return xp, players[user_id].level
