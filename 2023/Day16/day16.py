heatedGrid=set()
grid=[]
part1v2Seen = set()
part1v2Skip = set()

def isSplitter(r,c)->int:
    '''returns 1 for - and -1 for |'''
    if grid[r][c] =='-':
        return 1
    if grid[r][c] == '|':
        return -1
    return 0


def isMirror(r,c)->int:
    """ returns 1 for \\ and -1 for /"""
    if grid[r][c] == '\\':
        return 1 # 1 equals backslash
    if   grid[r][c] == '/':
        return -1
    return 0



heatedNonEmptyGrid = set()

def part1v2(r:int,c:int,direction:str):
    if part1v2Skip.__contains__(((r,c), direction)) or r<0 or c<0 or r==len(grid) or c>len(grid[r]):
        return
    part1v2Seen.add((r,c))
    part1v2Skip.add(((r,c), direction))


    if direction == 'r':
        if c == len(grid[0]):
            return

        while True:
            if c == len(grid[0]):
                return
            if grid[r][c] == '.':
                part1v2Seen.add((r,c))
                part1v2Skip.add(((r,c), direction))
                c+=1
            else:
                break
        
        mirror = isMirror(r,c)
        if mirror == 1:
            part1v2(r+1,c,'d')
            return
        elif mirror == -1:
            part1v2(r-1,c,'u')
            return
        else:
            split =isSplitter(r,c)
            if split == 1:
                part1v2(r,c+1,'r')
                return
            elif split == -1:
                part1v2(r-1,c,'u')
                part1v2(r+1,c,'d')
                return
    elif direction == 'l':
        if c<0:
            return
    

        while True:
            if c<0:
                return
            if grid[r][c] == '.':
                part1v2Seen.add((r,c))
                part1v2Skip.add(((r,c), direction))
                c-=1
            else:
                break
        
        mirror = isMirror(r,c)
        if mirror == 1:
            part1v2(r-1,c,'u')
            return
        elif mirror == -1:
            part1v2(r+1,c,'d')
            return
        else:
            split = isSplitter(r,c)
            if split == 1:
                part1v2(r,c-1, 'l')
                return
            elif split == -1:
                part1v2(r+1,c,'d')
                part1v2(r-1,c,'u')
                return
    
    elif direction == 'd':
        if r==len(grid):
            return
        
        while True:
            if r==len(grid):
                return
            if grid[r][c] == '.':
                part1v2Seen.add((r,c))
                part1v2Skip.add(((r,c), direction))
                r=r+1
            else:
                break
        
        mirror = isMirror(r,c)

        if mirror == 1:
            part1v2(r,c+1,'r')
            return
        elif mirror ==-1:
            part1v2(r,c-1,'l')
            return
        else:
            split = isSplitter(r,c)
            if split==1:
                part1v2(r,c+1,'r')
                part1v2(r,c-1,'l')
                return
            elif split==-1:
                part1v2(r+1,c,'d')
                return
    
    elif direction == 'u':
        if r<0:
            return
        
        while True:
            if r<0:
                return
            if grid[r][c]=='.':
                part1v2Seen.add((r,c))
                part1v2Skip.add(((r,c), direction))
                r=r-1
            else:
                break
        
        mirror =isMirror(r,c)
        if mirror == 1:
            part1v2(r,c-1,'l')
            return
        elif mirror == -1:
            part1v2(r,c+1,'r')
            return
        else:
            split= isSplitter(r,c)
            if split ==1:
                part1v2(r,c+1,'r')
                part1v2(r,c-1,'l')
                return
            elif split ==-1:
                part1v2(r-1,c,'u')
                return


            


