"""
Dieses Modul definiert die Basisklasse `Strategy` für Strategien
im Gefangenendilemma.

Die Klasse `Strategy` enthält grundlegende Attribute und Methoden,
die von spezifischen Strategien geerbt und angepasst werden können.
Dazu gehören Methoden zur Reaktion auf Züge des Gegners sowie zur
probabilistischen Entscheidung über Kooperation oder
Defektion.
"""

import random


class Strategy:
    """
    Basisklasse für Strategien im Gefangenendilemma.

    Attribute:
    - defect (bool): Konstante, die Defektion repräsentiert.
    - cooperate (bool): Konstante, die Kooperation repräsentiert.
    - classid (int): Eine eindeutige ID für die Strategie (Standard: 0).
    - nice (bool): Gibt an, ob die Strategie als "nice" gilt (Standard: False).
    - name (str): Der Name der Strategie.
    """
    defect = False
    cooperate = True
    classid = 0  # Muss noch gesetzt werden
    nice = False
    name = ""

    def __init__(self) -> None:
        self.classid = -1

    def react(self, _currentturn, _myhist, _hishist):
        """
        Standardreaktion der Strategie.

        Diese Methode gibt standardmäßig Kooperation zurück und sollte von
        spezifischen Strategien überschrieben werden.

        Parameter:
        - currentturn (int): Die aktuelle Runde der Simulation.
        - myhist (list): Die Historie der eigenen Züge.
        - hishist (list): Die Historie der Züge des Gegners.

        Rückgabewert:
        - bool: Standardmäßig `Strategy.cooperate`.
        """
        return Strategy.cooperate

    def react_prob_cooperate(self, prob):
        """
        Kooperiere mit gegebener Wahrscheinlichkeit.
        """
        if prob > (random.random()*100):
            return self.cooperate
        return self.defect

    def react_prob_defect(self, prob):
        """
        Kooperiere nicht mit gegebener Wahrscheinlichkeit.
        """
        return self.react_prob_cooperate(100-prob)
