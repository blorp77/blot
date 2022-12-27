import os
import discord

from dotenv import load_dotenv
from discord.ext import commands
from minesweeper import Minesweeper
from music_cog import music_cog


load_dotenv()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.add_cog(music_cog(bot))
    print(f'{bot.user} has connected to Discord!')

@commands.command(name = "minesweeper", aliases=["ms"], help="Generates an 8 by 8 Minesweeper board with 10 mines.")
async def minesweeper(ctx):
    mine = Minesweeper()
    mine.new_game(8, 8, 10)

    await ctx.send(mine.print_to_discord())

#start the bot with our token
bot.run(os.getenv("DISCORD_TOKEN"))