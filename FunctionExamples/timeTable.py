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

dict0 = {'05:00':', 该起床啦', 
        '05:05':', 快去洗刷吧。别忘了把水烧上',
        '05:20':', 该跑步了哦，坚持就是胜利',
        '06:00':',  每天洗个澡，愉快一整天',
        '06:20':', 做个冥想，全天一目了然',
        '06:30':', 吃早饭啦，鸡蛋、咸菜和煎饼早点',
        '07:00':', 开始学习吧，别忘了您的家庭责任',
        '10:00':', 再学一小时，就开始做饭啦',
        '11:00':', 做一个大菜，接满水桶，烧足热水',
        '12:30':', 午休二十分钟，下午精神倍儿爽',
        '12:50':', 开始下午的学习吧',
        '16:50':',  休息一下吧，下午的学习任务结束啦',
        '17:00':', 吃晚饭喽，记得刷锅刷碗啊',
        '18:00':', 晚上学习开始啦，坚持就是胜利',
        '20:50':', 休息吧，当天任务完成',
        '21:00':', 回顾总结这一天都干了啥，干得怎么样',
        '21:40':', 做做明天的计划吧',
        '22:00':', 洗刷吧，养成睡前刷牙洗脸的好习惯',
        '22:30':', 睡觉啦，良好的休息是效率的保障',
}

engineio = pyttsx3.init()

while True:
    if str in dict0:
        engineio.say('现在是' + str + dict0[str])
        engineio.runAndWait()
    else:
        time.sleep(60)
