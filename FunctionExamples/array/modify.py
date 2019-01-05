import numpy as np

def appendMatrix(arr, data):
    return np.append(arr, data, axis = 0)

def divideArr(data, col):
    index = col - 1
    dx = data[:,0:index]
    dy = data[:,index]
    return dx, dy
