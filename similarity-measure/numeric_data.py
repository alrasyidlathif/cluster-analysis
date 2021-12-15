import numpy as np

def euclidean(point1, point2):
    return np.sqrt(np.sum(np.square(point1-point2)))
