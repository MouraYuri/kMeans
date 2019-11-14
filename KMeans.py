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
        cYc = randint(dataset['yCordinate'].min(), dataset['yCordinate'].max()) #centroid Y coordinate
        centroidDataframe = centroidDataframe.append(pd.DataFrame([[cXc, cYc]], columns=['xCordinate', 'yCordinate']), ignore_index=True)
        centroidsList.append(pd.DataFrame([], columns=['xCordinate', 'yCordinate']))

    #finding the nearest centroid for each point in dataset
    for y in range(len(dataset)):
        point = dataset.iloc[y]
        distanceDf = pd.DataFrame([], columns=['distance'])
        #calculating the distance between one point and the centroids
        for x in range(k):
            centroid = centroidDataframe.iloc[x]
            dist = la.norm(point-centroid)
            distanceDf = distanceDf.append(pd.DataFrame([[dist]], columns=['distance']), ignore_index=True)
            #print("distance between point {} and centroid {} is {}\n".format(point, centroid, dist))
        print(distanceDf.idxmin())
        
            




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
