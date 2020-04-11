from matplotlib import pyplot as plt
from copy import deepcopy
import numpy as np

plt.rcParams['figure.figsize'] = (10, 10)
plt.style.use('ggplot')

# Euclidian Distance
dist = lambda a, b, ax=1: np.linalg.norm(a - b, axis=ax)

# init
k = 3
datas = [ list(map(int, data.split(';')[1:])) for data in open('sampleData.csv').read().splitlines()[1:]  ]
f1 = [ x[0] for x in datas ]
f2 = [ x[1] for x in datas ]

#Plot read points
plt.scatter(f1,f2, c='#050505', s=50)

# Clustering
# Random Centroid X dan Y
centroids = np.array([ datas[i] for i in np.random.randint(0,len(datas), k) ], dtype=np.float32)

# Plot Random Centroid
plt.scatter(centroids[0], centroids[1], marker="*", s=200, c='g')

# Find a new Centroid
centroids_old = np.zeros(centroids.shape)
clusters = np.zeros(len(datas))
error = dist(centroids, centroids_old, None)
while error != 0:
	for i in range(len(datas)) :
		distance = dist(datas[i], centroids)
		cluster = np.argmin(distance)
		clusters[i] = cluster
	centroids_old = deepcopy(centroids)

	for i in range(k):
		points = [datas[j] for j in range(len(datas)) if clusters[j] == i]
		centroids[i] = np.mean(points, axis=0)
	error = dist(centroids, centroids_old, None)

colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()
for i in range(k):
	points = np.array([datas[j] for j in range(len(datas)) if clusters[j] == i])
	ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])

ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='#050505')

print 'centroid optimal'
print centroids

plt.show()
