import main

class DummyMessage:
    def __init__(self, s):
        self.content = s
        self.mentions = ["@epos95"]


d = DummyMessage("!grab @Epos95")
print(f"Testing grab with string \"{d.content}\"")
main.grab(d)

print()


d2 = DummyMessage("!get")
print(f"Testing get with string \"{d2.content}\"")
main.get(d2)

