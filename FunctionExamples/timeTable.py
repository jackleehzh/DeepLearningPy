# coding:utf-8
import pyttsx3
import engineio
import wx

import time

class TimeTable(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Time Table', size=(300, 300))
        panel = wx.Panel(self, -1)
        self.button = wx.Button(panel, -1, 'confirm', pos=(50, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

    def OnClick(self, event):
        self.button.SetLabel('Clicked!')

str = time.strftime('%H:%M',time.localtime(time.time()))

dict0 = {'05:00':', 李印臣, 该起床啦', 
        '05:05':', 李印臣, 快去洗刷吧。别忘了把水烧上',
        '05:20':', 李印臣, 该跑步了哦，坚持就是胜利',
        '06:00':', 李印臣, 每天洗个澡，愉快一整天',
        '06:20':', 李印臣, 做个冥想，全天一目了然',
        '06:30':', 李印臣, 吃早饭啦，鸡蛋、咸菜和煎饼早点',
        '07:00':', 李印臣, 开始学习吧，别忘了您的家庭责任',
        '07:50':', 李印臣, 休息，休息一下',
        '08:00':', 李印臣, 调整好状态，学习又开始啦',
        '08:50':', 李印臣, 休息一下，劳逸结合',
        '09:00':', 李印臣, 学习啦，到你表演的时间啦',
        '09:50':', 李印臣, 放松一下吧，休息十分钟',
        '10:00':', 李印臣, 再学一小时，就开始做饭啦',
        '11:00':', 李印臣, 做一个大菜，接满水桶，烧足热水',
        '12:30':', 李印臣, 午休二十分钟，下午精神倍儿爽',
        '12:50':', 李印臣, 开始下午的学习吧',
        '13:40':', 李印臣, 休息，休息一下',
        '13:50':', 李印臣, 下午第二轮学习，开启啦',
        '14:40':', 李印臣, 休息一下，劳逸结合',
        '14:50':', 李印臣, 学习开始啦，加油加油',
        '15:40':', 李印臣, 休息十分钟，全身好轻松',
        '15:50':', 李印臣, 开始学习吧',
        '16:50':', 李印臣, 休息一下吧，下午的学习任务结束啦',
        '17:00':', 李印臣, 吃晚饭喽，记得刷锅刷碗啊',
        '18:00':', 李印臣, 晚上学习开始啦，坚持就是胜利',
        '18:50':', 李印臣, 休息休息吧',
        '19:00':', 李印臣, 再学一段吧',
        '19:50':', 李印臣, 休息调整一下',
        '20:00':', 李印臣, 最后一波学习啦，胜利就在眼前',
        '20:50':', 李印臣, 休息吧，当天任务完成',
        '21:00':', 李印臣, 回顾总结这一天都干了啥，干得怎么样',
        '21:40':', 李印臣, 做做明天的计划吧',
        '22:00':', 李印臣, 洗刷吧，养成睡前刷牙洗脸的好习惯',
        '22:30':', 李印臣, 睡觉啦，良好的休息是效率的保障'}

engineio = pyttsx3.init()

#app = wx.App()
#frame = ButtonFrame()
#frame.Show()
#app.MainLoop()

#for key in dict0:
#    engineio.say('现在是' + key + dict0[key])
#    engineio.runAndWait()

while True:
    if str in dict0:
        engineio.say('现在是' + str + dict0[str])
        engineio.runAndWait()
    else:
        time.sleep(10)
