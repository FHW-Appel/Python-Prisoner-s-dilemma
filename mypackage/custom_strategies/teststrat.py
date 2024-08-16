from ..basestrategy import Strategy


class FirstCosumStrat(Strategy):

    def __init__(self) -> None:
        self.name = "First Custom Strategy"

    def react(self, currentturn, myhist, hishist):
        print(currentturn)
        if (1 > currentturn):
            return Strategy.cooperate
        else:
            return hishist[currentturn-2]    
