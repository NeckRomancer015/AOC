from typing import List

def getInput(InputPath:str)->List[int]:
    Input = []
    with open(InputPath) as file:
        for line in file:
            Input.append(int(line.strip()))
        file.close()
    return Input

def p1(Input : List[int]) -> None:
    Input.sort()
    diff = [0,1]
    currentV = 0
    for i in Input:
        if i -currentV == 1:
            diff[0]=diff[0]+1
        elif i- currentV == 3:
            diff[1]=diff[1]+1
        else:
            print("Wrong")
        currentV = i
    
    print(diff[0]*diff[1])


def main():
    Input = getInput(r'2020\Day_10\input.txt')
    p1(Input=Input)

if __name__ == '__main__':
    main()