import pygame


pygame.init()
screen = pygame.display.set_mode((750, 850))
pygame.display.set_caption("Gomoku")

border_left = 25
border_right = 725
border_top = 25
border_bottom = 725
width = 50
height = 50
msg_font = pygame.font.Font(None, 32)


class Button:
    
    def __init__(self, x, y, width, height, msg, color, click_color, msg_color):
        self.msg = msg
        self.color = color
        self.click_color = click_color
        self.msg_color = msg_color
        self.rect = pygame.Rect(x, y, width, height)
        self.clicked = False

    def draw(self, screen):
        if self.clicked:
            pygame.draw.rect(screen, self.click_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        msg_surf = msg_font.render(self.msg, 1, self.msg_color)
        msg_rect = msg_surf.get_rect(center = self.rect.center)
        screen.blit(msg_surf, msg_rect)

    def handle_event(self, event, game):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.clicked:
                    print("The game was started")
                else:
                    if game.winner == 0:
                        self.clicked = True
                        game.started = True
                        print("Start the game")
                    else:
                        self.clicked = True
                        game.started = True
                        game.player = 1
                        game.winner = 0
                        game.map = [0] * 15
                        for i in range(15):
                            game.map[i] = [0] * 15
                        print("Start the game again")
           
class Game:
    def __init__(self):
        self.started = False
        self.player = 1
        self.winner = 0
        self.map = [0] * 15
        for i in range(15):
            self.map[i] = [0] * 15

    def start(self):
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
        
        button.draw(screen)
        button_computer.draw(screen)

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
button = Button(50, 750, 200, 50, "person VS person", (135, 80, 10), (115, 60, 0), (255, 255, 255))
button_computer = Button(280, 750, 230, 50, "person VS computer", (135, 80, 10), (115, 60, 0), (255, 255, 255))
game = Game()


while True:
    for event in pygame.event.get():
        button.handle_event(event, game)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            game.mouse_click(x, y)
            
    game.start()           
    pygame.display.flip()

