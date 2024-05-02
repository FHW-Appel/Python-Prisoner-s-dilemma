
from mypackage.ruleset import Ruleset

class PPDSimulation:

    def __init__(self) -> None:
        pass

    def runsim(self):
        rule = Ruleset()
        candidates = self.initcandidates()
        for rep in rule.repetitions():
            for candidate1 in candidates:
                for candidate2 in candidates:
                    for rou in rule.rounds:
                        pass
    
    def initcandidates(self):
        pass


class Strategy:
    defect = False
    cooperate = True

    def __init__(self) -> None:
        pass # Hier muss noch der Name der jeweiligen Strategie definiert werden

    def react(currentrun, myhist, hishist):
        return Strategy.cooperate