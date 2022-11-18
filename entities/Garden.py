from entities.Rabbit import Rabbit


class Garden:
    carrots = 200
    rabbits = [Rabbit(), Rabbit()]

    def __init__(self):
        self.rabbits[0].setSex("M")
        self.rabbits[1].setSex("F")

    def eat(self):
        for rabbit in self.rabbits:
            if rabbit.alive == 1:
                if self.carrots > 0:
                    self.carrots = self.carrots - 1
                    rabbit.feed(1)
                else:
                    rabbit.feed(0)

    def growCarrots(self):
        self.carrots = self.carrots + 200
