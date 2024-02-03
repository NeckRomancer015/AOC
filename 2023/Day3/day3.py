import re
from collections import defaultdict
specialCharacters = ['/','!','#','$','%','%','^','&','*','(',')','+','=','-','_',]

def checkAround(grid, x, y):    
        for r in [-1,0,1]:
            for c in [-1,0,1]:
                if 0<=x+r<len(grid) and 0<=y+c<len(grid[x]):
                    if grid[x+r][y+c].isdigit() or grid[x+r][y+c] == '.':
                        continue
                    else:
                        return True
        return False


def checkAround2(grid, x, y):    
        for r in [-1,0,1]:
            for c in [-1,0,1]:
                if 0<=x+r<len(grid) and 0<=y+c<len(grid[x]):
                    if grid[x+r][y+c] == '*':
                        return (True,[x+r,y+c])
        return (False,[x+r,y+c])

def p1(grid):
    plus2 = 2
    sum = 0
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            temp = grid[r][c]
            if temp.isnumeric():
                if c>0:
                    if grid[r][c-1].isnumeric():
                        continue
                if r>0 and r<len(grid): 
                    if grid[r-1][c] != '.' and not grid[r-1][c].isnumeric():#directly above
                        t = str(grid[r][c])
                        if grid[r][c+1].isnumeric():
                            t+= str(grid[r][c+1])
                        if grid[r][c+2].isnumeric():
                            t+= str(grid[r][c+2])
                        sum+=int(t)
                        continue                    
                    if grid[r-1][c+1] != '.' and not grid[r-1][c+1].isnumeric():           #above middle
                        t = str(grid[r][c])
                        if grid[r][c+1].isnumeric():
                            t+= str(grid[r][c+1])
                        if grid[r][c+2].isnumeric():
                            t+= str(grid[r][c+2])
                        sum+=int(t)
                        continue                        
                    if grid[r-1][c+2] != '.' and not grid[r-1][c+2].isnumeric(): #above right
                        t = str(grid[r][c])
                        if grid[r][c+1].isnumeric():
                            t+= str(grid[r][c+1])
                        if grid[r][c+2].isnumeric():
                            t+= str(grid[r][c+2])
                        sum+=int(t)
                        continue  
                    if grid[r+1][c]!='.' and not grid[r+1][c].isnumeric():#bottom left
                        t = str(grid[r][c])
                        if grid[r][c+1].isnumeric():
                            t+= str(grid[r][c+1])
                        if grid[r][c+2].isnumeric():
                            t+= str(grid[r][c+2])
                        sum+=int(t)
                        continue  
                    if grid[r+1][c+1]!='.' and not grid[r+1][c+1].isnumeric():#bottom middle
                        t = str(grid[r][c])
                        if grid[r][c+1].isnumeric():
                            t+= str(grid[r][c+1])
                        if grid[r][c+2].isnumeric():
                            t+= str(grid[r][c+2])
                        sum+=int(t)
                        continue  
                    if grid[r+1][c+2]!='.' and not grid[r+1][c+2].isnumeric():#bottom right
                        t = str(grid[r][c])
                        if grid[r][c+1].isnumeric():
                            t+= str(grid[r][c+1])
                        if grid[r][c+2].isnumeric():
                            t+= str(grid[r][c+2])
                        sum+=int(t)
                        continue  
                    if (c < len(grid[r])-3):
                        if grid[r-1][c+3] !='.' and not grid[r-1][c+3].isnumeric(): #above right diagonal
                            t = str(grid[r][c])
                            if grid[r][c+1].isnumeric():
                                t+= str(grid[r][c+1])
                            if grid[r][c+2].isnumeric():
                                t+= str(grid[r][c+2])
                            sum+=int(t)
                            continue  
                        if grid[r][c+3]!='.' and not grid[r][c+3].isnumeric(): #right
                            t = str(grid[r][c])
                            if grid[r][c+1].isnumeric():
                                t+= str(grid[r][c+1])
                            if grid[r][c+2].isnumeric():
                                t+= str(grid[r][c+2])
                            sum+=int(t)
                            continue  
                        if (grid[r+1][c+3]!='.' and not grid[r+1][c+3].isnumeric()): #bottom right diagonal
                            t = str(grid[r][c])
                            if grid[r][c+1].isnumeric():
                                t+= str(grid[r][c+1])
                            if grid[r][c+2].isnumeric():
                                t+= str(grid[r][c+2])
                            sum+=int(t)
                            continue  
                    if c> 1:
                        if grid[r-1][c-1]!='.' and not grid[r-1][c+3].isnumeric(): #left diagonal
                            t = str(grid[r][c])
                            if grid[r][c+1].isnumeric():
                                t+= str(grid[r][c+1])
                            if grid[r][c+2].isnumeric():
                                t+= str(grid[r][c+2])
                            sum+=int(t)
                            continue  
                        if grid[r][c-1]!='.' and not grid[r][c-1].isnumeric():                   #left 
                            t = str(grid[r][c])
                            if grid[r][c+1].isnumeric():
                                t+= str(grid[r][c+1])
                            if grid[r][c+2].isnumeric():
                                t+= str(grid[r][c+2])
                            sum+=int(t)
                            continue  
                elif r == 0:
                    if grid[r+1][c]!='.' and not grid[r+1][c].isnumeric():#bottom left 
                        t = str(grid[r][c])
                        if grid[r][c+1].isnumeric():
                            t+= str(grid[r][c+1])
                        if grid[r][c+2].isnumeric():
                            t+= str(grid[r][c+2])
                        sum+=int(t)
                        continue  
                    if grid[r+1][c+1]!='.' and not grid[r+1][c+1].isnumeric():#bottom middle  
                        t = str(grid[r][c])
                        if grid[r][c+1].isnumeric():
                            t+= str(grid[r][c+1])
                        if grid[r][c+2].isnumeric():
                            t+= str(grid[r][c+2])
                        sum+=int(t)
                        continue  
                    if grid[r+1][c+2]!='.' and not grid[r+1][c+2].isnumeric():#bottom right  
                        t = str(grid[r][c])
                        if grid[r][c+1].isnumeric():
                            t+= str(grid[r][c+1])
                        if grid[r][c+2].isnumeric():
                            t+= str(grid[r][c+2])
                        sum+=int(t)
                        continue  
                    if c>1:
                        if grid[r][c-1]!='.' and not grid[r][c-1].isnumeric():                   #left 
                            t = str(grid[r][c])
                            if grid[r][c+1].isnumeric():
                                t+= str(grid[r][c+1])
                            if grid[r][c+2].isnumeric():
                                t+= str(grid[r][c+2])
                            sum+=int(t)
                            continue  
                    if (c < len(grid[r])-2):
                        if grid[r][c+3]!='.' and not grid[r][c+3].isnumeric(): #right  
                            t = str(grid[r][c])
                            if grid[r][c+1].isnumeric():
                                t+= str(grid[r][c+1])
                            if grid[r][c+2].isnumeric():
                                t+= str(grid[r][c+2])
                            sum+=int(t)
                            continue  
                        if (grid[r+1][c+3]!='.' and not grid[r+1][c+3].isnumeric()): #bottom right diagonal  
                            t = str(grid[r][c])
                            if grid[r][c+1].isnumeric():
                                t+= str(grid[r][c+1])
                            if grid[r][c+2].isnumeric():
                                t+= str(grid[r][c+2])
                            sum+=int(t)
                            continue  
                elif r == len(grid):
                    if grid[r-1][c] != '.' and not grid[r-1][c].isnumric():#directly above  
                        t = str(grid[r][c])
                        if grid[r][c+1].isnumeric():
                            t+= str(grid[r][c+1])
                        if grid[r][c+2].isnumeric():
                            t+= str(grid[r][c+2])
                        sum+=int(t)
                        continue  
                    if grid[r-1][c+1] != '.' and not grid[r-1][c+1].isnumric():           #above middle  
                        t = str(grid[r][c])
                        if grid[r][c+1].isnumeric():
                            t+= str(grid[r][c+1])
                        if grid[r][c+2].isnumeric():
                            t+= str(grid[r][c+2])
                        sum+=int(t)
                        continue              
                    if grid[r-1][c+2] != '.' and not grid[r-1][c+2].isnumric(): #above right  
                        t = str(grid[r][c])
                        if grid[r][c+1].isnumeric():
                            t+= str(grid[r][c+1])
                        if grid[r][c+2].isnumeric():
                            t+= str(grid[r][c+2])
                        sum+=int(t)
                        continue  
                    if (c < len(grid[r])-2):
                        if grid[r-1][c+3] !='.' and not grid[r-1][c+3].isnumeric(): #above right diagonal  
                            t = str(grid[r][c])
                            if grid[r][c+1].isnumeric():
                                t+= str(grid[r][c+1])
                            if grid[r][c+2].isnumeric():
                                t+= str(grid[r][c+2])
                            sum+=int(t)
                            continue  
                        if grid[r][c+3]!='.' and not grid[r][c+3].isnumeric(): #right   
                            t = str(grid[r][c])
                            if grid[r][c+1].isnumeric():
                                t+= str(grid[r][c+1])
                            if grid[r][c+2].isnumeric():
                                t+= str(grid[r][c+2])
                            sum+=int(t)
                            continue  


                    
                    


    return sum


