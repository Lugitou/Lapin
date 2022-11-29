from random import randint

from entities.Rabbit import Rabbit


class Garden:
    carrots = 200
    rabbits = [Rabbit(), Rabbit()]
    nbCarrotEachYear = 200

    def __init__(self, nbCarrotStart, nbCarrotEachYear):
        self.rabbits[0].setSex("M")
        self.rabbits[1].setSex("F")
        self.rabbits[0].setAge(365)
        self.rabbits[1].setAge(365)
        self.carrots = nbCarrotStart
        self.nbCarrotEachYear = nbCarrotEachYear

    def eat(self):
        for rabbit in self.rabbits:
            if rabbit.alive == 1:
                if self.carrots > 0:
                    self.carrots = self.carrots - 1
                    rabbit.feed(1)
                else:
                    rabbit.feed(0)

    def growCarrots(self):
        self.carrots = self.carrots + self.nbCarrotEachYear

    def growRabbits(self):
        for rabbit in self.rabbits:
            if rabbit.alive == 1:
                rabbit.age = rabbit.age + 1
                if rabbit.age > rabbit.maxAge * 365:
                    rabbit.alive = 0

    def reproduce(self):
        for rabbit in self.rabbits:
            if rabbit.sex == "M" and rabbit.alive == 1 and rabbit.reproduction == 0 and rabbit.age > 364:
                for r in self.rabbits:
                    if r.sex == "F" and r.reproduction == 0 \
                            and r.age > 364 and r.alive == 1:
                        r.reproduced()
                        rabbit.reproduced()
                        for i in range(randint(1, 6)):
                            self.rabbits.append(Rabbit())
        for rabbit in self.rabbits:
            rabbit.reproduction = 0
