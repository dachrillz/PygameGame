import numpy as np
from opensimplex import OpenSimplex
import random

def GeneratePerlinNoise(height,width,resolution):
    '''
    This function generates a sloppy version of Perlin noise as numpy array, it needs to be square as of now.
    TODO: more parameters so that one can customize it's use.
    '''
    tmp = OpenSimplex()
    finalGrid = np.zeros((height,width),dtype=float)
    
    x = np.linspace(0,resolution,height)
    y = np.linspace(0,resolution,width)

    for i in range(len(finalGrid)):
        for j in range(len(finalGrid[i])):
            finalGrid[i][j] = tmp.noise2d(x[i], y[j])
          
    #normalize the grid
    smallestValue = np.amin(finalGrid)
    finalGrid = finalGrid - smallestValue
    largestValue = np.amax(finalGrid)
    finalGrid = finalGrid/largestValue
    
    del tmp
    
    #return
    return finalGrid
            
def getLargestValue(largestValue,z1,z2,z3,z4):
    '''
    Support function
    '''
    return max(largestValue,z1,z2,z3,z4)
    
def convertValuesToInt(finalGrid):
        length = len(finalGrid)
        grid = np.zeros((length,length),dtype=int)
        for i in range(length):
            for j in range(length):
                grid[i][j] = int(finalGrid[i][j]*10)
                
        return grid
                
    

