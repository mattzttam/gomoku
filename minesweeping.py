#mine sweeping
import random
def print_color(text, color):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m'
    }
    reset = '\033[0m'

    print(f"{colors[color]}\033[1;40m{text}{reset}", end='')
 

def init_board(c, l):
    all_ls = []
    for i in range(c):
        line_ls = []
        for j in range(l):
            line_ls.append(0)
        all_ls.append(line_ls)
    return all_ls

def pretty_print(board):
    for line in board:
        for b in line:
            if b == 0:
                print_color('# ', 'blue')
            elif b == 9:
                print_color('- ', 'white')
            elif b == '*':
                print_color('* ', 'red')
            else:
                text = str(b) + ' '
                print_color(text, 'white')
        print()

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

col = 25
lin = 25
mine_num = 10

n = int(int(col - 13) / 2)
print('* ' * n + 'M I N E   S W E E P I N G ' + '* ' * n)
print()
board = init_board(col, lin)
set_mine(mine_num, board)
pretty_print(board)
