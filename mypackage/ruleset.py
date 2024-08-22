#

import random

class Ruleset:
    defect = False
    cooperate = True
    
    def __init__(self) -> None:
        self.suckers = 0 # S Auszahlung des Trottels 
        self.both_defects = 1 # P bestrafen
        self.both_cooperates = 3 # R belohnen
        self.temptation = 5 # T Auszahlung der Versuchung
        self.turns_rand = False # Verkürzung bzw. Verlängerung der Anzahl der Runden
        self.turns_base = 200 # Anzahl der Runden die eine Paarung aufeinandertrifft 
        self.turns = self.set_rounds()
        self.repetitions = 5 # Anzahl der Simulationswiederholungen

    def set_rounds(self):
        if self.turns_rand:
            return  self.turns_base + int ((random.random() - 0.5) * 2 * 20)
        else:
            return self.turns_base
        
    def evaluate_points(self, c1behave, c2behave, pointsc1, pointsc2):
        if (self.cooperate == c1behave) and (self.cooperate == c2behave):
            pointsc1 += self.both_cooperates
            pointsc2 += self.both_cooperates
        else: 
            if (self.cooperate == c1behave) and (self.defect == c2behave):
                pointsc1 += self.suckers
                pointsc2 += self.temptation
            else:
                if (self.defect == c1behave) and (self.cooperate == c2behave):
                    pointsc1 += self.temptation
                    pointsc2 += self.suckers
                else:
                    if (self.defect == c1behave) and (self.defect == c2behave):
                        pointsc1 += self.both_defects
                        pointsc2 += self.both_defects
        return [pointsc1, pointsc2]

