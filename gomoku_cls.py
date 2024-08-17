import pygame

pygame.init()
border_left = 25
border_right = 725
border_top = 25
border_bottom = 725
width = 50
height = 50
msg_font = pygame.font.Font(None, 32)

class Game:
    def __init__(self, screen, button, button_computer):
        self.started = False
        self.screen = screen
        self.button = button
        self.button_computer = button_computer
        self.player = 1
        self.winner = 0
        self.map = [0] * 15
        for i in range(15):
            self.map[i] = [0] * 15

    def start(self):
        screen = self.screen
        screen.fill("#EE9A49")
        for x in range(15):
            pygame.draw.line(screen, "#000000", [border_left + width * x, border_top], [border_left + width * x, border_bottom], 2)
        for y in range(15):
            pygame.draw.line(screen, "#000000", [border_left, border_top + height * y], [border_right, border_top + height * y], 2)
            pygame.draw.circle(screen, "#000000", [25 + 50 * 7, 25 + 50 * 7], 8) 
                
        x, y = pygame.mouse.get_pos()
        if y <= (border_bottom + 25):
            x = round((x - border_left) / width) * width + border_left
            y = round((y - border_top) / height) * height + border_top
    
            pygame.draw.rect(screen, "#FFFFFF", [x - 25, y - 25, 50, 50], 2)
        
        self.button.draw(screen)
        self.button_computer.draw(screen)

        for row in range(15):
            for column in range(15):
                if self.map[row][column] == 1:
                    pygame.draw.circle(screen, "#000000", [column * width + border_left, row * height + border_top], 25)
                elif self.map[row][column] == 2:
                    pygame.draw.circle(screen, "#FFFFFF", [column * width + border_left, row * height + border_top], 25)
        if self.winner != 0:
            if self.winner == 1:
                msg = "Black won"
                color = (0, 0, 0)
            else:
                msg = "White won"
                color = (255, 255, 255)
            msg_font = pygame.font.Font(None, 70)
            msg_surf = msg_font.render(msg, 1, color)
            screen.blit(msg_surf, [485, 775])
            pygame.display.flip()
            #pygame.time.delay(3000)
            self.button.clicked = False

    def horizental_next(self, x, y, offset):
        return ( x + offset, y )
    def vertical_next(self, x, y, offset):
        return ( x , y + offset )
    def incremental_next(self, x, y, offset):
        return ( x + offset, y - offset )
    def decrease_next(self, x, y, offset):
        return ( x + offset, y + offset )

    def inside_board(self, x, y):
        return x > 0 and x < 15 and y > 0 and y < 15

    def checkSingle(self, row, column, next_coord, player):
        score = 1
        for i in range(4):
            t= next_coord(column, row, i)
            x = t[0]
            y = t[1]
            t1 = next_coord(x, y, 1)
            x1 = t1[0]
            y1 = t1[1]
            if self.inside_board(x, y) and self.inside_board(x1, y1):
                if self.map[y][x] == self.map[y1][x1]:
                    score += 1
                else:
                    break
        for j in range(4):
            t= next_coord(column, row, -j)
            x = t[0]
            y = t[1]
            t1 = next_coord(x, y, -1)
            x1 = t1[0]
            y1 = t1[1]
            if self.inside_board(x, y) and self.inside_board(x1, y1):
                if self.map[y][x] == self.map[y1][x1]:
                    score += 1
                else:
                    break
        if score == 5:
            return True
        if player == 2:
            if score > 5:
                return True


    def check(self, row, column, player):
        res0 = self.checkSingle(row, column, self.horizental_next, player)
        if res0 == True:
            return res0
        res1 = self.checkSingle(row, column, self.vertical_next, player)
        if res1 == True:
            return res1
        res2 = self.checkSingle(row, column, self.incremental_next, player)
        if res2 == True:
            return res2
        res3 = self.checkSingle(row, column, self.decrease_next, player)
        if res3 == True:
            return res3

    def mouse_click(self, x, y):
        if y <= border_bottom + 25:
            if self.started:
                column = round((x - 25) / 50)
                row = round((y - 25) / 50)
                print(column, row)
                if self.map[row][column] == 0:
                    self.map[row][column] = self.player
                    if self.check(row, column, self.player):
                        self.winner = self.player
                    else:
                        if self.player == 1:
                            self.player = 2
                        else:
                            self.player = 1
                else:
                    print("There is a piece") 
            else:
                print("The game isn't start")
