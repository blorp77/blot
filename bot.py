import os
import discord

from discord.ext import commands
from minesweeper import Minesweeper
from music_cog import music_cog

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    # bot.remove_command('help')
    await bot.add_cog(music_cog(bot))
    print(f'{bot.user} has connected to Discord!')



@bot.command()
async def minesweeper(ctx):
    mine = Minesweeper()
    mine.new_game(8, 8, 10)

    await ctx.send(mine.print_to_discord())

#start the bot with our token
# bot.run(os.getenv("TOKEN"))
bot.run("MTA1NzM0NDIyNDI3OTkyODkyMw.GJsfzw.SvPX-tBAlCoifsJJ7YLLL9kuhdxQnsRtaqDzb0")