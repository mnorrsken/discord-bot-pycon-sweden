import discord
import discord.ui
from discord.ext import commands

from bot.cogs.gamer import GammerCogs

from config import GUILD_ID


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="/", intents=intents)

    async def setup_hook(self) -> None:
        await self.add_cog(GammerCogs(self), guild=discord.Object(id=GUILD_ID))
        await self.tree.sync(guild=discord.Object(id=GUILD_ID))

    async def on_ready(self) -> None:
        await self.change_presence(
            activity=discord.Game(name="⚽️ FIFA"),
            status=discord.Status.do_not_disturb,
        )
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")
