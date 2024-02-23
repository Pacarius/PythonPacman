import numpy
TILESIZE = [16, 16]
MAP = [36, 29]
WINDOWSIZE = numpy.multiply(TILESIZE, MAP)
DirectionMap = {
    'N': [0,-1],
    'E': [1,0],
    'S': [0,1],
    'W': [-1,0],
    'C': [0,0]
}    

