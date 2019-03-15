#显示信息
# encoding=utf8 
import sys
import importlib
import time
import remind
import threading

def loadData(filename):
    list0 = []
    dict0 = {}
    count = 0
    f = open(filename, encoding='utf8')

    while True:
        line = f.readline()
        if not line:
            break

        list0.append(line)
        num = line[line.rfind('【') + 1:-2]
        dict0[num] = count
        count = count + 1
            
    f.close()
    return list0, dict0

def loadInfo(filename):
    list0 = []
    f = open(filename, encoding='utf8')

    while True:
        line = f.readline()
        if not line:
            break

        list0.append(line)
           
    f.close()
    return list0

def initInfo(filename1, filename2):
    f = open(filename1, encoding='utf8')
    f2 = open(filename2, 'w', encoding='utf8')
    count = 0
#重点等级（1-3），难点等级（1-3），疑点（1-3），记忆次数,
#本次是否通过，开始学习时间，最后学习时间
    key = 0
    diffcult = 0
    doubt = 0
    rememberTimes = 0
    isOK = 0
    time1 = 0
    time2 = 0
    while True:
        line = f.readline()
        if not line:
            break
        
        line = line.strip()
        num = line[line.rfind('【') + 1:-1]
        print(num + ' ' + str(key) + ' ' + str(diffcult) + ' ' + str(doubt)
            + ' ' + str(rememberTimes) + ' ' + str(isOK) + ' ' + str(time1)
            + ' ' + str(time2), file=f2) 
        count = count + 1
            
    f.close()
    f2.close()

def maxNum(filename):
    f = open(filename, encoding='utf8')
    count = 0
    maxnum = 0
  
    while True:
        line = f.readline()
        if not line:
            break

        line = line.strip()
        if count > 0:
            num = int(line[line.rfind('【') + 1:-1]) 
            if num > maxnum:
                maxnum = num
                
        count = count + 1
    print(maxnum)            
    f.close()

filename1 = '/Users/jacklee/Desktop/2020.txt'
filename2 = '/Users/jacklee/Desktop/2020-2.txt'
#loadData(filename1)
#loadInfo(filename2)

def getTime(list0):
    list5 = []
    for a in list0:
        if(len(a.strip()) > 7):
            arr = a.split(' ')
            b = int(arr[6])
            list5.append(b)
    return list5

def remind(list0):
    while True:
        for a in list0:
 #           if int(time.time() - a) < 100:
 #               print(int(time.time() - a))
            remind.remind(0, int(time.time() - a))

def show(filename1, filename2):
    list0, dict0 = loadData(filename1)
    list2 = loadInfo(filename2)
    list4 = getTime(list2)
    t = threading.Thread(target=remind,args=(list4,))
    t.setDaemon(True) ## thread1,它做为程序主线程的守护线程,当主线程退出时,thread1线程也会退出,由thread1启动的其它子线程会同时退出,不管是否执行完任务
    t.start()
    layer = 0
    uplayerBeginline = 0
    sameLayer = False
    while True:
        count = 0
        count2 = 0
        list3 = [0]
        begin = False
        
        for a in list0:
            c = a.count('	')
            a = a.strip()
            
            if begin and c < layer:
                uplayerBeginline = list3[0]
                break
            if c < layer - 1:
                sameLayer = False
            if c == layer - 1 and sameLayer == False:
                list3[0] = count
                sameLayer = True
            if c == layer and count >= uplayerBeginline:
                begin = True
                if count2 == 0:
                    print('0.\t返回上一层')
                count2 = count2 + 1                      
                print(str(count2) + '.\t' + a)
                list3.append(count)
 
            count = count + 1
                
        print('a.\t增加内容')
        print('d.\t删除内容')
        print('m.\t修改内容')
        print('e.\t退出')
        print(list3)
        list2 = updateInfo(list3, list2)
        writeFile(filename2, list2)
        num = input("请输入：")
        if num == 'e':
            return
        else:
            num = int(num)
        if num == -1:
            break
        if num == 0:
            layer = layer - 1
        else:
            layer = layer + 1
        uplayerBeginline = list3[num]
        
    return list3

def updateInfo(list0, list2):
    key = 0
    diffcult = 0
    doubt = 0
    rememberTimes = 0
    isOK = 0
    time1 = 0
    time2 = 0
    num = 0
    for a in list0:
        
        if(len(list2[a].strip()) < 7):
            continue
        arr = list2[a].split(' ')
        num = arr[0]
        key = int(arr[1])
        diffcult = int(arr[2])
        doubt = int(arr[3])
        rememberTimes = int(arr[4])
        isOK = int(arr[5])
        time1 = int(arr[6])
        time2 = int(time.time())
        print(time2)
        if time1 == 0:
            time1 = time2
        
        #print(num + ' ' + str(key) + ' ' + str(diffcult) + ' ' + str(doubt)
 #           + ' ' + str(rememberTimes) + ' ' + str(isOK) + ' ' + str(time1)
 #           + ' ' + str(time2))
        list2[a] = num + ' ' + str(key) + ' ' + str(diffcult) + ' ' + str(doubt) + ' ' + str(rememberTimes) + ' ' + str(isOK) + ' ' + str(time1) + ' ' + str(time2)
    return list2

def writeFile(filename, list0):
    f = open(filename, 'w', encoding='utf8')
    for a in list0:
        if len(a.strip()) > 7:
            print(a, file=f)
    f.close()
    

#updateInfo()
show(filename1, filename2)
#remind.remind(0, 0)
