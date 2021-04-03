import main
import asyncio

class DummyMessage:
    def __init__(self, s):
        self.content = s
        self.mentions = ["@epos95"]



async def m():

    d = DummyMessage("!grab @Epos95")
    print(f"Testing grab with string \"{d.content}\"")
    await main.grab(d)

    print()

    d2 = DummyMessage("!get")
    print(f"Testing get with string \"{d2.content}\"")
    await main.get(d2)

    print()

    d3 = DummyMessage("!test")
    print(f"Testing on_message with string \"{d3.content}\"")
    await main.on_message(d3)

    d4 = DummyMessage("!grab")
    print(f"Testing on_message with string \"{d4.content}\"")
    await main.on_message(d4)


asyncio.run(m())
