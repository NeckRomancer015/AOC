import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions

def win_condition(board:list):

    for i in range(len(board[0])):
        col = [row[i] for row in board]
        if col.count('-1') == len(col):
            return True
    
    for i in range(len(board)):
        if board[i].count('-1') == len(board[i]):
            return True


def p2(f):
    drawn_numbers = []
    
    boards = []
    temp = []
    last_board = []
    for line in common_functions.read_file_line_by_line(f):
        if drawn_numbers == []:
            drawn_numbers=common_functions.get_numbers_as_list(line)
        elif line =='':
            if temp  != []:
                boards.append(temp)
                temp = []
        else:
            temp.append(common_functions.get_numbers_as_list(line))
    boards.append(temp)
    
    boards_won = []
    for bingo in drawn_numbers:
        for board in boards:
            for i in range(0,len(board)):
                for j in range(0,len(board[i])):
                    if bingo == board[i][j]:
                        board[i][j] = '-1'
                    
        if win_condition(board):
            if board in boards_won:
                continue
            ans = 0
            for i in board:
                for j in i:
                    if j !='-1':
                        ans+=int(j)
            boards_won.append(board)
            last_board.append(ans*int(bingo))
    print(last_board[-1])
    

def p1(f):
    drawn_numbers = []
    
    boards = []
    temp = []
    for line in common_functions.read_file_line_by_line(f):
        if drawn_numbers == []:
            drawn_numbers=common_functions.get_numbers_as_list(line)
        elif line =='':
            if temp  != []:
                boards.append(temp)
                temp = []
        else:
            temp.append(common_functions.get_numbers_as_list(line))
    boards.append(temp)
    
    for bingo in drawn_numbers:
        for board in boards:
            for i in range(0,len(board)):
                for j in range(0,len(board[i])):
                    if bingo == board[i][j]:
                        board[i][j] = '-1'
                    
            if win_condition(board):
                ans = 0
                for i in board:
                    for j in i:
                        if j !='-1':
                            ans+=int(j)
                print(ans*int(bingo))
                return



def main():
    f = r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"
    p1(f)
    p2(f)


if __name__ == '__main__':
    main()