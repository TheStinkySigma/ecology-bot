import discord
from discord.ext import commands
from K import *
import os
import random
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

advices = [
    "Посадить дерево.",
    "Построить скворечник, синичник.",
    "Повесить и своевременно наполнять кормушку, поилку для птиц.",
    "Ездить волонтером на проекты по спасению, восстановлению, учету животных."
]
photos = [
    "https://wallpaperaccess.com/full/2024849.jpg",
    "https://tse1.mm.bing.net/th?id=OIP.Y_PnCTMny6EFS6rncOrsawHaD_&pid=Api&P=0&h=180",
    "https://tse4.mm.bing.net/th?id=OIP.RpMpymO1vuhDhMeB06qXfgHaEK&pid=Api&P=0&h=180",
]
@bot.command()
async def advice(ctx):
    await ctx.send(random.choice(advices))
@bot.command()
async def photo(ctx):
    await ctx.send(random.choice(photos))
bot.run(key())
