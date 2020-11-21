import discord

with open("token.txt","r") as file:
    token = file.read()

me = discord.Client()

counter = 0

@me.event
async def on_message(message):
    global counter
    if message.author == me.user or not message.channel.id in [779814081573552148,779782709005910078]:
        return
    counter += 1
    try:
        counter = int(message.content)
    except ValueError:
        pass

    if not counter % 100:
        await me.change_presence(activity = discord.Game("A counting game... We are in the {}s".format(str(counter))))

    if "249999" in message.content:
        await message.channel.send("250000")

me.run(token,bot = False)
