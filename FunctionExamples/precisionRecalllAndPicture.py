# coding:utf8

import numpy as np
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
#生成任意维空数组
def getEmptyArr(dim, shape):
    if dim!=len(shape):
        print("Error!指定每一维数组的长度时出错")
    else:
        result=[]
        dimensions_num=1
        while dimensions_num<dim:
#注意此处要用深拷贝
            result=[copy.deepcopy(result) for i in range(shape[-1-dimensions_num])]
            dimensions_num+=1
        return result

#生成与给定数组相同的任意维空数组
def getEmptyArrLike(data):
#注意list必须转成array或matrix，才能使用ndim和shape属性
    dim = np.array(data).ndim
    shape = list(np.array(data).shape) #元组不可以更改元素值，因此转成list
    shape[0] = 0
    result = getEmptyArr(dim, shape)
    return result

def generateData(upperBound, row, col):
    return np.mat(np.random.randint(upperBound, size=(row, col)))
#注意matrix不支持del函数，但list可以
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
#list不支持这种写法，但matrix可以
    dx = data[:,0:index]
    dy = data[:,index]
    return dx, dy

#留出法
def holdOut(data, times):
    index = []
    tsdata = getEmptyArrLike(data)
    for i in range(36):
        a = random.randint(0,99)
#去除重复的下标
        if a not in index:
            index.append(a)
#list可用这种写法，matrix的写法为arr = np.append(arr, data, axis = 0)
            tsdata.append(data[a].tolist()[0])
        else:
            i = i - 1

    trdata = delElems(data, index)
    return tsdata, trdata

#自助法
def bootStrapping(data, times):
    trdata = getEmptyArrLike(data)
    index = []
    
    for i in range(100):
        a = random.randint(0,99)
        trdata.append(data[a].tolist()[0])
        if a not in index:
            index.append(a)
        
    tsdata = delElems(data, index)
    return tsdata, trdata

def divideData(data, divideFunc, times):
    return divideFunc(data, times)
#线性回归
def linearRegression(trdx, trdy):
    return (trdx.T * trdx).I * trdx.T * trdy

def pridect(tsdx, w):
    return tsdx * w
#返回预测结果
def studyMachine(data, elvFunc, frequency):
    w = 0
    for i in range(frequency):
#分离出训练集与测试集
        tsdata, trdata = divideData(data, elvFunc, i)
#分离出数据与标签
        trdx, trdy = divideArr(reshape(trdata, [len(trdata), 6]), 6)
        tsdx, tsdy = divideArr(reshape(tsdata, [len(tsdata), 6]), 6)
        w = w + linearRegression(trdx, trdy)
    w = w / frequency
    return pridect(tsdx, w)
#获取P-R曲线的点（预测值为取正例的概率，对这个概率排序，排序中的每个元素的查全率（召回率）则为float(i + 1) / len(ret)）
def getPoints(data, elvFunc, frequency):
    ret = studyMachine(data, elvFunc, frequency)
    ret = sorted(ret, reverse=True)
    result = getEmptyArr(2, [0, 2])
    result.append([1, 0])
    for i in range(len(ret)):
        result.append([ret[i], float(i + 1) / len(ret)])
    result.append([0, 1])
    return result

def PR(x, y, x2, y2):
    xy = [0, 1]
    plt.figure(figsize=(7, 7)) #画布大小
    plt.plot(x, y, 'b', x2, y2, 'k', lw = 1.5) # 蓝色的线
    plt.plot(x, y, 'yo', x2, y2, 'ro') #离散的点
    plt.plot(xy, xy, 'g:')
    plt.axis('tight')
    plt.xlabel('recall')
    plt.ylabel('precision')
    plt.title('P-R curved shape')
    plt.legend()
    plt.show()

data = generateData(2, 100, 6)
result = getPoints(data, holdOut, 10)
result2 = getPoints(data, bootStrapping, 10)
x, y = divideArr(reshape(result, [len(result), 2]), 2)
x2, y2 = divideArr(reshape(result2, [len(result2), 2]), 2)
PR(x, y, x2, y2)

