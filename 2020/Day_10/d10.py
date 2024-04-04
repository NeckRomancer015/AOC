from typing import List

def getInput(InputPath:str)->List[int]:
    Input = []
    with open(InputPath) as file:
        for line in file:
            Input.append(int(line.strip()))
        file.close()
    return Input

def p2(Input: List[int]) ->None:    
    Input.insert(0,0)
    totalVariations = 0    
    n = len(Input)
    totalVariations = [0] * n
    totalVariations[0] = 1  

    for i in range(1, n):
        for j in range(i):
            if Input[i] - Input[j] <= 3:
                totalVariations[i] += totalVariations[j]

    print("Part 2 Answer is: ", totalVariations[n-1])


def p1(Input : List[int]) -> None:
    Input.sort()
    diff = [0,1]
    currentV = 0
    for i in Input:
        if i -currentV == 1:
            diff[0]+=1
        elif i- currentV == 3:
            diff[1]+=1
        else:
            print("Wrong")
        currentV = i
    
    print(diff[0]*diff[1])
    
def main():
    Input = getInput(r'2020\Day_10\input.txt')
    p1(Input=Input)
    p2(Input=Input)

if __name__ == '__main__':
    main()