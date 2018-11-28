#plt.legend(label, loc, ncol)
#loc(设置图例显示的位置)
#'best'         : 0, (only implemented for axes legends)(自适应方式)
#'upper right'  : 1,
#'upper left'   : 2,
#'lower left'   : 3,
#'lower right'  : 4,
#'right'        : 5,
#'center left'  : 6,
#'center right' : 7,
#'lower center' : 8,
#'upper center' : 9,
#'center'       : 10,
#ncol(设置列的数量，使显示扁平化，当要表示的线段特别多的时候会有用)

import numpy as np  
import matplotlib.pyplot as plt  

x = np.arange(1, 11, 0.01)
y = np.sin(x)
plt.figure(figsize = (8, 4))  
plt.plot(x, y, label='Demo1', color='red', linewidth=3)  
#显示图例
plt.legend()

#面向对象的方式
fig = plt.figure()
ax = fig.add_subplot(221)
# 第一种
# l后面不加逗号会出错，一定要注意
l, = ax.plot(x, y, 'g--', lw=3)
l.set_label('Demo2')
ax.legend(loc = 4)
 
# 第二种
ax = fig.add_subplot(222)
ax.plot(x,  y, label='Demo3', lw=3)
ax.legend(loc = 2)
 
# 第三种
ax = fig.add_subplot(212)
ax.plot(x, y)
ax.legend(['Demo4'], loc = 0)
   
plt.show() 
