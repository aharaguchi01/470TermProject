import numpy as np
from vpython import *

class boid:
    
    def __init__(self):
        x, y, z = np.random.uniform(0,20), np.random.uniform(0,20), np.random.uniform(0,20)
        a, b, c = np.random.uniform(-1,1), np.random.uniform(-1,1), np.random.uniform(-1,1)
        self.cone = cone(pos=vector(x,y,z), axis=vector(a,b,c), length=1, radius=0.3, color=color.blue)
        self.velocity = np.random.uniform(0,1)
        
    def move(self):
        self.velocity = np.random.uniform(0,1)
        if self.cone.pos.x > 20 or self.cone.pos.x < 0:
            self.cone.axis = -1 * self.cone.axis
        elif self.cone.pos.y > 20 or self.cone.pos.y < 0:
            self.cone.axis = -1 * self.cone.axis
        elif self.cone.pos.z > 20 or self.cone.pos.z < 0:
            self.cone.axis = -1 * self.cone.axis
        unit = self.cone.axis.norm()
        self.cone.pos = self.cone.pos + self.velocity * unit * 0.1
    
    def separate(self):
        pass
    
    def align(self):
        pass
    
    def cohere(self):
        pass 
