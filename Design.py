from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
import pygame

angle = 0  # starting rotational angle for the penguine
xPenguine = -270  # penguine x coordinate
yPenguine = 259  # penguine y coordinate
delsh=0

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-300, 800, -300, 300, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    # gluLookAt(xPenguine, 0, 1, xPenguine, yPenguine, 0, 0, 1, 0)


def backGround():
    global shift
    texture = glGenTextures(1)
    back_ground = pygame.image.load("sky.jpg")

    background_raw = pygame.image.tostring(back_ground, "RGBA", 1)

    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, back_ground.get_width(), back_ground.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE,
                 background_raw)
    glEnable(GL_TEXTURE_2D)
    glLoadIdentity()
    glTranslate(shift,0,0)
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-300, -300, 0)

    glTexCoord(1, 0)
    glVertex(10000, -300, 0)

    glTexCoord(1, 1)
    glVertex(10000, 300, 0)

    glTexCoord(0, 1)
    glVertex(-300, 300, 0)
    glEnd()
    glDisable(GL_TEXTURE_2D)


# def conicSections(a, b, x, y):
#     glBegin(GL_POLYGON)
#
#     for th in np.arange(0, 2 * pi, .001):
#         r = (a * b) / sqrt(((b ** 2) * (cos(th) ** 2)) + ((a ** 2) * (sin(th) ** 2)))
#         x1 = r * sin(th)
#         y1 = r * cos(th)
#         glVertex2d(x + x1, y + y1)
#
#     glEnd()


def Torus2d(angle, length, radius, width, samples):
    if samples < 3:
        samples = 3
    outer = radius + width
    glBegin(GL_QUAD_STRIP)
    for i in range(samples + 1):
        a = angle + (i / samples) * length
        glVertex2d(radius * cos(a), radius * sin(a))
        glVertex2d(outer * cos(a), outer * sin(a))

    glEnd()


def circle(r, x1, y1):
    glColor(255,215,0)
    for th in np.arange(0, 2 * pi, .001):
        x = r * sin(th)+x1
        y = r * cos(th)+y1
        glBegin(GL_LINES)

        glVertex2d(x , y )
        glVertex2d(x1,y1)

        glEnd()


def MouseMotion(x, y):
    print((6 * x / 8) - 300, " ", (6 * (-y + 500) / 5) - 300)



deltaangle=0
m=0
def keyboard(key, x, y):
    global deltaangle
    global m
    if key == b"d" or key == b"D" or key == GLUT_KEY_DOWN:
        deltaangle=-30
        m=-5
    if key == b"a" or key == b"A" or key == GLUT_KEY_UP:
        deltaangle = 30
        m=5
    if key== b"s":
        deltaangle=0
        m=0
    if key == b'\x1b':
        sys.exit()


shift=0
def cliff():
    global vtime
    global shift
    global delsh
    # left most vertical Part
    if vtime>.9:
        shift-= delsh

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glLoadIdentity()
    glColor(1, 1, 1)
    glTranslate(shift,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(-400, 240)
    glVertex2d(-400, 40)
    glVertex2d(-199, 40)
    glVertex2d(-199, 160)
    glVertex2d(-270, 240)
    glEnd()
    glLoadIdentity()
    # the joint between the vertical and horizontal parts.
    glTranslate(-98.7+shift, 40, 0)
    Torus2d(radians(180), 1.57079633, 100, 150, 10)
    glLoadIdentity()
    # the horizontal part.
    glTranslate(shift,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(-100, -210)
    glVertex2d(190, -210)
    glVertex2d(190, -10)
    glVertex2d(90, -60)
    glVertex2d(-100, -60)
    glEnd()
    glLoadIdentity()
    # circle(20,60,0)
    glPopAttrib()
    glPopMatrix()


def drawPenguine():
    global angle
    global xPenguine
    global yPenguine

    texture = glGenTextures(1)
    penguine = pygame.image.load("penguine.png")

    penguine_raw = pygame.image.tostring(penguine, "RGBA", 1)

    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 4, penguine.get_width(), penguine.get_height(), 1, GL_RGBA, GL_UNSIGNED_BYTE,
                 penguine_raw)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_TEXTURE_2D)

    glLoadIdentity()

    glTranslate(xPenguine, yPenguine, 0)
    glRotate(angle, 0, 0, 1)
    glTranslate(-xPenguine, -yPenguine, 0)

    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex2d(xPenguine - 20, yPenguine - 45)

    glTexCoord(1, 0)
    glVertex2d(xPenguine + 20, yPenguine - 45)

    glTexCoord(1, 1)
    glVertex2d(xPenguine + 20, yPenguine + 45)

    glTexCoord(0, 1)
    glVertex2d(xPenguine - 20, yPenguine + 45)
    glEnd()

    glDisable(GL_TEXTURE_2D)

def drawText(string, x, y):
    glLineWidth(10)
    glColor(1,0,0,.5) # Yellow color
    glLoadIdentity() # WHY?
    glTranslate(x,y,0)
    glScale( .7 , 1 , 1 )
    string = string.encode( ) # conversion from unicode string to byte string
    for char in string:
         glutStrokeCharacter( GLUT_STROKE_ROMAN , char )










samples = 0
t = 0
vx = 15
vy = 50
vtime=0
startV=20
thetaTH=.4363

def draw():
    global xPenguine
    global yPenguine
    global angle
    global samples, t, vx, vy
    global vtime
    global startV
    global thetaTH
    global deltaangle
    global m
    global shift
    global delsh
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    backGround()
    # Movement beginning

    if xPenguine < -190 and yPenguine > 155:
        angle = -130
        xPenguine += 10
        yPenguine = -(8 / 7 * xPenguine) - (360 / 7)
    elif xPenguine >= -190 and xPenguine < 200 and yPenguine > 60:
        angle = -180
        yPenguine -= 20
    elif yPenguine <= 120 and xPenguine < -90:

        if samples < 11:
            angle += 15
            a = radians(180) + (samples / 10) * 1.57079633
            xPenguine = 100 * cos(a) - 90
            if yPenguine < 10:
                yPenguine = 100 * sin(a) + 50
            else:
                yPenguine = 100 * sin(a) + 40
            samples += 2

    elif xPenguine < 80:
        xPenguine += 60
    elif xPenguine < 200:
        angle = -40
        xPenguine += 60
        yPenguine = .5 * xPenguine - 93

    elif vtime<.9:
        xPenguine=xPenguine+startV*cos(thetaTH)*vtime
        yPenguine=yPenguine+startV*sin(thetaTH)*vtime-.5*10*vtime**2
        vtime=vtime+.25
        angle-=10
    else :

        if yPenguine<=-300:
            drawText("Game Over",0,0)
            delsh=0
        else:
            angle = -90 + deltaangle
            yPenguine += m
            delsh=15


    drawPenguine()

    cliff()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutCreateWindow(b"Penguine")
# glutFullScreen()
# glutEnterGameMode()
glutDisplayFunc(draw)
glutKeyboardFunc(keyboard)
glutSpecialFunc(keyboard)
glutPassiveMotionFunc(MouseMotion)
glutIdleFunc(draw)
myInit()
glutMainLoop()
