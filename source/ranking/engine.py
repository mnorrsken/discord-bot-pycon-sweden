from typing import Union

from discord import Member, User

from source.ranking.repository.repository import open_players_file, save_players_file
from source.ranking.schemas import PlayerDetails, Ranking


def add_xp(user: Union[User, Member]) -> None:
    ranking: Ranking = open_players_file()
    user_id = str(user.id)

    if user_id in ranking.players:
        ranking.players[user_id].exp = ranking.players[user_id].exp + 50
        if ranking.players[user_id].exp == 100:
            ranking.players[user_id].exp = 0
            ranking.players[user_id].level = ranking.players[user_id].level + 1
    else:
        ranking.players[user_id] = PlayerDetails(exp=50, level=1)

    save_players_file(ranking)


def get_ranking(user: Union[User, Member]) -> [str, int]:
    ranking: Ranking = open_players_file()
    user_id = str(user.id)
    if user_id in ranking.players:
        xp: int = ranking.players[user_id].exp
    else:
        ranking.players[user_id] = PlayerDetails(exp=0, level=1)
        xp = 0
    return xp, ranking.players[user_id].level
