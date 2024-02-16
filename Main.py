import pygame
from pygame.locals import *
from DEFS import *
from Chara import *
class GAME(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOWSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
        self.Chara = Character()
    def setBackground(self):
        self.background = pygame.surface.Surface(WINDOWSIZE).convert()
        self.background.fill([0, 0, 0])
    def start(self):
        self.setBackground()
    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.Chara.update(dt)
        self.checkEvents()
        self.render()
    def checkEvents(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
    def render(self):
        self.screen.blit(self.background, (0,0))
        self.Chara.render(self.screen)
        pygame.display.update()

game = GAME()
game.start()
while True:
    game.update()