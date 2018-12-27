# coding: utf-8
import requests
import itchat
import random

itchat.auto_login()

itchat.send('Hello, filehelper', toUserName='filehelper')

import requests
import itchat
import random

KEY = '2c425e188d5e4d58ad23798f634cddf3'

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

def my_friends():
    friends = itchat.get_friends(update= True)
    return friends

def my_friends_sex(friends):

    total = len(friends[1:])
    print(total)
    for i in friends[1:]:
        print(i["NickName"])
        print(i["City"])
        print(i["Province"])
        print(i["Signature"])
        print(i["Sex"])
        

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    my_friends_sex(my_friends())
    print(msg.text)
    print(msg.fromUserName)
    result = itchat.search_friends()
    print(result)
#    author = itchat.search_friends(nickName='李印臣「哲艺科心」')[0]
#    author.send('greeting, 36!')
    defaultReply = 'I received: ' + msg['Text']
    robots=['——李印臣','——印臣','——Jacklee']
    reply = get_response(msg['Text'])+random.choice(robots)
    return reply or defaultReply

#itchat.auto_login(enableCmdQR=True)
itchat.auto_login()
#itchat.auto_login(hotReload=True)
itchat.run()


