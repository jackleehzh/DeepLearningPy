import numpy as np
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

def getEmptyMatrix(n):
    return np.empty(shape=[0, n])
