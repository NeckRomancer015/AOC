import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions


def p1(f):
    l1 = []
    l2 = []
    for line in common_functions.read_file_line_by_line(file_path=f):
        val = common_functions.get_numbers_as_list(line)
        l1.append(int(val[0]))
        l2.append(int(val[1]))
    
    l1.sort()
    l2.sort()
    ans = 0

    for i in range(0,len(l1)):
        ans+= abs(l1[i]-l2[i])
    
    print(ans)



def p2(f):
    l1 = []
    l2 = dict()
    for line in common_functions.read_file_line_by_line(file_path=f):
        val = common_functions.get_numbers_as_list(line)
        l1.append(int(val[0]))
        if int(val[1]) in l2.keys():
            l2[int(val[1])]+=1
        else:
            l2[int(val[1])] =1
    
    ans = 0
    for i in range(0,len(l1)):
        if l1[i] in l2.keys():
            ans+= l1[i]*l2[l1[i]]
    print(ans)



def main():
    p1(r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt")
    p2(r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt")





if __name__ == "__main__":
    main()