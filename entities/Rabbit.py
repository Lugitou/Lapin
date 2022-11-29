import random


class Rabbit:
    alive = 1
    sex = "M"
    reproduction = 0
    age = 0
    maxAge = 6
    fed: 1

    def __init__(self):
        self.sex = ("M", "F")[random.randint(0, 1)]

    # On nourrit le lapin ici
    # Si il n'est pas nourri, on passe son age maximum à 4 ans
    # Si il n'est pas nourri et qu'il n'avait déjà pas été nourri la semaine précédente, il meurt
    def feed(self, flag):
        if not flag:
            self.fed = flag
            self.maxAge = 4
            if self.fed == 0:
                self.alive = 0

    def setSex(self, sex):
        self.sex = sex

    def reproduced(self):
        self.reproduction = 1

    def setAge(self, age):
        self.age = age
