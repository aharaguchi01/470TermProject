# implement hawk class
import numpy as np
from vpython import *

class hawk:
    def __init__(self):
        x, y, z = np.random.uniform(0, 20), np.random.uniform(0, 20), np.random.uniform(0, 20)
        a, b, c = np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(-1, 1)

        self.cone = cone(pos=vector(x, y, z), axis=vector(a, b, c), color=color.red)
        self.velocity = np.random.uniform(0.5, 1)

    def move(self, dt = 0.1):
        unit = self.cone.axis.norm()
        self.cone.pos = self.cone.pos + self.velocity*unit*dt
        if self.cone.pos.x > 20 or self.cone.pos.x < 0:
            self.cone.axis.x = -self.cone.axis.x
        if self.cone.pos.y > 20 or self.cone.pos.y < 0:
            self.cone.axis.y = -self.cone.axis.y
        if self.cone.pos.z > 20 or self.cone.pos.z < 0:
            self.cone.axis.z = -self.cone.axis.z

    def chase(self):
        pass

    def eat(self):
        pass
