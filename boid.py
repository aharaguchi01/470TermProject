import numpy as np
from vpython import *

global boxSize
boxSize = 100
class boid:
    
    def __init__(self):
        x, y, z = np.random.uniform(-1*boxSize/2, boxSize/2), np.random.uniform(-1*boxSize/2, boxSize/2), np.random.uniform(-1*boxSize/2, boxSize/2)
        center = vector(x,y,z)
        a, b, c = np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        ball = sphere(pos=center, radius=1)
        rExtension = box(pos=center+vector(1.4,0,0), length=1, width=0.5, height=0.5)
        lExtension = box(pos=center-vector(1.4,0,0), length=1, width=0.5, height=0.5)
        rPanel = box(pos=center+vector(2,0,0), length=0.2, height=6, width=4)
        lPanel = box(pos=center-vector(2,0,0), length=0.2, height=6, width=4)
        self.tie = compound([ball, rExtension, lExtension, rPanel, lPanel])
        self.tie.axis = vector(a,b,c)
        # self.cone = cone(pos=vector(x, y, z), axis=vector(a, b, c), length=1, radius=0.3, color=color.blue)
        self.velocity = np.random.uniform(0.5, 1.5)
        
    # axis is defined so they end up moving sideways, need to figure this out
    def move(self):
        self.velocity = np.random.uniform(0, 1)
        # if self.tie.pos.x > boxSize:
        #     self.tie.pos.x = 0
        # if self.tie.pos.x < 0:
        #     self.tie.pos.x = boxSize
        # if self.tie.pos.y > boxSize:
        #     self.tie.pos.y = 0
        # if self.tie.pos.y < 0:
        #     self.tie.pos.y = boxSize
        # if self.tie.pos.z > boxSize:
        #     self.tie.pos.z = 0
        # if self.tie.pos.z < 0:
        #     self.tie.pos.z = boxSize
        unit = self.tie.axis.norm()
        self.tie.pos = self.tie.pos + self.velocity * unit * 0.1
    
    def separate(self):
        pass
    
    def align(self):
        pass
    
    def cohere(self):
        pass 
