#!/usr/bin/env python3

import discord
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv(verbose=True)
myUserToken = os.getenv("USER_TOKEN")
welcomeChannelId = int(os.getenv("WELCOME_CHANNEL_ID"))
welcomeBotId = int(os.getenv("WELCOME_BOT_ID"))


class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(afk=True)
        channel = client.get_channel(welcomeChannelId)

    async def on_message(self, message):
        if message.channel.id != welcomeChannelId:
            return
        if message.author.id != welcomeBotId:
            return
        if message.author.id == client.user.id:
            return
        if message.author.id == welcomeBotId:
            if message.channel.id == welcomeChannelId:
                if message.content.startswith("Hello"):
                    if len(message.embeds) > 0:
                        if "Welcome to" in message.embeds[0].title:
                            await message.channel.send("welcome")
                            print(message.content)


client = MyClient()
client.run(myUserToken, bot=False)
