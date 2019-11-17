# kMeans
Non supervised learning clustering algorithm.

## Algorithm  
-We start taking a value K and a set of point {x1,x2,...,xn} as input.  
-Then we place centroids {c1,c2,...,ck} at random locations.  
-(repeat the steps below until none of clusters assignments change)  
-Now, for each point xi we find the nearest centroid cj and assign the point to the cluster j.  
-After that, for each cluster j=1,...,k we update the centroid cj:  
--new centroid cj = mean of all points xi assigned to cluster j in previous step  

## Centroids at random locations:



