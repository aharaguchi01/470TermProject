import boid as b
import hawk as h
from vpython import * 

# set environment


boids = []

for i in range(100):
    boids.append(b.boid())
    
hawk = h.hawk()

while 1:
    rate(100)
    for boid in boids:
        boid.move()
    hawk.move()
