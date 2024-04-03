from typing import List

def getInput(InputPath:str)->List[int]:
    Input = []
    with open(InputPath) as file:
        for line in file:
            Input.append(int(line.strip()))
        file.close()
    return Input

def validateP1(currentNum:int, preambleList : List[int])->bool:
    for i in range(0,len(preambleList)-1):
        for j in range(i, len(preambleList)):
            if preambleList[i]+preambleList[j] == currentNum:
                return True
    return False

def p1(Input : List[int], preamble : int) -> int:
    
    for i in range(preamble, len(Input)):
        tempList = Input[i-preamble:i]
        if  not validateP1(currentNum=Input[i], preambleList=tempList):
            return Input[i]
    
    return -1


def p2(targetNum :int, Input: List[int])->int:
    currentIndex = 0
    contigiousList = []
    contigiousList.append(Input[currentIndex])
    maxIndex = len(Input)
    while True:
        if sum(contigiousList) == targetNum:
            print("Min: ",min(contigiousList),' Max: ',max(contigiousList))
            return min(contigiousList)+max(contigiousList)
        if sum(contigiousList) > targetNum:
            del contigiousList[0]
            continue
        if sum(contigiousList) < targetNum:
            currentIndex+=1
            contigiousList.append(Input[currentIndex])
        if maxIndex == currentIndex:
            print("Part 2 Failed")
            return -1

def main():
    Input = getInput(r"2020\Day 9\input.txt")
    p1Answer = p1(Input=Input, preamble=25)
    print("Part 1 answer is: ", p1Answer) if p1Answer !=-1 else print("Failed")
    print("Part 2 answer is: ",p2(targetNum=p1Answer, Input=Input))

if __name__ == '__main__':
    main()