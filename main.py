import boid as b
import hawk as h
import flock as f
from vpython import * 


flockSize = 10

# tunable parameters (0<p<1, dictate relative imporance of each rule)
s = 0.3 # separation
a = 0.6 # alignment
c = 0.2 # cohesion

speed = 1 # between 0 and 1 ish 


flock = f.flock(flockSize)
    
# hawk = h.hawk()

# figure out how to bind s, a, c, and speed to sliders
# ss = slider(bind=s)

scene.autoscale = False

while 1:
    rate(100)
    for boid in flock.boids:
        boid.move(boid.moveVect(flock, s, a, c), speed)
    # hawk.move()
