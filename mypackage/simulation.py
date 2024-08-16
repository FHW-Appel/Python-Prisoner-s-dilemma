
from .ruleset import Ruleset
from .basestrategy import Strategy
from .default_strategies.defaultstrat import * # importiert alle Klassen des Files "defaultstrat"
from .custom_strategies import * # Hier muss noch ein Befehl gefunden werden mit dem alle Klassen eines Ordners eingebunden werden können.


class PPDSimulation:

    def __init__(self) -> None:
        pass

    def runsimtest(self):
        listOfStrategies = Strategy.__subclasses__() # Ereugt eine Liste aller Klassen, die von Strategy abgeleitet wurden 
        print(listOfStrategies) # Gebe die Strategie 0 aus 
        rule = Ruleset()
        c1 = listOfStrategies[0]() # Erstelle ein Objekt der ersten Strategie
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
        listOfStrategies = Strategy.__subclasses__() # Ereugt eine Liste aller Klassen, die von Strategy abgeleitet wurden 
        strategyObjects = []
        for iStrategy in listOfStrategies:
            strategyObjects.append(iStrategy()) # Erstelle Objekte der definierten Strategien
        return strategyObjects
