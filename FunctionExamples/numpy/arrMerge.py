import numpy as np

a = np.floor(10*np.random.rand(2,2))
b = np.floor(10*np.random.rand(2,2))

print(a)
print(b)
#hstack()在行上合并
c = np.hstack((a,b))
#vstack()在列上合并
d = np.vstack((a,b))
print(c)
print(d)
