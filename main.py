# 

from mypackage.simulation import PPDSimulation

def main():
    ppdsim = PPDSimulation()
    #ppdsim.runsimtest()
    #candidates = ppdsim.initcandidates()
    #ppdsim.runsimtest2()   
    ppdsim.runsim()
    exit(0)
    

if __name__ == "__main__":
    main()
    
