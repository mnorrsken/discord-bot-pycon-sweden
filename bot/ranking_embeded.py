import discord
from typing import Union
from discord import User, Member

from schemas.ranking_embeded import Players, PlayerDetails
from utils.util_ranking_embeded import open_players_file, save_players_file


def add_xp(user: Union[User, Member]):
    ranking = open_players_file()
    user_id = str(user.id)

    if user_id in ranking.players:
        ranking.players[user_id].exp = ranking.players[user_id].exp + 50
        if ranking.players[user_id].exp == 100:
            ranking.players[user_id].exp = 0
            ranking.players[user_id].level = ranking.players[user_id].level + 1
    else:
        ranking.players[user_id] = PlayerDetails(exp=50, level=1)

    save_players_file(ranking)


def get_ranking_embeded(user: Union[User, Member]):
    ranking = open_players_file()
    user_id = str(user.id)

    if user_id in ranking.players:
        xp = ranking.players[user_id].exp
        print(True, xp)
    else:
        ranking.players[user_id] = PlayerDetails(exp=0, level=1)
        xp = 0
        print(False, xp)

    print(xp)

    boxes = int(xp / 100 * 10)
    embed = discord.Embed(title=f"{user}'s level stats", description="", color=0x397882)
    embed.add_field(name="XP", value=f"{xp}/100", inline=True)
    embed.add_field(name="Level", value=ranking.players[user_id].level, inline=True)
    embed.add_field(
        name="Progress Bar [lvl]",
        value=boxes * ":full_moon:" + (10 - boxes) * ":new_moon:",
        inline=False,
    )
    embed.set_thumbnail(url=user.display_avatar)
    return embed
