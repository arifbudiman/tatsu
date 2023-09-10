#!/usr/bin/env python3

import asyncio
import os
from pytz import timezone
import pytz
import discord
from datetime import datetime
from dotenv import load_dotenv

# load environment variables
load_dotenv(verbose=True)
myUserToken = os.getenv("USER_TOKEN")
tatsuBotId = int(os.getenv("TATSUBOT_ID"))

class MyClient(discord.Client):

    async def on_ready(self):
        # os.system("clear")
        print('Logged on as', self.user)

    async def on_message(self, message):
        # if message is from tatsu
        if message.author.id == tatsuBotId:
            # if this is Greench
            if "The chatting from" in message.content and "got the attention of the Greench!" in message.content:
                serverName = message.channel.guild.name
                if len(message.embeds) > 0:
                    await asyncio.sleep(10)
                    try:
                        currentTime = datetime.now(tz=pytz.utc).astimezone(timezone('US/Pacific')).strftime("%a %x %X %Z")
                        if "taunting" in message.embeds[0].thumbnail.url:
                            await message.add_reaction("<:snowball_throw:780656490259808266>")
                            print(currentTime + " " + serverName + ": taunting - snowball_throw")
                        elif "bored" in message.embeds[0].thumbnail.url:
                            await message.add_reaction("<:negotiate:780657414570639421>")
                            print(currentTime + " " + serverName + ": bored - negotiate")
                        elif "eager" in message.embeds[0].thumbnail.url:
                            await message.add_reaction("<:strategise:780657398867296266>")
                            print(currentTime + " " + serverName + ": eager - strategise")
                    except Exception as e:
                        print("ERR: ", e)
                        raise

client = MyClient()
client.run(myUserToken, bot=False)
