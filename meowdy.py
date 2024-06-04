import discord
import os
from dotenv import load_dotenv

load_dotenv('meowdytoken.env')

token = str(os.getenv('TOKEN'))

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("{0.user} is ready to go!".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = (message.content)

    print (f'Message {user_message} by {username} on {channel}')
    
    if channel == "general":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Meowdy, pardner {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Get along, little doggy {username}')

client.run(token)