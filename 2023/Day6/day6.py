import re



def p1(Time:list, Dist:list):
    count=1

    for i in range(len(Time)):
        t = int(Time[i])
        tempCount = 0
        for j in range(int(Time[i])):
            speed = j*t
            if speed > int(Dist[i]):
                tempCount+=1
            t=t-1
        count = count * tempCount
    return count

def p2(Time, Distance):
    count = 0
    t = int(Time)
    for j in range(int(Time)):
        speed = j*t
        if speed > int(Distance):
            count+=1
        t=t-1
    
    return count
with open('input.txt') as input:
    TimeFlag = False
    DistanceArray=[]
    TimeArray=[]
    for line in input:
        _,line = re.split(':',line)
        line = line.strip()
        if not TimeFlag:
            TimeFlag = True            
            TimeArray = re.findall('\d+',line)
        else:
            DistanceArray = re.findall('\d+',line)
    print(TimeArray)
    print(DistanceArray)
    print(p1(TimeArray,DistanceArray))
    stringTimeArray = ''
    stringDistArray = ''
    for i in TimeArray:
        stringTimeArray+=i
    for d in DistanceArray:
        stringDistArray+=d
    print(stringTimeArray)
    print(stringDistArray)
    print(p2(stringTimeArray,stringDistArray))