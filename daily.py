#!/usr/bin/env python3

import discord
import os
import asyncio
from dotenv import load_dotenv

load_dotenv(verbose=True)
myUserToken = os.getenv("USER_TOKEN")
#tatsuBotId = int(os.getenv("TATSUBOT_ID"))
botChannelId = int(os.getenv("DAILY_CHANNEL_ID"))
dailyRecipient = os.getenv("DAILY_RECIPIENT")


class MyClient(discord.Client):

    async def on_ready(self):
        client.change_presence(afk=True)
        channel = client.get_channel(botChannelId)
        await channel.send("t!quests 1")
        await asyncio.sleep(7)
        await channel.send("t!rep " + dailyRecipient)
        await asyncio.sleep(7)
        await channel.send("t!daily " + dailyRecipient)
        print("Done.")
        await client.close()


client = MyClient()
client.run(myUserToken, bot=False)
