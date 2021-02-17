import discord
import json

token = "read from file lol"

bot = discord.Client()
# best structure? fuck if i know just yeet it into a json file 
# adopt the json structure from the LTU discord bot to keep the json updated

def add_quote(msg):
    # this function should add things to the json
    pass

# maybe add undo feature
async def grab(msg, *args, **kwargs):
    if len(msg.mentions) == 1:
        user = msg.mentions[0]
        
        # iterate over the message list from the server and find the latest one by userid

    else:
        # grab the last message that wasnt sent by the bot
        print("grab the last message")

        # this limit is flexible
        async for message in msg.channel.history(limit=20):
            if message.author != bot.user and message.author != msg.author:
                add_quote(message)
                return
                
async def random(msg, *args, **kwargs):
    pass

async def get(msg, *args, **kwargs):
    # this should check if the content of the message contains any name to check 
    pass


# this is damn therapeutic man
methods = {
    "!grab" : grab,
    "!get"  : get,
    "!random" : random,
}

@bot.event
async def on_ready():
    print("Bot ready")
    print(f"logged in as {bot.user.name}")

@bot.event
async def on_message(msg):
    print("got a message lul")
    command = msg.content.split(" ")[0]

    # remove this error check later
    if not command:
        print("What kinda message would even trigger this?")
        return

    # lmao imagine using try/catch
    if command in methods:
        await methods[command](msg)



if "__main__" == __name__:
    bot.run(token)
