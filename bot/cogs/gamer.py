import random

import discord
from discord.ext import commands
from source.main import games_source
from config import CHANNEL_ID
from bot.ranking_embeded import get_ranking_embeded, add_xp

# https://replit.com/@maxc0dez/levelling-system#levelsys.py


async def refresh_channel_games(bot):

    # Getting the channel
    channel = bot.get_channel(CHANNEL_ID)
    # channel.purge
    # channel.get
    # channel.delete_messages()
    # Getting the role
    # role = discord.utils.get(channel.guild.roles, name='Orange')
    # Sending the message
    await channel.purge(limit=5)

    # embed
    # nameslist = '\n'.join(nameslist) # Joining the list with newline as the delimiter
    # for game in games_source.get_games():
    games = games_source.get_games()
    print(games)
    # nameslist = "\n".join(games)
    # print(nameslist)
    embeds = []
    for game in games:
        em = discord.Embed(
            title=game,
            # url="https://realdrewdata.medium.com/",
            description="This is an embed that will show how to build an embed and the different components",
            color=0x109319,
        )
        embeds.append(em)
        # embeds.add_field(name="GAMES", value=nameslist)
    print(embeds)
    message = await channel.send(embeds=embeds)
    await channel.send(view=VoteView())


class NewGame(discord.ui.Modal, title="New Game"):
    name = discord.ui.TextInput(label="Name", placeholder="Type name here...", min_length=3, max_length=50)

    async def on_submit(self, interaction: discord.Interaction):
        games_source.add_game(self.name.value)
        embed = GameEmbeded(title=self.name.value)
        await interaction.response.send_message(
            f"Thanks for your for adding new game, {self.name.value}!", ephemeral=True, embed=embed
        )


class GameEmbeded(discord.Embed):
    def __init__(self, title):
        super().__init__(
            title=title,
            url="https://store.steampowered.com/app/1811260/EA_SPORTS_FIFA_23/",
            # https://store.steampowered.com/search/?term=Fifa+23
            description="This is an embed that will show how to build an embed and the different components",
            color=0x109319,
        )


class Vue(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="hello-button-2", custom_id="hello-button-2", style=discord.ButtonStyle.red)
    async def hello_button_2(self, interaction, button: discord.Button):
        await interaction.response.send_message("HOLA")


class CounterView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="0", custom_id="counter", style=discord.ButtonStyle.green)
    async def counter_button(self, interaction, button: discord.Button):
        button.label = str(int(button.label) + 1)
        await interaction.response.edit_message(view=self)


class VoteButton(discord.ui.Button):
    def __init__(self, label: str):
        super().__init__(label=label)

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.name in self.view.users:
            await interaction.response.send_message(f"Don't cheat. {interaction.user}")
        else:
            await interaction.response.send_message(f"User {interaction.user}. Choose: {self.label}")
            self.view.results[self.label] = self.view.results[self.label] + 1
            self.view.users.append(interaction.user.name)
        return await super().callback(interaction)


class VoteView(discord.ui.View):
    users = []
    results = {}

    def __init__(self):
        super().__init__()
        for game in games_source.get_games():
            self.results[game] = 0
            self.add_item(VoteButton(label=game))


class GammerCogs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name="hello", description="Bot says hello to you")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello {interaction.user.name}!")

    @discord.app_commands.command(name="hello-button", description="Bot says hello to you")
    async def hello_button(self, interaction: discord.Interaction):
        view = discord.ui.View()
        button = discord.ui.Button(label="hello", custom_id="hello", style=discord.ButtonStyle.red)

        async def button_callback(interaction: discord.Interaction):
            await interaction.response.send_message("hi")

        button.callback = button_callback
        view.add_item(button)
        await interaction.response.send_message(view=view)

    @discord.app_commands.command(name="hello-button-2", description="Bot says hello to you")
    async def hello_button_2(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=Vue())

    @discord.app_commands.command(name="counter")
    async def counter(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=CounterView())

    @discord.app_commands.command(name="animals", description="Get your favorite animal")
    async def animals(self, interaction: discord.Interaction):
        view = discord.ui.View()
        select = discord.ui.Select(
            options=[
                discord.SelectOption(label="monkey", description="if you like monkey click me", emoji="🐵"),
                discord.SelectOption(label="panda", description="if you like panda click me", emoji="🐼"),
                discord.SelectOption(label="dog", description="if you like monkey click me", emoji="🐶"),
            ]
        )

        async def select_callback(interaction: discord.Interaction):
            await interaction.response.send_message(select.values[0])

        select.callback = select_callback
        view.add_item(select)
        await interaction.response.send_message(f"Select your animals", view=view)

    @discord.app_commands.command(
        name="random-choose-the-game", description="Help you to choose which game you want to play"
    )
    async def games(self, interaction: discord.Interaction):
        view = discord.ui.View()
        options = [
            discord.SelectOption(label=game, description=f"Pick this if like {game}!")
            for game in games_source.get_games()
        ]
        select = discord.ui.Select(
            placeholder="Choose your game!", min_values=2, max_values=len(options), options=options
        )

        async def select_callback(interaction: discord.Interaction):
            chosen_game = random.choice(select.values)
            await interaction.response.send_message(chosen_game)

        select.callback = select_callback
        view.add_item(select)
        await interaction.response.send_message(f"Select your games", view=view)

    @discord.app_commands.command(name="vote-for-game", description="Select game")
    async def vote(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Select to want play", view=VoteView())

    @discord.app_commands.command(name="ranking", description="get ranking")
    async def ranking(self, interaction: discord.Interaction):
        print(interaction.user)
        print(interaction.user.id)
        await interaction.response.send_message(embed=get_ranking_embeded(interaction.user))

    @discord.app_commands.command(name="add-new-game", description="Select game")
    async def new_game(self, interaction: discord.Interaction):
        await interaction.response.send_modal(NewGame())
        # await add
        add_xp(interaction.user)
        await refresh_channel_games(self.bot)

    @discord.app_commands.command(name="game-details", description="Select game")
    async def game_details(self, interaction: discord.Interaction):
        # view =
        # self.
        view = discord.ui.View()
        embed = discord.Embed(
            title="Sample Embed",
            url="https://realdrewdata.medium.com/",
            description="This is an embed that will show how to build an embed and the different components",
            color=0x109319,
        )

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(
            name="RealDrewData",
            url="https://twitter.com/RealDrewData",
            icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg",
        )

        embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")

        embed.add_field(
            name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=False
        )
        embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
        embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)

        embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")
        # view.add_item(embed)
        embed = GameEmbeded()
        await interaction.response.send_message(embed=embed)
        await refresh_channel_games(self.bot)

        # return self.
        # await interaction.response.send_modal(NewGame())
