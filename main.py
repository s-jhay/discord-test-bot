import json
import os
from queue import Empty

from dotenv import load_dotenv
import discord
from discord.ext import commands
import requests

# region environment loading
load_dotenv('.env')
bot_api_key = os.getenv('DISCORD_BOT_API_KEY')
channel_id_01 = int(os.getenv('DISCORD_BOT_CHANNEL_ID_01'))
rapid_api_url = os.getenv('DISCORD_BOT_RAPID_API_URL')
rapid_api_key = os.getenv('DISCORD_BOT_RAPID_API_KEY')
rapid_api_host = os.getenv('DISCORD_BOT_RAPID_API_HOST')
# endregion

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("Bot is now ready for use.")
    print("-------------------------")

# region events
@client.event
async def on_member_join(member):
    channel = client.get_channel(channel_id_01)
    await channel.send(f"Hello, {member}.")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(channel_id_01)
    await channel.send(f"Goodbye, {member}.")
# endregion

# region commands
@client.command()
async def test(ctx):
    await ctx.send("Pong.")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am a bot.")

@client.command()
async def goodbye(ctx):
    await ctx.send("Goodbye.")

# region bless
# commented out to avoid API overage fees for now
# @client.command()
# async def bless(ctx, *args):
#     url = rapid_api_url
#     headers = {
#     "X-RapidAPI-Key": rapid_api_key,
#     "X-RapidAPI-Host": rapid_api_host
#     }
#     return_string = ""

#     # endpoint scheme is as follows:
#     # /<book>/<chapter>/<verse-start>/<verse-end>/<translation>/
#     if len(args) != 2:
#         book = "Eze"
#         chapter = "23"
#         verse = "20"
#         return_string = "Usage: !bless <book> <verse>\nFor example:\n"

#     else:
#         book = args[0]
#         cherse = args[1].split(":")
#         chapter = cherse[0]
#         verse = cherse[1]

#     url = url + f"{book}/{chapter}/{verse}/{verse}/KJV/"
    
#     response = requests.request("GET", url, headers=headers)
#     print(response.text)
#     passage = json.loads(response.text)[0]["kjv"] + "\n*( ͡° ͜ʖ ͡°)*"
#     return_string = return_string + f"Book: {book}\nChapter: {chapter}\nVerse: {verse}\n Passage: {passage}\n"
# endregion
# endregion

client.run(bot_api_key)