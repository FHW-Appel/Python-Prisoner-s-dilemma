"""
Hauptmodul für die Ausführung der Simulation des Gefangenendilemmas.

Dieses Modul importiert die Klasse `PPDSimulation` aus dem Paket
`mypackage.simulation` und führt die Simulation aus. Die Simulation
umfasst verschiedene Strategien, die
im Gefangenendilemma gegeneinander antreten.

Funktionen:
- main(): Initialisiert und startet die Simulation.

Verwendung:
Führe dieses Modul direkt aus, um die Simulation zu starten.
"""

from mypackage.simulation import PPDSimulation


def main():
    ppdsim = PPDSimulation()
    # ppdsim.runsimtest()
    # candidates = ppdsim.initcandidates()
    # ppdsim.runsimtest2()
    ppdsim.runsim()
    exit(0)


if __name__ == "__main__":
    main()