def part1(r:int,c:int, direction:str):
    if direction == 'r':
        if c+1 >= len(grid[r]):
            return
        else:
            c=c+1
            if heatedGrid.__contains__(((r,c), direction)):
                return
            heatedGrid.add(((r,c), direction))
            heatedNonEmptyGrid.add((r,c))
            while True:
                if grid[r][c] == '.':
                    if c+1>=len(grid[r]):
                        return
                    else:
                        c=c+1
                        if heatedGrid.__contains__(((r,c),direction)):
                            return
                    heatedGrid.add(((r,c), direction))
                    heatedNonEmptyGrid.add((r,c))
                else:
                    break
            
            mirror = isMirror(r,c)
            if mirror !=0:
                if mirror==1:
                    part1(r,c,'d')
                    return
                else:
                    part1(r,c,'u')
                    return
            else:
                splitter = isSplitter(r,c)
                if splitter == 1:
                    part1(r,c,'r')
                    return
                elif splitter==-1:
                    part1(r,c,'u')
                    part1(r,c,'d')
                    return
    elif direction== 'l':
        if c-1<0:
            return
        else:
            c=c-1
            if heatedGrid.__contains__(((r,c), direction)):
                return
            heatedGrid.add(((r,c), direction))
            heatedNonEmptyGrid.add((r,c))
            while True:
                if grid[r][c] == '.':
                    if c-1<0:
                        return
                    else:
                        c=c-1
                        if heatedGrid.__contains__(((r,c),direction)):
                            return
                    
                    heatedGrid.add(((r,c), direction))
                    heatedNonEmptyGrid.add((r,c))
                else:
                    break

            
            mirror = isMirror(r,c)
            if mirror!=0:
                if mirror == 1:
                    part1(r,c,'u')
                    return
                elif mirror == -1:
                    part1(r,c,'d')
                    return
            else:
                splitter = isSplitter(r,c)
                if splitter==1:
                    part1(r,c,'l')
                    return
                elif splitter == -1:
                    part1(r,c,'d')
                    part1(r,c,'u')
                    return
    elif direction == 'd':
        if r+1 >= len(grid):
            return
        else:
            r=r+1
            if heatedGrid.__contains__(((r,c), direction)):
                return
            heatedGrid.add(((r,c), direction))
            
            heatedNonEmptyGrid.add((r,c))
            while True:
                if grid[r][c]=='.':
                    if r+1>=len(grid):
                        return
                    else:
                        r=r+1
                        if heatedGrid.__contains__(((r,c),direction)):
                            return
                    
                    heatedNonEmptyGrid.add((r,c))
                    heatedGrid.add(((r,c), direction))
                else:
                    break
            
            mirror = isMirror(r,c)
            if mirror!=0:
                if mirror==1:
                    part1(r,c,'r')
                    return
                else:
                    part1(r,c,'l')
                    return
            else:
                splitter = isSplitter(r,c)
                if splitter==1:
                    part1(r,c,'l')
                    part1(r,c,'r')
                    return
                else:
                    part1(r,c,'d')
                    return
    elif direction == 'u':
        if r-1 <0:
            return
        else:
            r=r-1
            if heatedGrid.__contains__(((r,c), direction)):
                return
            
            heatedNonEmptyGrid.add((r,c))
            heatedGrid.add(((r,c), direction))
            while True:
                if grid[r][c]=='.':
                    if r-1<0:
                        return
                    else:
                        r=r-1
                        if heatedGrid.__contains__(((r,c),direction)):
                            return
                    
                        heatedNonEmptyGrid.add((r,c))
                        heatedGrid.add(((r,c), direction))
                else:
                    break
            
            mirror = isMirror(r,c)
            if mirror !=0:
                if mirror==1:        
                    part1(r,c,'l')
                    return
                else:
                    part1(r,c,'r')  
                    return      
            else:
                splitter=isSplitter(r,c)
                if splitter==1:
                    part1(r,c,'r')
                    part1(r,c,'l')
                    return
                else:
                    part1(r,c,'u')  
                    return  
    else:
        print(direction)



with open('input.txt') as input:
    for line in input:
        line = line.strip()
        line=line.strip('\n')
        grid.append(list(line))

for g in grid:
    print(g)

# heatedGrid.add(((0,0),'r'))
# heatedNonEmptyGrid.add((0,0))
# part1(0,0,'r')
# print(len(heatedNonEmptyGrid))


newGrid=[]
ans=0
for r in range(len(grid)):        
    tempGrid= ''
    for c in range(len(grid[0])):
        if part1v2Skip.__contains__(((r,c), 'd'))or part1v2Skip.__contains__(((r,c), 'r'))or part1v2Skip.__contains__(((r,c), 'u'))or part1v2Skip.__contains__(((r,c), 'l')):
            tempGrid+='#'
            ans+=1
        else:
            tempGrid+='.'
    print(tempGrid)
    tempGrid=''

print(ans)


part1v2(0,0,'r')

# for s in part1v2Skip:
#     print(s)


print(len(part1v2Seen))
