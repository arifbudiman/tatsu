#!/usr/bin/env python3

import argparse
import discord
import os
import asyncio
from random import choice
from dotenv import load_dotenv

load_dotenv(verbose=True)
myUserToken = os.getenv("USER_TOKEN")
tatsuBotId = int(os.getenv("TATSUBOT_ID"))
botChannelId = int(os.getenv("BOT_CHANNEL_ID"))
cookieRecipients = os.getenv("COOKIE_RECIPIENTS").split(",")


class MyClient(discord.Client):

    channelId = botChannelId

    async def on_ready(self):

        channel = client.get_channel(self.channelId)

        os.system("clear")

        for cookieRecipient in cookieRecipients:

            print(f"Giving cookie to {cookieRecipient}")
            await channel.send("t!cookie " + cookieRecipient)
            interval = choice(range(7, 9))
            print(f"Waiting for {interval} seconds..")
            await asyncio.sleep(interval)

        print("Done.")
        await client.close()


parser = argparse.ArgumentParser(description="""
This script will give tatsu cookies.
""")
parser.add_argument("--channel", help="channel ID to give cookies in")
args = parser.parse_args()
CHANNELID = args.channel

client = MyClient()
client.channelId = int(CHANNELID)
client.run(myUserToken, bot=False)
