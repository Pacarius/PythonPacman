import pygame

class Node(object):
    def __init__(self, x, y):
        self.position = [x, y]
        self.neighbours = {'N':None, 'S':None,'W':None,'E':None}
    
    def render(self, screen):
        for i in self.neighbours.keys():
            if self.neighbours[i] is not None:
                lstart = self.position
                lend = self.neighbours[i].position
                pygame.draw.line(screen, [255, 255, 255], lstart, lend, 4)
                pygame.draw.circle(screen, [255, 0, 0], self.position, 12)

class NodeGroup(object):
    def __init__(self) :
        self.nodeList = []
    
    def testNodes(self):
        nodeA = Node(80 ,80)
        nodeB = Node(160, 80)
        nodeC = Node(80, 160)
        nodeD = Node(160, 160)
        nodeE = Node(208, 160)
        nodeF = Node(80, 320)
        nodeG = Node(208, 320)
        nodeA.neighbours['E'] = nodeB
        nodeA.neighbours['S'] = nodeC
        nodeB.neighbours['W'] = nodeA
        nodeB.neighbours['S'] = nodeD
        nodeC.neighbours['N'] = nodeA
        nodeC.neighbours['E'] = nodeD
        nodeC.neighbours['S'] = nodeF
        nodeD.neighbours['N'] = nodeB
        nodeD.neighbours['W'] = nodeC
        nodeD.neighbours['E'] = nodeE
        nodeE.neighbours['W'] = nodeD
        nodeE.neighbours['S'] = nodeG
        nodeF.neighbours['N'] = nodeC
        nodeF.neighbours['E'] = nodeG
        nodeG.neighbours['N'] = nodeE
        nodeG.neighbours['W'] = nodeF
        self.nodeList = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG]
    
    def render(self, screen):
        for i in self.nodeList:
            i.render(screen)