from minesweeping_lib import *
import pygame
MOUSE_LEFT = 1
MOUSE_RIGHT = 3
block_empty = 'block_empty.png'
block_one = 'block_one.png'
block_two = 'block_two.png'
block_three = 'block_three.png'
block_four = 'block_four.png'
block_five = 'block_five.png'
block_six = 'block_six.png'
block_nine = 'block_nine.png'
block_light_nine = 'block_light_nine.png'
block_flag = 'block_flag.png'
block_unknowned = 'block_unknowned.png'
mine_appear = 'mine_appear.png'
mine_unexplosioned = 'mine_unexplosioned.png'
mine_explosioned = 'mine_explosioned.png'

#img_ls = [block_empty, block_one, block_two, block_three, block_four, block_five, block_six, \
#          block_nine, block_light_nine, block_flag, block_unknowned, mine_appear, \
#          mine_unexplosioned, mine_explosioned]
COL = 9
ROW = 9
mine_num = 10

def check(b_col, b_row, ls):
    if b_col + 1 < COL:
        if not [b_row, b_col + 1] in ls:
            ls.append([b_row, b_col + 1])
            if board[b_row][b_col + 1] == 0:
                check(b_col + 1, b_row, ls)

    if b_col - 1 >= 0:
        if not [b_row, b_col - 1] in ls:
            ls.append([b_row, b_col - 1])
            if board[b_row][b_col - 1] == 0:
                check(b_col - 1, b_row, ls)

    if b_row + 1 < ROW:
        if not [b_row + 1, b_col] in ls:
            ls.append([b_row + 1, b_col])
            if board[b_row + 1][b_col] == 0:
                check(b_col, b_row + 1, ls)

    if b_row - 1 >= 0:
       if not [b_row - 1, b_col] in ls:
            ls.append([b_row - 1, b_col])
            if board[b_row - 1][b_col] == 0:
                check(b_col, b_row - 1, ls)


    if b_col + 1 < COL and b_row + 1 < ROW:
        if not [b_row + 1, b_col + 1] in ls:
            ls.append([b_row + 1, b_col + 1])
            if board[b_row + 1][b_col + 1] == 0:
                check(b_col + 1, b_row + 1, ls)

    if b_col - 1 >= 0 and b_row + 1 < ROW:
        if not [b_row + 1, b_col - 1] in ls:
            ls.append([b_row + 1, b_col - 1])
            if board[b_row + 1][b_col - 1] == 0:
                check(b_col - 1, b_row + 1, ls)

    if b_col + 1 < COL and b_row - 1 >= 0:
        if not [b_row - 1, b_col + 1] in ls:
            ls.append([b_row - 1, b_col + 1])
            if board[b_row - 1][b_col + 1] == 0:
                check(b_col + 1, b_row - 1, ls)

    if b_col - 1 >= 0 and b_row - 1 >= 0:
       if not [b_row - 1, b_col - 1] in ls:
            ls.append([b_row - 1, b_col - 1])
            if board[b_row - 1][b_col - 1] == 0:
                check(b_col - 1, b_row - 1, ls)

    return ls

def start_game(col, row):
    board = init_board(col, row)
    set_mine(mine_num, board)
    set_number(board, col, row)
    player_board = init_player_board(col, row)
    return board, player_board

class Block(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.top, self.rect.left = location

    def click(block, b_col, b_row):
        if player_board[b_row][b_col] == '>':
            return
        to_open_ls = []

        player_board[b_row][b_col] = board[b_row][b_col]
        screen.blit(block.image, block.rect)
        pygame.display.flip()

        if board[b_row][b_col] == 0:
            check(b_col, b_row, to_open_ls)

        for pos in to_open_ls:
            player_board[pos[0]][pos[1]] = board[pos[0]][pos[1]]


    def light(x, y, block):
        b_x = block.rect.x
        b_y = block.rect.y
        b_row = int(b_y / 35)
        b_col = int(b_x / 35)

        if (b_x < x < b_x + 35) and (b_y < y < b_y + 35):
            if player_board[b_row][b_col] == 9:
                player_board[b_row][b_col] = '^'
        else:
            if player_board[b_row][b_col] == '^':
                player_board[b_row][b_col] = 9
        #display_board()
        screen.blit(block.image, block.rect)


pygame.init()
screen = pygame.display.set_mode((COL * 35, ROW * 35))
pygame.display.set_caption("MINE SWEEPING")
screen.fill([255, 255, 255])

msg_font = pygame.font.Font(None, 32)

board, player_board = start_game(COL, ROW)
print(board)
def display_board():
    blocks = []
    for i in range(ROW):
        for j in range(COL):
            location = [i * 35, j * 35]
            if player_board[i][j] == 9:
                block = Block(block_nine, location)
            elif player_board[i][j] == 0:
                block = Block(block_empty, location)
            elif player_board[i][j] == '^':
                block = Block(block_light_nine, location)
            elif player_board[i][j] == 1:
                block = Block(block_one, location)
            elif player_board[i][j] == 2:
                block = Block(block_two, location)
            elif player_board[i][j] == 3:
                block = Block(block_three, location)
            elif player_board[i][j] == 4:
                block = Block(block_four, location)
            elif player_board[i][j] == 5:
                block = Block(block_five, location)
            elif player_board[i][j] == 6:
                block = Block(block_six, location)
            elif player_board[i][j] == '*':
                block = Block(mine_appear, location)
            elif player_board[i][j] == '>':
                block = Block(block_flag, location)
            elif player_board[i][j] == '?':
                block = Block(block_unknowned, location)
            blocks.append(block)
    return blocks

clock = pygame.time.Clock()
while True:
    blocks = display_board()
    for block in blocks:
        screen.blit(block.image, block.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_LEFT:
                x, y = pygame.mouse.get_pos()
                blocks = display_board()
                for block in blocks:
                    b_x = block.rect.x
                    b_y = block.rect.y
                    b_row = int(b_y / 35)
                    b_col = int(b_x / 35)

                    if (b_x < x < b_x + 35) and (b_y < y < b_y + 35):
                        Block.click(block, b_col, b_row)
                continue
            elif event.button == MOUSE_RIGHT:
                x, y = pygame.mouse.get_pos()
                blocks = display_board()
                for block in blocks:
                    b_x = block.rect.x
                    b_y = block.rect.y
                    b_row = int(b_y / 35)
                    b_col = int(b_x / 35)

                    original = player_board[b_row][b_col]
                    if (b_x < x < b_x + 35) and (b_y < y < b_y + 35):
                        if original != 9 and original != '^' and original != '>' and original != '?':
                            continue;
                        if original == 9 or original == '^':
                            new_value = '>'
                        elif original  == '>':
                            new_value = '?'
                        elif original == '?':
                            new_value = '^'
                        player_board[b_row][b_col] = new_value
                        blocks = display_board()
                        for block in blocks:
                            screen.blit(block.image, block.rect)

                continue
        elif event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            blocks = display_board()
            for block in blocks:
                Block.light(x, y, block)

    pygame.display.flip()
    clock.tick(30)
