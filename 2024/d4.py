import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions


def isXMAS(temp:str):
    if temp=='XMAS':
        return True

    return False

def isAMAS(temp:str):
    if temp == 'MAS':
        return True

def build_AMAS(coord,grid)->bool:
    d= [(-1,-1),(-1,1),(1-1),(1,1)]
    
    xmas_found = 0

    r,y = coord[0],coord[1]
            
    ##left diagonal
    top_left = [r-1,y-1]
    bottom_left = [r+1,y-1]

    ##right diagonal
    top_right = [r-1,y+1]
    bottom_right=[r+1,y+1]

    if 0<=top_left[0]<len(grid) and 0<=top_left[1]<len(grid[r]):
        if 0<=bottom_right[0]<len(grid) and 0<=bottom_right[1]<len(grid[r]):
            if grid[top_left[0]][top_left[1]] == 'M':
                if grid[bottom_right[0]][bottom_right[1]] == 'S':
                    xmas_found+=1
            elif grid[top_left[0]][top_left[1]] == 'S':
                if grid[bottom_right[0]][bottom_right[1]] == 'M':
                    xmas_found+=1
    


    if 0<=top_right[0]<len(grid) and 0<=top_right[1]<len(grid[r]):
        if 0<=bottom_left[0]<len(grid) and 0<=bottom_left[1]<len(grid[r]):
            if grid[top_right[0]][top_right[1]] == 'M':
                if grid[bottom_left[0]][bottom_left[1]] == 'S':
                    xmas_found+=1
            elif grid[top_right[0]][top_right[1]] == 'S':
                if grid[bottom_left[0]][bottom_left[1]] == 'M':
                    xmas_found+=1

    if xmas_found==2:
        return 1
    return 0

def p2(f):
    found=0
    for r in range(0,len(f)):
        for y in range(0,len(f[r])):
            if f[r][y] == 'A':           
                found+=build_AMAS([r,y],grid=f)
    
    print(f"Part 2 :{found}")
        
    

def build_temp(coord,grid)->bool:
    d = [(-1,-1),(-1,0),(-1,1),
         (0,-1),    (0,1),
          (1,-1),(1,0),(1,1) ]
    
    xmas_found = 0

    r,y = coord[0],coord[1]
    xmas = 'X'
    for offset in d:
        dx,dy = offset[0],offset[1]
        xmas = 'X'                   
        xr,xy = r+dx,y+dy
        
        for i in range(0,5):
            if 0<=xr<len(grid) and 0<=xy<len(grid[r]):
                xmas+=grid[xr][xy]
                if len(xmas)>4:
                    break
                if xmas not in 'XMAS':
                    break
                elif isXMAS(xmas):
                    xmas_found+=1
                    break            
            else:
                break
            
            xr,xy = xr+dx,xy+dy
    return xmas_found
    
    

def p1(f:list):
    goal =  'XMAS'
    found=0
    for r in range(0,len(f)):
        for y in range(0,len(f[r])):
            if f[r][y] == 'X':                
                found+=build_temp([r,y],grid=f)
    
    print(f"Part 1 :{found}")
                      



def main():
    f = r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"
    grid =[]
    for line in common_functions.read_file_line_by_line(f):
        grid.append(list(line))
    p1(grid)
    p2(grid)


if __name__ == "__main__":
    main()