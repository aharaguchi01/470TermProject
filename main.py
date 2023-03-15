import boid as b
import hawk as h
import flock as f
from vpython import * 

scene.title = "A New Hope\n"

flockSize = 20
flock = f.flock(flockSize)

global includeHawk
includeHawk = True
    
if includeHawk:
    hawk = h.hawk()

def setSep(s):
    ws.text = '{:1.2f}'.format(s.value)
    scene.append_to_caption('\n\n')

def setAlign(s):
    wa.text = '{:1.2f}'.format(s.value)
    scene.append_to_caption('\n\n')

def setCoh(s):
    wc.text = '{:1.2f}'.format(s.value)
    scene.append_to_caption('\n\n')


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
cc = slider(min=0.0, max=1, value=0.5, length=220, bind=setCoh, right=25)
wc = wtext(text='{:1.2f}'.format(cc.value))
scene.append_to_caption(' Coherence\n')
scene.append_to_caption('       ')
scene.append_to_caption('\n\n')

while 1:
    rate(10)
    for boid in flock.boids:
        if boid.tie.visible == True:
            if includeHawk:
                boid.move(hawk, flock.boids, a=aa.value, c=cc.value, s=ss.value, r=0.5)
            else:
                boid.moveNoHawk(flock.boids, a=aa.value, c=cc.value, s=ss.value, r=0.5)
    if includeHawk:
        hawk.move(flock.boids)
