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

    def growRabbits(self):
        for rabbit in self.rabbits:
            if rabbit.alive == 1:
                rabbit.age = rabbit.age + 1
                if rabbit.age > rabbit.maxAge * 365:
                    rabbit.alive = 0

    def reproduce(self):
        for rabbit in self.rabbits:
            if rabbit.sex == "M":
                for r in self.rabbits:
                    if r.sex == "F" and r.reproduction == 0 and rabbit.reproduction == 0 \
                            and r.age > 365 and rabbit.age > 365 \
                                and r.alive == 1 and rabbit.alive == 1:
                        r.reproduced()
                        rabbit.reproduced()
                        self.rabbits.append(Rabbit())
        for rabbit in self.rabbits:
            rabbit.reproduction = 0
