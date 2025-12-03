import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
from common_functions import *


def p1():
    count=0
    for line in read_file_line_by_line(r'C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt'):
        first=0
        second=0
        for battery in range(0,len(line)):
            currenT_bat = int(line[battery])
            if first ==0: # index 0
                first =currenT_bat
            elif currenT_bat>first:
                if battery < len(line)-1:
                    first = currenT_bat
                    second = 0 # have to reset second
                else: # line was like 123456789, we making sure we assign to second on the last character
                    second = currenT_bat
            elif currenT_bat>second:
                second = currenT_bat
        
        count+= (first*10)+second
    
    print(f"Part 1 : {count}")

def p2():
    pass
            
                    



def main():
    p1()
    p2()
if __name__ == '__main__':
    main()
        
