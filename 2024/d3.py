import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions
import re
def p1(f):
    ans = 0
    for line in common_functions.read_file_line_by_line(f):
        matches = re.findall(r"mul\((\d+),(\d+)\)",line)
        for num1,num2 in matches:
            ans+= (int(num1)*int(num2))
    
    print(f"Part 1 is {ans}")

                

def p2(f):
    ans = 0
    enabled = True
    for line in common_functions.read_file_line_by_line(f):
        pattern = r"mul\((\d+),(\d+)\)"
        matches = {
                m.start(): (m.group(1),m.group(2))
                for m in re.finditer(pattern, line)
        }
        p = r"(don't\(\)|do\(\))"
        do_dont = {m.start(): m.group() for m in re.finditer(p,line)}
        print(do_dont)
        for match_object in matches.keys():
            for i in range(match_object, 0,-1):
                if i in do_dont.keys():
                    if do_dont[i] == 'do()':
                        enabled = True
                        break
                    elif do_dont[i] == "don't()":
                        enabled = False
                        break
            
            if enabled:
                v = matches[match_object]
                ans+=(int(v[0])*int(v[1]))
        
    print(f"Part 2 is {ans}")


def main():
    f = r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"
    p1(f)
    p2(f)


if __name__ == '__main__':
    main()