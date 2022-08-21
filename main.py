import os

from dotenv import load_dotenv
import discord
from discord.ext import commands


# region environment loading
load_dotenv('.env')
bot_api_key = os.getenv('BOT_API_KEY')
# endregion

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("Bot is now ready for use.")
    print("-------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am a bot.")

@client.command()
async def goodbye(ctx):
    await ctx.send("Goodbye.")

@client.command()
async def test(ctx):
    await ctx.send("Pong.")

client.run(bot_api_key)
