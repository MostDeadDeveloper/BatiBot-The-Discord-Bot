# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USERID = os.getenv('DISCORD_USER')

client = discord.Client()
BOT_MODE = True
SELECTED_CHANNEL_INDEX = 0
SELECTED_CHANNEL = ""

 # Develop a condition to reply to specific messages made that pertain to you. 
 # Develop a bot mode and user mode shift. So I can shift from a bot talking to me being the  person talking
 #  - this needs asynchronous input and output. Continously ask for input when not in idle and can speak instead of the bot. 
    # - when in idle, the bot will talk
    # - configure in the future, to make the bot to react to certain conditions a bit better, the current proposed solution
        # / is just reacting to certain keywords
    # - 
 # 
# Current Desired Features:
        # - Perform some form of switcheroo with user and bot interchangeably
        # - greet the new members joining when in Bot Mode
        # - perform a interchangeable chat interaction between the new joining member when not in Bot Mode
            # / a possible integration is that after greeting the user of newly joining, it asks the user to leave bot mode and 
            # / chat with the new joined member. 
            # / if no, then just go to idle and wait for further responses. 
        # - the bot must also be able to check for new messages and check if their is a specific keyword pertaining to the author of the bot.
            # / if it is  a message pertaining to the author, tell the message sender to wait as they notify the creator of his/her response
            # / and we leave bot mode and go into user mode
            # / if no, then just go to idle and wait for further responses.
        # set up some form of logging to .log files. Log errors to discord.log and make a log file for the conversations made and received in conversation.log
# Future Wants: 
    # - Make Bot Mode like an actual bot, reacting to common messages that needs to be responded.
    # Shift to user and bot mode in any form of time, it is not only limited to after a new member joining
    # Make a channel where they can talk to the bot asking some common or repetitive questions, if it is not in this channel the bot does not reply appropriately.

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # print('Available Channels: {}'.format(client.guilds[0].channels[-1]))
    
    print("Available Guilds: ")
    for index, guild in enumerate(client.guilds):
        print("[{}] - {}".format(index , guild))

    selected_index = int(input("Input Your Selected Guild To Implant Bot: "))

    print("Available Channels")
    for index, channel in enumerate(client.guilds[selected_index].channels):
        print("[{}] - {}".format(index , channel))

    selected_channel_index = int(input("Input Your Selected Channel To Implant Bot: "))

    SELECTED_CHANNEL = client.guilds[selected_index].channels[selected_channel_index]
    #await client.guilds[selected_index].channels[selected_channel_index].send("Discord Bot Online.")

    print(SELECTED_CHANNEL)


@client.event
async def on_message(message):
    print(
        "{}'s Message: {} Channel: {} ".format(
            message.author,
            message.content,
            message.channel,
        )
    )

    if message.author == client.user:
        return 

    if message.content.startswith('$replace'):
        await message.channel.send('Conducting an act of Replacement.')
    
    # messages are for test purpose only. insert a more 'formal' message for actual use.
    randomMessage = [
        "busy pa si boss Vincent, reply na lang siya mamaya.", 
        "naghuhugas pa ng pinggan. jk babalik 'yon maya-maya.",
        "tulog pa ata, gisingin ko wait. chour rreply nalang siya mamaya"
    ]

    randomGreeting = [
        "Yoww",
        "'Sup",
        "Hii",
        "Hallu"
    ]
    # if the author is mentioned, and send back a message. 
    # replace @!723498127944056845 with the ID of the user that is needed to be checked for mentions.
    if '@!723498127944056845' in message.content:
        # send in a custom message
    #   if BOT_MODE == False: 
    #       response = input('Type in your reply: ')
    #       await message.channel.send(f"{message.author.mention}, {response}") 
    #   else:
            print(f"{message.author} mentioned you!")
            response = random.choice(randomMessage)
            greet = random.choice(randomGreeting)
            await message.channel.send(f"{greet} {message.author.mention}!, {response}") 
    
    #responds to mentions - from BoredPaper's PR
    #for x in message.mentions:
    #    if (x == client.user):
    #        await message.channel.send(f"{message.author.mention} hello there")
        

# @client.event
# async def on_member_join(member):
    # await member.create_dm()
    # await member.dm_channel.send(
        # 'Hi {member.name}, welcome to my Discord server!'
    # )
client.run(TOKEN)

