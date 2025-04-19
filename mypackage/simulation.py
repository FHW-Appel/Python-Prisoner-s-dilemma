
from .ruleset import Ruleset
from .basestrategy import Strategy
# importiert alle Klassen des Files "defaultstrat"
from .default_strategies.defaultstrat import *
# Hier muss noch ein Befehl gefunden werden,
# mit dem alle Klassen eines Ordners eingebunden werden können.
from .custom_strategies import *
from .GUIs import GUIresults

import pandas as pd


class PPDSimulation:

    def __init__(self) -> None:
        pass

    def runsimtest(self):
        # Ereuge eine Liste aller Klassen, die von Strategy abgeleitet wurden
        listOfStrategies = Strategy.__subclasses__()
        print(listOfStrategies)  # Gebe die Strategien aus
        rule = Ruleset()
        c1 = listOfStrategies[0]()  # Erstelle ein Objekt der ersten Strategie
        c2 = RandomStrat()
        histc1 = []
        histc2 = []
        for turn in range(0, rule.turns-1):
            histc1.append(c1.react(turn, histc1, histc2))
            histc2.append(c2.react(turn, histc2, histc1))
            print(histc1)
            print(histc2)
            # Punkte Berechnen und vergeben
        return None

    def runsimtest2(self):
        testStrategy = Strategy()
        testResult = 1
        for testRuns in range(1, 100):
            if (testStrategy.defect == testStrategy.reactProbDefect(30)):
                testResult += 1
        print(testResult)
        return None

    def runsim(self):
        rule = Ruleset()
        candidates = self.initcandidates()
        num_candidates = len(candidates)
        strategie_names = []
        for i0 in range(num_candidates):
            strategie_names.append(candidates[i0].name)
        # print(candidates.name)
        sim_results = pd.DataFrame({"Strategie Objekt": candidates,
                                    "Strategie Name": strategie_names,
                                    "Total Points": [0] * num_candidates,
                                    "Average Points": [0] * num_candidates})
        print(sim_results)
        # Schleife über alle Kandidaten bis auf den letzten Kandidaten
        for i1 in range(num_candidates-1):
            # Schleife ab candidate1 + 1
            for i2 in range(i1+1, num_candidates):
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
        GUIresults.showresultsGUI(self, sim_results)
        return None

    def initcandidates(self):
        # Ereugt eine Liste aller Klassen, die von Strategy abgeleitet wurden
        listOfStrategies = Strategy.__subclasses__()
        strategyObjects = []
        for iStrategy in listOfStrategies:
            # Erstelle Objekte der definierten Strategien
            strategyObjects.append(iStrategy())
        return strategyObjects

    def showresults(self, sim_results):
        print("Results")
        show_results = sim_results[["Strategie Name",
                                    "Total Points",
                                    "Average Points"]]
        show_results.sort_values(by="Total Points",
                                 ascending=False,
                                 inplace=True)
        print(show_results)
        return None
