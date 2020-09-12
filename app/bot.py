from dotenv import load_dotenv
import os
import random

import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USERID = os.getenv('DISCORD_USER')

client = discord.Client()
BOT_MODE = True
SELECTED_CHANNEL_INDEX = 0
SELECTED_CHANNEL = None

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # print('Available Channels: {}'.format(client.guilds[0].channels[-1]))
    
    print("Available Guilds: ")
    for index, guild in enumerate(client.guilds):
        print("[{}] - {}".format(index , guild))

    selected_index = int(input("Input Your Selected Guild To Implant Bot."))

    print("Available Channels")
    for index, channel in enumerate(client.guilds[selected_index].channels):
        print("[{}] - {}".format(index , channel))

    selected_channel_index = int(input("Input Your Selected Channel To Implant Bot."))

    SELECTED_CHANNEL = client.guilds[selected_index].channels[selected_channel_index]
    await client.guilds[0].channels[-2].send("Discord Bot Online.")

    print(SELECTED_CHANNEL)


@client.event
async def on_message(message):
    print(
        "{}'s Message: {} Channel: {} ".format(
            message.author,
            message.content,
            message.channel
        )
    )

    if message.author == client.user:
        return

    if message.content.startswith('$replace'):
        await message.channel.send('Conducting an act of Replacement.')

    #await client.guilds[selected_index].channels[selected_channel_index].send("Discord Bot Online.")
    print(SELECTED_CHANNEL)


    # messages are for test purpose only. insert a more 'formal' message for actual use.
    randomMessage = [
        'User is unavailable at the moment. I will contact the user regarding your inquiry.',

        'The User is Quite Busy at The Moment, Don\'t Worry, I will contact them for you! Thank you.',
    ]

    randomGreeting = [
        'Greetings!',
        'Hi!',
    ]
    userid = int(USERID)
    mentionid = f'@!{userid}'
# `@!` is needed to be added to the user ID to check for mentions.
    if mentionid in message.content:
        # option for send in a custom message
    #   if BOT_MODE == False: 
    #       response = input('Type in your reply: ')
    #       await message.channel.send(f"{message.author.mention}, {response}") 
    #   else:

        guild = message.author.guild
        member = discord.Guild.get_member(
            self=guild,
            user_id=userid
        )

        # checks if the user's status is online. 
        if member.status is not discord.Status.online:
            response = random.choice(randomMessage)
            greet = random.choice(randomGreeting)

            msgStr = (f'{greet} {message.author.mention}!, {response}')
            fromDescription = (f'A reply to {member.nick}\'s message!')

            embed = discord.Embed(
                title=None,
                description=None,
                colour = discord.Color.blue()
            )
            embed.add_field(
                name=fromDescription,
                value=message.content,
                inline=False
            )
            await message.channel.send(
                embed=embed,
                content=msgStr
            )

    #responds to mentions - from BoredPaper's PR
    # for x in message.mentions:
        # if (x == client.user):
            # await message.channel.send(f"{greet}, {message.author.mention}")

# @client.event
# async def on_member_join(member):
    # await member.create_dm()
    # await member.dm_channel.send(
        # 'Hi {member.name}, welcome to my Discord server!'
    # )
client.run(TOKEN)

