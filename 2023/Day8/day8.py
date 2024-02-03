import re
from Node import Node
from collections import defaultdict
directions = 'LRLRLRLRRLRRRLRLRLRRRLLRRLRRLRRLLRRLRRLRLRRRLRRLLRRLRRRLRRLRRRLRRRLLLRRLLRLLRRRLLRRLRLLRLLRRRLLRRLRRLRRRLRRLRLRRLRRLRLLRLRRRLRLRRLRLLRRLRRRLRRLRLRRLLLRRLRRRLRRRLRRLRRRLRLRRLRRLRRRLRRLRRLRRLRRLRRRLLRRRLLLRRRLRRLRRRLLRRRLRRLRRLLLLLRRRLRLRRLRRLLRRLRRLRLRLRRRLRRRLRRLLLRRRR'
from math import gcd
mapOfNodes = dict()
currentNode = None
mapofStartingNodes=[]
def p1(currentNode):
    length = len(directions)
    count = 0
    steps = 0
    while True:
        if count>=length:
            count= 0
        curDir= directions[count]
        leftChild,rightChild = mapOfNodes[currentNode]
        if curDir == 'L':
            currentNode = leftChild
        else:
            currentNode = rightChild
        steps+=1
        if currentNode == 'ZZZ':
            break
        count+=1

    print(steps)

def p2(startingNodes :list):
    nextNodesToVist= set()
    
    step =0
    count = 0
    length = len(directions)
    while True:
        if count >=length:
            count=0
        curDir= directions[count]
        for node in startingNodes:
            leftChild,rightChild = mapOfNodes[node]
            if curDir == 'L':
                nextNodesToVist.add(leftChild)
            else:
                nextNodesToVist.add(rightChild)
        step+=1
        breakLoop = True
        for i in nextNodesToVist:
            if i[-1] != 'Z':
                breakLoop = False
                break
        if breakLoop:
            break
        else:
            count+=1
            startingNodes= []
            startingNodes = list(nextNodesToVist)
            nextNodesToVist.clear()
    print(step)


def lcm(a):
    lc = 1
    for i in a:
        lc = lc*i//gcd(lc, i)
    return lc

def p2v2(v2):
    ans = 1
    z = []
    for i in v2:
        steps =0
        count = 0
        length = len(directions) 
        currentNode = i
        while True:
            if count>=length:
                count= 0
            curDir= directions[count]
            leftChild,rightChild = mapOfNodes[currentNode]
            if curDir == 'L':
                currentNode = leftChild
            else:
                currentNode = rightChild
            steps+=1
            if currentNode[-1] == 'Z':
                break
            count+=1
            
        z.append(steps)
    print(lcm(z))

with open('input.txt') as input:
    for line in input:
        a,b = re.split(' = ', line)
        Name  = a.strip()
        leftChild, rightChild = b.split(', ')
        leftChild = leftChild.strip().strip('\(').strip()
        rightChild = rightChild.strip().strip('\)\n').strip()
        if Name == 'AAA':
            currentNode = Name
        if Name[-1] == 'A':
            mapofStartingNodes.append(Name)
        mapOfNodes[Name] = (leftChild,rightChild)

print(mapofStartingNodes)
##p1(currentNode)

p2v2(mapofStartingNodes)