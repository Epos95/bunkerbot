import discord
from discord.ext import tasks
import json

from random import randint
from typing import List

import datetime

with open("token.txt", "r") as f:
    token = f.read()

bot = discord.Client()
# best structure? fuck if i know just yeet it into a json file 
# adopt the json structure from the LTU discord bot to keep the json updated

async def add_quote(msg: discord.Message, grabber: str, time: datetime) -> None:
    # this function should add things to the json

    with open("file.json", "r") as f:
        d = json.load(f)

    with open("file.json", "w") as f:
        d["quotes"][len(d["quotes"])+1] = {
            "user" : msg.author.name,
            "grabber" : grabber,
            "datetime" : str(time),
            "quote" : msg.content
        }

        json.dump(d, f, indent=4)

    await msg.channel.send("Succesfully grabbed message!")

# maybe add undo feature
async def grab(msg: discord.Message, *args, **kwargs) -> None:
    if len(msg.mentions) == 1:
        # this does not work

        user = msg.mentions[0]

        async for message in msg.channel.history(limit=200): 
            if message.author == user:
                await add_quote(message, msg.author.name, msg.created_at)
                return

    else:
        # this limit is flexible
        async for message in msg.channel.history(limit=200):
            if message.author != bot.user and message.author != msg.author:
                # Rewrite this to use the nicknames of users instead
                await add_quote(message, msg.author.name, msg.created_at)
                return

                
async def random(msg: discord.Message, *args, **kwargs) -> None:
    # get a random quote from the json
    with open("file.json", "r+") as f:

        d = json.load(f)
        id = str(randint(1,len(d["quotes"])))
        quote = d["quotes"][id]

        await msg.channel.send(f"{quote['user']} said: ```{quote['quote']}``` at {quote['datetime']}. Grabbed by {quote['grabber']}")

async def bait(msg: discord.message, *args, **kwargs) -> None:
    async for message in msg.channel.history(limit=100):
        if message.author != bot.user and message.author != msg.author:
            await msg.channel.send(f"Shame on you, {message.author}!")
            return

async def suggest(msg: discord.message) -> None:
    # should add suggestions to a text file 
    splat = msg.content.split(" ")[1:]

    if splat:
        with open("suggestions.txt", "a") as f:
            f.write(" ".join(splat) + "\n")

        await msg.channel.send("Thank you for your suggestion!")

@tasks.loop(minutes=2)
async def times():
    # check if its midnight on a friday, caturday or sunday
    # (night to saturday, night to sunday and night to monday)

    # print midnight cat

    # get channel by channelid 

    # get cat gif

    # send message to channel

    pass


methods = {
    "!grab" : grab,
    "!get"  : get,
    "!random" : random,
    "!bait" : bait,
    "!suggest" : suggest
}

@bot.event
async def on_ready() -> None:
    print("Bot ready")
    print(f"logged in as {bot.user.name}")
    times.start()
    

@bot.event
async def on_message(msg: discord.Message) -> None:
    command = msg.content.split(" ")[0]

    if not command:
        # a trailing space before text makes this happen but discord should make it safe
        # test before removing
        return

    try: 
        await methods[command](msg)
    except:
        pass

if "__main__" == __name__:
    bot.run(token)
