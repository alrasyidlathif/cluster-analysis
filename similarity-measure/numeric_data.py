import numpy as np

def euclidean(point1, point2):
    return np.sqrt(np.sum(np.square(point1-point2)))

def manhattan(point1, point2):
    return np.sum(np.abs(point1-point2))
