---------------------------CODE-----------------------------                        
import math

def euclidean_distance(p1, p2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

k = int(input("Enter number of clusters (k): "))
n = int(input("Enter number of points: "))

points = []
print("Enter the points (x y format for each point):")
for i in range(n):
    point = list(map(float, input(f"Point {i+1}: ").split()))
    points.append(point)

centroids = []
print(f"Enter initial {k} centroids (x y format for each centroid):")
for i in range(k):
    centroid = list(map(float, input(f"Centroid {i+1}: ").split()))
    centroids.append(centroid)

clusters = [[] for _ in range(k)]
iteration = 0

while True:
    iteration += 1
    print(f"\nIteration {iteration}:")
    clusters = [[] for _ in range(k)]
    for point in points:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        nearest_index = distances.index(min(distances))
        clusters[nearest_index].append(point)
    new_centroids = []
    for cluster in clusters:
        if len(cluster) == 0:
            new_centroids.append([0]*len(points[0]))
        else:
            new_centroid = [sum(dim)/len(cluster) for dim in zip(*cluster)]
            new_centroids.append(new_centroid)
    if new_centroids == centroids:
        print("K-Means converged. Centroids did not change.")
        break
    else:
        centroids = new_centroids

print("\nFinal Clusters:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: {cluster}")

print("\nFinal Centroids:")
for i, centroid in enumerate(centroids):
    print(f"Centroid {i+1}: {centroid}")




