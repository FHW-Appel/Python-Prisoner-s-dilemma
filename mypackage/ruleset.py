#

import random

class Ruleset:

    def __init__(self) -> None:
        self.suckers = 0 # S Auszahlung des Trottels 
        self.both_defects = 1 # P bestrafen
        self.both_cooperates = 3 # R belohnen
        self.temptation = 5 # T Auszahlung der Versuchung
        self.roundsrand = False # Verkürzung bzw. Verlängerung der Anzahl der Runden
        self.roundsbase = 5 # Anzahl der Runden die eine Paarung aufeinandertrifft 
        self.rounds = self.setrounds()
        self.repetitions = 5 # Anzahl der Simulationswiederholungen

    def setrounds(self):
        if self.roundsrand:
            return  self.roundsbase + int ((random.random() - 0.5) * 2 * 20)
        else:
            return self.roundsbase
