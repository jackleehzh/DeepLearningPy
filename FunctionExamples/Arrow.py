#注释有三种，分别为:
#ax.text()：文本注释，只能填写文本
#ax.arrow()：箭头标记，不能填写文本 
#ax.annotate()：箭头注释，在箭头的位置可以填写文本
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# fc: filling color
# ec: edge color
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(-2, -2, "Sample A", ha="center", va="center", size=20,
    bbox=bbox_props)
ax.text(2, 2, "Sample B", ha="center", va="center", size=20,
    bbox=bbox_props)
 
# lw: line width
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="r", lw=2)
t = ax.text(0, 0, "Direction", ha="center", va="center", rotation=45,
      size=15,
      bbox=bbox_props)
 
bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)

A = np.array([1,-3])
B = np.array([3,-1])
C = np.array([2,0])

#s : 箭尾的注释 
#xy : 箭头坐标 
#xytext : 箭尾坐标 
#arrowprops：设置箭头标致的格式（字典）
ax.annotate("", xy=(B[0], B[1]), xytext=(A[0], A[1]),arrowprops=dict(arrowstyle="->"))

ax.arrow(A[0], A[1], C[0]-A[0], C[1]-A[1],
             length_includes_head=True,# 增加的长度包含箭头部分
             head_width=0.25, head_length=0.5, fc='r', ec='b')
ax.grid()
ax.set_aspect('equal')

#default show range（0，1）
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

plt.show()
