grid = []


def p1(g):
       
    for i in range(len(g)-1):
        isHorizontal = True
        for ii in range(len(g)):
            up = i - ii
            down = i+ii+1
            if 0<=up<down<len(g):
                for c in range(len(g[0])):
                    if g[up][c]!=g[down][c]:
                        isHorizontal = False
                        break
        if isHorizontal:
            return ((i+1)*100)


    for c in range(len(g[0])-1):
        isVertical = True
        for cc in range(len(g[0])):
            left = c-cc
            right = c+cc+1
            if 0<=left<right<len(g[0]):                
                for r in range(len(g)):
                    if g[r][left] != g[r][right]:
                        isVertical = False
                        break
        if isVertical:
            print("Vertical: ", c," ",c+1, "VerticalAnswer:", c+1)
            return c+1
    


total = 0
with open('input.txt') as input:
    nextGrid = False
    for line in input:
        line= line.strip().strip('\n')
        if line == "":
            total+=p1(grid)
            grid= []
            nextGrid = True
            continue
        grid.append(list(line))

total+=p1(grid)
print(total)