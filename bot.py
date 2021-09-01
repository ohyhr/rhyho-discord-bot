# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
#TOKEN = 'MjcyMDA1NjAwMzUzNzE0MTc2.WIIa9A.LBIQv3Ig8blKA5Clc99unSzIO3I'
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)