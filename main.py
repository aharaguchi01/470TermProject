import boid as b
import hawk as h
import flock as f
from vpython import * 

# box to help with visualization, remove later
side = 50.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk
wallR = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.green)
wallL = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.green)
wallB = box (pos=vector(0, -side, 0), size=vector(s3, thk, s3),  color = color.green)
wallT = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.green)
wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.green)

flockSize = 20
flock = f.flock(flockSize)
    
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

scene.autoscale = False

while 1:
    rate(10)
    for boid in flock.boids:
        boid.move(flock.boids, a=aa.value, c=cc.value, s=ss.value)
    hawk.move(flock)
