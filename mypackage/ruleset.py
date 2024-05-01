#

import random

class Ruleset:
    __suckers = 0 # S Auszahlung des Trottels 
    __both_defects = 1 # P bestrafen
    __both_cooperates = 3 # R belohnen
    __temptation = 5 # T Auszahlung der Versuchung
    __rounds = 200 # Anzahl der Runden die eine Paarung aufeinandertrifft
    __roundsrand = True # Verkürzung bzw. Verlängerung der Anzahl der Runden
    __repetitions = 5 # Anzahl der Simulationswiederholungen

    def s():
        return Ruleset.__suckers
    
    def p():
        return Ruleset.__both_defects
    
    def r():
        return Ruleset.__suckers
    
    def t():
        return Ruleset.__temptation
    
    def rounds():
        if Ruleset.__roundsrand:
            return Ruleset.__rounds + int ((random.random() - 0.5) * 2 * 20)
        else:
            return Ruleset.__rounds
    
    def repetitions():
        return Ruleset.__repetitions
    
        

    
