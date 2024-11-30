import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions




def p1(file_path):
    horizontal = 0
    depth = 0
    for line in common_functions.read_file_line_by_line(file_path=file_path):
        val = int(common_functions.get_numbers_as_string(line))
        if 'forward' in line:
            horizontal+=val
        elif 'down' in line:
            depth+=val
        elif 'up' in line:
            depth-=val
    print(horizontal*depth)
def p2(f):
    h = 0
    d =0
    a = 0

    for l in common_functions.read_file_line_by_line(file_path=f):
        val = int(common_functions.get_numbers_as_string(l))

        if 'up' in l:
            a-=val
        elif 'down' in l:
            a+=val
        elif 'forward' in l:
            h+=val
            d += (a*val)
    print(d)
    print(h)
    print(h*d)

def main():
    p1(r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt")
    p2(r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt")
if __name__ == '__main__':
    main()


