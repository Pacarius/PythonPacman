from DEFS import TILESIZE
import numpy
import pygame.key
class Character(object):
    def __init__(self):
        self.id = 0
        self.position = [200, 400]
        #North(N)/ East(E)/ South(S)/ West(W)/ C(Cunt)
        self.direction = 'C'
        self.speed = 100 * TILESIZE[1]/16
        self.radius = 10
        self.color = [255, 255, 0]
    DirectionMap = {'N': [0,-1],
                    'E': [1,0],
                    'S': [0,1],
                    'W': [-1,0],
                    'C': [0,0]
    }
    def update(self, dt):
        self.direction = self.GetKey()
        tmp = numpy.multiply(self.DirectionMap[self.direction], numpy.full(numpy.shape(self.position), self.speed * dt))
        print(self.position)
        self.position = numpy.add(self.position, tmp)
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