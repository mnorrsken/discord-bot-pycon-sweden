from ranking.repository.repository import open_players_file, save_players_file
from ranking.schemas import PlayerDetails


def add_xp(user_id: int) -> None:
    user_id: str = str(user_id)
    players: dict[str, PlayerDetails] = open_players_file()
    if user_id in players:
        players[user_id].exp = players[user_id].exp + 50
        if players[user_id].exp == 100:
            players[user_id].exp = 0
            players[user_id].level = players[user_id].level + 1
    else:
        players[user_id] = PlayerDetails(exp=50, level=1)
    save_players_file(players)


def get_ranking(user_id) -> tuple[int, int, int]:
    players: list[PlayerDetails] = open_players_file()
    user_id = str(user_id)
    if user_id in players:
        return players[user_id].exp, 100, players[user_id].level
    else:
        return 50, 100, 1
