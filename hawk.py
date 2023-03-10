# implement hawk class
import numpy as np
from vpython import *

global boxSize
boxSize = 100
class hawk:
    def __init__(self):
            # creates tie fighter composite shape and places randomly in the scene
        x, y, z = np.random.uniform(-1 * boxSize / 2, boxSize / 2), np.random.uniform(-1 * boxSize / 2,boxSize / 2), np.random.uniform(-1 * boxSize / 2, boxSize / 2)
        center = vector(x, y, z)
        a, b, c = np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        body = cone(pos=center, axis=vector(0, 0, 4), radius=0.5)
        rPanel = box(pos=center, axis=vector(1, 0.5, 0), length=0.2, width=1, height=6)
        lPanel = box(pos=center, axis=vector(1, -0.5, 0), length=0.2, width=1, height=6)
        self.x_wing = compound([body, rPanel, lPanel])
        self.x_wing.axis = vector(a, b, c)
        self.x_wing.velocity = vector(a,b,c)
        self.view = 70 # view radius for neighborhood

    def move(self, dt = 0.1):
        unit = self.x_wing.axis.norm()
        self.x_wing.pos = self.x_wing.pos + self.x_wing.velocity*unit*dt
        if self.x_wing.pos.x > 20 or self.x_wing.pos.x < 0:
            self.x_wing.axis.x = -self.x_wing.axis.x
        if self.x_wing.pos.y > 20 or self.x_wing.pos.y < 0:
            self.x_wing.axis.y = -self.x_wing.axis.y
        if self.x_wing.pos.z > 20 or self.x_wing.pos.z < 0:
            self.x_wing.axis.z = -self.x_wing.axis.z
    # keeps boid within bounds
    def edge(self):
        buffer = 90
        turn = 1
        if self.x_wing.pos.x < -buffer / 2:
            self.x_wing.velocity.x += turn
        if self.x_wing.pos.x > buffer / 2:
            self.x_wing.velocity.x -= turn
        if self.x_wing.pos.y < -buffer / 2:
            self.x_wing.velocity.y += turn
        if self.x_wing.pos.y > buffer / 2:
            self.x_wing.velocity.y -= turn
        if self.x_wing.pos.z < -buffer / 2:
            self.x_wing.velocity.z += turn
        if self.x_wing.pos.z > buffer / 2:
            self.x_wing.velocity.z -= turn
    def chase(self):
        pass

    def eat(self):
        pass
