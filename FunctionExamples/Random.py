import numpy as np
#low、high、size三个参数。
#默认high是None,如果只有low，那范围就是[0,low)。
#如果有high，范围就是[low,high)
arr = np.random.randint(2, size = 10)
print(arr)
mat = np.random.randint(5, size=(2, 4))
print(mat)

#从标准正态分布中返回一个或多个样本值
#1)当函数括号内没有参数时，则返回一个浮点数； 
#2）当函数括号内有一个参数时，则返回秩为1的数组，不能表示向量和矩阵； 
#3）当函数括号内有两个及以上参数时，则返回对应维度的数组，能表示向量或矩阵； 
#4）np.random.standard_normal（）函数与np.random.randn()类似，但是np.random.standard_normal（）的输入参数为元组（tuple）. 
#5)np.random.randn()的输入通常为整数，但是如果为浮点数，则会自动直接截断转换为整数。
a = np.random.randn()
arr = np.random.randn(2)
mat = np.random.randn(3, 4)
print(a)
print(arr)
print(mat)

#从“0~1”均匀分布的随机样本中返回一个或多个样本值,不包括1
#使用方法与np.random.randn()函数相同 
arr = np.random.randn(10)
arr2 = np.random.rand(10)
print(arr)
print(arr2)
