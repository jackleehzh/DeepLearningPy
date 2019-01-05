import numpy as np

a = np.floor(10*np.random.rand(3,3))
b = np.floor(10*np.random.rand(3,3))

print(a)
print(b)
#hstack()在行上合并
c = np.hstack((a,b))
#or
#c = np.column_stack((a,b))
#vstack()在列上合并
d = np.vstack((a,b))
#or
#d = np.row_stack((a,b))
print(c)
print(d)

e = np.hsplit(c,3)
f = np.vsplit(d,3)
print(e)
print(f)

g = c.reshape(2,3,3)
#or
#g = np.floor(10*np.random.rand(3,3,3))
h = np.dsplit(g,3)
print(g)
print(h)
