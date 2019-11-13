import numpy.linalg as la
from matplotlib import pyplot as plt
import numpy
from random import randint
import pandas as pd

'''
DA UM GIT PULL AE
'''

def preProcessingData(data):
    for x in range(len(data)):
        data[x] = data[x].split(' ')
        data[x][1] = data[x][1].rstrip()
        data[x][0], data[x][1] = int(data[x][0]), int(data[x][1])
    df = pd.DataFrame(data, columns = ['xCordinate', 'yCordinate'])
    return df

def kMeans(dataset,  k):
    centroidDataframe = pd.DataFrame([], columns = ['xCordinate', 'yCordinate'])

    
    #placing centroids at random locations
    for y in range(k):
        cXc = randint(dataset['xCordinate'].min(), dataset['xCordinate'].max()) #centroid X coordinate
        cYc = randint(dataset['yCordinate'].min(), dataset['yCordinate'].max()) #centroid X coordinate
        centroidDataframe = centroidDataframe.append(pd.DataFrame([[cXc, cYc]], columns=['xCordinate', 'yCordinate']))
    print("centroidDataframe => {}".format(centroidDataframe))

    #finding the nearest centroid for each point in dataset



'''
    plt.scatter(centroidXcoordinate, centroidYcoordinate, color=['blue'])
    plt.scatter(setXpoints, setYpoints, color=['red'])

    for x in range(len(pontosX)):
        for y in range(k):



    plt.show()
'''

data = open("...", 'r')
data = data.readlines()
data = preProcessingData(data)
print(data)
kMeans(data, 2)
