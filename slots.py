#!/usr/bin/env python3

import sys
import discord
import os
import asyncio
from random import choice
from dotenv import load_dotenv

# load environment variables
load_dotenv(verbose=True)
myUserToken = os.getenv("USER_TOKEN")
botChannelId = int(os.getenv("BOT_CHANNEL_ID"))

targetSlots = 10

class MyClient(discord.Client):

    async def on_ready(self):

        attempt = 0
        channel = client.get_channel(botChannelId)

        while attempt < targetSlots:
            os.system("clear")
            try:
                attempt += 1
                print(f"Attempt {attempt}")
                await channel.send("t!slots")

            except Exception as e:
                print(e)
                raise

            interval = choice(range(8, 10))
            if attempt < targetSlots:
                print(f"Waiting for {interval} seconds..")
                await asyncio.sleep(interval)

        print("Done.")
        sys.exit(0)

client = MyClient()
client.run(myUserToken, bot=False)
