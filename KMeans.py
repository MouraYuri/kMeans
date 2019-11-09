import numpy.linalg as la
from matplotlib import pyplot as plt
import numpy
from random import randint
import pandas as pd

def preProcessingData(data):
    for x in range(len(data)):
        data[x] = data[x].split(' ')
        data[x][1] = data[x][1].rstrip()
        data[x][0], data[x][1] = int(data[x][0]), int(data[x][1])
    df = pd.DataFrame(data, columns = ['xCordinate', 'yCordinate'])
    return df

def kMeans(dataset,  k):
    centroidDataframe = pd.DataFrame([], columns = ['xCordinate', 'yCordinate'])
    for y in range(k):
        centroidDataframe.insert(column="xCordinate", value=(randint(dataset['xCordinate'].min(), dataset['xCordinate'].max())))
        centroidDataframe.insert(column="yCordinate", value=(randint(dataset['yCordinate'].min(), dataset['yCordinate'].max())))
    print(centroidDataframe)


'''
    plt.scatter(centroidXcoordinate, centroidYcoordinate, color=['blue'])
    plt.scatter(setXpoints, setYpoints, color=['red'])

    for x in range(len(pontosX)):
        for y in range(k):



    plt.show()
'''

data = open("C:/Users/YuriPc/Desktop/Python Projects/KMeans/data.txt", 'r')
data = data.readlines()
data = preProcessingData(data)
print(data)
kMeans(data, 2)
