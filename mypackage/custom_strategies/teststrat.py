"""
Dieses Modul definiert benutzerdefinierte Strategien für das Gefangenendilemma.
"""

from ..basestrategy import Strategy


class CooperateEverySecondRound(Strategy):
    """
    Diese Strategie defektiert jede zweite Runde.
    """
    name = "Alternate"
    nice = False

    def react(self, currentturn, _myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if currentturn % 2 == 0:
            return Strategy.cooperate
        return Strategy.defect
