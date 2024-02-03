
import re
from collections import Counter

def getPattern(numbers :list):
    difference = []
    for i in range(len(numbers)-1,0,-1):
        difference.append(int(numbers[i])-int(numbers[i-1]))
    
    difference.reverse()
    return difference

def insertLoop(numbers:list)->int:    
    difference = getPattern(numbers)
    
    if difference.count(difference[0]) == len(difference):
        numbers.append(int(numbers[-1])+int(difference[0]))
        return int(numbers[-1])
    else:
        ans  =int(insertLoop(difference))
        numbers.append(int(numbers[-1])+ans)
        return int(numbers[-1])


def insertLoop2(numbers:list)->int:    
    difference = getPattern(numbers)
    
    if difference.count(difference[0]) == len(difference):
        numbers.insert(0,int(numbers[0])-int(difference[0]))
        return int(numbers[0])
    else:
        ans  =int(insertLoop(difference))
        numbers.insert(0,int(numbers[0])-ans)
        return int(numbers[0])

part1 = 0
part2 = 0
with open('input.txt') as input:
    for line in input:
        line = line.strip()
        numbers = re.split(' ', line)
        part1 += insertLoop(numbers=numbers)
        numbers.reverse()
        part2 += insertLoop(numbers=numbers)
    print(part1)
    print(part2)