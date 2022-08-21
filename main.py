import json
import os

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

@client.command()
async def bless(ctx):
    url = rapid_api_url

    headers = {
	"X-RapidAPI-Key": rapid_api_key,
	"X-RapidAPI-Host": rapid_api_host
    }

    response = requests.request("GET", url, headers=headers)

    await ctx.send(json.loads(response.text)[0]["verses"][0]["kjv"] + " *( ͡° ͜ʖ ͡°)*")
# endregion

client.run(bot_api_key)