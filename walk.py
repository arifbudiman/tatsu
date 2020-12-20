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
tatsuBotId = int(os.getenv("TATSUBOT_ID"))

class MyClient(discord.Client):

    myUserName = ""
    petIsTired = False
    targetWalk = 20
    channelId = botChannelId

    async def on_ready(self):

        cycle = 0
        walkAttempt = 0
        channel = client.get_channel(self.channelId)
        myUserName = client.user.name + "#" + client.user.discriminator

        while walkAttempt < self.targetWalk:
            os.system("clear")
            cycle += 1
            
            if cycle % 3 == 1:
                print(f"Feeding")
                await channel.send("t!tg feed")
            else:
                walkAttempt += 1
                print(f"Walk attempt {walkAttempt}")
                await channel.send("t!tg walk")

            interval = choice(range(5, 8))
            if walkAttempt < self.targetWalk:
                print(f"Waiting for {interval} seconds..")
                await asyncio.sleep(interval)

        print("Done.")
        await client.close()

parser = argparse.ArgumentParser(description="""
This script will walk tatsu pet.
""")
parser.add_argument("--count", help="how many times to walk pet")
parser.add_argument("--channel", help="channel ID to walk pet in")
args = parser.parse_args()
COUNT = args.count
CHANNELID = args.channel

client = MyClient()
client.targetWalk = int(COUNT)
client.channelId = int(CHANNELID)
client.run(myUserToken, bot=False)
