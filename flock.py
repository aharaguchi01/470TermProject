import boid
from vpython import * 

class flock:
    
    def __init__(self, flockSize):
        self.boids = [boid.boid() for i in range(flockSize)]
        self.flockSize = flockSize
        
    # computes center of mass of the flock
    def cm(self):
        x = 0
        y = 0
        z = 0
        for boid in self.boids:
            x += boid.tie.pos.x
            y += boid.tie.pos.y
            z += boid.tie.pos.z
        return vector(x / self.flockSize, y / self.flockSize, z / self.flockSize)
    
    # computes average heading (direction) of flock
    def heading(self):
        x = 0
        y = 0
        z = 0
        for boid in self.boids:
            x += boid.tie.axis.x
            y += boid.tie.axis.y
            z += boid.tie.axis.z
        return vector(x / self.flockSize, y / self.flockSize, z / self.flockSize)
    