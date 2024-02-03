
verticalGrid = []
horizontalGrid = []

def p1(vG, hG):
    verticalAnswer = 1
    for c in range(len(vG[0])):
        columnEqual = True
        for r in range(len(vG)):
            if vG[r][c] != vG[r][c+1]:
                columnEqual = False
                break
        if columnEqual:
            print("Vertical: ", c," ",c+1)
            vG+=c
            break

    print(verticalAnswer)
    horizontalAnswer = 0
    for i in range(len(hG)):
        if hG[i] == hG[i+1]:
            print(i+1, i+2)
            horizontalAnswer = (i+1)*100
            break
    print(horizontalAnswer)
    return (horizontalAnswer+verticalAnswer)


total = 0
with open('input.txt') as input:
    populateHorizontalGrid = False
    for line in input:
        line= line.strip().strip('\n')
        print(line)
        if line == "" and populateHorizontalGrid:
            total+=p1(verticalGrid,horizontalGrid)
            verticalGrid= []
            horizontalGrid= []
            populateHorizontalGrid= False
            continue
        if line  == "" and populateHorizontalGrid==False:
            populateHorizontalGrid = True
            continue
        if not populateHorizontalGrid:
            verticalGrid.append(list(line))
        else:
            horizontalGrid.append(list(line))


print(total)