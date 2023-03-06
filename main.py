import boid as b
import hawk as h
import flock as f
from vpython import * 


flockSize = 10

# tunable parameters (0<p<1, dictate relative importance of each rule)
# s = 0.08 # separation
# a = 0.06 # alignment
# c = 0.05 # cohesion

speed = 1 # between 0 and 1 ish 

flock = f.flock(flockSize)
    
# hawk = h.hawk()

def setSep(s):
    ws.text = '{:1.2f}'.format(s.value)
    scene.append_to_caption('\n\n')

def setAlign(s):
    wa.text = '{:1.2f}'.format(s.value)
    scene.append_to_caption('\n\n')

def setCoh(s):
    wc.text = '{:1.2f}'.format(s.value)
    scene.append_to_caption('\n\n')


# figure out how to bind s, a, c, and speed to sliders
ss = slider(min=0.0, max=1.0, value=0.5, length=220, bind=setSep, right=15)
ws = wtext(text='{:1.2f}'.format(ss.value))
scene.append_to_caption(' Separation\n')
scene.append_to_caption('       ')
scene.append_to_caption('\n\n')
aa = slider(min=0.0, max=1.0, value=0.5, length=220, bind=setAlign, right=20)
wa = wtext(text='{:1.2f}'.format(aa.value))
scene.append_to_caption(' Alignment\n')
scene.append_to_caption('       ')
scene.append_to_caption('\n\n')
cc = slider(min=0.0, max=1.0, value=0.5, length=220, bind=setCoh, right=25)
wc = wtext(text='{:1.2f}'.format(cc.value))
scene.append_to_caption(' Coherence\n')
scene.append_to_caption('       ')

scene.autoscale = False

while 1:
    rate(100)
    for boid in flock.boids:
        boid.move(boid.moveVect(flock, a=aa.value, c=cc.value, s=ss.value), speed)
    # hawk.move()
