#

class Strategy:
    defect = False
    cooperate = True
    classid = 0 # Muss noch gesetzt werden

    def __init__(self) -> None:
        self.name = ""
        self.totalscore = 0
        self.classid = -1

    def react(self, currentturn, myhist, hishist):
        return Strategy.cooperate
    
    def updatetotalscore(self, points):
        self.totalscore += points