import random
import copy
import numpy as np

def getArr(ndim):
    arr = []
    if ndim == 2:
        arr = np.empty(shape=[0, 6], dtype=np.int32)
    return arr

def appendArr(arr, data, ndim):
    if ndim == 2:
        arr = np.append(arr, data, axis = 0)
    elif ndim == 1:
        arr.append(data)
    return arr

def delElems(data, index):
    index = sorted(index, reverse=True)
    #trdata = copy.deepcopy(data)
    trdata = getArr(np.array(data).ndim)
    for i in range(len(data) - 1):
        if i not in index:
            trdata = appendArr(trdata, data[i], np.array(data).ndim)
    return trdata

#留出法
def holdOut(data, i):
    print("留出法")
    #随机采样
#    index = [random.randint(0,99) for _ in range(36) ]
    index = []
    tsdata = getArr(np.array(data).ndim)
    for i in range(36):
        a = random.randint(0,99)
        if a not in index:
            index.append(a)
            tsdata = appendArr(tsdata, data[a], np.array(data).ndim)
        else:
            i = i - 1

    #剔除采样数据
    trdata = delElems(data, index)
    print(tsdata)
    print(trdata)
    return tsdata, trdata

#交叉验证法
def crossValidation(data, i):
    print("交叉验证法")
    tsdata = data[i * 10: (i + 1) *10]
    if np.array(data).ndim == 2:
        trdata = np.vstack((data[0:i * 10], data[(i + 1) *10:]))
    elif np.array(data).ndim == 1:
        trdata = data[0:i * 10] + data[(i + 1) *10:]
    return tsdata, trdata

#自助法
def bootStrapping(data, i):
    print("自助法")
    trdata = getArr(np.array(data).ndim)
    index = []
    
    for i in range(100):
        a = random.randint(0,99)
        trdata = appendArr(trdata, data[a], np.array(data).ndim)
        if a not in index:
            index.append(a)
        
    tsdata = delElems(data, index)
    return tsdata, trdata

def divideData(data, divideFunc, i):
    return divideFunc(data, i)

def main():
    data=[random.randint(0,100) for _ in range(100) ]
    tsdata, trdata = divideData(data, bootStrapping, 0)
    
    print("initial data")
    print(data)
    print("sample tsdata")
    print(tsdata)
    print("training trdata")
    print(trdata)

#main()
