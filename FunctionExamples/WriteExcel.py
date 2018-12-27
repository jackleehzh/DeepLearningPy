from xlrd import open_workbook
from xlutils.copy import copy
import xlwt
import os

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()   # 初始化样式
    font = xlwt.Font()       # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height

    style.font = font
    return style
def writeUsersInfo(usersInfo):
    excel = ""
    rows = 1
    if os.path.exists("collection.xls"):
        rexcel = open_workbook("collection.xls") # 用wlrd提供的方法读取一个excel文件
        rows = rexcel.sheets()[0].nrows # 用wlrd提供的方法获得现在已有的行数
        excel = copy(rexcel) # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    else:
        excel = xlwt.Workbook(encoding='utf-8')
        table = excel.add_sheet("微信好友信息列表")
        style = set_style('Arial', 220, True)
        table.write(0, 0, "序号", style)
        table.write(0, 1, "昵称", style)
        table.write(0, 2, "姓名", style)
        table.write(0, 3, "标签", style)
        table.write(0, 4, "性别", style)
        table.write(0, 5, "省份", style)
        table.write(0, 6, "城市", style)
        table.write(0, 7, "付费金额", style)
        table.write(0, 8, "个性签名", style)
    table = excel.get_sheet(0) # 用xlwt对象的方法获得要操作的sheet
    
    row = rows
    for key in usersInfo:
        table.write(row, 0, row) # xlwt对象的写方法，参数分别是行、列、值
        table.write(row, 1, key)
        table.write(row, 4, usersInfo[key][2])
        table.write(row, 5, usersInfo[key][1])
        table.write(row, 6, usersInfo[key][0])
        table.write(row, 8, usersInfo[key][3])
        row += 1
    excel.save("collection.xls") # xlwt对象的保存方法，这时便覆盖掉了原来的excel
