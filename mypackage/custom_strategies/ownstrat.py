"""
Dieses Modul definiert benutzerdefinierte Strategien für das Gefangenendilemma.
"""

try:
    from basestrategy import Strategy
except ImportError:
    from ..basestrategy import Strategy


class OwnStrat(Strategy):
    """
    Diese Strategie in diesen Zeilen beschreiben
    """
    name = "Name der Strategie bitte anpassen"
    nice = False

    def react(self, currentturn, myhist, hishist):
        """
        Reaktion der Strategie basierend auf der aktuellen Runde.
        """
        if currentturn == 0:
            return self.defect
        else:
            return self.cooperate


# Main-Funktion, die ausschließlich für den Test der Strategie verwendet wird.
if __name__ == "__main__":
    # Test, der prüft ob die selbst programmierte Strategie
    # funktionsfähig ist.
    print("Test wurde gestartet.")
    strategy = OwnStrat()
    print(f"Strategie: {strategy.name} wurde erstellt.")
    # Test, ob die Strategie nice ist:
    myhist = []
    hishist = []
    for i in range(1000):
        myhist.append(strategy.react(i, myhist, hishist))
        hishist.append(strategy.cooperate)
    # Wenn hishist immer cooperate ist,
    # dann ist die Strategie wahrscheinlich nice
    if all(x == strategy.cooperate for x in myhist):
        print("Die Strategie ist wahrscheinlich nice.")
        # Test, ob die Strategie einen groll hegt,
        # sprich wenn der Gegner einmal
        # defekt war, dann wird die Strategie auch defekt sein
        myhist.append(strategy.react(i, myhist, hishist))
        hishist.append(strategy.defect)
        for i in range(50):
            myhist.append(strategy.react(i, myhist, hishist))
            hishist.append(strategy.cooperate)
        if all(x == strategy.defect for x in myhist[-50:]):
            print("Die Strategie hat wahrscheinlich einen Groll.")
        else:
            print("Die Strategie hat keinen Groll.")
    else:
        print("Die Strategie ist nicht nice.")
    # Weitere Tests mit Zufälligen Eingabewerten
    for j in range(20):
        myhist = []
        hishist = []
        for i in range(50):
            myhist.append(strategy.react(i, myhist, hishist))
            hishist.append(strategy.react_prob_cooperate(50))
    myhist = []
    hishist = []
    for i in range(2000):
        myhist.append(strategy.react(i, myhist, hishist))
        hishist.append(strategy.react_prob_cooperate(50))
    print("Weitere Tests erfolgreich abgeschlossen.")

# Um die Strategie zu testen kann einfach
#   python ownstrat.py
# ausgeführt werden.
#
# Soll die Strategie in der Simulationsumgebung getestet werden,
# dann muss der folgende Befehl ausgeführt werden:
#   python -m mypackage.custom_strategies.ownstrat
