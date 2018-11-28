#导入科学计算包
import numpy as np
from numpy.linalg import solve

result = np.mat([1, 2, 3]).T    #常数项列矩阵

#随机生成一个3 * 3的整型矩阵，元素的最大值为10
data = np.mat(np.random.randint(10, size=(3, 3)))
print(data)

x = solve(data,result)     #方程组的解
print(x)
