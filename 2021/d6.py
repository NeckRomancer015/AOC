import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions
import re


def p1(f):
    todays_fish = []
    for line in common_functions.read_file_line_by_line(f):
        todays_fish = common_functions.retrieve_numbers.get_numbers_as_int_in_list(line)
    
    for i in range(80):
        tomorrows_fish=[]

        for fish in todays_fish:
            if fish>0:
                tomorrows_fish.append(fish-1)
            if fish == 0:
                tomorrows_fish.append(8)
                tomorrows_fish.append(6)
        todays_fish = tomorrows_fish
    
    print(f"part 1 : {len(todays_fish)}")

def p2(f):
    todays_fish = {i:0 for i in range(0,9)}
    for line in common_functions.read_file_line_by_line(f):
        starting_fish = common_functions.retrieve_numbers.get_numbers_as_int_in_list(line)
        for fish in starting_fish:
            todays_fish[fish]+=1

    
    
    for i in range(256):
        tomorrows_fish={i:0 for i in range(0,9)}

        for i in range(8,-1,-1):
            if i ==0:
                tomorrows_fish[8] = todays_fish[0]
                tomorrows_fish[6]+=todays_fish[0]
            else:
                tomorrows_fish[i-1]=todays_fish[i]
        
        todays_fish = tomorrows_fish
    
    totalfish = sum(todays_fish.values())
    print(f"part 2 : {totalfish}")

def main():
    f = r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"
    p1(f)
    p2(f)

if __name__ == '__main__':
    main()