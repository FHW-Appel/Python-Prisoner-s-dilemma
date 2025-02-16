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


class Friedman(Strategy):
    
    def __init__(self) -> None:
        self.name = "Friedman"
        self.cheated = False

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn):
            self.cheated = False
            return Strategy.cooperate
        else:
            if (Strategy.defect == hishist[-1]):
                self.cheated = True
            if (True == self.cheated):
                return Strategy.defect
            else:
                return Strategy.cooperate 
            

class Joss(Strategy):

    def __init__(self) -> None:
        self.name = "Joss"

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn):
            if (0 < (random.random() - 0.1)):
                return Strategy.cooperate
            else:
                return Strategy.defect  
        else:
            if (Strategy.defect == hishist[-1]):
                return Strategy.defect
            else:
                if (0 < (random.random() - 0.1)):
                    return Strategy.cooperate
                else:
                    return Strategy.defect   