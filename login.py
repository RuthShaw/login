#!-*- coding:utf -8-*-
''' 编写登陆接口
    输入用户名密码
    认证成功后显示欢迎界面
    输入三次后锁定 '''
import pickle
import time

f = open('wrongNum.txt', 'rb')
wrongNum = pickle.load(f)
f.close()
f = open('wrongTime.txt', 'rb')
wrongTime = pickle.load(f)
f.close()

# create the dict to save the users' info.
codes = open('userInfo.txt','r')
users = dict()
for line in codes:
    line = line.strip().split(' ')
    name = line[0]
    users[name] = line[1]

# judge whether the info. is right
i=0    # 输错名字最多运行三次
while i < 3:
    # create the login page
    name = input("Name : ")
    if name in users:
        if time.time() - wrongTime[name] > 60:  # 距离上次错误时间是否过了1min
            wrongNum[name] = 0
        while int(wrongNum[name]) < 3:
            #print(wrongNum[name])
            code = input("Code : ")
            inputTime = time.time()   # inputTime现在是输入密码的时间
            if users[name] == code:
                print("Welcome to the secret garden %s" % name)
                wrongTime[name] = time.time()
                wrongNum[name] = 0
                break
            else :
                print("the password is wrong")
                temp = int(wrongNum[name])
                temp += 1
                wrongNum[name] = str(temp)
                print(inputTime - wrongTime[name])

                if inputTime - wrongTime[name] > 60:  # 距离上次错误时间是否过了1min
                    wrongNum[name] = 0  # 如果超过1min，错误次数归0
                    print(wrongNum[name])
                wrongTime[name] = time.time()
        if int(wrongNum[name]) == 3:
            print("Please try again after 1 min!")

        break

    else:
        print(name,"is not the user!")
        i += 1
# import time
# save the variables
f = open('wrongNum.txt', 'wb')
pickle.dump(wrongNum, f)
f.close()
f = open('wrongTime.txt', 'wb')
pickle.dump(wrongTime, f)
f.close()



