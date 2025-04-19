#

from ..basestrategy import Strategy


class TitForTat(Strategy):

    def __init__(self) -> None:
        self.name = "Tit for Tat"
        self.nice = True

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn):
            return Strategy.cooperate
        else:
            return hishist[-1]


class RandomStrat(Strategy):

    def __init__(self) -> None:
        self.name = "Random"
        self.nice = False

    def react(self, currentturn, myhist, hishist):
        # Kooperiere zu einer Wahrscheinlichkeit von 50 %
        return self.reactProbCooperate(50)


class Friedman(Strategy):

    def __init__(self) -> None:
        self.name = "Friedman"
        self.cheated = False
        self.nice = True

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn):
            self.cheated = False
            return Strategy.cooperate
        else:
            if (Strategy.defect == hishist[-1]):
                self.cheated = True
            if self.cheated:
                return Strategy.defect
            else:
                return Strategy.cooperate


class Joss(Strategy):

    def __init__(self) -> None:
        self.name = "Joss"
        self.nice = False

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn):
            # Kooperiere zu einer Wahrscheinlichkeit von 90 %
            return self.reactProbCooperate(90)
        else:
            if (Strategy.defect == hishist[-1]):
                return Strategy.defect
            else:
                # Kooperiere zu einer Wahrscheinlichkeit von 90 %
                return self.reactProbCooperate(90)


class Davis(Strategy):

    def __init__(self) -> None:
        self.name = "Davis"
        self.cheated = False

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn):  # Die ersten Runde
            self.cheated = False
            self.nice = True
        if (9 >= currentturn):  # Die ersten 10 Runden
            # Die ersten 10 Runden wird immer kooperiert
            return Strategy.cooperate
        else:  # Ab der 11 Runde
            # Wurde diese Strategie in der letzten Runde betrogen?
            if (Strategy.defect == hishist[-1]):
                self.cheated = True  # Merke Dir, dass du betrogen wurdest
            if self.cheated:  # Wurdest du schon mal betrogen?
                return Strategy.defect
            else:
                return Strategy.cooperate


class Grofman(Strategy):

    def __init__(self):
        self.name = "Grofman"
        self.nice = True

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn):  # Die ersten Runde
            return Strategy.cooperate
        else:
            # Wenn in der letzten Runde keine Einigkeit bestand
            if (hishist[-1] != myhist[-1]):
                # Kooperiere zu einer Wahrscheinlichkeit von 28.6 %
                return self.reactProbCooperate(28.6)
            else:
                return Strategy.cooperate


class Feld(Strategy):

    def __init__(self):
        self.name = "Feld"
        self.nice = False

    def react(self, currentturn, myhist, hishist):
        if (0 == currentturn):  # Die ersten Runde
            return Strategy.cooperate
        else:
            # Wenn in der letzten Runde kooperiert wurde
            if (Strategy.cooperate == hishist[-1]):
                # Kooperiere nicht zu einer Wahrscheinlichkeit,
                # die von Runde zu Runde steigt
                return self.reactProbDefect(currentturn/3)
            else:
                # Wenn in der letzten Runde nicht kooperiert wurde,
                # dann kooperiere nicht
                return Strategy.defect


class Testfortft(Strategy):

    def __init__(self) -> None:
        self.name = "Tester"
        self.nice = False
        self.opponent_is_retaliating = False

    def react(self, currentturn, myhist, hishist):
        if (1 >= currentturn):
            # In der ersten zwei Runde wird nicht kooperiert
            return Strategy.defect
        # In der dritten Runde wird evaluiert, ob der Gegner zurückschlägt
        elif (2 == currentturn):
            if (Strategy.defect == hishist[-1]):
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
