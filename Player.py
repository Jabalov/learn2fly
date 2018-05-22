from OpenGL.GL import *
from OpenGL.GLUT import *
import pygame
def drawPenguine(x,y,angle):
    xPenguine=x
    yPenguine=y

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
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glTranslate(xPenguine, yPenguine, 0)
    glRotate(angle, 0, 0, 1)
    glTranslate(-xPenguine, -yPenguine, 0)

    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex2d(xPenguine - 10, yPenguine - 20)

    glTexCoord(1, 0)
    glVertex2d(xPenguine + 10, yPenguine - 20)

    glTexCoord(1, 1)
    glVertex2d(xPenguine + 10, yPenguine + 20)

    glTexCoord(0, 1)
    glVertex2d(xPenguine - 10, yPenguine + 20)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glDeleteTextures(1, texture)
    glPopAttrib()
    glPopMatrix()