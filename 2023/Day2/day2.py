'''12 red , 13 green , and 14 blue'''
import re



    
def combo(g : str):
    for day in g:
        cubes = day.split(",")

        for c in cubes:
            if c.__contains__('r'):
                num = c.replace("r","")
                num = num.replace(" ","")
                s = int(num)
                if s>12 :
                    return False
            if c.__contains__('g'):
                num = c.replace("g","")
                num = num.replace(" ","")
                s = int(num)
                if s>13 :
                    return False
            if c.__contains__('b'):
                num = c.replace("b","")
                num = num.replace(" ","")
                s = int(num)
                if s>14 :
                    return False
    
    return True
            
def combo2(g : str):
    mr = 0
    mg=0
    mb=0
    for day in g:
        cubes = day.split(",")
        for c in cubes:
            if c.__contains__('r'):
                num = c.replace("r","")
                num = num.replace(" ","")
                s = int(num)
                if s > mr:
                    mr=s
            if c.__contains__('g'):
                num = c.replace("g","")
                num = num.replace(" ","")
                s = int(num)
                if s > mg:
                    mg=s
            if c.__contains__('b'):
                num = c.replace("b","")
                num = num.replace(" ","")
                s = int(num)
                if s > mb:
                    mb=s
    return mr*mb*mg

def P1():
    total=0
    with open('input.txt') as input:
        gameId = 1
        for line in input:
            rep = "Game "+str(gameId)+": "
            line = line.replace(rep, "")
            line= line.replace(" red","r")
            line= line.replace(" blue","b")
            line= line.replace(" green","g")
            line= line.replace("\n","")
            combos = re.split(";", line)
            if combo(combos):
                total+=gameId                
            gameId+=1
                
    return total



def P2():
    total=0
    with open('input.txt') as input:
        gameId = 1
        for line in input:
            rep = "Game "+str(gameId)+": "
            line = line.replace(rep, "")
            line= line.replace(" red","r")
            line= line.replace(" blue","b")
            line= line.replace(" green","g")
            line= line.replace("\n","")
            combos = re.split(";", line)
            total += combo2(combos)               
            gameId+=1
                
    return total
print(P2())


