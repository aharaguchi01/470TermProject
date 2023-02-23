import boid as b
import hawk as h
import flock as f
from vpython import * 

# set environment

flockSize = 10
nearRange = 4 # this number sets the range of a given boid's "neighborhood"

# tunable parameters (0<p<1, dictate relative imporance of each rule)
s = 1 # separation
a = 0.5 # alignment
c = 0.5 # cohesion


flock = f.flock(flockSize)
    
hawk = h.hawk()

while 1:
    rate(100)
    for boid in flock.boids:
        boid.move(flock, nearRange, s, a, c)
    hawk.move()
