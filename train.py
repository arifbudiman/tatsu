#!/usr/bin/env python3

import sys
import signal
import discord
import os
import time
import asyncio
import math
from random import choice
from dotenv import load_dotenv

# load environment variables
load_dotenv(verbose=True)
myUserToken = os.getenv("USER_TOKEN")
tatsuBotId = int(os.getenv("TATSUBOT_ID"))
botChannelId = int(os.getenv("BOT_CHANNEL_ID"))

# global variables
myUserName = ""
myUserId = 0
petIsTired = False
timeStart = time.strftime("%a %x %X %Z")

# global variables with customizable values
maxFatigue = 511

client = discord.Client()

@client.event
async def on_ready():

    global petIsTired
    global myUserName
    global myUserId

    # exit handler
    def handleExit(signalNumber, frame):
        timeEnd = time.strftime("%a %x %X %Z")
        print("Program terminated. Started: " + timeStart + ". Ended: " + timeEnd)
        with open("tatsu.log", "a+") as f:
            f.write("Started: " + timeStart + ". Ended: " + timeEnd + "\n")
        sys.exit(1)

    signal.signal(signal.SIGINT, handleExit)
    signal.signal(signal.SIGTERM, handleExit)

    botChannel = client.get_channel(botChannelId)
    myUserId = client.user.id
    myUserName = client.user.name + "#" + client.user.discriminator
    restPeriod = math.ceil(18.1132 * maxFatigue)
    attempt = 0

    while True:
        os.system("clear")
        try:
            print(f"Status: Attempted {attempt}x.")

            if petIsTired == False:
                attempt += 1
                await botChannel.send("t!tg train")
            elif petIsTired == True:
                print("Can't train anymore; pet is tired. Resting for {} seconds from {}.".format(restPeriod, time.strftime("%a %x %X %Z")))
                await asyncio.sleep(restPeriod)
                petIsTired = False
                await botChannel.send("t!tg clean")
                await asyncio.sleep(7)
                await botChannel.send("t!tg play")
                await asyncio.sleep(7)
                await botChannel.send("t!tg feed")
                await asyncio.sleep(7)

        except Exception as e:
            print("ERR: ", e)
            raise

        interval = choice(range(6, 9))
        print(f"Waiting for {interval} seconds..")
        await asyncio.sleep(interval)

@client.event
async def on_message(message):

    global petIsTired

    # ignore my own message
    if message.author.id == myUserId:
        return

    # ignore other channels
    if message.channel.id != botChannelId:
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

if __name__ == "__main__":
    try:
        client.run(myUserToken, bot=False)
    except Exception as e:
        print(e)
