from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame



WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
left=0
bottom=0
right=0
top=0

w=-200
s=-400

time_interval = 50 # try  2,5,7 msec


class RECTA:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

player = RECTA(0, 0, 100, 0)  # initial position of the indicator



def cube():
    glLoadIdentity()
    glColor(0,.8,0,0.3)
    glTranslate(400+s,200+w,0)
    glScale(60,40,0)
    glutSolidCube(10)
def cube1():
    glLoadIdentity()
    glTranslate(400+s,350+w,0)
    glBegin(GL_POLYGON)
    glColor(0,0,1,.5)
    glVertex2d(-300,50)
    glVertex2d(-300, 0)
    glVertex2d(-10, 0)
    glVertex2d(10, 25)
    glVertex2d(300, 25)
    glVertex2d(300, 50)
    glEnd()
def DrawRectangle(rect):
    glLoadIdentity()
    glColor(0,0,0)
    glTranslate(300+s, 300+w, 0)
    glScale(2.3,.5,0)
    glBegin(GL_LINE_LOOP)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()


def drawText(string, x, y):
    glLineWidth(2)
    glColor(0, 0, 0)  #  Color
    glLoadIdentity()
    glTranslate(x+50+s, y+w, 0)
    glScale(0.20, 0.13, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)




# Key Board Messages
def keyboard(key, x, y):
    if key == b"q":
        sys.exit(0)

mouse_y = 0
keyboard_y= 0

def MouseMotion(x, y):
   print(x , " ", y)
p=90
def arrow_press(key ,x,y):

    global keyboard_y
    if key == GLUT_KEY_DOWN:
        keyboard_y -=p

        if keyboard_y <= -180:
            keyboard_y=-180
    elif key == GLUT_KEY_UP:
        keyboard_y +=p
        if keyboard_y>=18:
            keyboard_y=0

def DisplayMenu():
    glClearColor(0, 0, 0, 0)
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glClear(GL_COLOR_BUFFER_BIT)

    cube()
    cube1()

    glColor(0,0,1)
    player.bottom = keyboard_y -50
    player.top = keyboard_y + 50

    DrawRectangle(player)
    glutSpecialFunc(arrow_press)

    string = "MAIN MENU  "
    drawText(string, 100, 370)

    string = "PLAY"
    drawText(string, 300, 300)

    string = "ABOUT "
    drawText(string, 300, 250)
    string = "QUIT "
    drawText(string, 300, 200)
    glPopAttrib()
    glPopMatrix()




def about():
    glClearColor(0, 102, 128, 0)
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glClear(GL_COLOR_BUFFER_BIT)

    #cube()
    #cube1()

    glColor(0, 0, 1)

    #glutSpecialFunc(arrow_press)
    glColor(0,1,0)
    drawText("MOHAMED ABO-GABL", 200, 370)
    drawText("OMAR ATTALLAH", 200, 340)
    drawText("OMAR SALEH", 200, 290)
    drawText("ABDALLAH EL-GENDY", 200, 250)
    drawText("ABDALLAH EL-SHORA", 200, 210)
    drawText("GHARIB AMER", 200, 170)
    drawText("ALY EL-DEWENY", 200, 130)
    drawText("ESLAM AHMED", 200, 90)
    drawText("AHMED EL-GEBALY", 200, 50)
    drawText("OSAMA EL-SHIKH", 200, 10)
    drawText("MOHAMED MOSTAFA", 200, -30)
    glPopAttrib()
    glPopMatrix()

def losser(res):
    glClearColor(0, 102, 128, 0)
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glClear(GL_COLOR_BUFFER_BIT)

    cube()
    #cube1()

    glColor(0, 0, 1)

    string = "GAME OVER  "
    drawText(string, 260, 250)

    string = "YOUR SCORE"
    drawText(string, 255, 200)

    string = res
    drawText(string, 340, 150)
    glPopAttrib()
    glPopMatrix()






