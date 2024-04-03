import math

def getInput(InputPath:str)->list:
    rows = []
    with open(InputPath) as file:
        for line in file:
            rows.append(line.strip())
    
    return rows

def getRowAndSeat(instruction:str):
    minR=0
    maxR = 127
    minS = 0
    maxS =7

    for r in range(0,6):
        if instruction[r]=='F':
            maxR=(minR+maxR)//2
        elif instruction[r]=='B':
            minR =math.ceil((minR+maxR)/2)

    row=0
    if instruction[6] == 'F':
        row = minR
    else:
        row=maxR

    for s in range(7,9):
        if instruction[s] == 'L':
            maxS = (minS+maxS)//2
        else:
            minS=math.ceil((minS+maxS)/2)
    S=0
    if 'L' == instruction[-1]:
        S=minS
    else:
        S=maxS
    
    #print(row, S)
    return (row*8)+S

def p1(rows:list)->None:
    maxID=0
    for row in rows:
        seatID = getRowAndSeat(row)
        if seatID>maxID:
            maxID=seatID
    
    
    print("Part 1 Answer: ", maxID)

def p2(rows:list)->None:    
    listOfSeats = []
    for row in rows:
        listOfSeats.append(getRowAndSeat(row))
    listOfSeats.sort()

    seatID = 0
    for i in range(1,len(listOfSeats)):
        if listOfSeats[i]-2== listOfSeats[i-1]:
            seatID= listOfSeats[i]-1
            break

    print("Part 2 Answer: ", seatID)


def main():
    p1(getInput(r"2020\Day 5\input.txt"))
    p2(getInput(r"2020\Day 5\input.txt"))



if __name__ == '__main__':
    main()


