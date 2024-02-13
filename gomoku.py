import pygame
from gomoku_cls import *


pygame.init()
screen = pygame.display.set_mode((750, 850))
pygame.display.set_caption("Gomoku")

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
           

button = Button(50, 750, 200, 50, "person VS person", (135, 80, 10), (115, 60, 0), (255, 255, 255))
button_computer = Button(280, 750, 230, 50, "person VS computer", (135, 80, 10), (115, 60, 0), (255, 255, 255))
game = Game(screen, button, button_computer)


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

