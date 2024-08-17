#mine sweeping library
import random
COL = 9
ROW = 9
mine_num = 10
#TODO

def init_board(c, r):
    all = []
    for i in range(r):
        one_row = []
        for j in range(c):
            one_row.append(9)
        all.append(one_row)
    return all

# TODO duplicated with init_board
def init_player_board(c, r):
    return init_board(c, r)

def mine_rand(board, col, row):
    c = random.randint(0, col - 1)
    r = random.randint(0, row - 1)
    if board[r][c] == '*':
        mine_rand(board, col, row)
    else:
        board[r][c] = '*'

def set_mine(num, board):
    for i in range(num):
        mine_rand(board, COL, ROW)

def set_number(board, max_col, max_row):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '*':
                continue
            count = 0
            if ((i + 1) <= max_row - 1):
                if board[i + 1][j] == '*':
                    count += 1
            if ((i - 1) >= 0):
                if board[i - 1][j] == '*':
                    count += 1
            if ((j + 1) <= max_col - 1):
                if board[i][j + 1] == '*':
                    count += 1
            if ((j - 1) >= 0):
                if board[i][j - 1] == '*':
                    count += 1
            if not((i + 1) > max_row - 1):
                if not((j + 1) > max_col - 1):
                    if board[i + 1][j + 1] == '*':
                        count += 1
            if not((i - 1) < 0):
                if not((j + 1) > max_col - 1):
                    if board[i - 1][j + 1] == '*':
                        count += 1
            if not((i + 1) > max_row - 1):
                if not((j - 1) < 0):
                    if board[i + 1][j - 1] == '*':
                        count += 1
            if not((i - 1) < 0):
                if not((j - 1) < 0):
                    if board[i - 1][j - 1] == '*':
                        count += 1
            #TODO
            board[i][j] = count


