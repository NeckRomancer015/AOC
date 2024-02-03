grid = []
coords = []
num = ['1','2','3','4','5','6','7','8','9']
with open('example.txt') as input:
    for line in input:
        grid.append(list(line.strip()))
    count = 1
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                grid[r][c] = count
                count+=1
            if (grid[r][c]) in num:
                coords.append([r,c])
    for r in grid:
        print(r)

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))
answer = 0
seen = []
for firstPair in range(len(coords)):
    for secondPair in range(len(coords)):
        if coords[firstPair] == coords[secondPair]:
            continue
        if (coords[firstPair], coords[secondPair]) in seen or (coords[secondPair], coords[firstPair]) in seen:
            continue
        answer +=manhattan(coords[firstPair], coords[secondPair])
        
        seen.append((coords[firstPair],coords[secondPair]))
print(coords)
print(answer)