#mine sweeping library
import random
def init_board(c, l):
    all_ls = []
    for i in range(c):
        line_ls = []
        for j in range(l):
            line_ls.append(9)
        all_ls.append(line_ls)
    return all_ls

def init_player_board(c, l):
    all_ls = []
    for i in range(c):
        line_ls = []
        for j in range(l):
            line_ls.append(9)
        all_ls.append(line_ls)
    return all_ls

def mine_rand(board):
    l = random.randint(0, 24)#TODO
    n = random.randint(0, 24)#TODO
    if board[l][n] == '*':
        mine_rand(board)
    else:
        board[l][n] = '*'

def set_mine(num, board):
    for i in range(num):
        mine_rand(board)

def set_number(board, col, lin):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '*':
                continue
            count = 0
            if not((i + 1) > lin - 1):
                if board[i + 1][j] == '*':
                    count += 1
            if not((i - 1) < 0):
                if board[i - 1][j] == '*':
                    count += 1
            if not((j + 1) > col - 1):
                if board[i][j + 1] == '*':
                    count += 1
            if not((j - 1) < 0):
                if board[i][j - 1] == '*':
                    count += 1
            if not((i + 1) > lin - 1):
                if not((j + 1) > col - 1):
                    if board[i + 1][j + 1] == '*':
                        count += 1
            if not((i - 1) < 0):
                if not((j + 1) > col - 1):
                    if board[i - 1][j + 1] == '*':
                        count += 1
            if not((i + 1) > lin - 1):
                if not((j - 1) < 0):
                    if board[i + 1][j - 1] == '*':
                        count += 1
            if not((i - 1) < 0):
                if not((j - 1) < 0):
                    if board[i - 1][j - 1] == '*':
                        count += 1
            #TODO
            board[i][j] = count

col = 25
lin = 25
mine_num = 10


board = init_board(col, lin)
player_board = init_player_board(col, lin)
set_mine(mine_num, board)
set_number(board, col, lin)
print(board)
