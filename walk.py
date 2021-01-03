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

# pet characteristics
maxFatigue = 511

class MyClient(discord.Client):

    myUserName = ""
    petIsTired = False
    channelId = botChannelId

    async def on_ready(self):

        self.petIsTired = False
        cycle = 0
        walkAttempt = 0
        channel = client.get_channel(self.channelId)
        client.change_presence(afk=True)
        self.myUserName = client.user.name + "#" + client.user.discriminator
        restPeriod = math.ceil(18.3431952663 * maxFatigue)

        while True:
            os.system("clear")
            cycle += 1

            if cycle % 3 == 1:
                print(f"Feeding")
                await channel.send("t!tg feed")
            else:
                walkAttempt += 1
                print(f"Walk attempt {walkAttempt}")
                await channel.send("t!tg walk")

            if self.petIsTired == False:
                interval = choice(range(7, 9))
                print(f"Waiting for {interval} seconds..")
                await asyncio.sleep(interval)
            elif self.petIsTired == True:
                print("{} Pet is fatigued. Resting until {}".format(self.pacificTime(), self.pacificTime() + timedelta(0, restPeriod)))
                await asyncio.sleep(restPeriod)
                self.petIsTired = False
                await channel.send("t!tg clean")
                await asyncio.sleep(7)
                await channel.send("t!tg play")
                await asyncio.sleep(7)
                await channel.send("t!tg feed")
                await asyncio.sleep(7)

        print("Done.")
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
                    # if embed title indicates a successful training
                    if "Going for a Walk" in message.embeds[0].title:
                        print(message.embeds[0].title)
                    # if embed title indicates a failed training
                    elif "Unable to Go for a Walk" in message.embeds[0].title:
                        print(message.embeds[0].title)
                        self.petIsTired = True

    @staticmethod
    def pacificTime():
        return datetime.now(tz=pytz.utc).astimezone(timezone('US/Pacific'))

client = MyClient()
client.run(myUserToken, bot=False)
