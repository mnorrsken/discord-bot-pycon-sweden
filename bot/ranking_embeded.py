import discord

level_data = {398601935873114123: 30}


def add_xp(user):
    print(type(user.id))
    if user.id in level_data:
        level_data[user.id] = level_data[user.id] + 10
    else:
        level_data[user.id] = 10


def get_ranking_embeded(user):
    # level_data = {}
    # temp = sorted(level_data.items(), ke =lambda x: x[1])
    # for i in range(len(temp)):
    #     level_data[temp[i][0]] = temp[i][1]
    print(level_data)

    print(user.id)
    print(type(user.id))
    if user.id in level_data:
        xp = level_data[user.id]
        print(True, xp)
    else:
        xp = 0
        print(False, xp)
        level_data[user.id] = 0

    print(xp)
    # xp = 30
    # rank = list(leveldata).index(author.id)
    xp *= 5
    lvl = 0
    while True:
        if xp < ((50 * (lvl**2)) + (50 * lvl)):
            break
        lvl += 1
    xp -= (50 * ((lvl - 1) ** 2)) + (50 * (lvl - 1))
    boxes = int((xp / (200 * ((1 / 2) * (lvl))) * 20))
    embed = discord.Embed(title=f"{user.id}'s level stats", description="", color=0x397882)
    # embed = discord.Embed(title = "Kamil Kulig's level stats".format(.author.name), description="", color= 0x397882)
    # embed.add_field(name="Name", value=self.author.mention, inline=True)
    embed.add_field(name="XP", value=f"{xp}/{int(200 *(1/2) *lvl)}", inline=True)
    embed.add_field(name="Level", value=lvl, inline=True)
    # embed.add_field(name="Rank", value="1", inline=True)
    # embed.add_field(name="Rank", value=f"{rank+1}/{ctx.guild.member_count}", inline=True)
    embed.add_field(
        name="Progress Bar [lvl]",
        value=boxes * ":blue_square:" + (20 - boxes) * ":white_large_square:",
        inline=False,
    )
    return embed
    # embed.set_thumbnail(url=ctx.author.display_avatar)
