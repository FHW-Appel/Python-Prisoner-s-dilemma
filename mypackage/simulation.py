
from .ruleset import Ruleset
from .basestrategy import Strategy
from .default_strategies.defaultstrat import TitForTat # Hier muss noch ein Befehl gefunden werden mit dem alle Classen einer Datei oder eines Ordners eingebunden werden können.
from .default_strategies.defaultstrat import RandomStrat


class PPDSimulation:

    def __init__(self) -> None:
        pass

    def runsimtest(self):
        rule = Ruleset()
        c1 = TitForTat()
        c2 = RandomStrat()
        histc1 = []
        histc2 = []
        for rou in range(0, rule.rounds-1):
            histc1.append(c1.react(rou, histc1, histc2))
            histc2.append(c2.react(rou, histc2, histc1))
            print(histc1)
            print(histc2)
            # Punkte Berechnen und vergeben


    
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
