import boid
from vpython import * 

class flock:
    
    def __init__(self, flockSize):
        self.boids = [boid.boid() for i in range(flockSize)]
        self.flockSize = flockSize
        
    # actually might not end up using these two methods
        
    # computes center of mass of the flock
    def cm(self):
        cm = vector(0,0,0)
        for boid in self.boids:
            cm += boid.tie.pos
        return cm / self.flockSize
    
    # computes average heading (direction) of flock
    def heading(self):
        dir = vector(0,0,0)
        for boid in self.boids:
            dir += boid.tie.axis
        return dir / self.flockSize
    