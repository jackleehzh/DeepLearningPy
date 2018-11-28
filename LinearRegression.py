#导入科学计算包
import numpy as np
from numpy.linalg import solve

#随机生成训练集和测试集，元素的最大值为10。训练集包含10个样例，测试集包含6个样例。
td = np.mat(np.random.randint(10, size=(10, 6)))
ld = np.mat(np.random.randint(10, size=(4, 6)))

#分离出数据和标签
tdx = td[:,0:5]
tdy = td[:,5]
ldx = ld[:,0:5]
ldy = ld[:,5]

#打印训练集和测试集
print(td)
print(ld)

#通过减少均方误差来优化参数
w = (tdx.T * tdx).I * tdx.T * tdy

#检测在测试集上的表现
ret = ldx * w

for elem in ret:
    if elem > 5:
        print("high")
    elif elem == 5:
        print("equal")
    else:
        print("low")
