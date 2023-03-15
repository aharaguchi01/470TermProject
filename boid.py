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
        d, e, f = np.random.uniform(0, 12), np.random.uniform(0, 12), np.random.uniform(0, 12)
        ball = simple_sphere(pos=center, radius=1, color=color.gray(0.5))
        rExtension = box(pos=center+vector(0,0,1.4), length=0.5, width=1, height=0.5, color=color.gray(0.5))
        lExtension = box(pos=center-vector(0,0,1.4), length=0.5, width=1, height=0.5, color=color.gray(0.5))
        rPanel = box(pos=center+vector(0,0,2), length=4, width=0.2, height=6, color=color.gray(0.5))
        lPanel = box(pos=center-vector(0,0,2), length=4, width=0.2, height=6, color=color.gray(0.5))
        self.tie = compound([ball, rExtension, lExtension, rPanel, lPanel])
        self.tie.axis = vector(a,b,c)
        self.tie.velocity = vector(d,e,f)
        self.view = 20 # view radius for neighborhood 
        self.runView = 10
        
        
    # moves one step based on changing axis
    def move(self, hawk, flock, a, c, s, r):
        self.cohere(flock, c)
        self.separate(flock, s)
        self.align(flock, a)
        self.run(hawk, r)
        self.edge()
        self.tie.axis = self.tie.velocity.norm()
        self.tie.pos += self.tie.velocity.norm()
        
    # moves one step based on changing axis
    def moveNoHawk(self, flock, a, c, s, r):
        self.cohere(flock, c)
        self.separate(flock, s)
        self.align(flock, a)
        self.edge()
        self.tie.axis = self.tie.velocity.norm()
        self.tie.pos += self.tie.velocity.norm()
        
    # keeps boid within bounds
    def edge(self):
        buffer = 90
        turn = 5
        if self.tie.pos.x < -buffer / 2:
            self.tie.velocity.x += turn
        if self.tie.pos.x > buffer / 2:
            self.tie.velocity.x -= turn
        if self.tie.pos.y < -buffer / 2:
            self.tie.velocity.y += turn
        if self.tie.pos.y > buffer / 2:
            self.tie.velocity.y -= turn
        if self.tie.pos.z < -buffer / 2:
            self.tie.velocity.z += turn
        if self.tie.pos.z > buffer / 2:
            self.tie.velocity.z -= turn
    
    # returns scalar distance from boid to another 
    def distanceTo(self, other):
        return math.sqrt(pow(other.tie.pos.x - self.tie.pos.x, 2)
                         + pow(other.tie.pos.y - self.tie.pos.y, 2)
                         + pow(other.tie.pos.z - self.tie.pos.z, 2))

    # returns scalar distance from boid to another 
    def distanceToHawk(self, hawk):
        return math.sqrt(pow(hawk.x_wing.pos.x - self.tie.pos.x, 2)
                         + pow(hawk.x_wing.pos.y - self.tie.pos.y, 2)
                         + pow(hawk.x_wing.pos.z - self.tie.pos.z, 2))
         
    # returns subset of flock containing boids in neighborhood of current boid 
    def getNeighborhood(self, flock):
        neighborhood = []
        for boid in flock:
            if boid != self:
                distance = self.distanceTo(boid)
                if distance <= self.view and boid.tie.visible == True:
                    neighborhood.append(boid)
        return neighborhood
    
    # changes axis away from other boids
    def separate(self, flock, s):
        minDistance = 10
        move = vector(0,0,0)
        for boid in flock:
            if boid != self:
                if self.distanceTo(boid) < minDistance:
                    move += self.tie.pos - boid.tie.pos
        self.tie.velocity += move * s
    
    # changes axis to align with flockmates
    def align(self, flock, a):
        neighborhood = self.getNeighborhood(flock)
        avg = vector(0,0,0)
        for boid in neighborhood:
            avg += boid.tie.axis
        if len(neighborhood) > 0:
            avg = avg / len(neighborhood)
            self.tie.velocity += (avg - self.tie.axis) * a
      
    # changes axis to move towards neighborhood center of mass      
    def cohere(self, flock, c):
        neighborhood = self.getNeighborhood(flock)
        cm = vector(0,0,0)
        for boid in neighborhood:
            cm.x += boid.tie.pos.x
            cm.y += boid.tie.pos.y
            cm.z += boid.tie.pos.z
        if len(neighborhood) > 0:
            cm.x = cm.x / len(neighborhood)
            cm.y = cm.y / len(neighborhood)
            cm.z = cm.z / len(neighborhood)
            self.tie.velocity += (cm - self.tie.pos) * c
            
    # oh no
    def run(self, hawk, r):
        runDistance = self.runView
        if self.distanceToHawk(hawk) < runDistance:
            self.tie.velocity += (self.tie.pos - hawk.x_wing.pos) * r
        