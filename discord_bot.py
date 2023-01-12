import discord

import get_anime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        retur

    if message.content.startswith('$dai anime'):
        unpacked_data = get_anime.unpack_anime_data()
        await message.channel.send(unpacked_data['image'])
        await message.channel.send(unpacked_data['message'])
