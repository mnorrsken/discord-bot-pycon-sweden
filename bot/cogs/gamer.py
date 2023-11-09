import discord
from discord.ext import commands
from ranking.engine import get_ranking

class GammerCogs(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(name='hello', description='Bot says hello to you')
    async def hello(self, interaction: discord.Interaction) -> None:
        # send a two line message with a banana emoji
        await interaction.response.send_message(f'Hello {interaction.user.name} :banana:!')
        
    @discord.app_commands.command(name='rank', description='Bot gets ranking')
    async def rank(self, interaction: discord.Interaction) -> None:
        # send a two line message with a banana emoji
        xp, max_xp, level = get_ranking(interaction.user.id)
        embed = discord.Embed(title=f'Ranking for {interaction.user.name}', description=f'Level: {level}\nXP: {xp}/{max_xp}', color=discord.Color.blue())
        embed.add_field(name='XP', value=f'{xp}/{max_xp}')
        embed.add_field(name='Level', value=level)
        embed.set_thumbnail(url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=embed)


