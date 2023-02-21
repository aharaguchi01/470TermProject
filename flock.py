import boid
from vpython import * 

class flock:
    
    def __init__(self, flockSize):
        self.boids = [boid.boid() for i in range(flockSize)]
        self.flockSize = flockSize
        
    # computer center of mass of the flock
    def cm(self):
        x = 0
        y = 0
        z = 0
        for boid in self.boids:
            x += boid.cone.pos.x
            y += boid.cone.pos.y
            z += boid.cone.pos.z
        return vector(x / self.flockSize, y / self.flockSize, z / self.flockSize)