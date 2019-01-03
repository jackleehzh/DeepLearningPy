import random
import copy

def delElems(data, index):
    index = sorted(index, reverse=True)
    trdata = copy.deepcopy(data)
    for i in index:
        del(trdata[i])
    return trdata

data=[random.randint(0,100) for _ in range(100) ]
print("initial data")
print(data)


#留出法
#随机采样
print("留出法")
index = [random.randint(0,99) for _ in range(36) ]
tsdata = []
for i in index:
    tsdata.append(data[i])
print("sample tsdata")
print(tsdata)
print("sample index")
print(index)

#剔除采样数据
trdata = delElems(data, index)
print("training trdata")
print(trdata)


#交叉验证法
print("交叉验证法")
for i in range(10):
    jtsdata = data[i * 10: (i + 1) *10]
    jtrdata = data[0:i * 10] + data[(i + 1) *10:]
    print("sample jtsdata")
    print(jtsdata)
    print("training jtrdata")
    print(jtrdata)
    
    
#自助法
print("自助法")
ztrdata = []
ztrindex = []
for i in range(100):
    a = random.randint(0,99)
    ztrdata.append(data[a])
    if a not in ztrindex:
        ztrindex.append(a)
    
ztsdata = delElems(data, ztrindex)
print("sample ztsdata")
print(ztsdata)
print("training ztrdata")
print(ztrdata)
