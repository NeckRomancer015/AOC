import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions

def return_axis(a:int,b:int,constant:int,isX = True)->list[(int,int)]:
    if isX:
        axis = [(i,constant) for i in range(a,b+1)]
    else:        
        axis = [(constant,i) for i in range(a,b+1)]
    return axis

def return_full_coords(x1,y1,x2,y2)->list[(int,int)]:
    if x1==x2:
        if y1<y2:
            return return_axis(y1,y2,x1,False)
        elif y1 ==y2:
            return [(x1,y1)]
        else:
            return return_axis(y2,y1,x1,False)
    
    if y1 == y2:
        if x1==x2:
            return [(x1,y1)]
        elif x1<x2:
            return return_axis(x1,x2,y1)
        else:
            return return_axis(x2,x1,y2)
    


def p1(f):
    vents = dict()
    for line in common_functions.read_file_line_by_line(f):
        val = common_functions.get_numbers_as_list(line)
        x1,y1,x2,y2 = int(val[0]),int(val[1]),int(val[2]),int(val[3])
        if x1!=x2 and y1!=y2:
            continue
        else:
            full_coords = return_full_coords(x1,y1,x2,y2)
            for coord in full_coords:
                if coord in vents.keys():
                    vents[coord]+=1
                else:
                    vents[coord]=1
    
    ans=0
    for vent in vents.keys():
        if vents[vent] >1:
            ans+=1
    
    print(f"Part 1 : {ans}")

def return_diagonal_first_less_sec(x1,y1,x2,y2):
    temp = [t for t in range(x1,x2+1)]
    full_coords = []
    for x in temp:
        for y in range(y1,y2+1):
            full_coords.append((x,y))
    
    return full_coords


def p2(f):
    ans = 0
    vents = dict()
    for line in common_functions.read_file_line_by_line(f):
        val = common_functions.get_numbers_as_list(line)        
        x1,y1,x2,y2 = int(val[0]),int(val[1]),int(val[2]),int(val[3])
        if x1==x2 or y1==y2:
            full_coords = return_full_coords(x1,y1,x2,y2)
            for coord in full_coords:
                if coord in vents.keys():
                    vents[coord]+=1
                else:
                    vents[coord]=1
        elif common_functions.math_functions.is_points_diagonal(x1 = x1,y1=y1,x2=x2,y2=y2):
            full_coords= []
            diff_x = 1 if x2>x1 else -1
            diff_y = 1 if y2>y1 else -1

            tx,ty = x1,y1
            while (tx,ty)!=(x2,y2):
                full_coords.append((tx,ty))
                tx+=diff_x
                ty+=diff_y
            full_coords.append((x2,y2))
        
            for coord in full_coords:
                if coord in vents.keys():
                    vents[coord]+=1
                else:
                    vents[coord]=1




    for vent in vents.keys():
        if vents[vent] >1:
            ans+=1
    print(len(vents.keys()))
    print(f"Part 2 : {ans}")
def main():
    f = r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"
    p1(f)
    p2(f)


if __name__ =='__main__':
    main()