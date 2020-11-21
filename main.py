#!/usr/bin/env python3
import os
import discord

scriptDir = "/home/ubuntu/github/counting/"
os.chdir(scriptDir)

with open("token.txt","r") as file:
    token = file.read()

me = discord.Client()

counter = 0

def print_bool(to_test):
    val = eval(to_test)
    print(to_test,val)
    return val

async def has_role(role: discord.Role,member: discord.Member):
    return role in member.roles

@me.event
async def on_message(message):
    global glob_mess
    global counter
    global is_not_player

    glob_mess = message

    is_not_player = not await has_role(779788698379747348,message.author)

    if print_bool("glob_mess.author == me.user") or print_bool("not glob_mess.channel.id in [779782709005910078]") or print_bool("is_not_player"):
        print("")
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
