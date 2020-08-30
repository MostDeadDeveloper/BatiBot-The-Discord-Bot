# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # print('Available Channels: {}'.format(client.guilds[0].channels[-1]))
    await client.guilds[0].channels[-1].send("Discord Bot Online.")

@client.event
async def on_message(message):
    print("Content of Message Is: {}".format(message.content))
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
client.run(TOKEN)

