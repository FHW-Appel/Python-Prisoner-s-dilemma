
from .ruleset import Ruleset
from .basestrategy import Strategy
from .default_strategies.defaultstrat import * # importiert alle Klassen des Files "defaultstrat"
from .custom_strategies import * # Hier muss noch ein Befehl gefunden werden mit dem alle Klassen eines Ordners eingebunden werden können.
import pandas as pd

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

    def runsimtest2(self):
        testStrategy = Strategy()
        testResult = 1
        for testRuns in range(1,100):
            if (testStrategy.defect == testStrategy.reactProbDefect(30)):
                testResult += 1
        print(testResult)

    
    def runsim(self):
        rule = Ruleset()
        candidates = self.initcandidates()
        num_candidates = len(candidates)
        #print(candidates.name)
        sim_results = pd.DataFrame({"Startegie Objekt": candidates,
                                    "Total Points": [0] * num_candidates,
                                    "Average Points": [0] * num_candidates})
        print(sim_results)
        for i1 in range(num_candidates-1): # Schleife über alle Kandidaten bis auf den letzten Kandidaten
            for i2 in range(i1+1, num_candidates): # Schleife ab candidate1 + 1
                print("Paarung: " + candidates[i1].name + "   vs.   " + candidates[i2].name)
                for rep in range(rule.repetitions):
                    histc1 = []
                    histc2 = []
                    pointsc1 = 0
                    pointsc2 = 0
                    for turn in range(rule.turns):
                        histc1.append(candidates[i1].react(turn, histc1, histc2))
                        histc2.append(candidates[i2].react(turn, histc2, histc1))
                        [pointsc1, pointsc2] = rule.evaluate_points(histc1[turn], histc2[turn], pointsc1, pointsc2)
                    sim_results.loc[i1, "Total Points"] += pointsc1
                    sim_results.loc[i2, "Total Points"] += pointsc2
        sim_results["Average Points"] = sim_results["Total Points"] / (num_candidates-1) / rule.repetitions
        self.showresults(sim_results)

    
    def initcandidates(self):
        listOfStrategies = Strategy.__subclasses__() # Ereugt eine Liste aller Klassen, die von Strategy abgeleitet wurden 
        strategyObjects = []
        for iStrategy in listOfStrategies:
            strategyObjects.append(iStrategy()) # Erstelle Objekte der definierten Strategien
        return strategyObjects
    
    def showresults(self, sim_results):
        print("Results")
        print(sim_results.sort_values(by="Total Points", ascending=False))

