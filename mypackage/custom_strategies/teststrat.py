"""
Dieses Modul definiert benutzerdefinierte Strategien für das Gefangenendilemma.
"""

from ..basestrategy import Strategy


class FirstCosumStrat(Strategy):
    """
    Diese Strategie kooperiert in der ersten Runde und verwendet
    den Zug des Gegners aus der vorletzten Runde für die Entscheidung
    in den folgenden Runden.
    """

    def __init__(self) -> None:
        self.name = "First Custom Strategy"
        self.nice = True

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 1 > currentturn:
            return Strategy.cooperate
        return hishist[-2]
