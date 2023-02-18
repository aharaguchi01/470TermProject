import numpy as np
from vpython import *

global boxSize
boxSize = 20
class boid:
    
    def __init__(self):
        x, y, z = np.random.uniform(0, boxSize), np.random.uniform(0, boxSize), np.random.uniform(0, boxSize)
        a, b, c = np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        self.cone = cone(pos=vector(x, y, z), axis=vector(a, b, c), length=1, radius=0.3, color=color.blue)
        self.velocity = np.random.uniform(0.5, 1.5)
        
    def move(self):
        self.velocity = np.random.uniform(0, 1)
        if self.cone.pos.x > boxSize:
            self.cone.pos.x = 0
        if self.cone.pos.x < 0:
            self.cone.pos.x = boxSize
        if self.cone.pos.y > boxSize:
            self.cone.pos.y = 0
        if self.cone.pos.y < 0:
            self.cone.pos.y = boxSize
        if self.cone.pos.z > boxSize:
            self.cone.pos.z = 0
        if self.cone.pos.z < 0:
            self.cone.pos.z = boxSize
        unit = self.cone.axis.norm()
        self.cone.pos = self.cone.pos + self.velocity * unit * 0.1
    
    def separate(self):
        pass
    
    def align(self):
        pass
    
    def cohere(self):
        pass 
