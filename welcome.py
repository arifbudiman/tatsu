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

    counter = 0
    welcomeMessages = ["<:welkam:759501888646414406>", "welcome", "selamat datang",
                       "<:welcomedepan:698521074677055538><:welcomebelakang:698521042695618601>", 
                       "selamat <:welkam:759501888646414406> datang",
                       "welcome <:welkam:759501888646414406>", 
                       "<:welkam:759501888646414406> <:welcomedepan:698521074677055538><:welcomebelakang:698521042695618601> <:welkam:759501888646414406>"]

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
                            welcomeMessage = self.welcomeMessages[self.counter % len(self.welcomeMessages)]
                            await message.channel.send(welcomeMessage)
                            print(message.content)
                            print(welcomeMessage)
                            self.counter += 1


client = MyClient()
client.run(myUserToken, bot=False)
