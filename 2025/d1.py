import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
from common_functions import *


def p1():
    dial = 50
    count=0


    for line in read_file_line_by_line(r'ex.txt'):
        numb = retrieve_numbers.get_numbers_as_string(line)

        if line[0]== 'L':          
            dial-=int(numb)
            while True:
                if dial <0:
                    dial+=100
                else:
                    break
        else:
            dial+=int(numb)
            dial =dial % 100
        
        if dial == 0:
            count+=1
    print(f"Part 1 : {count}")

def p2():
    dial = 50
    count = 0

    for line in read_file_line_by_line("ex.txt"):
        numb = int(retrieve_numbers.get_numbers_as_string(line))

        if line[0] == "R":
            for _ in range(numb):
                dial = (dial + 1) % 100
                if dial == 0:
                    count += 1
        else:
            for _ in range(numb):
                dial = (dial - 1) % 100
                if dial == 0:
                    count += 1

    print(f"Part 2 : {count}")
          

def main():
      p1()
      p2()


if __name__ == '__main__':
    main()