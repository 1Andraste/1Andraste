import random
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import random

config = {
    'token': 'YOUR TOKEN',
    "guild": "768849576811036743",
    'bot': 'neuropostironyBoty',
    'id': 777649034424746014,
    'prefix': '/'
}

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36 OPR/74.0.3911.218'
      }

bot = commands.Bot(command_prefix=config['prefix'])


@bot.command()
@commands.has_role("ЦАРЬ И БОГ")
async def anek(ctx, *arg):
    if not arg:
        text = parser(random.randint(1, 1139))
    else:
        if int(arg[0]) < 1 or int(arg[0]) > 1139:
            await ctx.send("Столько нету")
            return
        else:
            text = parser(arg[0])
    await ctx.send("внимание анек")
    await ctx.send(text)


def parser(number):
    response = requests.get(url=f'https://baneks.ru/{number}')
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.find("meta", {"name": "description"})['content']
    return text


@bot.command()
@commands.has_role("ЦАРЬ И БОГ")
async def chill(ctx, *arg):
    await ctx.send(file=discord.File('chill.gif'))


@bot.command()
@commands.has_role("ЦАРЬ И БОГ")
async def gensh(ctx, *arg):
    await ctx.send(file=discord.File('genshin.gif'))


@bot.command()
@commands.has_role("ЦАРЬ И БОГ")
@commands.has_role("качок")
async def ger(ctx, *arg):
    await ctx.send(file=discord.File('ger.gif'))


@bot.command()
@commands.has_role("ЦАРЬ И БОГ")
async def renochka(ctx, *arg):
    await ctx.send(file=discord.File('video(1).gif'))


@bot.command()
@commands.has_role("ЦАРЬ И БОГ")
async def nikita_nedovolen(ctx, *arg):
    await ctx.send(file=discord.File('1.png'))


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


bot.run(config['token'])

