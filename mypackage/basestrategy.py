#

class Strategy:
    defect = False
    cooperate = True
    classid = 0 # Muss noch gesetzt werden

    def __init__(self) -> None:
        self.name = ""
        self.classid = -1

    def react(self, currentturn, myhist, hishist):
        return Strategy.cooperate
    