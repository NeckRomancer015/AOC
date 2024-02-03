


grid = []
newGrid = []
with open('input.txt') as input:
    for line in input:
        grid.append(list(line.strip().strip('\n')))
    

# for r in grid:
#     print(r)
# print()

R= len(grid)
C = len(grid[0])

# for c in range(C):
#     tempList = []
#     for r in range(R):
#         tempList.append(grid[r][c])
#     newGrid.append(tempList)

for c in range(C):
    for r in range(R):
        for rr in range(R):
            if grid[rr][c] == 'O' and rr>0 and grid[rr-1][c]=='.':
                grid[rr][c]='.'
                grid[rr-1][c]='O'


# for r in grid:
#     print(r)

total=0
for  r in range(R):
    for c in range(C):
        if grid[r][c]=='O':
            total+=R-r

print(total)