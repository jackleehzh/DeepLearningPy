# coding:utf8

import copy

def getArr(m,n,x):
    if m!=len(n):
        print("Error!指定每一维数组的长度时出错")
    else:
        result=[x for i in range(n[-1])]
        dimensions_num=1
        while dimensions_num<m:
            result=[copy.deepcopy(result) for i in range(n[-1-dimensions_num])]
            dimensions_num+=1
        return result

#用递归求解二项分布中的k次命中的概率值。这种递归类似斐波那契数列的递归，存在大量重复计算。
def binomial(N, k, p):
    if N == 0 and k == 0:
        return 1.0
    if N < 0 or k < 0:
        return 0.0
    return (1.0 - p) * binomial(N - 1, k, p) + p * binomial(N - 1, k - 1, p)

#改进版递归，保持已经计算过的结果，避免重复计算
def binomial2(N, k, p, M):
    if N == 0 and k == 0:
        return 1.0
    if N < 0 or k < 0:
        return 0.0
    if(M[N][k] == -1):
        M[N][k] = (1.0 - p) * binomial(N - 1, k, p) + p * binomial(N - 1, k - 1, p)
    return M[N][k]

def Binomial2(N, k, p):
    M = getArr(2, [N + 1, k + 1], -1)
    return binomial2(N, k, p, M)

#二项分布的迭代算法，速度快
def combination(N, k):
    NN = 1
    kk = 1
    minNum = N - k
    
    if minNum > k:
        tmp = minNum
        minNum = k
        k = tmp
        
    while minNum > 0:
        kk = kk * minNum
        minNum = minNum - 1
        
    while N > k:
        NN = NN * N
        N = N - 1

    return float(NN) / kk
    
def binomial3(N, k, p):
    a = 1
    b = 1
    c = combination(N, k)

    q = 1 - p
    while(N - k > 0):
        b = b * q
        N = N - 1
    
    while(k > 0):
        a = a * p
        k = k - 1
    
    return a * b * c

#根据置信度，计算临界概率值。这里涉及解一元高次方程。目前，五次以上的方程不存在公式解。此处采用的是试探法：如果结果相差很大，概率减半或加半；如果结果相差不大，概率减去结果差。如果得到的概率大于1或小于0，那么被减数减半，重做这次减法。
#由于二项分布的内在规律性，在N，k，p一定的情况下，a是固定有范围的，因此a不可任意赋值。
#假定的p作为第一次迭代的初始值
def confidence(N, k, p, a):
    times = 1

    while(True):
        conf = 0
        tmpk = k
        while(k <= N):
            conf = conf + binomial3(N, k, p)
            k = k + 1

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
        
        k = tmpk
        times = times + 1
        #print(p)
        if times > 100:
            print("参数错误")
            p = -1
            break
    
    #return round(p, 4)
    return p

#这个函数好像没什么用处
def limitConfidence(N, k, p, a):

    p1 = confidence(N, k, p, a)
    if p1 > 0:
        while(p - p1 > 0.00000000000000001):
            print(p)
            print(p1)
            print('\n\n')
            print('a')
            p = p1
            p1 = confidence(N, k, p, a)
    return p1

binomial(2, 1, 0.5)
Binomial2(2, 1, 0.5)
#print(binomial3(4, 2, 0.5))
print(limitConfidence(100, 70, 0.7, 0.00000001))
