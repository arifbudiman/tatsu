#!/usr/bin/env python3

import asyncio
import os
import discord
import time
from dotenv import load_dotenv

# load environment variables
load_dotenv(verbose=True)
myUserToken = os.getenv("USER_TOKEN")
tatsuBotId = int(os.getenv("TATSUBOT_ID"))

class MyClient(discord.Client):

    async def on_ready(self):
        os.system("clear")
        print('Logged on as', self.user)

    async def on_message(self, message):
        # if message is from tatsu
        if message.author.id == tatsuBotId:
            # if this is Greench
            if "The chatting from" in message.content and "got the attention of the Greench!" in message.content:
                currentTime = time.strftime("%a %x %X %Z")
                if len(message.embeds) > 0:
                    if "taunting" in message.embeds[0].thumbnail.url:
                        # react with :snowball_throw:
                        await asyncio.sleep(5)
                        await message.add_reaction('<:snowball_throw:780656490259808266>')
                        print(currentTime + " " + message.channel.guild.name + " Greench taunting - snowball_throw")
                        return
                    if "bored" in message.embeds[0].thumbnail.url:
                        # react with :negotiate:
                        await asyncio.sleep(5)
                        await message.add_reaction('<:negotiate:780657414570639421>')
                        print(currentTime + " " + message.channel.guild.name + " Greench bored - negotiate")
                        return
                    if "eager" in message.embeds[0].thumbnail.url:
                        # react with :strategise:
                        await asyncio.sleep(5)
                        await message.add_reaction('<:strategise:780657398867296266>')
                        print(currentTime + " " + message.channel.guild.name + " Greench eager - strategise")
                        return

client = MyClient()
client.run(myUserToken, bot=False)