def Travelling(grid :list, right=3, down=1)->int:
    numOfTrees = 0
    currentPoint = [0,0]
    outOfBounds = len(grid)
    rowSize = len(grid[0])
    while True:
        if currentPoint[0] > outOfBounds-1:
            break
        if grid[currentPoint[0]][currentPoint[1]] == '#':
            numOfTrees+=1
        currentPoint[0] +=down 
        currentPoint[1] =(currentPoint[1]+right) % rowSize
    
    return numOfTrees

def getInput(InputPath:str)->list:
    grid=[]
    with open(InputPath) as file:
        for line in file:
            grid.append(list(line.strip()))
    
    return grid

def p2(grid:list, p1Answer:int)->int:    
    part2 = [[1,1], [5,1], [7,1],[1,2]]
    p2Answer = p1Answer
    for combo in part2:
        p2Answer*= Travelling(grid=grid, right=combo[0], down=combo[1])
    
    return p2Answer

def main():
    grid = getInput(r"2020\Day 3\input.txt")
    p1Answer = Travelling(grid=grid)
    print("Part 1 answer is : ", p1Answer)
    print("Part 2 answer is : ", p2(grid=grid,p1Answer=p1Answer))
    

if __name__ == '__main__':
    main()