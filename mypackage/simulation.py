
from mypackage.ruleset import Ruleset

class PPDSimulation:

    def __init__(self) -> None:
        __rounds = Ruleset.rounds()
        __candidates = PPDSimulation.initcandidates()

    def runsim():
        for rep in Ruleset.repetitions():
            for candidate1 in PPDSimulation.__candidates:
                for candidate2 in PPDSimulation.__candidates:
                    for rou in PPDSimulation.__rounds:
                        pass
    
    def initcandidates():
        pass


class Strategy:
    defect = False
    cooperate = True

    def __init__(self) -> None:
        pass # Hier muss noch der Name der jeweiligen Strategie definiert werden

    def react(currentrun, myhist, hishist, myscore, hisscore):
        return Strategy.defect