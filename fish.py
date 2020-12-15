#!/usr/bin/env python3

import sys
import discord
import os
import asyncio
from random import choice
from dotenv import load_dotenv

# load environment variables
load_dotenv(verbose=True)
myUserToken = os.getenv("USER_TOKEN")
tatsuBotId = int(os.getenv("TATSUBOT_ID"))
botChannelId = int(os.getenv("BOT_CHANNEL_ID"))
fishCount = 0

targetFish = 10

class MyClient(discord.Client):

    async def on_ready(self):

        attempt = 0
        channel = client.get_channel(botChannelId)

        while fishCount < targetFish:
            os.system("clear")
            try:
                attempt += 1
                print(f"Attempt {attempt}")
                await channel.send("t!fish")

            except Exception as e:
                print("ERR: ", e)
                raise

            interval = choice(range(30, 33))
            if fishCount < targetFish:
                print(f"Waiting for {interval} seconds..")
                await asyncio.sleep(interval)

        print("Done.")
        sys.exit(0)

    async def on_message(self, message):

        global fishCount

        if message.author.id != tatsuBotId:
            return

        if message.channel.id != botChannelId:
            return

        # if message is from tatsu
        if message.author.id == tatsuBotId:
            # if it contains fish
            if "🐟" in message.content or "🐠" in message.content:
                fishCount += 1
                print(f"Fish collected so far: {fishCount}")
                return

client = MyClient()
client.run(myUserToken, bot=False)
