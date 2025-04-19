import pandas as pd
import matplotlib.pyplot as plt  # Import hinzufügen


class GUIresults:

    def __init__(self) -> None:
        pass

    def showresultsGUI(self, sim_results):
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
        return None
