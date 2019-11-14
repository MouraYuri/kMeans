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
    centroidsList = []

    
    
    #placing centroids at random locations
    for y in range(k):
        cXc = randint(dataset['xCordinate'].min(), dataset['xCordinate'].max()) #centroid X coordinate
        cYc = randint(dataset['yCordinate'].min(), dataset['yCordinate'].max()) #centroid X coordinate
        centroidDataframe = centroidDataframe.append(pd.DataFrame([[cXc, cYc]], columns=['xCordinate', 'yCordinate']))
        centroidsList.append(pd.DataFrame([], columns=['xCordinate', 'yCordinate']))
    #print("centroidDataframe => {}".format(centroidDataframe))
    #print("centroidsList => {}".format(centroidsList))

    #finding the nearest centroid for each point in dataset
    for y in range(dataset.size):
        ctrl = dataset.iloc[y]
        print(ctrl)
        #for x in range(k):
            




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
kMeans(data, 2)
