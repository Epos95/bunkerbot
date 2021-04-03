import discord
import json
from random import randint

import datetime

token = ""
with open("token.txt", "r") as f:
    token = f.read()

bot = discord.Client()
# best structure? fuck if i know just yeet it into a json file 
# adopt the json structure from the LTU discord bot to keep the json updated

def add_quote(msg: discord.Message, grabber: str, time: datetime) -> None:
    # this function should add things to the json
    with open("file.json", "r+") as f:
        d = json.load(f)

        d["quotes"][len(d["quotes"])+1] = {
            "user" : msg.author.name,
            "grabber" : grabber,
            "datetime" : time,
            "quote" : msg.content
        }
        
        json.dump(d, f)

# maybe add undo feature
async def grab(msg: discord.Message, *args, **kwargs) -> None:
    if len(msg.mentions) == 1:
        user = msg.mentions[0]
        # iterate over the message list from the server and find the latest one by userid
    else:
        # this limit is flexible
        async for message in msg.channel.history(limit=20):
            if message.author != bot.user and message.author != msg.author:
                add_quote(message, msg.author.name, msg.created_at)
                return
                
async def random(msg: discord.Message, *args, **kwargs) -> None:
    # get a random quote from the json
    with open("file.json", "r+") as f:
        d = json.load(f)
        id = str(randint(0,len(d["quotes"])))
        quote = d["quotes"][id]

        await msg.channel.send(f"*{quote['user']}* said ```{quote['grabber']}``` and was grabbed at {quote['time']}. This wonderful qoute grabbed by *{quote['grabber']}*")


async def get(msg: discord.Message, *args, **kwargs) -> list[discord.Message]:
    # this should check if the content of the message contains any name to check 
    pass

methods = {
    "!grab" : grab,
    "!get"  : get,
    "!random" : random,
}

@bot.event
async def on_ready() -> None:
    print("Bot ready")
    print(f"logged in as {bot.user.name}")

@bot.event
async def on_message(msg: discord.Message) -> None:
    command = msg.content.split(" ")[0]

    if not command:
        # a trailing space before text makes this happen but discord should make it safe
        # test before removing
        return

    # lmao imagine using try/catch
    try: 
        await methods[command](msg)
    except:
        pass

if "__main__" == __name__:
    bot.run(token)
