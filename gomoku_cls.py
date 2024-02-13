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
        if x >= border_left and x <= border_right and y >= border_top and y <= border_bottom:
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
            screen.blit(msg_surf, [180, 100])
            pygame.display.flip()
            #pygame.time.delay(3000)
            button.clicked = False
                    
    def check(self, row, column, player):
        score = 1
        for i in range(4):
            try:
                if self.map[row][column + i] == self.map[row][column + i + 1]:
                    score += 1
                else:
                    break
            except:
                break
        for j in range(4):
            try:
                if self.map[row][column - j] == self.map[row][column - j - 1]:
                    score += 1
                else:
                    break
            except:
                break
        if score == 5:
            return True
        if player == 2:
            if score > 5:
                return True
            
        score = 1
        for i in range(4):
            try:
                if self.map[row + i][column] == self.map[row + i + 1][column]:
                    score += 1
                else:
                    break
            except:
                break
        for j in range(4):
            try:
                if self.map[row - j][column] == self.map[row - j - 1][column]:
                    score += 1
                else:
                    break
            except:
                break
        if score == 5:
            return True
        if player == 2:
            if score > 5:
                return True
            
        score = 1
        for i in range(4):
            try:
                if self.map[row + i][column + i] == self.map[row + i + 1][column + i + 1]:
                    score += 1
                else:
                    break
            except:
                break
        for j in range(4):
            try:
                if self.map[row - j][column - j] == self.map[row - j - 1][column - j - 1]:
                    score += 1
                else:
                    break
            except:
                break
        if score == 5:
            return True
        if player == 2:
            if score > 5:
                return True
            
        score = 1
        for i in range(4):
            try:
                if self.map[row - i][column + i] == self.map[row - i - 1][column + i + 1]:
                    score += 1
                else:
                    break
            except:
                break
        for j in range(4):
            try:
                if self.map[row + j][column - j] == self.map[row + j + 1][column - j - 1]:
                    score += 1
                else:
                    break
            except:
                break
        if score == 5:
            return True
        if player == 2:
            if score > 5:
                return True
            
    def mouse_click(self, x, y):
        if x >= border_left and x <= border_right and y >= border_top and y <= border_bottom:
            if self.started:
                column = round((x - 25) / 50)
                row = round((y - 25) / 50)
                print(column + 1, row + 1)
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
