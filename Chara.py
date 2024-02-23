from DEFS import TILESIZE, DirectionMap
import numpy
import pygame.key
from Node import Node
import copy
class Character(object):
    def __init__(self, node):
        self.id = 0
        self.position = [200, 400]
        #North(N)/ East(E)/ South(S)/ West(W)/ C(Cunt)
        self.direction = 'C'
        self.speed = 100 * TILESIZE[1]/16
        self.radius = 10
        self.color = [255, 255, 0]
        self.node = node
        self.target = node
    #---------------------------------------------------
    def setPos(self):
        self.position = self.node.position
    def validDirection(self):
        if self.direction != 'C':
            if self.node.neighbours[self.direction] is not None:
                return True
        return False
    
    def getNewTarget(self):
        if self.validDirection():
            return self.node.neighbours[self.direction]
        return self.node
    
    #---------------------------------------------------
    def overshootComp(self):
        if self.target is not None:
            Uno = self.target.position - self.node.position
            Dos = self.position - self.node.position
            StupidUno = numpy.linalg.norm(Uno)**2
            StupidDos = numpy.linalg.norm(Dos)**2
            return StupidUno >= StupidDos
        return False
    #---------------------------------------------------

    def update(self, dt):
        self.direction = self.GetKey()
        tmp = numpy.multiply(DirectionMap[self.direction], numpy.full(numpy.shape(self.position), self.speed * dt))
        self.position = numpy.add(self.position, tmp)
        if self.overshootComp():
            self.node = self.target
            self.target = self.getNewTarget(self.direction)
            if self.target is not self.node:
                self.direction = self.direction
            else:
                self.direction = 'C'
            self.setPosition()
    def GetKey(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            tmp = 'N'
        elif key[pygame.K_DOWN]:
            tmp = 'S'
        elif key[pygame.K_LEFT]:
            tmp = 'W'
        elif key[pygame.K_RIGHT]:
            tmp = 'E'
        else:
            tmp = 'C'
        return tmp
    def render(self, screen):
        p = (round(self.position[0]),round(self.position[1]))
        pygame.draw.circle(screen, self.color, p, self.radius) 