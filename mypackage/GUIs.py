"""
Dieses Modul enthält die Klassen, die für die grafische Darstellung
der Simulationsergebnisse des Gefangenendilemmas verantwortlich ist.
"""

import matplotlib.pyplot as plt  # Import hinzufügen


class GUIresults:
    """
    Diese Klasse ist für die grafische Darstellung der Simulationsergebnisse
    des Gefangenendilemmas verantwortlich.
    """

    def show_results_gui(self, sim_results):
        """
        Zeigt die Ergebnisse der Simulation in einem
        horizontalen Balkendiagramm an.

        Die Strategien werden basierend auf ihrem Attribut "nice"
        farblich dargestellt:
        - Grüne Balken: Strategien, die "nice" sind.
        - Rote Balken: Strategien, die nicht "nice" sind.

        Parameter:
        - sim_results (DataFrame): Ein Pandas-DataFrame, der die
        Ergebnisse der Simulation enthält. Erwartet werden die Spalten:
        - "Strategie Objekt": Die Strategie-Objekte.
        - "Strategie Name": Der Name der Strategie.
        - "Average Points": Die durchschnittlichen Punkte der Strategie.

        Rückgabewert:
        - None
        """
        # Ermittle, ob eine Strategie "nice" ist
        sim_results["nice"] = sim_results["Strategie Objekt"].apply(lambda candidates: candidates.nice)
        # Sortiere das Ergebnis nach der durchschnittlichen Punktzahl
        sim_results.sort_values(by="Average Points", ascending=False, inplace=True)
        # Erstelle eine Farbliste basierend auf dem Attribut 'nice'
        colors = ['green' if nice else 'red' for nice in sim_results["nice"]]
        # Reduziere die Ausgabe auf die Spalten "Strategie Name" und "Average Points"
        show_results = sim_results[["Strategie Name", "Average Points"]]
        # Runde die Punktzahlen auf ganze Zahlen
        show_results["Average Points"] = show_results["Average Points"].round(0).astype(int)
        # Ausgabe in der Konsole
        print(show_results)
        # Erstelle ein horizontales Balkendiagramm
        plt.figure(num="Python-Prisoner-s-dilemma", figsize=(15, 10))
        plt.barh(show_results["Strategie Name"], show_results["Average Points"], color=colors)
        plt.xlabel("Average Points")
        plt.gca().invert_yaxis()  # Höchste Punktzahl oben anzeigen
        plt.show()
