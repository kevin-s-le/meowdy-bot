# imports necessary libraries for the bot
import discord
import os
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv # loads TOKEN from .env file

# uses TOKEN from .env file to match the variable token
token = str(os.getenv('TOKEN'))

# sets up intents for discord bot to allow it to send messages
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Event handler to show when the bot is ready to use
@client.event
async def on_ready():
    print("{0.user} is ready to go!".format(client))

# Event handler for when a message is received
@client.event
async def on_message(message):
    # extracts username, channel name, and the message that is sent to the discord server
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = (message.content)

    # prints the result in the console
    print (f'Message {user_message} by {username} on {channel}')
    
    # if statement to determine response based on what was sent to the discord server
    if channel == "general":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Meowdy, pardner {username} Your EC2 Data: {ec2_metadata.region}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Get along, little doggy {username}')

# starts the discord bot using the token from .env file
client.run(token)