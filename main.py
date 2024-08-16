# 

from mypackage.simulation import PPDSimulation

def main():
    ppdsim = PPDSimulation()
    ppdsim.runsimtest()
    candidates = ppdsim.initcandidates()

if __name__ == "__main__":
    main()
    
