import discord
from typing import Union
from discord import User, Member
from pydantic import BaseModel

from typing import Dict
from pydantic import BaseModel


class PlayerDetails(BaseModel):
    exp: int
    level: int


class Players(BaseModel):
    players: Dict[int, PlayerDetails]


ranking = Players(players={398601935873114123: {"exp": 50, "level": 3}})


def add_xp(user: Union[User, Member]):
    print(type(user.id))
    if user.id in ranking.players:
        ranking.players[user.id].exp = ranking.players[user.id].exp + 50
        if ranking.players[user.id].exp == 100:
            ranking.players[user.id].exp = 0
            ranking.players[user.id].level = ranking.players[user.id].level + 1
    else:
        ranking.players.players[user.id] = PlayerDetails(exp=50, level=1)


def get_ranking_embeded(user: Union[User, Member]):
    print(ranking)
    print(user.id)
    print(type(user.id))

    if user.id in ranking.players:
        xp = ranking.players[user.id].exp
        print(True, xp)
    else:
        ranking.players[user.id] = PlayerDetails(exp=0, level=1)
        xp = 0
        print(False, xp)

    print(xp)

    boxes = int(xp / 100 * 10)
    embed = discord.Embed(title=f"{user}'s level stats", description="", color=0x397882)
    embed.add_field(name="XP", value=f"{xp}/100", inline=True)
    embed.add_field(name="Level", value=ranking.players[user.id].level, inline=True)
    embed.add_field(
        name="Progress Bar [lvl]",
        value=boxes * ":full_moon:" + (10 - boxes) * ":new_moon:",
        inline=False,
    )
    embed.set_thumbnail(url=user.display_avatar)
    return embed
