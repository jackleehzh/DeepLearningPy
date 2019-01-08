"""
Iris数据集在模式识别研究领域是知名数据集。该数据集共包括150行记录，前四列为花萼长度，花萼宽度，花瓣长度，花瓣宽度4个用于识别鸢尾花的属性，第5列为鸢尾花的类别（分别为Setosa，Versicolour，Virginica三类）。
 Iris数据集可以从UCI数据集上直接下载，下载地址为：http://archive.ics.uci.edu/ml/datasets/Iris，数据格式为逗号分隔的文本文件。
"""
# coding:utf8

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as LR
from sklearn.metrics import mean_squared_error, r2_score

iris = datasets.load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=0)

clf = LR(multi_class='auto', solver = 'lbfgs')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Mean squared error: %.2f"
      % mean_squared_error(y_test, y_pred))
print('Variance score: %.2f' % r2_score(y_test, y_pred))
"""
说明如下：
一、如果使用下载的Iris数据集，可适用下列方式加载：
def iris_type(s):
    it={b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}
    return it[s]
path = 'iris.data.txt' #假定数据存在当前路径下
data0=np.loadtxt(path,dtype=float,delimiter=',',converters={4:iris_type})
data, target = np.split(data0,(4,),axis=1)
target = target.ravel()
X_train, X_test, y_train, y_test = train_test_split(
    data, target, test_size=0.3, random_state=0)
注意：可能是数据格式的原因，需要在字符串前面加一个b，形式如下： it={b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}。如果不加b，可能回报如下错误：KeyError: b'Iris-setosa'

二、LogisticRegression是一个函数，使用时如果忘记加()，将会报如下错误：
TypeError: fit() missing 1 required positional argument: 'y'
此时把LR.fit(X_train, y_train)改成LR().fit(X_train, y_train)即可。

三、使用LogisticRegression函数时，需要加上multi_class='auto', solver = 'lbfgs'这两个参数，否则出现警告：
FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.
FutureWarning: Default multi_class will be changed to 'auto' in 0.22. Specify the multi_class option to silence this warning.

四、Variance score
方差分数越接近1，说明模型越好。
"""

