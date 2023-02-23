import boid as b
import hawk as h
import flock as f
from vpython import * 

# set environment

flockSize = 10

flock = f.flock(flockSize)
    
hawk = h.hawk()

while 1:
    rate(100)
    for boid in flock.boids:
        boid.move()
    hawk.move()
