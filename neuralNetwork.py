import os
from fileOp import *
import numpy as np


if __name__ == "__main__":

    #Check if hyperparameters file is empty
    if not os.path.exists("hyperparameters.txt") or os.path.getsize("hyperparameters.txt") == 0:
        
        #Make sure we get a random seed 
        np.random.seed(42)

        #Initialise random weights and bias 
        weights = np.random.rand(3,1)
        bias = np.random.rand(1)

        #Write the above information to a file for future use
        writeHypers(weights, bias)
        
    else:
        
        #Get data from file
        weights = getWeightFromFile()
        bias = getBiasFromFile()

        print(weights)
        print(bias)




