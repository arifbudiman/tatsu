#!/usr/bin/env python3

import argparse
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

class MyClient(discord.Client):

    targetFish = 10
    channelId = botChannelId

    async def on_ready(self):

        attempt = 0
        channel = client.get_channel(self.channelId)

        while fishCount < self.targetFish:
            os.system("clear")
            attempt += 1
            # print(f"Attempt {attempt}")
            await channel.send("t!fish")
            interval = choice(range(30, 33))
            if fishCount < self.targetFish:
                # print(f"Waiting for {interval} seconds..")
                await asyncio.sleep(interval)

        # print("Done.")
        await client.close()

    async def on_message(self, message):

        global fishCount

        if message.author.id != tatsuBotId:
            return

        if message.channel.id != self.channelId:
            return

        # if message is from tatsu
        if message.author.id == tatsuBotId:
            # if it contains fish
            if "🐟" in message.content or "🐠" in message.content:
                fishCount += 1
            # print(f"Fish collected so far: {fishCount}")
            return

parser = argparse.ArgumentParser(description="""
This script will perform tatsu fishing.
""")
parser.add_argument("--count", help="how many fishes to catch")
parser.add_argument("--channel", help="channel ID to fish in")
args = parser.parse_args()
COUNT = args.count
CHANNELID = args.channel

client = MyClient()
client.targetFish = int(COUNT)
client.channelId = int(CHANNELID)
client.run(myUserToken)
