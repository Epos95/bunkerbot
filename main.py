import discord
import json

token = "read from file lol"

bot = discord.Client()
# best structure? fuck if i know just yeet it into a json file 
# adopt the json structure from the LTU discord bot to keep the json updated

def grab(msg, *args, **kwargs):
    # if a name is specified in content:
    #   get the last message of that user and add it 
    # else
    #   get the last message sent BESIDES the grab message and add it
    if len(msg.content) > len("!grab") and len(msg.mentions) == 1:
        user = msg.mentions[0]
        
        # iterate over the message list from the server and find the latest one by userid

    else:
        # grab the last message that wasnt sent by the bot
        pass
                
def random(msg, *args, **kwargs):
    pass

def get(msg, *args, **kwargs):
    # this should check if the content of the message contains any name to check 
    pass


d = {
    "!grab" : grab,
    "!get"  : get,
    "!random" : random,
}

@bot.event
async def on_ready():
    print("Weady UwU mothewfuwckew")

@bot.event
async def on_message(msg):
    print("got a message lul")
    command = msg.content.split(" ")

    # remove this error check later
    if not command:
        print("What kinda message would even trigger this?")
        return

    # lmao imagine using try/catch
    d[command](msg)


if "__main__" == __name__:
    bot.run(token)
