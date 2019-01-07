# coding:utf8

import numpy as np
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats

def getEmptyArr(dim, shape):
    if dim!=len(shape):
        print("Error!指定每一维数组的长度时出错")
    else:
        result=[]
        dimensions_num=1
        while dimensions_num<dim:
            result=[copy.deepcopy(result) for i in range(shape[-1-dimensions_num])]
            dimensions_num+=1
        return result

def getEmptyArrLike(data):
    dim = np.array(data).ndim
    shape = list(np.array(data).shape) #元组不可以更改元素值，因此转成list
    shape[0] = 0
    result = getEmptyArr(dim, shape)
    return result

def generateData(upperBound, row, col):
    return np.mat(np.random.randint(upperBound, size=(row, col)))

def delElems(data, index):
    index = sorted(index, reverse=True)
    data = data.tolist()
    for i in index:
        del(data[i])
    return data

def reshape(data, shape):
    data = np.mat(data)
    data.reshape(shape)
    return data

def divideArr(data, col):
    index = col - 1
    dx = data[:,0:index]
    dy = data[:,index]
    return dx, dy

def holdOut(data, times):
    index = []
    tsdata = getEmptyArrLike(data)
    for i in range(36):
        a = random.randint(0,99)
        if a not in index:
            index.append(a)
            tsdata.append(data[a].tolist()[0])
        else:
            i = i - 1

    trdata = delElems(data, index)
    return tsdata, trdata

def divideData(data, divideFunc, times):
    return divideFunc(data, times)

def linearRegression(trdx, trdy):
    return (trdx.T * trdx).I * trdx.T * trdy

def pridect(tsdx, w):
    return tsdx * w

def errRate(result, tsdy):
    count = 0
    for i in range(len(tsdy)):
        if (tsdy[i] == 0 and (result[i] + 0.5) > 1) or (tsdy[i] == 1 and result[i] < 0.5):
            count = count + 1
    return count / len(tsdy)

def studyMachine(data, elvFunc, frequency):
    w = 0
    for i in range(frequency):
        tsdata, trdata = divideData(data, elvFunc, i)
        trdx, trdy = divideArr(reshape(trdata, [len(trdata), 6]), 6)
        tsdx, tsdy = divideArr(reshape(tsdata, [len(tsdata), 6]), 6)
        w = w + linearRegression(trdx, trdy)
    w = w / frequency
    return pridect(tsdx, w), tsdy

#用二项检验得出临界概率
def confidence(N, k, p, a): 
    times = 1
    kk = np.arange(0,N + 1)

    while(True):
        ret = stats.binom.cdf(kk,N,p, loc=N - k + 1)
        conf = 1 - ret[-1]

        if conf > a + 0.000001 or conf < a - 0.000001:
            if p / 2 ** times < (conf - a):
                while(p - p / 2 ** times < 0):
                    times = times + 1
                p = p - p / 2 ** times
            elif p / 2 ** times < (a - conf):
                while(p - p / 2 ** times > 1):
                    times = times + 1
                p = p + p / 2 ** times
            else:
                q = conf - a
                while p - q > 1 or p - q < 0:
                    q = q / 2
                p = p - q
        else:
            break
        
        times = times + 1
        if times > 100:
            print("参数错误")
            p = -1
            break
    
    return p

data = generateData(2, 100, 6)

#选择模型：符合条件则输出相关信息，否则继续
def selectModule():
    while True:
        ret, tsdy = studyMachine(data, holdOut, 10)
        errR = errRate(ret, tsdy)
        p = 0.5
        N = len(tsdy)
        k = N * p

        p1 = confidence(N, k, p, 0.1)
        
        if errR < p1:
            print('OK')
            print(errR)
            print(p1)
            break
        else:
            print('false')

selectModule()
