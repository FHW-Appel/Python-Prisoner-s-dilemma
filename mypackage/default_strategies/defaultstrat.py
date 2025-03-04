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
                

class Davis(Strategy):
    
    def __init__(self) -> None:
        self.name = "Davis"
        self.cheated = False

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn): # Die ersten Runde
            self.cheated = False
        if (9 >= currentturn): # Die ersten 10 Runden
            return Strategy.cooperate # Die ersten 10 Runden wird immer kooperiert
        else: # Ab der 11 Runde
            if (Strategy.defect == hishist[-1]): # Wurde diese Strategie in der letzten Runde betrogen?
                self.cheated = True # Merke Dir, dass du betrogen wurdest
            if (True == self.cheated): # Wurdest du schon mal betrogen?
                return Strategy.defect
            else:
                return Strategy.cooperate


class Grofman(Strategy):

    def __init__(self):
        self.name = "Grofman"

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn): # Die ersten Runde
             return Strategy.cooperate
        else:
            if (hishist[-1] != myhist[-1]): # Wenn in der letzten Runde keine Einigkeit bestand
                if (0 < (random.random() - 0.286)):
                    return Strategy.cooperate
                else:
                    return Strategy.defect
            else:
                return Strategy.cooperate

    