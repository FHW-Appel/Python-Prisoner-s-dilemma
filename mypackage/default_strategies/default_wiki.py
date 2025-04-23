"""
Dieses Modul definiert die standard Strategien für das Gefangenendilemma
aus dem deutschen Wiki.
https://de.wikipedia.org/wiki/Gefangenendilemma
"""

from ..basestrategy import Strategy


class Axelrod(Strategy):
    """
    Diese Strategie kooperiert in der ersten Runde und kopiert anschließend
    den letzten Zug des Gegners.
    """
    name = "Axelrod (Tit for Tat)"
    nice = True

    def react(self, currentturn, _myhist, hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        if 0 == currentturn:
            return Strategy.cooperate
        return hishist[-1]


class Snape(Strategy):
    """
    Verrät in der ersten Runde und kopiert in den nächsten Runden
    (wie Tit for Tat) den vorherigen Spielzug des Spielpartners.
    Ist nicht von sich aus kooperationswillig.
    """
    name = "Severus Snape (Misstrauen)"
    nice = False

    def react(self, currentturn, _myhist, hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        if 0 == currentturn:
            return Strategy.defect
        return hishist[-1]


class Corleone(Strategy):
    """
    Diese Strategie kooperiert, bis der Gegner defektiert. Danach defektiert
    sie dauerhaft. Diese Strategie kann nicht verzeihen.
    """
    name = "Michael Corleone (Groll)"
    cheated = False
    nice = True

    def react(self, currentturn, _myhist, hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        if 0 == currentturn:
            self.cheated = False
            return Strategy.cooperate
        if self.cheated:
            return Strategy.defect
        if Strategy.defect == hishist[-1]:
            self.cheated = True
            return Strategy.defect
        return Strategy.cooperate


class Batman(Strategy):
    """
    Kooperiert bis zur ersten Abweichung. Dann ist er so lange feindlich,
    bis der Gewinn des Mitspielers aus seinem Abweichen aufgebraucht wurde.
    Dann kooperiert er wieder bis zum nächsten Abweichen von der kooperativen
    Lösung. Diese Strategie ist optimal bei kooperationswilligen Spielern,
    die Fehler begehen, also irrtümlich einen konfrontativen Zug machen.
    """
    name = "Batman (Bestrafer)"
    nice = True
    profit_of_opponent = 0

    def react(self, currentturn, myhist, hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        # In der ersten Runde kooperiert er immer.
        if 0 == currentturn:
            self.profit_of_opponent = 0
            return Strategy.cooperate
        # Wenn der Gegner defektiert, wird ebenfalls defektiert.
        if Strategy.defect == hishist[-1]:
            if Strategy.cooperate == myhist[-1]:
                self.profit_of_opponent += 5
            else:
                self.profit_of_opponent += 1
            return Strategy.defect
        # Wenn der Gegner wieder kooperiert, wird überprüft, ob der Gewinn des
        # Gegners aufgebraucht wurde. Wenn ja, kooperiert er wieder.
        # Ansonsten wird defektiert.
        if Strategy.cooperate == hishist[-1] and Strategy.defect == myhist[-1]:
            self.profit_of_opponent -= 3
            if self.profit_of_opponent <= 0:
                return Strategy.cooperate
            return Strategy.defect
        # Wenn der Gegner kooperiert und der Gewinn des Gegners
        # aufgebraucht ist, kooperiert er wieder.
        return Strategy.cooperate


class Pavlov(Strategy):
    """
    Diese Strategie kooperiert in der ersten Runde. Die Strategie
    verrät, falls der Gegner in der letzten Runde sich anders verhalten hat
    als sie selbst. Ansonsten kooperiert sie.
     Dies führt zu einem Wechsel des Verhaltens, wenn der Gewinn der Vorrunde
     klein war, aber zum Beibehalten des Verhaltens, wenn der Gewinn groß war.
    """
    name = "Iwan Pawlow (Win-Stay, Lose-Shift)"
    nice = True

    def react(self, currentturn, myhist, hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        if 0 == currentturn:
            return Strategy.cooperate
        if myhist[-1] == hishist[-1]:
            return Strategy.cooperate
        return Strategy.defect


class White(Strategy):
    """
    Kooperiert so lange, bis der Gegner defektiert. Dann wird in der nächsten Runde
    defektiert. Danach wird in den nächsten zwei Runde zweimal kooperiert,
    wenn der Gegner wieder defektiert, wird zweimal defektiert und anschließend
    wieder zweimal kooperiert und so weiter. Die Strategie ist also
    kooperationswillig, aber erhöht die Strafe, wenn der Gegner nicht kooperiert.
    """
    name = "Walter White (Gradual)"
    nice = True
    opponent_defect_count = 0
    retailiating_count = 0

    def react(self, currentturn, myhist, hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        # Verhalten in der ersten Runde:
        if 0 == currentturn:
            self.opponent_defect_count = 0
            return Strategy.cooperate
        # Zurückschlagen:
        if self.retailiating_count < self.opponent_defect_count:
            self.retailiating_count += 1
            return Strategy.defect
        # Versöhnung:
        if 1 < currentturn: # erst ab Runde 3 
            retailiating_end = self.retailiating_count == self.opponent_defect_count
            time_to_reconcile = myhist[-1] == Strategy.defect or myhist[-2] == Strategy.defect
            if retailiating_end and time_to_reconcile:
                return Strategy.cooperate
        # Verhalten, wenn der Gegner defektiert:
        if Strategy.defect == hishist[-1]:
            self.opponent_defect_count += 1
            self.retailiating_count = 1
            return Strategy.defect
        # Verhalten, wenn der Gegner kooperiert
        # und nicht zurückgeschlagen wird:
        return Strategy.cooperate


class Alfred(Strategy):
    """
    Diese Strategie kooperiert in der ersten Runde. Danach wird zweimal
    defektiert.
    Es wird weiterhin defektiert, wenn der in den Runden 2 und 3 der Gegner
    kooperiert hat.
    Wenn der Gegner in den Runden 2 und 3 einmal defektiert hat, wird
    in anschließend Tit for Tat gespielt.
    """
    name = "Ekel Alfred (Sondierer)"
    nice = False

    def react(self, currentturn, myhist, hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        # Verhalten in der ersten Runde:
        if 0 == currentturn:
            return Strategy.cooperate
        # Verhalten in Runde zwei und drei:
        if 2 >= currentturn:
            return Strategy.defect
        # Verhalten ab Runde vier:
        if hishist[-1] == Strategy.cooperate and hishist[-2] == Strategy.cooperate:
            # Wenn der Gegner in den Runden 2 und 3 kooperiert hat, wird defektiert.
            # Der Gegner wird ausgenommen
            return Strategy.defect
        return hishist[-1]  # Ansonsten wird das Verhalten des Gegners kopiert.


class Gekko(Strategy):
    """
    Diese Strategie defektiert immer.
    """
    name = "Gordon Gekko (Always Defect)"
    nice = False

    def react(self, _currentturn, _myhist, _hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        return Strategy.defect


class Forrest(Strategy):
    """
    Diese Strategie kooperiert immer.
    """
    name = "Forrest Gump (Always Cooperate)"
    nice = True

    def react(self, _currentturn, _myhist, _hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        return Strategy.cooperate


class Homer(Strategy):
    """
    Diese Strategie kooperiert oder defektiert zufällig mit einer
    Wahrscheinlichkeit von 50 %.
    """
    name = "Homer Simpson (Random)"
    nice = False

    def react(self, _currentturn, _myhist, _hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        # Kooperiere zu einer Wahrscheinlichkeit von 50 %
        return self.react_prob_cooperate(50)


class Jerry(Strategy):
    """
    Diese Strategie spielt die Folge kooperieren, kooperieren, defektieren.
    """
    name = "Jerry (Coop, Coop, Defekt)"
    nice = False

    def react(self, currentturn, _myhist, _hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        if 2 == currentturn % 3:
            return Strategy.defect
        return Strategy.cooperate


class Tom(Strategy):
    """
    Diese Strategie spielt die Folge kooperieren, kooperieren, defektieren.
    """
    name = "Tom (Defekt, Defekt, Coop)"
    nice = False

    def react(self, currentturn, _myhist, _hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        if 2 == currentturn % 3:
            return Strategy.cooperate
        return Strategy.defect


class Smee(Strategy):
    """
    Diese Strategie kooperiert, wenn die Mehrheit der Züge des Gegners
    kooperiert hat.
    """
    name = "Smee (Mehrheit)"
    nice = True

    def react(self, _currentturn, _myhist, hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        if len(hishist) == 0:
            return Strategy.cooperate
        num_of_coops = hishist.count(Strategy.cooperate)
        opponent_mostly_coop = num_of_coops >= len(hishist) / 2
        if opponent_mostly_coop:
            return Strategy.cooperate
        return Strategy.defect


class Flanders(Strategy):
    """
    Diese Strategie kooperiert in der ersten Runde defetektiert nur, wenn der
    Gegner in der letzten Runde defektiert hat und in der Runde davor
    ebenfalls defektiert hat.
    """
    name = "Ned Flanders (Tit for Two Tat)"
    nice = True

    def react(self, currentturn, _myhist, hishist):
        """Reaktion der Strategie basierend auf der aktuellen Runde."""
        if 1 >= currentturn:
            return Strategy.cooperate
        if Strategy.defect == hishist[-1] and Strategy.defect == hishist[-2]:
            return Strategy.defect
        return Strategy.cooperate
