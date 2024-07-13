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

def mine_rand(board, col, lin):
    l = random.randint(0, col - 1)
    n = random.randint(0, lin - 1)
    if board[l][n] == '*':
        mine_rand(board, col, lin)
    else:
        board[l][n] = '*'

def set_mine(num, board):
    for i in range(num):
        mine_rand(board, col, lin)

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


