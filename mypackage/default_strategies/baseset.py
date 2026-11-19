"""
Dieses Modul definiert einen Basissatz an Strategien, 
der zusammen mit den Strategien verwendet werden sollte, 
die von den Teilnehmenden dieses Kurses erstellt wurde.

Die Strategien erben von der Basisklasse `Strategy` und implementieren
unterschiedliche Verhaltensweisen, die im Gefangenendilemma angewendet
werden können.
"""

from ..basestrategy import Strategy

class RandomStratSkeptical(Strategy):
    """
    Diese Strategie kooperiert zufällig mit einer
    Wahrscheinlichkeit von 25 %.
    """
    name = "Random Skeptical"
    nice = False

    def react(self, _currentturn, _myhist, _hishist):
        """
        Reaktion der Strategie.
        """
        # Kooperiere zu einer Wahrscheinlichkeit von 25 %
        return self.react_prob_cooperate(25)

class RandomStrat(Strategy):
    """
    Diese Strategie kooperiert oder defektiert zufällig mit einer
    Wahrscheinlichkeit von 50 %.
    """
    name = "Random"
    nice = False

    def react(self, _currentturn, _myhist, _hishist):
        """
        Reaktion der Strategie.
        """
        # Kooperiere zu einer Wahrscheinlichkeit von 50 %
        return self.react_prob_cooperate(50)


class RandomStratIngoodfaith(Strategy):
    """
    Diese Strategie kooperiert zufällig mit einer 
    Wahrscheinlichkeit von 75 %.
    """
    name = "Random Gutgläubig"
    nice = False

    def react(self, _currentturn, _myhist, _hishist):
        """
        Reaktion der Strategie.
        """
        # Kooperiere zu einer Wahrscheinlichkeit von 75 %
        return self.react_prob_cooperate(75)


class Friedman(Strategy):
    """
    Diese Strategie kooperiert, bis der Gegner defektiert. Danach defektiert
    sie dauerhaft. Diese Strategie kann nicht verzeihen.
    """
    name = "Friedman (Groll)"
    nice = True

    def react(self, currentturn, _myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        return self.react_grudge(currentturn, _myhist, hishist)


class Friedman2(Strategy):
    """
    Diese Strategie kooperiert, bis der Gegner defektiert. Danach defektiert
    sie dauerhaft. Diese Strategie kann nicht verzeihen.
    """
    name = "Friedman 2 (Groll)"
    nice = True

    def react(self, currentturn, _myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        return self.react_grudge(currentturn, _myhist, hishist)


class Joss(Strategy):
    """
    Diese Strategie kooperiert mit einer Wahrscheinlichkeit von 90 %,
    außer der Gegner defektiert, dann wird auch defektiert.
    """
    name = "Joss"
    nice = False

    def react(self, currentturn, _myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:
            # Kooperiere zu einer Wahrscheinlichkeit von 90 %
            return self.react_prob_cooperate(90)
        if Strategy.defect == hishist[-1]:
            return Strategy.defect
        # Kooperiere zu einer Wahrscheinlichkeit von 90 %
        return self.react_prob_cooperate(90)


class Joss2(Strategy):
    """
    Diese Strategie kooperiert mit einer Wahrscheinlichkeit von 90 %,
    außer der Gegner defektiert, dann wird auch defektiert.
    """
    name = "Joss 2"
    nice = False

    def react(self, currentturn, _myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:
            # Kooperiere zu einer Wahrscheinlichkeit von 90 %
            return self.react_prob_cooperate(90)
        if Strategy.defect == hishist[-1]:
            return Strategy.defect
        # Kooperiere zu einer Wahrscheinlichkeit von 90 %
        return self.react_prob_cooperate(90)


class Forrest(Strategy):
    """
    Diese Strategie kooperiert immer.
    """
    name = "Forrest Gump (Always Cooperate)"
    nice = True

    def react(self, _currentturn, _myhist, _hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        return Strategy.cooperate


class Forrest2(Strategy):
    """
    Diese Strategie kooperiert immer.
    """
    name = "Forrest Gump 2 (Always Cooperate)"
    nice = True

    def react(self, _currentturn, _myhist, _hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        return Strategy.cooperate


class Gekko(Strategy):
    """
    Diese Strategie defektiert immer.
    """
    name = "Gordon Gekko (Always Defect)"
    nice = False

    def react(self, _currentturn, _myhist, _hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        return Strategy.defect


class Gekko2(Strategy):
    """
    Diese Strategie defektiert immer.
    """
    name = "Gordon Gekko 2(Always Defect)"
    nice = False

    def react(self, _currentturn, _myhist, _hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        return Strategy.defect