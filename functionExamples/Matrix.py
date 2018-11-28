#导入科学计算包
import numpy as np;

#随机生成一个3 * 4的整型矩阵，元素的最大值为10
data = np.mat(np.random.randint(10, size=(3, 4)))
print(data)

#对矩阵进行转置运算
data2 = data.T
print(data2)

#对矩阵进行乘法运算
data3 = data * data2
print(data3)

#对矩阵进行求逆运算
data4 = data3.I
print(data4)
