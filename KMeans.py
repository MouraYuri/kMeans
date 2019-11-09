import numpy.linalg as la
from matplotlib import pyplot as plt
import numpy
from random import randint
import pandas as pd

def preProcessingData(data):
    for x in range(len(data)):
        data[x] = data[x].split(' ')
        data[x][1] = data[x][1].rstrip()
    return data

def kMeans(dataset,  k):
    centroidXcoordinate, centroidYcoordinate = [], []
    setXpoints,setYpoints = [], []
    for x in dataset:
        setXpoints.append(int(x[0]))
        setYpoints.append(int(x[1]))
    for y in range(k):
        centroidXcoordinate.append(randint(numpy.amin(setXpoints),numpy.amax(setXpoints)))
        centroidYcoordinate.append(randint(numpy.amin(setYpoints),numpy.amax(setYpoints)))




    plt.scatter(centroidXcoordinate, centroidYcoordinate, color=['blue'])
    plt.scatter(setXpoints, setYpoints, color=['red'])
    '''    
    for x in range(len(pontosX)):
        for y in range(k):
    '''


    plt.show()


data = open("C:/Users/YuriPc/Desktop/Python Projects/KMeans/data.txt", 'r')
data = data.readlines()
data = preProcessingData(data)
print(data)




kMeans(data, 2)
