import boid as b
from vpython import * 

# set environment


boids = []

for i in range(100):
    boids.append(b.boid())

while 1:
    rate(100)
    for boid in boids:
        boid.move()
