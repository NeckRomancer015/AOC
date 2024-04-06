from typing import List
from copy import deepcopy

def getInput(FilePath:str)->List[List[str]]:
    grid : List[List[str]] = []
    with open(FilePath) as file:
        for line in file:
            grid.append(list(line.strip()))
    file.close()
    return grid


def checkSeatsInSight(r,c,grid:List[List[str]])->int:
    occ =0
    for sight_r in [-1,0,1]:
        for sight_c in [-1,0,1]:
            if sight_c==sight_r==0:continue
            rowLineOfSight = sight_r
            columnLineOfSight = sight_c
            while 0 <= r+rowLineOfSight < len(grid) and 0 <= c+columnLineOfSight < len(grid[0]):
                if grid[rowLineOfSight+r][columnLineOfSight+c] == '#':
                    occ+=1
                    break
                elif grid[rowLineOfSight+r][columnLineOfSight+c] == 'L':
                    break
                rowLineOfSight+=sight_r
                columnLineOfSight+=sight_c 
    
    return occ
                        


def CheckIfSeatsEmptyOrFilled(r:int, c:int, grid:List[List[str]])->int:
    occ=0
    for adj_r in [-1,0,1]:
        for adj_c in [-1,0,1]:
            if adj_r==adj_c==0:continue
            if 0<=c+adj_c < len(grid[0]) and 0<=r+adj_r <len(grid):
                if grid[r+adj_r][c+adj_c] == '#':
                    occ+=1
        
    return occ 

def p1(grid: List[List[str]])->None:
    count=0
    while True:
        movement=False
        newGrid = deepcopy(grid)
        for r in range(0,len(grid)):
            for c in range(0,len(grid[r])):                
                occ = CheckIfSeatsEmptyOrFilled(r,c,grid)
                if grid[r][c] == '.':
                    continue
                else:
                    if grid[r][c] == 'L' and occ == 0:
                        newGrid[r][c]='#'
                        movement=True
                    elif grid[r][c] == '#' and occ >=4:
                        newGrid[r][c]='L'
                        movement=True     

        grid=newGrid
        if not movement:
            break
        count+=1
        
    
    EmptySeats = 0
    for row in grid:
        EmptySeats+=sum(1 for r in row if r =='#')
        
    print("Iterations for Part 1: ",count)
    
    
    print("Part 1 Answer is: ", EmptySeats)


def p2(grid:List[List[str]]):

    count=0
    while True:
        movement=False
        newGrid = deepcopy(grid)
        for r in range(0,len(grid)):
            for c in range(0,len(grid[r])):
                occ = checkSeatsInSight(r,c,grid) 
                if grid[r][c] == '.':
                    continue
                else:
                    if grid[r][c] == 'L' and occ == 0:
                        newGrid[r][c]='#'
                        movement=True
                    elif grid[r][c] == '#' and occ >=5:
                        newGrid[r][c]='L'
                        movement=True
        grid=newGrid
        if not movement:
            break
        count+=1

    EmptySeats = 0
    for row in grid:
        EmptySeats+=sum(1 for r in row if r =='#')

    print("Iterations for Part 2: ",count)
    
    
    print("Part 2 Answer is: ", EmptySeats)

def main():
    p1grid = getInput(r"2020\Day_11\input.txt")
    p2Grid = deepcopy(p1grid)
    p1(p1grid)
    p2(p2Grid)
if __name__=='__main__':
    main()