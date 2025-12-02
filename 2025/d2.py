import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
from common_functions import *
from functools import cache

def is_valid(number:str)->bool:
    if len(number)>1:
        if len(number) %2  ==0:
            if number[0:len(number)//2] == number[len(number)//2:]:
                return False
    return True

@cache
def is_valid_p2(number:str)->bool:
    if len(number)>1: # number greater than 9
       if number.count(number[0]) == len(number):
            return False
       
       factors = math_functions.find_factors_optimized(len(number))
       if len(factors) <= 2: # 2 digit number
           return True
       
       mid = len(factors)//2
       first_half = factors[:mid]
       second_half = factors[mid:]
       if len(factors)%2 != 0: # this will include the squareroot of a number (only tricky part of this thing)
           first_half.append(factors[mid])
       second_half.reverse()# so we don't have to do fancy list comprehension

       for i in range(1,len(first_half)):
        first_pattern = number[0:first_half[i]]
        first_pattern_count = number.count(first_pattern)
        if  first_pattern_count == second_half[i]:
            return False
        second_pattern = number[0:second_half[i]] 
        second_pattern_count = number.count(second_pattern)
        if second_pattern_count == first_half[i]:
            return False
    return True

def p1():
    data = open(r'C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt').read().strip('\n').replace('\n','')
    numbers = data.split(",")
    count =0
    for pairs in numbers:
        pair = pairs.split('-')
        for id in range(int(pair[0]),int(pair[1])+1):
            if not is_valid(str(id)):
                count+=id
    
    print(f"Part 1: {count}")
        

def p2():
    data = open(r'C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt').read().strip('\n').replace('\n','')
    numbers = data.split(",")
    count =0
    for pairs in numbers:
        pair = pairs.split('-')
        for id in range(int(pair[0]),int(pair[1])+1):
            if not is_valid_p2(str(id)):
                count+=id
    
    print(f"Part 2: {count}")

def main():
    p1()
    p2()

if __name__ == '__main__':
    main()