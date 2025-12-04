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
    total_count=0
    for line in read_file_line_by_line(r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"):
        battery_pack = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}

        digits_to_keep = 12
        digits_to_remove = len(line) - digits_to_keep
        
        
        stack = []
        for digit in line:
            # While stack has elements, we still have digits to remove, 
            # and the current digit is greater than the last digit in the stack:
            while stack and digits_to_remove > 0 and stack[-1] < digit:
                stack.pop()
                digits_to_remove -= 1
            stack.append(digit)
        
        # If we still need to remove digits (can happen if numbers were ascending)
        # trim from the end to the required length
        final_sequence = "".join(stack[:digits_to_keep])
        
        total_count += int(final_sequence)
    print(f"Part 2:  {total_count}")
            
                    



def main():
    p1()
    p2()
if __name__ == '__main__':
    main()
        
