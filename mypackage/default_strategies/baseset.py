"""
Dieses Modul definiert einen Basissatz an Strategien, 
der zusammen mit den Strategien verwendet werden sollte, 
die von den Teilnehmenden dieses Kurses erstellt wurde.

Die Strategien erben von der Basisklasse `Strategy` und implementieren
unterschiedliche Verhaltensweisen, die im Gefangenendilemma angewendet
werden können.
"""

from ..basestrategy import Strategy

# class RandomStratSkeptical(Strategy):
#     """
#     Diese Strategie kooperiert zufällig mit einer
#     Wahrscheinlichkeit von 25 %.
#     """
#     name = "Random Skeptical"
#     nice = False

#     def react(self, _currentturn, _myhist, _hishist):
#         """
#         Reaktion der Strategie.
#         """
#         # Kooperiere zu einer Wahrscheinlichkeit von 25 %
#         return self.react_prob_cooperate(25)

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


# class RandomStratIngoodfaith(Strategy):
#     """
#     Diese Strategie kooperiert zufällig mit einer 
#     Wahrscheinlichkeit von 75 %.
#     """
#     name = "Random Gutgläubig"
#     nice = False

#     def react(self, _currentturn, _myhist, _hishist):
#         """
#         Reaktion der Strategie.
#         """
#         # Kooperiere zu einer Wahrscheinlichkeit von 75 %
#         return self.react_prob_cooperate(75)


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




# class Forrest2(Strategy):
#     """
#     Diese Strategie kooperiert immer.
#     """
#     name = "Forrest Gump 2 (Always Cooperate)"
#     nice = True

#     def react(self, _currentturn, _myhist, _hishist):
#         """Reaktion der Strategie basierend auf der aktuellen Runde."""
#         return Strategy.cooperate


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


class Testfortft2(Strategy):
    """
    Diese Strategie testet, ob der Gegner auf Defektion
    reagiert (zurückschlägt), und passt ihr Verhalten entsprechend an.

    Verhalten:
    - In den ersten zwei Runden wird immer defektiert.
    - In der dritten Runde wird evaluiert, ob der Gegner zurückschlägt:
      - Wenn der Gegner zurückschlägt, wird Tit-for-Tat gespielt.
      - Wenn der Gegner nicht zurückschlägt, wird dauerhaft defektiert.
   """
    name = "Tester TfT"
    nice = False
    opponent_is_retaliating = False

    def react(self, currentturn, _myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 1 >= currentturn:
            # In der ersten zwei Runde wird nicht kooperiert
            return Strategy.defect
        # In der dritten Runde wird evaluiert, ob der Gegner zurückschlägt
        if 2 == currentturn:
            if Strategy.defect == hishist[-1]:
                self.opponent_is_retaliating = True
                return Strategy.cooperate
            self.opponent_is_retaliating = False
            return Strategy.defect
        # Ab der dritten Runde wird entweder Tit for Tat gespielt
        # oder der Gegner ausgenommen
        if self.opponent_is_retaliating:
            # Mache das Gleiche wie der Gegner in der letzten Runde
            return hishist[-1]
        # Wenn der Gegner nicht zurückschlägt, dann kooperiere nicht
        return Strategy.defect


# class tit_for_tat(Strategy):
#     """
#     Diese Strategie in diesen Zeilen beschreiben
#     """
#     name = "Tit-for-Tat"
#     nice = True

#     def react(self, currentturn, myhist, hishist):
#         """
#         Reaktion der Strategie basierend auf der aktuellen Runde.
#         """
#         if currentturn == 0:
#             return self.cooperate
#         else:
#             return hishist[-1]
