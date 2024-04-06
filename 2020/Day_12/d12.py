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

    def setAbsValues(self)->None:
        if self.N >0 and self.S>0:
            if self.N>self.S:
                self.N-=self.S
                self.S=0
            elif self.S>self.N:
                self.S-=self.N
                self.N=0
            else:
                self.S,self.N=0,0
        if self.E>0 and self.W>0:
            if self.E>self.W:
                self.E-=self.W
                self.W=0
            elif self.W>self.E:
                self.W-=self.E
                self.E=0
            else:
                self.W,self.E = 0,0

def move(boat:ship, action:str, number:int):
    match boat.direction:
        case 'E':
            boat.E +=number
        case 'W':
            boat.W+=number
        case 'S':
            boat.S+=number
        case 'N':
            boat.N+=number

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
        move(boat=ferry, action=action, number=number)
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

def processActionToWaywordPoint(ferry:ship,wp:ship, nav:str):
    action,number = nav[0],int(nav[1:])
    if action in ['N','E','S','W']:
        wp.direction = action
        move(wp,action=action,number=number)
        wp.setAbsValues()

    elif action in ['R','L']:
        if number==180:
            wp.N,wp.S,wp.E,wp.W = wp.S,wp.N,wp.W,wp.E
        elif (action == "R" and number ==90) or (action == 'L' and number == 270):
            wp.E, wp.S,wp.W,wp.N=wp.N,wp.E,wp.S,wp.W
        elif (action == "L" and number ==90) or (action == 'R' and number == 270):
            wp.N, wp.E, wp.S, wp.W = wp.E, wp.S, wp.W, wp.N
    
    elif action == 'F':
        if wp.N>0:
            ferry.N+=(wp.N*number)
        if wp.S>0:
            ferry.S+=(wp.S*number)
        if wp.E>0:
            ferry.E+=(wp.E*number)
        if wp.W>0:
            ferry.W+=(wp.W*number)
        
        ferry.setAbsValues()
            


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

def p2(navigation:List[str]):
    ferry=ship()
    wayward_point = ship()
    wayward_point.E = 10
    wayward_point.N = 1

    for nav in navigation:
        processActionToWaywordPoint(ferry=ferry,wp=wayward_point,nav=nav)
    
    print("Part 2 Answer is: ", ferry.getManhattan())

def main():
    navigation = getInput(r"2020\Day_12\input.txt")
    p1(navigation)
    p2(navigation)

if __name__ == '__main__':
    main()