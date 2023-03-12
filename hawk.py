# implement hawk class
import numpy as np
from vpython import *
import math

global boxSize
boxSize = 100
class hawk:
    def __init__(self):
        # creates x-wing composite shape and places randomly in the scene
        x, y, z = np.random.uniform(-1 * boxSize / 2, boxSize / 2), np.random.uniform(-1 * boxSize / 2,boxSize / 2), np.random.uniform(-1 * boxSize / 2, boxSize / 2)
        center = vector(x, y, z)
        a, b, c = np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        d, e, f = np.random.uniform(0, 12), np.random.uniform(0, 12), np.random.uniform(0, 12)
        body = cone(pos=center, axis=vector(8, 0, 0), radius=0.8, color=color.red)
        rPanel = box(pos=center, axis=vector(0, 0, 1), up=vector(0, 3, 1), length=0.2, width=2, height=10, color=color.orange)
        lPanel = box(pos=center, axis=vector(0, 0, 1), up=vector(0, 3, -1), length=0.2, width=2, height=10, color=color.orange)
        self.x_wing = compound([body, rPanel, lPanel])
        self.x_wing.axis = vector(a, b, c)
        self.x_wing.velocity = vector(d, e, f)
        self.view = 20 # view radius for neighborhood
        self.boom = 5

    def move(self, flock):
        self.chase(flock)
        self.eat(flock)
        self.edge()
        self.x_wing.axis = self.x_wing.velocity.norm()
        self.x_wing.pos += self.x_wing.velocity.norm()

    # keeps hawk within bounds
    def edge(self):
        buffer = 80
        turn = 7
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

    # returns scalar distance from hawk to boid
    def distanceTo(self, other):
        return math.sqrt(pow(other.tie.pos.x - self.x_wing.pos.x, 2)
                         + pow(other.tie.pos.y - self.x_wing.pos.y, 2)
                         + pow(other.tie.pos.z - self.x_wing.pos.z, 2))

    def getNeighborhood(self, flock):
        neighborhood = []
        for boid in flock:
            boid.distance = self.distanceTo(boid)
            if boid.distance <= self.view and boid.tie.visible == True:
                neighborhood.append(boid)
        neighborhood.sort(key=lambda x: x.distance)
        return neighborhood

    def chase(self, flock):
        neighborhood = self.getNeighborhood(flock)
        if len(neighborhood) > 0:
            self.x_wing.velocity += (neighborhood[0].tie.pos - self.x_wing.pos)

    def eat(self, flock):
        neighborhood = self.getNeighborhood(flock)
        if len(neighborhood) > 0:
            dist = self.distanceTo(neighborhood[0])
            if dist < self.boom:
                # del neighborhood[0].tie
                neighborhood[0].tie.visible = False

