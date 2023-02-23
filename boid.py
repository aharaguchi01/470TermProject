import numpy as np
from vpython import *
import math

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
        bubble = sphere(pos=center, radius=4.2)
        bubble.opacity = 0
        self.tie = compound([ball, rExtension, lExtension, rPanel, lPanel, bubble])
        self.tie.axis = vector(a,b,c)
        # self.cone = cone(pos=vector(x, y, z), axis=vector(a, b, c), length=1, radius=0.3, color=color.blue)
        self.velocity = np.random.uniform(0.5, 1.5)
        
    # axis is defined so they end up moving sideways, need to figure this out
    # this method should implement the three rules with the direction to move in
    # dictated by the relative importance of each rule
    def move(self, s, a, c):
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
    
    # returns scalar distance from boid to another 
    def distanceTo(self, other):
        return math.sqrt(pow(other.tie.pos.x - self.tie.pos.x, 2)
                         + pow(other.tie.pos.y - self.tie.pos.y, 2)
                         + pow(other.tie.pos.z - self.tie.pos.z, 2))
        
    # checks to see if boid has collided with another 
    def checkOverlap(self, other):
        if self.tie.bubble.pos in other.tie.bubble.pos: # don't know if this actually works 
            return True
        return False
        
    # returns vector from self to other
    def r(self, other):
        x = other.tie.pos.x - self.tie.pos.x
        y = other.tie.pos.y - self.tie.pos.y
        z = other.tie.pos.z - self.tie.pos.z
        return vector(x, y, z)
       
    # returns subset of flock containing boids in neighborhood of current boid 
    def getNeighborhood(self, flock, nearRange):
        for boid in flock:
            boid.distance = self.distanceTo(boid)
        flock.sort(key=lambda x: x.distance)
        return flock[0:nearRange]
    
    def separate(self):
        pass
    
    # returns average heading (axis) of local flockmates
    def align(self, flock, nearRange):
        neighborhood = self.getNeighborhood(flock, nearRange)
        x = 0
        y = 0
        z = 0
        for boid in neighborhood:
            x += boid.tie.axis.x
            y += boid.tie.axis.y
            z += boid.tie.axis.z
        return vector(x / flock.flockSize, y / flock.flockSize, z / flock.flockSize)
    
    # returns vector from boid to center of mass of local flockmates
    def cohere(self, flock, nearRange):
        neighborhood = self.getNeighborhood(flock, nearRange)
        x = 0
        y = 0
        z = 0
        for boid in neighborhood:
            x += boid.tie.pos.x
            y += boid.tie.pos.y
            z += boid.tie.pos.z
        cm = vector(x / flock.flockSize, y / flock.flockSize, z / flock.flockSize)
        return cm - self.tie.pos
