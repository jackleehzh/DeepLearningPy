# coding:utf8
#相关代码
#https://github.com/jackleehzh/DeepLearningPy/blob/master/FunctionExamples/precisionRecalllAndPicture.py
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

#返回值处增加返回测试集的标签，用于后面统计真正例和反正例的数量
def studyMachine(data, elvFunc, frequency):
    w = 0
    for i in range(frequency):
        tsdata, trdata = divideData(data, elvFunc, i)
        trdx, trdy = divideArr(reshape(trdata, [len(trdata), 6]), 6)
        tsdx, tsdy = divideArr(reshape(tsdata, [len(tsdata), 6]), 6)
        w = w + linearRegression(trdx, trdy)
    w = w / frequency
    return pridect(tsdx, w), tsdy

#新增函数，统计真正例和反正例的数量
def statistics(result, tsdy):
    a = 0
    b = 0
    for i in range(len(tsdy)):
        if tsdy[i] == 1 and (result[i] + 0.5) > 1:
            a = a + 1
        if tsdy[i] == 0 and (result[i] + 0.5) > 1:
            b = b + 1
    return a, b

#函数中去掉了排序，因为该样本中排序后生成的图形不好看。由此也可以得知曲线形状受学习算法和排序结果以及呈现形式的影响，因此由其计算的AUC的值只能作为性能评估的参考。
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

def ROC(x, y, x2, y2):
    xy = [0, 1]
    plt.figure(figsize=(7, 7)) 
    plt.plot(x, y, 'b', x2, y2, 'k', lw = 1.5) 
    plt.plot(x, y, 'yo', x2, y2, 'ro')
    plt.plot(xy, xy, 'g:')
    plt.axis('tight')
    plt.xlabel('real positive')
    plt.ylabel('false positive')
    plt.title('ROC curved shape')
    plt.legend()
    plt.show()

def AUC(x, y):
    result = 0
    for i in range(len(x) - 1):
        result = result + (x[i + 1] - x[i]) * (y[i] + y[i + 1])
    return result / 2

data = generateData(2, 100, 6)
result = getPoints(data, holdOut, 10)
result2 = getPoints(data, bootStrapping, 10)
x, y = divideArr(reshape(result, [len(result), 2]), 2)
x2, y2 = divideArr(reshape(result2, [len(result2), 2]), 2)
print(AUC(x, y))
ROC(x, y, x2, y2)

