"""
Dieses Modul definiert die Klasse `PPDSimulation`, die die Simulation des
Gefangenendilemmas ausführt.

Die Simulation umfasst verschiedene Strategien, die gegeneinander antreten.
Das Modul enthält Methoden zur Initialisierung der Strategien, zur Durchführung
der Simulation und zur Darstellung der Ergebnisse.
"""

import pandas as pd

from .ruleset import Ruleset
from .basestrategy import Strategy
# importiert alle Klassen des Files "defaultstrat"
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from .default_strategies.defaultstrat import *
# Hier muss noch ein Befehl gefunden werden,
# mit dem alle Klassen eines Ordners eingebunden werden können.
from .custom_strategies import *  # pylint: disable=wildcard-import
from .guis import GUIresults


class PPDSimulation:
    """
    Klasse zur Durchführung der Simulation des Gefangenendilemmas.

    Diese Klasse enthält Methoden zur Initialisierung der Strategien,
    zur Durchführung der Simulation und zur Darstellung der Ergebnisse.
    """

    def __init__(self) -> None:
        pass

    def runsim(self):
        """
        Führt die vollständige Simulation des Gefangenendilemmas durch.

        Die Simulation umfasst mehrere Strategien, die in Paarungen
        gegeneinander antreten. Die Ergebnisse werden in einem DataFrame
        gespeichert und anschließend grafisch dargestellt.
        """
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
                print("Paarung: " + candidates[i1].name +
                      "   vs.   " + candidates[i2].name)
                for _ in range(rule.repetitions):
                    histc1 = []
                    histc2 = []
                    pointsc1 = 0
                    pointsc2 = 0
                    for turn in range(rule.turns):
                        histc1.append(candidates[i1].react(turn, histc1,
                                                           histc2))
                        histc2.append(candidates[i2].react(turn, histc2,
                                                           histc1))
                        [pointsc1, pointsc2] = rule.evaluate_points(
                            histc1[turn], histc2[turn], pointsc1, pointsc2)
                    sim_results.loc[i1, "Total Points"] += pointsc1
                    sim_results.loc[i2, "Total Points"] += pointsc2
        sim_results["Average Points"] = (
            sim_results["Total Points"] / (num_candidates-1) / rule.repetitions
        )
        GUIresults.show_results_gui(self, sim_results)

    def initcandidates(self):
        """
        Initialisiert alle Strategien, die von der Basisklasse `Strategy`
        abgeleitet wurden.

        Rückgabewert:
        - list: Eine Liste von Instanzen aller abgeleiteten Strategien.
        """
        # Ereugt eine Liste aller Klassen, die von Strategy abgeleitet wurden
        list_of_strategies = Strategy.__subclasses__()
        strategy_objects = []
        for i_strategy in list_of_strategies:
            # Erstelle Objekte der definierten Strategien
            strategy_objects.append(i_strategy())
        return strategy_objects

    def showresults(self, sim_results):
        """
        Gibt die Ergebnisse der Simulation in der Konsole aus.

        Parameter:
        - sim_results (DataFrame): Ein Pandas-DataFrame mit den Ergebnissen
          der Simulation.
        """
        print("Results")
        show_results = sim_results[["Strategie Name",
                                    "Total Points",
                                    "Average Points"]]
        show_results.sort_values(by="Total Points",
                                 ascending=False,
                                 inplace=True)
        print(show_results)
