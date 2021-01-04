#!/usr/bin/env python3

import asyncio
import os
from datetime import datetime, timedelta
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

        print("{} Feeding.".format(self.pacificTime()))
        await channel.send("t!tg feed")
        await asyncio.sleep(7)

        print("{} Starting training.".format(self.pacificTime()))

        while self.petIsTired == False:
            await channel.send("t!tg train")
            await asyncio.sleep(choice(range(6, 9)))

        print("{} Pet is fatigued. Stopping".format(self.pacificTime()))
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
                    if "Training Failed!" in message.embeds[0].title:
                        # print(message.embeds[0].title)
                        self.petIsTired = True

    @staticmethod
    def pacificTime():
        return datetime.now(tz=pytz.utc).astimezone(timezone('US/Pacific'))


client = MyClient()
client.run(myUserToken, bot=False)
