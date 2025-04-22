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
        super().__init__()
        self.name = "Tit for Tat"
        self.nice = True

    def react(self, currentturn, _myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:
            return Strategy.cooperate
        return hishist[-1]


class RandomStrat(Strategy):
    """
    Diese Strategie kooperiert oder defektiert zufällig mit einer
    Wahrscheinlichkeit von 50 %.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = "Random"
        self.nice = False

    def react(self, _currentturn, _myhist, _hishist):
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
        super().__init__()
        self.name = "Friedman"
        self.cheated = False
        self.nice = True

    def react(self, currentturn, _myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:
            self.cheated = False
            return Strategy.cooperate
        if self.cheated:
            return Strategy.defect
        if Strategy.defect == hishist[-1]:
            self.cheated = True
            return Strategy.defect
        return Strategy.cooperate


class Joss(Strategy):
    """
    Diese Strategie kooperiert mit einer Wahrscheinlichkeit von 90 %,
    außer der Gegner defektiert, dann wird auf defektiert.
    """
    def __init__(self) -> None:
        super().__init__()
        self.name = "Joss"
        self.nice = False

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


class Davis(Strategy):
    """
    Diese Strategie kooperiert in den ersten 10 Runden und spielt danach
    Friedman. Sie kann nicht verzeihen.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = "Davis"
        self.cheated = False

    def react(self, currentturn, _myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:  # Die ersten Runde
            self.cheated = False
            self.nice = True
        if 9 >= currentturn:  # Die ersten 10 Runden
            # Die ersten 10 Runden wird immer kooperiert
            return Strategy.cooperate
        # Ab der 11 Runde
        # Wurde diese Strategie in der letzten Runde betrogen?
        if Strategy.defect == hishist[-1]:
            self.cheated = True  # Merke Dir, dass du betrogen wurdest
        if self.cheated:  # Wurdest du schon mal betrogen?
            return Strategy.defect
        return Strategy.cooperate


class Grofman(Strategy):
    """
    Diese Strategie kooperiert in der ersten Runde. In den folgenden Runden
    kooperiert sie, wenn in der letzten Runde Einigkeit bestand (beide Spieler
    haben dasselbe gewählt). Wenn keine Einigkeit bestand, kooperiert sie mit
    einer Wahrscheinlichkeit von 28,6 %.
    """

    def __init__(self):
        super().__init__()
        self.name = "Grofman"
        self.nice = True

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:  # Die ersten Runde
            return Strategy.cooperate
        # Wenn in der letzten Runde keine Einigkeit bestand
        if hishist[-1] != myhist[-1]:
            # Kooperiere zu einer Wahrscheinlichkeit von 28.6 %
            return self.react_prob_cooperate(28.6)
        return Strategy.cooperate


class Feld(Strategy):
    """
    Diese Strategie kooperiert in der ersten Runde. In den folgenden Runden
    kooperiert sie, wenn der Gegner in der letzten Runde kooperiert hat.
    Wenn der Gegner nicht kooperiert hat, steigt die Wahrscheinlichkeit
    für Defektion mit jeder Runde.
    """

    def __init__(self):
        super().__init__()
        self.name = "Feld"
        self.nice = False

    def react(self, currentturn, _myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if 0 == currentturn:  # Die ersten Runde
            return Strategy.cooperate
        # Wenn in der letzten Runde kooperiert wurde
        if Strategy.cooperate == hishist[-1]:
            # Kooperiere nicht zu einer Wahrscheinlichkeit,
            # die von Runde zu Runde steigt
            return self.react_prob_defect(currentturn/3)
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
        super().__init__()
        self.name = "Tester"
        self.nice = False
        self.opponent_is_retaliating = False

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


class Grasskamp(Strategy):
    """
    Diese Strategie spielt weitensgehend Tit for Tat. Versucht jedoch herauszufinden,
    ob die gegnerische Strategie zufällig reagiert, um dann nur noch zu defekten.

    Verhalten
    - Dies Strategie spielt für die ersten 50 Runden Tit for Tat.
    - In Runde 51 wird defected.
    - Runde 52 bis 56 Tit for Tat
    - Es wird eine Überprüfung erstellt, die herausfinden möchte,
      ob der Gegner zufällig reagiert. Wenn dem so ist, dann wird immer defect.
    - Ein weiterer Test überprüft ob die andere Strategie Tit for Tat spielt,
      dann wird nurnoch Tit for Tat gespielt.
    - Wenn die andere Strategie nicht Tit for Tat spielt,
      dann wird alle 5 bis 15 Züge zufällig defect.
    """

    def __init__(self):
        super().__init__()
        self.name = "Grasskamp"
        self.nice = False
        self.opponent_is_retaliating = False
        self.opponent_playing_random = False
        self.counter_subturn = 0

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        def case_first_round():
            self.opponent_is_retaliating = False
            self.opponent_playing_random = False
            self.counter_subturn = 0
            return Strategy.cooperate

        def case_tit_for_tat():
            return hishist[-1]

        def case_defect():
            return Strategy.defect

        def case_check_opponent():
            self.check_if_retaliating(currentturn, myhist, hishist)
            self.check_if_random(currentturn, hishist)
            if self.opponent_playing_random:
                return Strategy.defect
            return Strategy.cooperate

        def case_late_game():
            if self.opponent_is_retaliating:
                return hishist[-1]
            if self.opponent_playing_random:
                return Strategy.defect
            self.counter_subturn += 1
            if 5 <= self.counter_subturn:
                if self.react_prob_defect(10):
                    return Strategy.cooperate
                else:
                    self.counter_subturn = 0
                    return Strategy.defect
            return Strategy.cooperate

        # Switch-case-ähnliche Struktur
        switch = {
            currentturn < 1: case_first_round,
            currentturn < 50: case_tit_for_tat,
            currentturn < 51: case_defect,
            currentturn < 56: case_tit_for_tat,
            currentturn < 57: case_check_opponent,
            currentturn >= 58: case_late_game,
        }

        # Führe die passende Funktion aus
        for condition, action in switch.items():
            if condition:
                return action()

        # Standardrückgabewert
        return Strategy.cooperate

    def check_if_retaliating(self, currentturn, myhist, hishist):
        """
        Diese Methode überprüft, ob der Gegner vergeltet.
        """
        if currentturn < 11:
            # Nicht genug Daten, um eine Aussage zu treffen
            self.opponent_is_retaliating = False
            return

        # Überprüfen, ob der Gegner vergeltet (Tit for Tat Verhalten)
        # basierend auf den letzten 10 Zügen
        retaliation_count = 0
        for i in range(1, 11):  # Überprüfe die letzten 10 Züge
            if myhist[-(i+1)] == hishist[-i]:
                retaliation_count += 1

        # Mehrheitsentscheidung: Wenn mehr als die Hälfte der letzten 
        # 10 Züge Vergeltung war
        self.opponent_is_retaliating = retaliation_count > 5

    def check_if_random(self, currentturn, hishist):
        """
        Diese Methode überprüft, ob der Gegner zufällig reagiert.
        """
        if currentturn < 6:
            # Nicht genug Daten, um eine Aussage zu treffen
            self.opponent_playing_random = False
            return

        # Berechne die Kooperationsrate
        cooperation_rate = (sum(hishist) / len(hishist)) * 100
        # Zwischen 30% und 70% nehme ein zufälliges verhalten an.
        if 30 <= cooperation_rate <= 70:
            self.opponent_playing_random = True
        else:
            self.opponent_playing_random = False
