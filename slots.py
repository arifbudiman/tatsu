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
botChannelId = int(os.getenv("BOT_CHANNEL_ID"))

class MyClient(discord.Client):

    targetSlots = 20
    channelId = botChannelId

    async def on_ready(self):

        attempt = 0
        channel = client.get_channel(self.channelId)

        while attempt < self.targetSlots:
            os.system("clear")
            attempt += 1
            # print(f"Attempt {attempt}")
            await channel.send("t!slots")
            interval = choice(range(8, 10))
            if attempt < self.targetSlots:
                # print(f"Waiting for {interval} seconds..")
                await asyncio.sleep(interval)

        # print("Done.")
        await client.close()

parser = argparse.ArgumentParser(description="""
This script will play tatsu slots.
""")
parser.add_argument("--count", help="how many times to play slots")
parser.add_argument("--channel", help="channel ID to play slots in")
args = parser.parse_args()
COUNT = args.count
CHANNELID = args.channel

client = MyClient()
client.targetSlots = int(COUNT)
client.channelId = int(CHANNELID)
client.run(myUserToken)
