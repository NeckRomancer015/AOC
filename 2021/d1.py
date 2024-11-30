import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions



def p1():
    temp = ''
    increase = 0
    for line in common_functions.read_file_line_by_line(r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"):
        if temp == '':
            temp = int(line)
        else:
            if int(line)>temp:
                increase+=1
            temp = int(line)
    print(increase)


def p2():
    s1,s2,s3 =[],[],[]
    increase = 0
    count = 0
    for line in common_functions.read_file_line_by_line(r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"):
        if count ==0:
            s1.append(int(line))

        elif count == 1:
            s1.append(int(line))
            s2.append(int(line))

        elif count == 2:
            s1.append(int(line))
            s2.append(int(line))
            s3.append(int(line))

        elif count%3 == 0:
            s2.append(int(line))
            s3.append(int(line))
            if sum(s2)>sum(s1):
                increase+=1
            s1 = []
            s1.append(int(line))

        elif count%3 == 1:
            s1.append(int(line))
            s3.append(int(line))
            if sum(s3)>sum(s2):
                increase+=1
            s2=[]
            s2.append(int(line))
        elif count%3 == 2:            
            s1.append(int(line))
            s2.append(int(line))
            if sum(s1)>sum(s3):
                increase+=1
            s3=[]
            s3.append(int(line))
        count+=1
    
    print(increase)
                
                    
                
            

def main():
    p1()
    p2()

if __name__=='__main__':
    main()