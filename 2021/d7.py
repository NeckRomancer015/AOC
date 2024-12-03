import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions
import re

def p1(f):
    lowest_fuel = None
    crabs = []
    for line in common_functions.read_file_line_by_line(f):
        crabs = common_functions.retrieve_numbers.get_numbers_as_int_in_list(line)
    
    crabs.sort()
    smallest_crab,biggest_crab = crabs[0], crabs[-1]

    
    for i in range(smallest_crab,biggest_crab+1):
        current_fuel =0
        for crab in crabs:
            current_fuel+=abs(crab-i)
        if lowest_fuel==None or lowest_fuel>current_fuel:
            lowest_fuel=current_fuel

    print(f"Part 1: {lowest_fuel}")

def p2(f):    
    lowest_fuel = None
    crabs = []
    for line in common_functions.read_file_line_by_line(f):
        crabs = common_functions.retrieve_numbers.get_numbers_as_int_in_list(line)
    
    crabs.sort()
    smallest_crab,biggest_crab = crabs[0], crabs[-1]

    
    for i in range(smallest_crab,biggest_crab+1):
        current_fuel =0
        steps=0
        for crab in crabs:
            steps=abs(crab-i)
            current_fuel += sum([step for step in range(1,steps+1)])
        if lowest_fuel==None or lowest_fuel>current_fuel:
            lowest_fuel=current_fuel

    print(f"Part 2: {lowest_fuel}")


def main():
    f=r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"
    p1(f)
    p2(f)

if __name__ == '__main__':
    main()