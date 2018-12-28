# coding: utf-8
import requests
import itchat
import random
import threading
import time
import datetime
import WriteExcel3

KEY = '2c425e188d5e4d58ad23798f634cddf3'
AUTOFLAG = False
SettingStep = -1
TMSetting = ['您好，欢迎使用印臣微信定时提醒吃药服务，请输入您每天吃药的时间，时间采用24小时制，不同的时间之间用逗号隔开。形式如下：09:00，13:00，20:00。输入完成后直接点击发送即完成微信吃药提醒设置。', '设置成功，感谢您的信任。印臣']

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

def friendsInfo():
    friends = itchat.get_friends(update= True)
    return friends

def my_friends(friendsInfo):
    usersInfo = dict()
    for friend in friendsInfo[1:]:
        sex = "其他"
        if friend["Sex"] == 1:
            sex = "男性"
        elif friend["Sex"] == 2:
            sex = "女性"
        usersInfo[friend["NickName"]] = [friend["City"], friend["Province"], sex, friend["Signature"], friend['UserName']]
        #print(i["Signature"])
    return usersInfo

def auto_reply(usersInfo, NickName):
    robots=['——李印臣']
    title = ""
    if usersInfo[NickName][2] == "男性":
        title = "少爷"
    elif usersInfo[NickName][2] == "女性":
        title = "大小姐"

    reply = ''
    if usersInfo[NickName][1] != '':
        reply = "来自" + usersInfo[NickName][1] + "省"
    if usersInfo[NickName][0] != '':
        reply = reply + usersInfo[NickName][0] + "市"
    if reply != '':
        reply = reply + "的"
    
    #reply = get_response(msg['Text'])+random.choice(robots)
    reply = reply + NickName  + title + "您好，印臣给您拜年了!" +random.choice(robots)
    return reply

def remind(usersInfo, NickName):
    robots='——李印臣'
    title = ""
    #if usersInfo[NickName][2] == "男性":
 #       title = "少爷"
 #   elif usersInfo[NickName][2] == "女性":
 #       title = "大小姐"
    
    remind = NickName  + title + "您好，印臣提醒您吃药了!" + robots
    #查找用户的userid
    itcaht_user_name = itchat.search_friends(name=NickName)[0]['UserName']
    #利用send_msg发送消息
    print(itcaht_user_name)
    itchat.send_msg(remind,toUserName=itcaht_user_name)
    
def timerfun(sched_time) :
    flag = 0
    while True:
        now = datetime.datetime.now()
        if now > sched_time and now < sched_time + datetime.timedelta(seconds=1) :  # 因为时间秒之后的小数部分不一定相等，要标记一个范围判断
            remind('', '李')
            time.sleep(1)    # 每次判断间隔1s，避免多次触发事件
            flag = 1
        else :
             #print('schedual time is {0}'.format(sched_time))
             #print('now is {0}'.format(now))
            if flag == 1 :
                #datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]]) 
                sched_time = sched_time + datetime.timedelta(seconds=5)  # 把目标时间增加一个小时，一个小时后触发再次执行
                flag = 0

def isAuto(text):
    global AUTOFLAG
    if text == '撩你':
        AUTOFLAG = True
    elif text == '下去吧':
        AUTOFLAG = False
    return AUTOFLAG

def whichSettingStep(text):
    global SettingStep
    if text == '设置':
        SettingStep = 0
    #elif text == '去吧':
    else:
        strs = text.split('[,:.。]')
        print(strs)
        SettingStep = False
    return ISSETTING

@itchat.msg_register(itchat.content.FRIENDS)
def deal_with_friend(msg):
    tmp = msg['Content']
    content = tmp[tmp.find('content=') + 9:].split('\"')[0].strip()
    if content is not None and content != '':
        if content == '吃药提醒':
            itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
            itchat.send_msg(TMSetting[0], msg['RecommendInfo']['UserName'])

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    usersInfo = my_friends(friendsInfo())
    #WriteExcel.writeUsersInfo(usersInfo)
    reply = ''
    if isAuto(msg['Text']):
        reply = get_response(msg['Text'])+'——纯机器人'
    else:
        reply = auto_reply(usersInfo, msg['User']['NickName'])
    defaultReply = 'I received: ' + msg['Text']
    
    return reply or defaultReply
#WriteExcel3.writeUsersInfo("")
#itchat.auto_login(enableCmdQR=True)
itchat.auto_login()

#sched_time = datetime.datetime(2018,12,28,12,53,10)   #设定初次触发事件的时间点
#print('run the timer task at {0}'.format(sched_time))
#th = threading.Timer(5, timerfun, ([sched_time]))
#th.start()
remind('', "36")
#itchat.auto_login(hotReload=True)
itchat.run()


