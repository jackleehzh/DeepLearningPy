import numpy as np
import matplotlib.pyplot as plt

for i in range(100):
    X = np.random.randint(100, size = 50)
    #print(X)
    y = 50 * (np.random.randn(50) + 1)

    size = np.random.randint(200, size = 50)
    color = np.random.randint(256, size = 50)
    plt.scatter(X, y, s = size, c = color * color * color)
    #plt.scatter(X, y)
    # x，y取值范围设置
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.ion()
    plt.pause(0.1)
    plt.close()
# 保存图片到指定路径
plt.savefig("/Users/jacklee/Desktop/HeightAndWeight.png")
# 展示图片
#plt.show()
