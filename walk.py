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

    async def on_ready(self):

        await client.change_presence(afk=True)
        channel = client.get_channel(botChannelId)
        self.myUserName = client.user.name + "#" + client.user.discriminator

        print("{} Cleaning.".format(self.pacificTime()))
        await channel.send("t!tg clean")
        await asyncio.sleep(7)

        print("{} Playing.".format(self.pacificTime()))
        await channel.send("t!tg play")
        await asyncio.sleep(7)

        cycle = 0

        print("{} Starting walks.".format(self.pacificTime()))

        while self.petIsTired == False:

            cycle += 1

            if cycle % 3 == 1:
                await channel.send("t!tg feed")
            else:
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


client = MyClient()
client.run(myUserToken, bot=False)
