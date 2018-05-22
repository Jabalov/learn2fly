from OpenGL.GLUT import *
import numpy as np
from math import *
import pygame
from Player import drawPenguine
from Terrains import *
from Music import *
from coins import *
from Menu import *
angle = 0  # starting rotational angle for the penguine
xPenguine = -270  # penguine x coordinate
yPenguine = 259  # penguine y coordinate
extraspeed=0
pause=False
loss=False
result=0


def iceBergCollision(xpenguine,ypenguine,penguinehight,shift):
    xice=shift+700
    if xPenguine+penguinehight > xice-175 and xpenguine+penguinehight<xice-150:
       if ypenguine<=82/25*(xpenguine-shift)-2022:
            return True
    elif xpenguine+penguinehight>xice-150 and xpenguine+penguinehight<xice-115:
        if ypenguine<=4/5*(xpenguine-shift)-658:
            return True
    elif xpenguine+penguinehight>xice-115 and xpenguine+penguinehight<xice-90:
        if ypenguine<=23/5*(xpenguine-shift)-2881:
            return True
    elif xpenguine+penguinehight>xice-90 and xpenguine+penguinehight<xice-40:
        if ypenguine<=11/10*(xpenguine-shift)-746:
            return True
    elif xpenguine+penguinehight>xice-40 and xpenguine+penguinehight<xice-20:
        if ypenguine<=7/2*(xpenguine-shift)-2330:
             return True
    elif xpenguine+penguinehight>xice-20 and xpenguine+penguinehight<xice+11:
        if ypenguine<=-2*(xpenguine-shift)+1410:
            return True
    elif xpenguine+penguinehight>xice+11 and xpenguine+penguinehight<xice+135:
        if ypenguine<=12/25*(xpenguine-shift)-1754/5:
            return True


def drawText(string, x, y):
    glLineWidth(5)
    glColor(1,0,0,.5)
    glTranslate(x,y,0)
    glScale( .2 , 1 , 1 )
    string = string.encode( ) # conversion from unicode string to byte string
    for char in string:
         glutBitmapCharacter( GLUT_STROKE_ROMAN , char )

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-300, 300, -300, 300, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    # gluLookAt(xPenguine, 0, 1, xPenguine, yPenguine, 0, 0, 1, 0)



gameOver=True
aboutc=False
def keyboard(key, x, y):
    global angle
    global keyboard_y
    global xPenguine,extraspeed,pause,gameOver,aboutc
    if (key == b"d" or key == b"D" or key == GLUT_KEY_RIGHT or key == b'\xed') and xPenguine > 190 and not gameOver and not pause:
        angle -= 10
        if angle > 0:
            angle=0
        if angle < -180:
            angle =-180

    if (key == b"a" or key == b"A" or key == GLUT_KEY_LEFT or key == b'\xd4') and xPenguine > 190 and not gameOver and not pause:
        angle += 10

        if angle > 0:
            angle=0
        if angle < -180:
            angle =-180


    if key == b'\x1b':
        if aboutc:
            aboutc=False
            gameOver=True
        else:
            sys.exit()

    if key==b' ' and not gameOver and not pause:
        if extraspeed==15:
            extraspeed=0
        else:
            extraspeed=15

    if key ==b'p' or  key ==b'P' and not gameOver:
        if pause:
            pause=False
        else:
            pause=True


    if key == GLUT_KEY_DOWN and gameOver:
        keyboard_y -= 90

        if keyboard_y <= -350:
            keyboard_y = -270
    if key == GLUT_KEY_UP and gameOver:
        keyboard_y += 90
        if keyboard_y >= 18:
            keyboard_y = 0

    if key==b'\r' and gameOver:
        if player.top == 50 :
            gameOver=False
        elif player.top==-40:
            aboutc=True
        elif player.top==-130:
            sys.exit()


def MouseMotion(x, y):
   print((6 * x / 8)-300 , " ", (3*-y/5)+300)







samples = 0
t = 0
v = 0
intro=True

timeBeforeStart=0
LittlePush=4
def draw():
    global xPenguine
    global yPenguine
    global angle
    global samples, t, v,intro,gameOver,timeBeforeStart,extraspeed,pause,LittlePush,aboutc,loss,result
    icebergShift=500 #iceberg shift in x axis
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    backGround()





    vx=0


    # Movement beginning
    if not pause and not gameOver and not aboutc and not loss:
        if xPenguine>190 and yPenguine<=-300:
            #gameOver=True
            loss=True
        elif (xPenguine < -190 and yPenguine > 155) and intro:
            angle = -130

            xPenguine += 3
            yPenguine = -(8 / 7 * xPenguine) - (360 / 7)
            v=-3
        elif (xPenguine >= -190 and xPenguine < 200 and yPenguine > 60) and intro:
            angle = -180
            v=-3-9.8*timeBeforeStart
            yPenguine -= -v* timeBeforeStart + .5*timeBeforeStart*timeBeforeStart*1  # where g is the gravity and =1

            timeBeforeStart+=1
        elif (yPenguine <= 120 and xPenguine < -90) and intro:

            if samples < 11:
                angle += 8
                a = radians(180) + (samples / 10) * 1.57079633
                xPenguine = 100 * cos(a) - 90

                yPenguine = 100 * sin(a) + 50

                samples += 1

        elif xPenguine < 80 and intro:
            xPenguine += -v/5
            yPenguine = -50
        elif xPenguine < 200 and intro :
            angle = -60
            xPenguine += -v/5
            yPenguine = .5 * xPenguine - 93



        elif not gameOver:


                intro=False
                vx = (v/5 * sin(radians(angle))) + extraspeed *abs(sin(radians(angle)))
                vy = -v/5 * sin(radians(-angle))-9.8*t
                xPenguine+=vx*t +LittlePush

                if LittlePush>0:
                     LittlePush-=.1
                else:
                    LittlePush=0


                if extraspeed==0:
                    yPenguine=(vy*t-.5*t*t)+yPenguine
                else:
                    yPenguine += extraspeed * cos(radians(angle))
                    t=1

                if (iceBergCollision(xPenguine, yPenguine,30,icebergShift)):
                    loss = True

                t += .05

    res = str(result)
    if gameOver:
        DisplayMenu()
        xPenguine = -270
        yPenguine = 259
        intro=True
        samples = 0
        t = 0
        v = 0
        timeBeforeStart = 0
        extraspeed=0
        LittlePush = 4

    if aboutc:
        about()
        xPenguine = -270
        yPenguine = 259
        intro = True
        samples = 0
        t = 0
        v = 0
        timeBeforeStart = 0
        extraspeed = 0
        LittlePush = 4

    if loss:
        glLoadIdentity()
        losser(res)
        xPenguine = -270
        yPenguine = 259
        intro = True
        samples = 0
        t = 0
        v = 0
        timeBeforeStart = 0
        extraspeed = 0
        LittlePush = 4

    else:

        if not pause:
            glLoadIdentity()
            glTranslate(-xPenguine ,-yPenguine ,0)






    if not gameOver and not loss and not aboutc:
        drawPenguine(xPenguine,yPenguine,angle)


        cliff(icebergShift)

        drawGround()
        result=coins(xPenguine,yPenguine)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(800, 500)
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
