import os
import re
scores = dict()

try:
    for line in open('stream.txt', 'rt'):
        name,surname,score = re.split(' +',line.strip())
        fullName = name+' '+surname
        try:
            scores[fullName]+=float(score)
        except KeyError:
            scores[fullName] = float(score)
        except:
            print("Not a number")
except IOError as e:
    print(os.strerror(e.errno))


for k in sorted(scores.keys()):
    print(k, ' ', scores[k])

import platform
print(platform.uname())

import datetime

print(datetime.date.today())

import time
print(time.time())

d = datetime.date.fromtimestamp(time.time())
print(d)

print(datetime.date.today())

t = datetime.time(hour=23, minute=59,second=59,microsecond=9, fold=1)
print(t)
