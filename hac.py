import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt


X = np.array([[0.40,0.53],
              [0.22,0.32],
              [0.35,0.32],
              [0.26,0.19],
              [0.08,0.41],
              [0.35,0.30],
              [0.80,0.98],
              [0.28,0.33]
])

def calculate_distance(p1, p2):
	'''
		It works for either single point or cluster,
        It works n-dimensional also
	'''
	dist = 999999
	for i in p1:
		for j in p2:
			temp = 0
			for k in range(len(i)):
				temp += (i[k] - j[k])**2
			dist = min(dist, temp**0.5)
	return dist

def getClustersToGroup(matrix):
	'''
		It returns the indexes of matrix which items/clusters to be merged
	'''
	minIndex = [-1,-1]
	minValue = 99999
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if(minValue > matrix[i][j]):
				minValue = matrix[i][j]
				minIndex = [i,j]
	return minIndex
    


samples     = [[X[i]] for i in range(X.shape[0])]

n = len(samples)

while n>1:
    print('Sample size before clustering    :- ', n)
    matrix = [[9999 for i in range(n)] for i in range(n)]

    for i in range(n):
    	for j in range(n):
    		if(i>j):
    			matrix[i][j] = calculate_distance(samples[i], samples[j])


    c1, c2 = getClustersToGroup(matrix)

    print('Clusters before grouping         :-', samples)

    print('Cluster Node 1                   :-',samples[c1])
    print('Cluster Node 2                   :-',samples[c2])

    

    samples[c1].extend(samples[c2])
    print('Cluster attained                 :-', samples[c1])
    
    samples.pop(c2)
    n -= 1
    
    print('Sample size after clustering     :-', n)
    print('\n')


Z = linkage(X, 'single')
fig = plt.figure(figsize=(25, 10))
dn = dendrogram(Z)