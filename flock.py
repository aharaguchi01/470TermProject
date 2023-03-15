import boid
from vpython import * 

class flock:
    
    def __init__(self, flockSize):
        self.boids = [boid.boid() for i in range(flockSize)]
        self.flockSize = flockSize
                
    # computes center of mass of the flock
    def cm(self):
        cm = vector(0,0,0)
        for boid in self.boids:
            cm += boid.tie.pos
        return cm / self.flockSize
    