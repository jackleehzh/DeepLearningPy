import random
import copy

def delElems(data, index):
    index = sorted(index, reverse=True)
    trdata = copy.deepcopy(data)
    for i in index:
        del(trdata[i])
    return trdata

#留出法
def holdOut(data):
    print("留出法")
    #随机采样
    index = [random.randint(0,99) for _ in range(36) ]
    tsdata = []
    for i in index:
        tsdata.append(data[i])

    #剔除采样数据
    trdata = delElems(data, index)
    return tsdata, trdata

#交叉验证法
def crossValidation(data):
    print("交叉验证法")
    jtsdata = []
    jtrdata = []
    
    for i in range(10):
        tsdata = data[i * 10: (i + 1) *10]
        trdata = data[0:i * 10] + data[(i + 1) *10:]
        jtsdata.append(tsdata)
        jtrdata.append(trdata)
    return jtsdata, jtrdata

#自助法
def bootStrapping(data):
    print("自助法")
    trdata = []
    index = []
    for i in range(100):
        a = random.randint(0,99)
        trdata.append(data[a])
        if a not in index:
            index.append(a)
        
    tsdata = delElems(data, index)
    return tsdata, trdata

def divideData(data, divideFunc):
    return divideFunc(data)

def main():
    data=[random.randint(0,100) for _ in range(100) ]
    tsdata, trdata = divideData(data, crossValidation)
    
    print("initial data")
    print(data)
    print("sample tsdata")
    print(tsdata)
    print("training trdata")
    print(trdata)

main()
