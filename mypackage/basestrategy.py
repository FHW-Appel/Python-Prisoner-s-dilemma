#

import random


class Strategy:
    defect = False
    cooperate = True
    classid = 0  # Muss noch gesetzt werden
    nice = False

    def __init__(self) -> None:
        self.name = ""
        self.classid = -1

    def react(self, currentturn, myhist, hishist):
        return Strategy.cooperate

    def reactProbCooperate(self, prob):
        # Kooperiere mit der übergebenen Wahrscheinlichkeit
        if (prob > (random.random()*100)):
            return self.cooperate
        else:
            return self.defect

    def reactProbDefect(self, prob):
        return self.reactProbCooperate(100-prob)
