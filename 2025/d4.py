import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
from common_functions import *


def p1(grid : list[list]):
    count =0
    for row in range(0,len(grid)):        
        for col in range(0,len(grid[row])):
            temp = 0 
            if grid[row][col] == '@':
                neigh_coord = math_functions.get_neighbors(row,col)
                for n in neigh_coord:
                    n_x = n[0]# this is more readable
                    n_y = n[1]
                    if 0<=n_x<len(grid) and 0<=n_y<len(grid[row]):
                        if grid[n_x][n_y] == '@':
                            temp+=1
                if temp<4:
                    count+=1
    
    print(f"Part 1 : {count}")


def p2(grid : list[list]):
    count = 0
    change = []

    while True:
        for row in range(0,len(grid)): # can look at making a common function in the future        
            for col in range(0,len(grid[row])):
                temp = 0 
                if grid[row][col] == '@':
                    neigh_coord = math_functions.get_neighbors(row,col)
                    for n in neigh_coord:
                        n_x = n[0] 
                        n_y = n[1]
                        if 0<=n_x<len(grid) and 0<=n_y<len(grid[row]):
                            if grid[n_x][n_y] == '@':
                                temp+=1
                    if temp<4:
                        change.append((row,col))
                        count+=1
        if change:
            for coord in change:
                x,y = coord[0],coord[1]
                grid[x][y] = '.'
            change = [] # have to clear the list to break the loop
        else:
            break
    
    print(f"Part 2 : {count}")
    
            

def main():
    grid = []
    for line in read_file_line_by_line(r'C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt'):
        grid.append(list(line))
    
    p1(grid=grid)
    p2(grid=grid)

if __name__ == '__main__':
    main()