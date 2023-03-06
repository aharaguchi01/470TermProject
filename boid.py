import numpy as np
from vpython import *
import math

global boxSize
boxSize = 100

class boid():
    
    def __init__(self):
        # creates tie fighter composite shape and places randomly in the scene
        x, y, z = np.random.uniform(-1*boxSize/2, boxSize/2), np.random.uniform(-1*boxSize/2, boxSize/2), np.random.uniform(-1*boxSize/2, boxSize/2)
        center = vector(x,y,z)
        a, b, c = np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        ball = sphere(pos=center, radius=1)
        rExtension = box(pos=center+vector(0,0,1.4), length=0.5, width=1, height=0.5)
        lExtension = box(pos=center-vector(0,0,1.4), length=0.5, width=1, height=0.5)
        rPanel = box(pos=center+vector(0,0,2), length=4, width=0.2, height=6)
        lPanel = box(pos=center-vector(0,0,2), length=4, width=0.2, height=6)
        self.tie = compound([ball, rExtension, lExtension, rPanel, lPanel])
        self.tie.axis = vector(a,b,c)
        # sets view radius for neighborhood
        self.view = 5
        
    # takes in unit vector of desired direction of motion, and moves one step
    def move(self, vect, speed):
        self.tie.axis = vect
        self.tie.pos += self.tie.axis * speed
        if self.tie.pos.x >= boxSize or self.tie.pos.y >= boxSize or self.tie.pos.z >= boxSize:
            self.tie.axis = -1 * self.tie.axis
    
    # computes vector to move in, based on three rules and their relative importance
    def moveVect(self, flock, s, a, c):
        # self.velocity = np.random.uniform(0, 1)
        separate = self.separate(flock) * s
        align = self.align(flock) * a
        cohere = self.cohere(flock) * c
        return separate + align + cohere
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
        # unit = self.tie.axis.norm()
        # self.tie.pos = self.tie.pos + self.velocity * unit * 0.1
    
    # returns scalar distance from boid to another 
    def distanceTo(self, other):
        return math.sqrt(pow(other.tie.pos.x - self.tie.pos.x, 2)
                         + pow(other.tie.pos.y - self.tie.pos.y, 2)
                         + pow(other.tie.pos.z - self.tie.pos.z, 2))
        
    # checks to see if boid has collided with another 
    def checkOverlap(self, other):
        if self.distanceTo(other) <= 3.5: # this 3.5 is rather arbitraty
            return True
        return False
        
    # returns vector from self to other
    def r(self, other):
        x = other.tie.pos.x - self.tie.pos.x
        y = other.tie.pos.y - self.tie.pos.y
        z = other.tie.pos.z - self.tie.pos.z
        return vector(x, y, z)
       
    # returns subset of flock containing boids in neighborhood of current boid 
    def getNeighborhood(self, flock):
        neighborhood = []
        for boid in flock.boids:
            boid.distance = self.distanceTo(boid)
            if boid.distance <= self.view:
                neighborhood.append(boid)
        return neighborhood
    
    def separate(self, flock):
        neighborhood = self.getNeighborhood(flock)
        toOther = vector(0,0,0)
        for boid in neighborhood:
            toOther += self.r(boid)
        toOther = toOther / len(neighborhood)
        return -1 * toOther
    
    # returns average heading (axis) of local flockmates
    def align(self, flock):
        neighborhood = self.getNeighborhood(flock)
        axis = vector(0,0,0)
        for boid in neighborhood:
            axis += boid.tie.axis
        return norm(axis / flock.flockSize)
    
    # returns unit vector from boid to center of mass of local flockmates
    def cohere(self, flock):
        neighborhood = self.getNeighborhood(flock)
        cm = vector(0,0,0)
        for boid in neighborhood:
            cm += boid.tie.pos
        cm = cm / flock.flockSize
        return norm(cm - self.tie.pos)
