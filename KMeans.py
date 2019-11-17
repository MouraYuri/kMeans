import numpy.linalg as la
from matplotlib import pyplot as plt
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
    clusters, previousClusters = [], []

    #placing centroids at random locations
    for y in range(k):
        cXc = randint(dataset['xCordinate'].min(), dataset['xCordinate'].max()) #centroid X coordinate
        cYc = randint(dataset['yCordinate'].min(), dataset['yCordinate'].max()) #centroid Y coordinate
        centroidDataframe = centroidDataframe.append(pd.DataFrame([[cXc, cYc]], columns=['xCordinate', 'yCordinate']), ignore_index=True)
        
        #filling the clusters and previousClusters list with empty dataframes
        clusters.append(pd.DataFrame([], columns=['xCordinate', 'yCordinate']))
        previousClusters.append(pd.DataFrame([], columns=['xCordinate', 'yCordinate']))

    while True:

        #finding the nearest centroid for each point in dataset
        for y in range(len(dataset)):
            point = dataset.iloc[y]
            distanceDf = pd.DataFrame([], columns=['distance'])
        
            #calculating the distance between one point and the centroids
            for x in range(k):
                centroid = centroidDataframe.iloc[x]
                dist = la.norm(point-centroid)
                distanceDf = distanceDf.append(pd.DataFrame([[dist]], columns=['distance']), ignore_index=True)
        
            #getting the index of the min distance
            indexmin = distanceDf.idxmin()[0]
            
            #assigning the point to the cluster
            clusters[indexmin] = clusters[indexmin].append([point], ignore_index=True) 

        #comparing previous dataframe with the current one
        counter = 0
        for x in range(k):
            if (clusters[x].equals(previousClusters[x])):
                counter = counter + 1
        if (counter==k):
            break 

        #updating centroids
        for x in range(k):
            axisSum = clusters[x].sum(axis=0)
            xMean, yMean = axisSum[0]/len(clusters[x]), axisSum[1]/len(clusters[x]) #!/0
            centroidDataframe.at[x, 'xCordinate'], centroidDataframe.at[x, 'yCordinate'] = xMean, yMean

        #saving the clusters in a new list and cleaning the current clusters list
        previousClusters = []
        for x in range(k):
            previousClusters.append(clusters[x].copy(deep=True))
            clusters[x] = pd.DataFrame([], columns=['xCordinate', 'yCordinate'])

    for cluster in clusters:
        plt.scatter(cluster['xCordinate'], cluster['yCordinate'], color=['blue'])
    plt.scatter(centroidDataframe['xCordinate'],centroidDataframe['yCordinate'], color=['red'] )
    plt.show()


data = open("./KMeans/data.txt", 'r')
data = data.readlines()
data = preProcessingData(data)
kMeans(data, 3)
