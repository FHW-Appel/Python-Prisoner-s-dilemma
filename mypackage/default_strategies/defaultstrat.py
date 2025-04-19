"""
Dieses Modul definiert Standardstrategien für das Gefangenendilemma.

Die Strategien erben von der Basisklasse `Strategy` und implementieren
unterschiedliche Verhaltensweisen, die im Gefangenendilemma angewendet
werden können.
"""

from ..basestrategy import Strategy


class TitForTat(Strategy):
    """
    Diese Strategie kooperiert in der ersten Runde und kopiert anschließend
    den letzten Zug des Gegners.
    """

    def __init__(self) -> None:
        self.name = "Tit for Tat"
        self.nice = True

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:
            return Strategy.cooperate
        else:
            return hishist[-1]


class RandomStrat(Strategy):
    """
    Diese Strategie kooperiert oder defektiert zufällig mit einer
    Wahrscheinlichkeit von 50 %.
    """

    def __init__(self) -> None:
        self.name = "Random"
        self.nice = False

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        # Kooperiere zu einer Wahrscheinlichkeit von 50 %
        return self.react_prob_cooperate(50)


class Friedman(Strategy):
    """
    Diese Strategie kooperiert, bis der Gegner defektiert. Danach defektiert
    sie dauerhaft. Diese Strategie kann nicht verzeihen.
    """

    def __init__(self) -> None:
        self.name = "Friedman"
        self.cheated = False
        self.nice = True

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:
            self.cheated = False
            return Strategy.cooperate
        else:
            if Strategy.defect == hishist[-1]:
                self.cheated = True
            if self.cheated:
                return Strategy.defect
            else:
                return Strategy.cooperate


class Joss(Strategy):
    """
    Diese Strategie kooperiert mit einer Wahrscheinlichkeit von 90 %,
    außer der Gegner defektiert, dann wird auf defektiert.
    """
    def __init__(self) -> None:
        self.name = "Joss"
        self.nice = False

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:
            # Kooperiere zu einer Wahrscheinlichkeit von 90 %
            return self.react_prob_cooperate(90)
        else:
            if Strategy.defect == hishist[-1]:
                return Strategy.defect
            else:
                # Kooperiere zu einer Wahrscheinlichkeit von 90 %
                return self.react_prob_cooperate(90)


class Davis(Strategy):
    """
    Diese Strategie kooperiert in den ersten 10 Runden und spielt danach
    Tit-for-Tat.
    """

    def __init__(self) -> None:
        self.name = "Davis"
        self.cheated = False

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:  # Die ersten Runde
            self.cheated = False
            self.nice = True
        if 9 >= currentturn:  # Die ersten 10 Runden
            # Die ersten 10 Runden wird immer kooperiert
            return Strategy.cooperate
        else:  # Ab der 11 Runde
            # Wurde diese Strategie in der letzten Runde betrogen?
            if Strategy.defect == hishist[-1]:
                self.cheated = True  # Merke Dir, dass du betrogen wurdest
            if self.cheated:  # Wurdest du schon mal betrogen?
                return Strategy.defect
            else:
                return Strategy.cooperate


class Grofman(Strategy):
    """
    Diese Strategie kooperiert in der ersten Runde. In den folgenden Runden
    kooperiert sie, wenn in der letzten Runde Einigkeit bestand (beide Spieler
    haben dasselbe gewählt). Wenn keine Einigkeit bestand, kooperiert sie mit
    einer Wahrscheinlichkeit von 28,6 %.
    """

    def __init__(self):
        self.name = "Grofman"
        self.nice = True

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:  # Die ersten Runde
            return Strategy.cooperate
        else:
            # Wenn in der letzten Runde keine Einigkeit bestand
            if hishist[-1] != myhist[-1]:
                # Kooperiere zu einer Wahrscheinlichkeit von 28.6 %
                return self.react_prob_cooperate(28.6)
            else:
                return Strategy.cooperate


class Feld(Strategy):
    """
    Diese Strategie kooperiert in der ersten Runde. In den folgenden Runden
    kooperiert sie, wenn der Gegner in der letzten Runde kooperiert hat.
    Wenn der Gegner nicht kooperiert hat, steigt die Wahrscheinlichkeit
    für Defektion mit jeder Runde.
    """

    def __init__(self):
        self.name = "Feld"
        self.nice = False

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:  # Die ersten Runde
            return Strategy.cooperate
        else:
            # Wenn in der letzten Runde kooperiert wurde
            if Strategy.cooperate == hishist[-1]:
                # Kooperiere nicht zu einer Wahrscheinlichkeit,
                # die von Runde zu Runde steigt
                return self.react_prob_defect(currentturn/3)
            else:
                # Wenn in der letzten Runde nicht kooperiert wurde,
                # dann kooperiere nicht
                return Strategy.defect


class Testfortft(Strategy):
    """
    Diese Strategie testet, ob der Gegner auf Defektion
    reagiert (zurückschlägt), und passt ihr Verhalten entsprechend an.

    Verhalten:
    - In den ersten zwei Runden wird immer defektiert.
    - In der dritten Runde wird evaluiert, ob der Gegner zurückschlägt:
      - Wenn der Gegner zurückschlägt, wird Tit-for-Tat gespielt.
      - Wenn der Gegner nicht zurückschlägt, wird dauerhaft defektiert.
   """

    def __init__(self) -> None:
        self.name = "Tester"
        self.nice = False
        self.opponent_is_retaliating = False

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 1 >= currentturn:
            # In der ersten zwei Runde wird nicht kooperiert
            return Strategy.defect
        # In der dritten Runde wird evaluiert, ob der Gegner zurückschlägt
        elif 2 == currentturn:
            if Strategy.defect == hishist[-1]:
                self.opponent_is_retaliating = True
                return Strategy.cooperate
            else:
                self.opponent_is_retaliating = False
                return Strategy.defect
        else:  # Ab der dritten Runde wird entweder Tit for Tat gespielt
            # oder der Gegner ausgenommen
            if self.opponent_is_retaliating:
                # Mache das Gleiche wie der Gegner in der letzten Runde
                return hishist[-1]
            else:
                # Wenn der Gegner nicht zurückschlägt, dann kooperiere nicht
                return Strategy.defect
