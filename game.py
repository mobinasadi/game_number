from random import randint


class game:
    def __init__(self , add:int):
        self.add = add
    def hats(self):
        global hadss
        while self.add != hadss:
            if self.add < hadss:
                print("Choose a smaller number")
            else:
                print("Choose a large number")
            hadss = int(input("hads bezan : "))
        print("Wow you won")
        input("press enter byby")
hadss=int(input("guess number ? "))
pc = randint(0,99)
s = game(add=pc)
d=s.hats()
