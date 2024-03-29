import pygame
from pygame.locals import *
from DEFS import *
from Chara import *
from Node import NodeGroup
'''
Closely following code from pacmancode.com
'''
class GAME(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOWSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
    def setBackground(self):
        self.background = pygame.surface.Surface(WINDOWSIZE).convert()
        self.background.fill([0, 0, 0])
    def start(self):
        self.setBackground()
        self.nodes = NodeGroup()
        self.nodes.testNodes()
        self.Chara = Character(self.nodes.nodeList[0])
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
        self.nodes.render(self.screen)
        self.Chara.render(self.screen)
        pygame.display.update()
game = GAME()
game.start()
while True:
    game.update()