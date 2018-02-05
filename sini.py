#__author:  ruthshaw
#date:      2018/2/4

import pickle
import time


codes = open('userInfo.txt','r')
users = dict()
users2 = dict()
#users['time'] = time.time()

for line in codes:
    lines = line.strip().split(' ')
    name = lines[0]
    users[name] = 0
    users2[name] = time.time()
codes.close()


f = open('wrongNum.txt', 'wb')
pickle.dump(users,f)
f.close()
f = open('wrongTime.txt', 'wb')
pickle.dump(users2,f)
f.close()