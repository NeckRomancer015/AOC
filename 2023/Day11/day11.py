import re
from collections import defaultdict, Counter
grid = []

coords = []
with open('input.txt') as input:
    for line in input:
        grid.append(list(line.strip()))
    count = 1
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                grid[r][c] = count
                coords.append([r,c])
                count+=1
    for r in grid:
        print(r)
    
    listOfColumns = []
    listOfROws = []
    for r in range(len(grid)):
        addRow=True
        for c in range(len(grid[0])):
            if grid[r][c] !='.':
                addRow=False
        if addRow:
            listOfROws.append(r)
    
    for c in range(len(grid[0])):
        add = True
        for r in range(len(grid)):
            if grid[r][c]!='.':
                add = False
        if add:
            listOfColumns.append(c)

print(listOfROws)
print(listOfColumns)
print(coords)



for r in range(len(grid)):
    for c in range(len(grid[r])):
        print(str(grid[r][c]), end  = "", sep="")
    print()

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def IncrementAnswer(a,b):
    count=0
    for r in listOfROws:
        if a[0]<r and b[0]>=r:
            count+=1
    for c in listOfColumns:
        if a[1]<c and b[1]>=c:
            count+1
    return count

def p1():
    for coord in coords:
        origR = coord[0]
        origC = coord[1]
        for r in listOfROws:
            if origR>r:
                coord[0]=coord[0]+1
        for c in listOfColumns:
            if origC> c:
                coord[1] = coord[1]+1

def p2():
    for coord in coords:
        origR = coord[0]
        origC = coord[1]
        for r in listOfROws:
            if origR>r:
                coord[0]=coord[0]+(1000000-1)
        for c in listOfColumns:
            if origC> c:
                coord[1] = coord[1]+(1000000-1)
# for coord in coords:
#     origR = coord[0]
#     origC = coord[1]
#     for r in listOfROws:
#         if origR>r:
#             coord[0]=coord[0]+1
#     for c in listOfColumns:
#         if origC> c:
#             coord[1] = coord[1]+1
p2()
answer = 0
seen = []
print(coords)
# for firstPair in range(len(coords)):
#     for secondPair in range(len(coords)):
#         if coords[firstPair] == coords[secondPair]:
#             continue
#         if (coords[firstPair], coords[secondPair]) in seen or (coords[secondPair], coords[firstPair]) in seen:
#             continue
#         answer +=manhattan(coords[firstPair], coords[secondPair])
        
#         seen.append((coords[firstPair],coords[secondPair]))

for firstPair in range(len(coords)):
    for secondPair in range(firstPair+1, len(coords)):
        if coords[firstPair] == coords[secondPair]:
            continue
        if (coords[firstPair], coords[secondPair]) in seen or (coords[secondPair], coords[firstPair]) in seen:
            continue
        answer +=manhattan(coords[firstPair], coords[secondPair])

        seen.append((coords[firstPair],coords[secondPair]))



print(answer)