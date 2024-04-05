from typing import List
from copy import deepcopy

def getInput(FilePath:str)->List[List[str]]:
    grid : List[List[str]] = []
    with open(FilePath) as file:
        for line in file:
            grid.append(list(line.strip()))
    file.close()
    return grid

def CheckIfSeatsEmptyOrFilled(r:int, c:int, grid:List[List[str]]):
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
                if grid[r][c] == '.':
                    continue
                else:
                    if grid[r][c] == 'L' and CheckIfSeatsEmptyOrFilled(r,c,grid) == 0:
                        newGrid[r][c]='#'
                        movement=True
                    elif grid[r][c] == '#' and CheckIfSeatsEmptyOrFilled(r,c,grid) >=4:
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


def main():
    p1grid = getInput(r"2020\Day_11\input.txt")
    p2Grid = deepcopy(p1grid)
    p1(getInput(r"2020\Day_11\input.txt"))

if __name__=='__main__':
    main()