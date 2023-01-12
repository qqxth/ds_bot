import asyncio
import os

from dotenv import load_dotenv

import discord_bot

load_dotenv()

os.system('bc')


BOT_TOKEN = os.getenv('BOT_TOKEN')

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def main():
    discord_bot.client.run(BOT_TOKEN)

asyncio.run(main())