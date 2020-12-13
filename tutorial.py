
class myclass:
    zahl = 42
    string = "zeichenkette"

    def __init__(self):
        print('')

    def do_something(self, neuezahl):
        self.zahl = neuezahl

instanz = myclass()
instanz.do_something(1337)
print(instanz.zahl)
