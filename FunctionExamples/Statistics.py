#coding:utf-8

import xlrd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.matplotlib_fname() #将会获得matplotlib包所在文件夹

filename = '/Users/jacklee/Desktop/collection.xlsx'

workbook = xlrd.open_workbook(filename)
Data_sheet = workbook.sheets()[0]

rowNum = Data_sheet.nrows
colNum = Data_sheet.ncols

def printResult(tmpDict):
    tmp = sorted(tmpDict.items(), key=lambda item:item[1], reverse = True)
    for t in tmp:
        print(t[0] + " : " + str(t[1]))

def drawPic(tmpDict):
    plt.rcParams['font.sans-serif'] = u'SimHei'
 #   plt.rcParams['font.family']='sans-serif'
 #   plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    label_list = tmpDict.keys()    # 横坐标刻度显示值
    num_list1 = tmpDict.values()       # 纵坐标值1
    x = range(len(num_list1))
    """
    绘制条形图
    left:长条形中点横坐标
    height:长条形高度
    width:长条形宽度，默认值0.8
    label:为后面设置legend准备
    """
    rects1 = plt.bar(left=x, height=num_list1, width=0.4, alpha=0.8, color='red', label="一部门")
    plt.ylim(0, 50)     # y轴取值范围
    plt.ylabel("数量")
    """
    设置x轴刻度显示值
    参数一：中点坐标
    参数二：显示值
    """
    plt.xticks([index + 0.2 for index in x], label_list)
    plt.xlabel("年份")
    plt.title("某某公司")
    plt.legend()     # 设置题注
    # 编辑文本
    for rect in rects1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
    plt.show()


Tables = dict()
Sexs = dict()
Provinces = dict()
Cities = dict()
for i in range(rowNum - 1):
    i = i + 1
    table = Data_sheet.cell_value(i, 3)
    sex = Data_sheet.cell_value(i, 4)
    province = Data_sheet.cell_value(i, 5)
    city = Data_sheet.cell_value(i, 6)
    Tables[table] = Tables.get(table, 0) + 1
    Sexs[sex] = Sexs.get(sex, 0) + 1
    Provinces[province] = Provinces.get(province, 0) + 1
    Cities[city] = Cities.get(city, 0) + 1

printResult(Tables)
drawPic(Tables)
printResult(Sexs)
drawPic(Sexs)
printResult(Provinces)
drawPic(Provinces)
printResult(Cities)
drawPic(Cities)
