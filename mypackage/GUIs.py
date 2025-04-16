import pandas as pd
import matplotlib.pyplot as plt  # Import hinzufügen

class GUIresults:

    def __init__(self) -> None:
        pass

    def showresultsGUI(self, sim_results):
        show_results = sim_results[["Strategie Name", "Average Points"]]
        show_results["Average Points"] = show_results["Average Points"].round(0).astype(int)
        show_results.sort_values(by="Average Points", ascending=False, inplace=True)
        print(show_results)
        # Erstelle ein horizontales Balkendiagramm
        plt.figure(num="Python-Prisoner-s-dilemma", figsize=(10, 6))
        plt.barh(show_results["Strategie Name"], show_results["Average Points"], color='skyblue')
        plt.xlabel("Average Points")
        plt.gca().invert_yaxis()  # Höchste Punktzahl oben anzeigen
        plt.show()
        return None
