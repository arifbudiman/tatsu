#!/usr/bin/env python3

import argparse
import discord
import os
import asyncio
import math
import pytz
from random import choice
from dotenv import load_dotenv
from pytz import timezone
from datetime import datetime, timedelta

# load environment variables
load_dotenv(verbose=True)
myUserToken = os.getenv("USER_TOKEN")
botChannelId = int(os.getenv("BOT_CHANNEL_ID"))
tatsuBotId = int(os.getenv("TATSUBOT_ID"))
botChannelId = int(os.getenv("BOT_CHANNEL_ID"))


class MyClient(discord.Client):

    myUserName = ""
    petIsTired = False
    targetWalk = 10
    channelId = botChannelId

    async def on_ready(self):

        await client.change_presence(afk=True)
        channel = client.get_channel(self.channelId)
        self.myUserName = client.user.name + "#" + client.user.discriminator

        cycle = 0
        attempt = 0

        print("{} Starting walks.".format(self.pacificTime()))

        while self.petIsTired == False and attempt < self.targetWalk:

            cycle += 1

            if cycle % 3 == 1:
                await channel.send("t!tg feed")
            else:
                attempt += 1
                await channel.send("t!tg walk")

            await asyncio.sleep(choice(range(7, 9)))

        print("{} Pet is fatigued. Stopping.".format(self.pacificTime()))
        await client.close()

    async def on_message(self, message):

        if message.author.id == client.user.id:
            return

        if message.channel.id != botChannelId:
            return

        if message.author.id != tatsuBotId:
            return

        # if the message is from tatsu
        if message.author.id == tatsuBotId:
            # if it's for me and it's a result of pet interaction
            if self.myUserName in message.content and "Interacting with Pet" in message.content:
                # if there's embed
                if len(message.embeds) > 0:
                    # if embed title indicates a failed training
                    if "Unable to Go for a Walk" in message.embeds[0].title:
                        # print(message.embeds[0].title)
                        self.petIsTired = True

    @staticmethod
    def pacificTime():
        return datetime.now(tz=pytz.utc).astimezone(timezone('US/Pacific'))


parser = argparse.ArgumentParser(description="""
This script takes pet for a walk.
""")
parser.add_argument("--count", help="how many times to walk pet")
parser.add_argument("--channel", help="channel ID to walk pet in")
args = parser.parse_args()
COUNT = args.count
CHANNELID = args.channel

client = MyClient()
client.targetWalk = int(COUNT)
client.channelId = int (CHANNELID)
client.run(myUserToken)
