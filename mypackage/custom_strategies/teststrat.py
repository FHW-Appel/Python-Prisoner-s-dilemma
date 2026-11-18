"""
Dieses Modul definiert benutzerdefinierte Strategien für das Gefangenendilemma.
"""

from ..basestrategy import Strategy


class Vertrauen(Strategy):
    """
    Diese Strategie defektiert jede zweite Runde.
    """
    name = "Vertrauen"
    nice = True

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if currentturn == 0:
            return Strategy.cooperate
        return hishist[-1]
    
class Misstrauen(Strategy):
    """
    Diese Strategie defektiert jede zweite Runde.
    """
    name = "Misstrauen"
    nice = False

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        return Strategy.defect


class Verrat(Strategy):
    """
    Diese Strategie defektiert jede zweite Runde.
    """
    name = "Verrat im letzten Moment"
    nice = False

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if currentturn == 0:
            return Strategy.cooperate
        if currentturn < 190:
            return hishist[-1]
        return Strategy.defect


class Gegenteil(Strategy):
    """
    Diese Strategie defektiert jede zweite Runde.
    """
    name = "Gegenteil"
    nice = False

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if currentturn == 0:
            return self.react_prob_cooperate(50)
        return not hishist[-1]


class Naiv(Strategy):
    """
    Diese Strategie defektiert jede zweite Runde.
    """
    name = "Naiv"
    nice = True

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        return Strategy.cooperate
    
class Zufall(Strategy):
    """
    Diese Strategie defektiert jede zweite Runde.
    """
    name = "Zufall"
    nice = False

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        return self.react_prob_cooperate(50)