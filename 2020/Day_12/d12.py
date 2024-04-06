from typing import List
import math
class ship():
    def __init__(self) -> None:
        self.direction='E'
        self.N =0
        self.S=0
        self.W = 0
        self.E = 0
    
    def __str__(self) -> str:
        return "N = {N}, S = {S}, E= {E}, W= {W} , D={D}".format(N=self.N, S=self.S, E=self.E, W=self.W, D=self.direction)

    def __repr__(self) -> str:
        return "D: {d}, NEWS: {N}{E}{W}{S}".format(N=self.N, S=self.S, E=self.E, W=self.W, D=self.direction)

    def getManhattan(self)->int:
        x= abs(self.E-self.W)
        y = abs(self.N-self.S)
        print(x,"+",y)
        return x+y

def move(ferry:ship, action:str, number:int):
    match ferry.direction:
        case 'E':
            ferry.E +=number
        case 'W':
            ferry.W+=number
        case 'S':
            ferry.S+=number
        case 'N':
            ferry.N+=number

def rotate(ferry:ship, action: str, number:int)->None:
    nesw = ['N','E','S','W']
    if number == 180:
        ferry.direction = nesw[(nesw.index(ferry.direction)+2)%len(nesw)]    
    elif (action == "R" and number ==90) or (action == 'L' and number == 270):
        ferry.direction = nesw[(nesw.index(ferry.direction)+1)%len(nesw)]
    elif (action == "L" and number ==90) or (action == 'R' and number == 270):
        ferry.direction = nesw[(nesw.index(ferry.direction)-1)%len(nesw)]

def processAction(ferry:ship, nav:str):
    action,number = nav[0],int(nav[1:])
    if action == 'F':
        move(ferry=ferry, action=action, number=number)
    elif action == "R" or action== 'L':
        rotate(ferry=ferry, action=action,number=number)
    elif action == 'N':
        ferry.N+=number
    elif action=='S':
        ferry.S+=number
    elif action=='E':
        ferry.E+=number
    elif action=='W':
        ferry.W+=number


def getInput(FilePath:str)->List[str]:
    navigation = list()
    with open(FilePath) as file:
        for line in file:
            navigation.append(line.strip())
    
    return navigation

def p1(navigation:List[str]):
    ferry = ship()
    for nav in navigation:
        processAction(ferry=ferry,nav=nav)
    
    print("Part 1 Answer is: ", ferry.getManhattan())

def main():
    p1(getInput(r"2020\Day_12\input.txt"))

if __name__ == '__main__':
    main()