#!/usr/bin/env python3
import os
import discord

scriptDir = "/home/ubuntu/github/counting/"
os.chdir(scriptDir)

with open("token.txt","r") as file:
    token = file.read()

me = discord.Client()

counter = 0

@me.event
async def on_message(message):
    global counter
    if message.author == me.user or not message.channel.id in [779782709005910078]:
        return
    counter += 1
    try:
        counter = int(message.content)
    except ValueError:
        pass

    if not counter % 100:
        await me.change_presence(activity = discord.Game("A counting game... We are in the {}s".format(str(counter))))

    if counter == 249999:
        await message.channel.send("250000")

me.run(token,bot = False)
