
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
        for turn in range(0, rule.turns-1):
            histc1.append(c1.react(turn, histc1, histc2))
            histc2.append(c2.react(turn, histc2, histc1))
            print(histc1)
            print(histc2)
            # Punkte Berechnen und vergeben


    
    def runsim(self):
        rule = Ruleset()
        candidates = self.initcandidates()
        for candidate1 in candidates[:-1]: # Schleife über alle Kandidaten bis auf den letzten Kandidaten
            for candidate2 in candidates[candidates.index(candidate1)+1:]: # Schleife ab candidate1 + 1
                print("Paarung: " + candidate1.name + "   vs.   " + candidate2.name)
                for rep in range(rule.repetitions):
                    histc1 = []
                    histc2 = []
                    pointsc1 = 0
                    pointsc2 = 0
                    for turn in range(rule.turns):
                        histc1.append(candidate1.react(turn, histc1, histc2))
                        histc2.append(candidate2.react(turn, histc2, histc1))
                        [pointsc1, pointsc2] = rule.evaluate_points(histc1[turn], histc2[turn], pointsc1, pointsc2)
                        # Punkte in Pandas zählen
                    print(pointsc1)
                    print(histc1)
                    print(histc2)
                    print(pointsc2)
    
    def initcandidates(self):
        listOfStrategies = Strategy.__subclasses__() # Ereugt eine Liste aller Klassen, die von Strategy abgeleitet wurden 
        strategyObjects = []
        for iStrategy in listOfStrategies:
            strategyObjects.append(iStrategy()) # Erstelle Objekte der definierten Strategien
        return strategyObjects
