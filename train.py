#!/usr/bin/env python3

import asyncio
import math
import os
from datetime import datetime
from random import choice

import discord
import pytz
from dotenv import load_dotenv
from pytz import timezone

# load environment variables
load_dotenv(verbose=True)
myUserToken = os.getenv("USER_TOKEN")
tatsuBotId = int(os.getenv("TATSUBOT_ID"))
botChannelId = int(os.getenv("BOT_CHANNEL_ID"))

# global variables
myUserName = ""
petIsTired = False

# pet characteristics
maxFatigue = 511

class MyClient(discord.Client):

    async def on_ready(self):

        global petIsTired
        global myUserName

        channel = client.get_channel(botChannelId)
        myUserName = client.user.name + "#" + client.user.discriminator
        restPeriod = math.ceil(18.3431952663 * maxFatigue)
        attempt = 0

        while True:
            os.system("clear")
            try:
                print(f"{self.pacificTime()} Attempted {attempt}x.")
                if petIsTired == False:
                    attempt += 1
                    await channel.send("t!tg train")
                elif petIsTired == True:
                    print("{} Pet is fatigued. Resting for {} seconds.".format(self.pacificTime(), restPeriod))
                    await asyncio.sleep(restPeriod)
                    petIsTired = False
                    await channel.send("t!tg clean")
                    await asyncio.sleep(7)
                    await channel.send("t!tg play")
                    await asyncio.sleep(7)
                    await channel.send("t!tg feed")
                    await asyncio.sleep(7)

            except Exception as e:
                print("ERR: ", e)
                raise

            interval = choice(range(6, 9))
            print(f"Waiting for {interval} seconds..")
            await asyncio.sleep(interval)

    async def on_message(self, message):

        global petIsTired

        if message.author.id == client.user.id:
            return

        if message.channel.id != botChannelId:
            return

        if message.author.id != tatsuBotId:
            return

        # if the message is from tatsu
        if message.author.id == tatsuBotId:
            # if it's for me and it's a result of pet interaction
            if myUserName in message.content and "Interacting with Pet" in message.content:
                # if there's embed
                if len(message.embeds) > 0:
                    # if embed title indicates a successful training
                    if "Training Success!" in message.embeds[0].title:
                        print(message.embeds[0].title)
                    # if embed title indicates a failed training
                    elif "Training Failed!" in message.embeds[0].title:
                        print(message.embeds[0].title)
                        petIsTired = True

    @staticmethod
    def pacificTime():
        return datetime.now(tz=pytz.utc).astimezone(timezone('US/Pacific')).strftime("%a %x %X %Z")

client = MyClient()
try:
    client.run(myUserToken, bot=False)
except Exception as e:
    print(e)