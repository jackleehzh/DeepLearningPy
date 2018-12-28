# coding: utf-8
import requests
import itchat
import random

KEY = '2c425e188d5e4d58ad23798f634cddf3'
AUTOFLAG = False

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
        usersInfo[friend["NickName"]] = [friend["City"], friend["Province"], sex, friend["Signature"]]
        #print(i["Signature"])
    return usersInfo

def auto_reply(usersInfo, NickName):
    robots=['——李印臣']
    title = "您"
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

def isAuto(text):
    global AUTOFLAG
    if text == '撩你':
        AUTOFLAG = True
    elif text == '下去吧':
        AUTOFLAG = False
    return AUTOFLAG

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    usersInfo = my_friends(friendsInfo())
 #   WriteExcel.writeUsersInfo(usersInfo)
    
        
    reply = ''
    if isAuto(msg['Text']):
        reply = get_response(msg['Text'])+'——纯机器人'
    else:
        reply = auto_reply(usersInfo, msg['User']['NickName'])
    defaultReply = 'I received: ' + msg['Text']
    
    return reply or defaultReply

#itchat.auto_login(enableCmdQR=True)
itchat.auto_login()
#itchat.auto_login(hotReload=True)
itchat.run()


