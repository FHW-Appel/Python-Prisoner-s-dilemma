#

from ..basestrategy import Strategy
import random


class TitForTat(Strategy):

    def __init__(self) -> None:
        self.name = "Tit for Tat"
        self.nice = True

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn):
            return Strategy.cooperate
        else:
            return hishist[-1]    


class RandomStrat(Strategy):

    def __init__(self) -> None:
        self.name = "Random"
        self.nice = False

    def react(self, currentturn, myhist, hishist):
        return self.reactProbCooperate(50) # Kooperiere zu einer Wahrscheinlichkeit von 50 % 


class Friedman(Strategy):
    
    def __init__(self) -> None:
        self.name = "Friedman"
        self.cheated = False
        self.nice = True

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
        self.nice = False

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn): 
            return self.reactProbCooperate(90) # Kooperiere zu einer Wahrscheinlichkeit von 90 % 
        else:
            if (Strategy.defect == hishist[-1]):
                return Strategy.defect
            else:
                return self.reactProbCooperate(90) # Kooperiere zu einer Wahrscheinlichkeit von 90 % 
                

class Davis(Strategy):
    
    def __init__(self) -> None:
        self.name = "Davis"
        self.cheated = False

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn): # Die ersten Runde
            self.cheated = False
            self.nice = True
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
        self.nice = True

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn): # Die ersten Runde
             return Strategy.cooperate
        else:
            if (hishist[-1] != myhist[-1]): # Wenn in der letzten Runde keine Einigkeit bestand
                return self.reactProbCooperate(28.6) # Kooperiere zu einer Wahrscheinlichkeit von 28.6 %
            else:
                return Strategy.cooperate
            
class Feld(Strategy):

    def __init__(self):
        self.name = "Feld"
        self.nice = False

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn): # Die ersten Runde
             return Strategy.cooperate
        else:
            if (Strategy.cooperate == hishist[-1]): # Wenn in der letzten Runde kooperiert wurde
                return self.reactProbDefect(currentturn/3) # Kooperiere nicht zu einer Wahrscheinlichkeit, die von Runde zu Runde steigt
            else:
                return Strategy.defect # Wenn in der letzten Runde nicht kooperiert wurde, dann kooperiere nicht


class Testfortft(Strategy):

    def __init__(self) -> None:
        self.name = "Tester"
        self.nice = False
        self.opponent_is_retaliating = False
    
    def react(self, currentturn, myhist, hishist):
        if (1 >= currentturn):
            return Strategy.defect # In der ersten zwei Runde wird nicht kooperiert
        elif (2 == currentturn): # In der dritten Runde wird evaluiert, ob der Gegner zurückschlägt
            if (Strategy.defect == hishist[-1]):
                self.opponent_is_retaliating = True
                return Strategy.cooperate
            else:
                self.opponent_is_retaliating = False
                return Strategy.defect
        else: # Ab der dritten Runde wir entweder Tit for Tat gespielt oder der Gegner ausgenommen
            if (self.opponent_is_retaliating == True):
                return hishist[-1] # Mache das Gleiche wie der Gegner in der letzten Runde
            else:
                return Strategy.defect # Wenn der Gegner nicht zurückschlägt, dann kooperiere nicht
        