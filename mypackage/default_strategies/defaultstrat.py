#

from ..basestrategy import Strategy
import random


class TitForTat(Strategy):

    def __init__(self) -> None:
        self.name = "Tit for Tat"

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn):
            return Strategy.cooperate
        else:
            return hishist[-1]    


class RandomStrat(Strategy):

    def __init__(self) -> None:
        self.name = "Random"

    def react(self, currentturn, myhist, hishist):
        if (0 < (random.random() - 0.5)):
            return Strategy.cooperate
        else:
            return Strategy.defect    