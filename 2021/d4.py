import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions

def win_condition(board:list):

    for i in range(len(board[0])):
        col = [row[i] for row in board]
        if col.count('x') == len(col):
            return True
    
    for i in range(len(board)):
        if board[i].count('x') == len(board[i]):
            return True


def p2(f):
    drawn_numbers = []
    
    boards = []
    temp = []
    last_score = 0
    for line in common_functions.read_file_line_by_line(f):
        if drawn_numbers == []:
            drawn_numbers=common_functions.retrieve_numbers.get_numbers_as_list(line)
        elif line =='':
            if temp  != []:
                boards.append(temp)
                temp = []
        else:
            temp.append(common_functions.retrieve_numbers.get_numbers_as_list(line))
    boards.append(temp)
    
    boards_won = []
    for bingo in drawn_numbers:
        for board_num,board in enumerate(boards):            
            if board_num in boards_won:
                continue
            for i in range(0,len(board)):
                for j in range(0,len(board[i])):
                    if bingo == board[i][j]:
                        board[i][j] = 'x'
                    
            if win_condition(board):
                ans = 0
                for i in board:
                    for j in i:
                        if j !='x':
                            ans+=int(j)
                boards_won.append(board_num)
                last_score=ans*int(bingo)
    print(last_score)
    
                

def p1(f):
    drawn_numbers = []
    
    boards = []
    temp = []
    for line in common_functions.read_file_line_by_line(f):
        if drawn_numbers == []:
            drawn_numbers=common_functions.retrieve_numbers.get_numbers_as_list(line)
        elif line =='':
            if temp  != []:
                boards.append(temp)
                temp = []
        else:
            temp.append(common_functions.retrieve_numbers.get_numbers_as_list(line))
    boards.append(temp)

    for bingo in drawn_numbers:
        for board in boards:
            for i in range(0,len(board)):
                for j in range(0,len(board[i])):
                    if bingo == board[i][j]:
                        board[i][j] = 'x'
                    
            if win_condition(board):
                ans = 0
                for i in board:
                    for j in i:
                        if j !='x':
                            ans+=int(j)
                print(ans*int(bingo))
                return



def main():
    f = r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"
    p1(f)
    p2(f)


if __name__ == '__main__':
    main()