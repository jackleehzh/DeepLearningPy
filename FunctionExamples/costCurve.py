# coding:utf8
#相关代码
#https://github.com/jackleehzh/DeepLearningPy/blob/master/FunctionExamples/precisionRecalllAndPicture.py
#https://github.com/jackleehzh/DeepLearningPy/blob/master/FunctionExamples/ROC.py
import numpy as np
import random
import matplotlib as mpl
import matplotlib.pyplot as plt

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
    shape = list(np.array(data).shape) 
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

def linearRegression(trdx, trdy):
    return (trdx.T * trdx).I * trdx.T * trdy

def pridect(tsdx, w):
    return tsdx * w

def studyMachine(data, elvFunc, frequency):
    w = 0
    for i in range(frequency):
        tsdata, trdata = divideData(data, elvFunc, i)
        trdx, trdy = divideArr(reshape(trdata, [len(trdata), 6]), 6)
        tsdx, tsdy = divideArr(reshape(tsdata, [len(tsdata), 6]), 6)
        w = w + linearRegression(trdx, trdy)
    w = w / frequency
    return pridect(tsdx, w), tsdy

def statistics(result, tsdy):
    a = 0
    b = 0
    for i in range(len(tsdy)):
        if tsdy[i] == 1 and (result[i] + 0.5) > 1:
            a = a + 1
        if tsdy[i] == 0 and (result[i] + 0.5) > 1:
            b = b + 1
    return a, b

#计算正例概率p
def calculateP(tsdy):
    a = 0
    for i in range(len(tsdy)):
        if tsdy[i] == 1:
            a = a + 1
    p = float(a) / len(tsdy)
    return p

#计算混淆矩阵
def getConfusionMatrix(result, tsdy):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(len(tsdy)):
        if result[i] >= 0.5 and tsdy[i] == 1:
            TP = TP + 1
        elif result[i] >= 0.5 and tsdy[i] == 0:
            FP = FP + 1
        elif result[i] < 0.5 and tsdy[i] == 0:
            TN = TN + 1
        else:
            FN = FN + 1
    TPR = float(TP) / (TP + FN)
    FPR = float(FP) / (TN + FP)
    FNR = 1- TPR
    
def getPoints(data, elvFunc, frequency):
    ret, tsdy = studyMachine(data, elvFunc, frequency)
    a, b = statistics(ret, tsdy)
    result = getEmptyArr(2, [0, 2])
    result.append([0, 0])
    x = 0
    y = 0
    for i in range(len(ret)):
        if tsdy[i] == 1 and (ret[i] + 0.5) > 1:
            y = y + 1.0 / a
        if tsdy[i] == 0 and (ret[i] + 0.5) > 1:
            x = x + 1.0 / b
        result.append([x, y])
    result.append([1, 1])
    return result

#增加了这个坐标转换及绘图函数
def ROCtoCostCurve(x, y):
    plt.figure(figsize=(7, 7))
    for i in range(len(x)):
        if float(x[i]) > 0 and float(x[i]) < 1 and float(y[i]) > 0 and float(y[i]) < 1:
            plt.plot([0, 1], [float(x[i]), 1 - float(y[i])], 'b', lw = 1.5) 
            plt.plot([0, 1], [float(x[i]), 1 - float(y[i])], 'yo')
    plt.plot([0, 0], [0, 1], 'r', [1, 1], [0, 1], 'r', lw = 1.5) 
    plt.plot([0, 0], [0, 1], 'go', [1, 1], [0, 1], 'go')
    
    plt.axis('tight')
    plt.title('cost curved shape')
    plt.legend()
    plt.show()
    
data = generateData(2, 100, 6)
result = getPoints(data, holdOut, 10)
x, y = divideArr(reshape(result, [len(result), 2]), 2)
ROCtoCostCurve(x, y)
