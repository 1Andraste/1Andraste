import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from config import settings
import asyncio
import requests
import random
from discord_webhook import DiscordWebhook
from bs4 import BeautifulSoup


client = discord.Client()
url = 'http://anekdotov.net/'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36 OPR/74.0.3911.218'
      }

def parser(num):
    response = requests.get(url)  
    html = response.content                             
    soup = BeautifulSoup(html, "lxml") 
    aneki = []   
    anek_list = soup.find_all('div', {'class':"anekdot"})
    for i in anek_list:
     aneki.append(i)
    anek = str(aneki[num]).replace('<div class="anekdot">', '').replace('</div>', '').replace('<br/>' , '')
    msg = anek

    return msg

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


num = 0
@client.event
async def on_message(message):
    if message.content.startswith('') and message.author.id != client.user.id and message.content.startswith('') != message.content.startswith('/'):
        channel = message.channel
        global n, number
    if message.content.startswith('/ane'):
        global num
        channel = message.channel
        await channel.send(parser(num))
        num += 1
        if num == 15:
            num = 0
    if message.content.startswith('/qwe'):              #svastika
        channel = message.channel 
        await channel.send(file=discord.File('1.png'))

client.run(settings['token'])

