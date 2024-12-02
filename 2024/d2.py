import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions
import copy

def isSafe_2(val:list):
    if isSafe(val):
        return True
    
    for i in range(0,len(val)):
        c = copy.deepcopy(val)
        del c[i]
        if isSafe(c):
            return True
        

    return False

def isSafe(val:list):    
    if val[0]==val[1]:
            return False
    
    isAsc=False
    if val[0]<val[1]:
        isAsc = True
    if isAsc:
        for v in range(0,len(val)):
            if v == len(val)-1:
                return True
            if val[v+1]<= val[v]:
                return False
            elif  val[v+1] -val[v] >3:
                return False
    else:
        for v in range(0,len(val)):
            if v == len(val)-1:
                return True
            if val[v]<=val[v+1]:
                return False
            elif val[v]-val[v+1]>3:
                return False
    return True

def p1(f):
    safe = 0

    for line in common_functions.read_file_line_by_line(f):
        val  = common_functions.retrieve_numbers.get_numbers_as_int_in_list(line)

        if isSafe(val):
            safe+=1
    
    print(f"Part 1 : {safe}")

def p2(f):
    safe = 0

    for line in common_functions.read_file_line_by_line(f):
        val  = common_functions.retrieve_numbers.get_numbers_as_int_in_list(line)
        if isSafe_2(val):
            safe+=1
    
    print(f"Part 2 : {safe}")


def main():
    f= r'C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt'
    p1(f)
    p2(f)

if __name__ == '__main__':
    main()