def p1v2(grid):
    rows = len(grid)
    columns = len(grid[0])
    currentN=''
    total=0
    has_gear = False
    for r in range(0,rows):
        for c in range(0,columns+1):
            if c< columns and grid[r][c].isdigit():
                temp = grid[r][c]
                currentN+=temp
                if(checkAround(grid,r,c)):
                    has_gear=True
                
            elif has_gear:
                total+=int(currentN)
                has_gear=False
                currentN=''
            else:
                has_gear= False    
                currentN=''
    return total


def p2(grid):
    rows = len(grid)
    columns = len(grid[0])
    currentN=''
    total=0

    mapOfGears = defaultdict(list)
    for r in range(0,rows):
        coords= set()
        for c in range(0,columns+1):
            if c< columns and grid[r][c].isdigit():
                temp = grid[r][c]
                currentN+=temp
                flag, crd = checkAround2(grid, r, c)
                x,y = crd
                if flag:
                    coords.add((crd[0],crd[1]))
            elif currentN!='':
                for coord in coords:
                    mapOfGears[coord].append(int(currentN))   
                currentN=''
                coords= set()
            else:
                currentN=''
    
    for gear,num in mapOfGears.items():
        if len(num) == 2:
            total+= num[0]*num[1]
    return total
    

with open('input.txt') as input:
    grid = []
    for line in input:
        line = line.replace('\n',"")
        grid.append(line)
    print(p2(grid))


