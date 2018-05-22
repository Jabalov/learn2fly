from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
import pygame



score = 0


def drawCoin(r=12, x0=225, y0=105, drawc=True):
    if drawc:
        glPushMatrix()
        glPushAttrib(GL_ALL_ATTRIB_BITS)
        glColor(255, 215, 0)
        glBegin(GL_POLYGON)
        for theta in np.arange(0, 2 * pi, .1):
            x = x0 + r * cos(theta)
            y = y0 + r * sin(theta)
            glVertex(x, y, -0.5)
        glEnd()
        glPopAttrib()
        glPopMatrix()
    else:
        r=30
        glPushMatrix()
        glPushAttrib(GL_ALL_ATTRIB_BITS)
        glColor(255, 0, 255)
        glBegin(GL_POLYGON)
        for theta in np.arange(0, 2 * pi, .1):
            x = x0 + r * cos(theta)
            y = y0 + r * sin(theta)
            glVertex(x, y, -0.5)
        glEnd()
        glPopAttrib()
        glPopMatrix()

radius=20
listx=[]
listy=[]
listdrawcon=[]
listc=[]
x=255
y=105
m=100

for i in range(1,50):
    if y>1000:
        m=-100
    elif y<500:
        m=100
    listx.append(x)
    listy.append(y)
    listdrawcon.append(True)
    listc.append(0)
    x+=200
    y+=m

def coins(xPenguine,yPenguine):
    global listx,listy,radius,listdrawcon,listc
    score=0
    for i in range(0,len(listx)):
        if ((xPenguine - listx[i]) ** 2 + (yPenguine - listy[i]) ** 2 <= (radius**2)):
            listdrawcon[i]=False
            listc[i]=1
        drawCoin(radius,listx[i],listy[i],listdrawcon[i])
        score+=listc[i]
    return score