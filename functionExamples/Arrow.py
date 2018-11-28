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

#default show range（0，1）
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

plt.show()
