#

import random

class Ruleset:

    def __init__(self) -> None:
        self.suckers = 0 # S Auszahlung des Trottels 
        self.both_defects = 1 # P bestrafen
        self.both_cooperates = 3 # R belohnen
        self.temptation = 5 # T Auszahlung der Versuchung
        self.turns_rand = False # Verkürzung bzw. Verlängerung der Anzahl der Runden
        self.turns_base = 5 # Anzahl der Runden die eine Paarung aufeinandertrifft 
        self.turns = self.set_rounds()
        self.repetitions = 5 # Anzahl der Simulationswiederholungen

    def set_rounds(self):
        if self.turns_rand:
            return  self.turns_base + int ((random.random() - 0.5) * 2 * 20)
        else:
            return self.turns_base
