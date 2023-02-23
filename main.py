import boid as b
import hawk as h
import flock as f
from vpython import * 

# set environment

flockSize = 1
nearRange = 20 # this number sets the range of a given boid's "neighborhood"

# tunable parameters (0<p<1, dictate relative imporance of each rule)
s = 1 # separation
a = 1 # alignment
c = 1 # cohesion


flock = f.flock(flockSize)
    
hawk = h.hawk()

while 1:
    rate(100)
    for boid in flock.boids:
        boid.move()
    hawk.move()
