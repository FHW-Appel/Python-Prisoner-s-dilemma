from ..basestrategy import Strategy


class FirstCosumStrat(Strategy):

    def __init__(self) -> None:
        self.name = "First Custom Strategy"
        self.nice = True

    def react(self, currentturn, myhist, hishist):
        if (1 > currentturn):
            return Strategy.cooperate
        else:
            return hishist[-2]
