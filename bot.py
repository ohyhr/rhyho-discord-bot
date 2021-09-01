# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event #confirms the bot has connected to discord
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the server, please read the rules and react to select your role.'
    )

@client.event #event for messages and commands
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!about'):
        await message.channel.send('Hi, I am the rhyho bot, I can do a variety of things, use "!help" to see all my commands')

    if message.content.startswith('!help'): #Provides all commands
        await message.channel.send('temp placeholder') #feedsback list of commands


client.run(TOKEN)