"""
Dieses Modul definiert die Klasse `Ruleset`, die die Regeln für das
Gefangenendilemma festlegt und die Punktevergabe basierend auf den
Aktionen der Spieler berechnet.

Die Klasse enthält Methoden zur Festlegung der Anzahl der Runden und zur
Bewertung der Punkte basierend auf den Aktionen der Spieler.
"""

import random


class Ruleset:
    """
    Klasse zur Definition der Regeln für das Gefangenendilemma.

    Attribute:
    - defect (bool): Konstante, die Defektion repräsentiert.
    - cooperate (bool): Konstante, die Kooperation repräsentiert.
    - suckers (int): Punkte für den Spieler, der kooperiert, während der
      Gegner defektiert.
    - both_defects (int): Punkte für beide Spieler, wenn beide defektieren.
    - both_cooperates (int): Punkte für beide Spieler, wenn beide kooperieren.
    - temptation (int): Punkte für den Spieler, der defektiert, während der
      Gegner kooperiert.
    - turns_rand (bool): Gibt an, ob die Anzahl der Runden zufällig variiert.
    - turns_base (int): Basisanzahl der Runden.
    - turns (int): Tatsächliche Anzahl der Runden.
    - repetitions (int): Anzahl der Wiederholungen der Simulation.
    """
    defect = False
    cooperate = True

    def __init__(self) -> None:
        self.suckers = 0  # S Auszahlung des Trottels
        self.both_defects = 1  # P bestrafen
        self.both_cooperates = 3  # R belohnen
        self.temptation = 5  # T Auszahlung der Versuchung
        # Verkürzung bzw. Verlängerung der Anzahl der Runden
        self.turns_rand = False
        # Anzahl der Runden die eine Paarung aufeinandertrifft
        self.turns_base = 200
        self.turns = self.set_rounds()
        self.repetitions = 5  # Anzahl der Simulationswiederholungen

    def set_rounds(self):
        """
        Legt die Anzahl der Runden fest.

        Wenn `turns_rand` aktiviert ist, wird die Anzahl der Runden zufällig
        um bis zu ±20 variiert. Andernfalls wird die Basisanzahl der Runden
        verwendet.

        Rückgabewert:
        - int: Die Anzahl der Runden.
        """
        if self.turns_rand:
            return self.turns_base + int((random.random() - 0.5) * 2 * 20)
        return self.turns_base

    def evaluate_points(self, c1behave, c2behave, pointsc1, pointsc2):
        """
        Bewertet die Punkte basierend auf den Aktionen der Spieler.

        Parameter:
        - c1behave (bool): Aktion des ersten Spielers (kooperieren oder
        defektieren).
        - c2behave (bool): Aktion des zweiten Spielers (kooperieren oder
        defektieren).
        - pointsc1 (int): Aktuelle Punkte des ersten Spielers.
        - pointsc2 (int): Aktuelle Punkte des zweiten Spielers.

        Rückgabewert:
        - list[int, int]: Aktualisierte Punkte für beide Spieler.
        """
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
