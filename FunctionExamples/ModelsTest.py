import numpy as np
from sklearn.linear_model import LogisticRegression  #导入逻辑回归模型
from sklearn.linear_model import LinearRegression #导入线性回归模型
from sklearn.tree import DecisionTreeRegressor #导入树回归模型
from sklearn.svm import SVR #导入支持向量机模型
from sklearn.neighbors import KNeighborsRegressor #导入K-近邻模型

td = np.mat(np.random.randint(10, size=(10, 6)))
pd = np.mat(np.random.randint(10, size=(4, 6)))
tdx = td[:,0:5]
tdy = td[:,5]
pdx = pd[:,0:5]
pdy = pd[:,5]

def predict(clf):
    #order：'C' — 按行，'F' — 按列，'A' — 原顺序，'k' — 元素在内存中的出现顺序
    clf.fit(tdx, np.ravel(tdy,order='C'))
    return clf.predict(pdx)

ret = predict(LogisticRegression())
ret2 = predict(LinearRegression())
ret3 = predict(DecisionTreeRegressor())
ret4 = predict(SVR())
ret5 = predict(KNeighborsRegressor())

for i in range(len(ret)):
    print(str(np.array(pdy)[i][0]) + " : " + str(ret[i]) + " : " + str(int(ret2[i])) + " : "
          + str(int(ret3[i])) + " : " + str(int(ret4[i])) + " : " + str(int(ret5[i])))
