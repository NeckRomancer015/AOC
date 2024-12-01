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
    todays_fish = []
    for line in common_functions.read_file_line_by_line(f):
        todays_fish = common_functions.retrieve_numbers.get_numbers_as_int_in_list(line)
    
    for i in range(256):
        tomorrows_fish=''

        for fish in todays_fish:
            if int(fish)>0:
                val = str(int(fish)-1)
                tomorrows_fish+=val
            if int(fish) == 0:
                tomorrows_fish+='8'
                tomorrows_fish+='6'
        todays_fish = re.findall(r'\d',tomorrows_fish)
    
    print(f"part 2 : {len(todays_fish)}")

def main():
    f = r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"
    p1(f)
    p2(f)

if __name__ == '__main__':
    main()