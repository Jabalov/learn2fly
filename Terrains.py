import pygame
from geometricShapes import *

def cliff(icebergShift):

    texture = glGenTextures(1)
    back_ground = pygame.image.load("iceberg.png")

    background_raw = pygame.image.tostring(back_ground, "RGBA", 1)

    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 4, back_ground.get_width(), back_ground.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE,
                 background_raw)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_TEXTURE_2D)

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex2d(400+icebergShift, -600)

    glTexCoord(1, 0)
    glVertex2d(1000+icebergShift, -600)

    glTexCoord(1, 1)
    glVertex2d(1000+icebergShift, 200)

    glTexCoord(0, 1)
    glVertex2d(400+icebergShift, 200)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glDeleteTextures(1, texture)
    glPopAttrib()
    glPopMatrix()
    # left most vertical Part
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.498, 1.000, 0.831)
    glBegin(GL_POLYGON)
    glVertex2d(-600, 240)
    glVertex2d(-600, 40)
    glVertex2d(-199, 40)
    glVertex2d(-199, 160)
    glVertex2d(-270, 240)
    glEnd()
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    # the joint between the vertical and horizontal parts.
    glColor(0.498, 1.000, 0.831)
    glTranslate(-98.7, 40, 0)
    Torus2d(radians(180), 1.57079633, 100, 150, 10)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.498, 1.000, 0.831)
    # the horizontal part.
    glBegin(GL_POLYGON)
    glVertex2d(-300, -300)
    glVertex2d(190, -300)
    glVertex2d(190, -10)
    glVertex2d(90, -60)
    glVertex2d(-300, -60)
    glEnd()
    glPopAttrib()
    glPopMatrix()


    # the left down of the cliff
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0.498, 1.000, 0.831)
    # the horizontal part.
    glBegin(GL_POLYGON)
    glVertex2d(-600, -300)
    glVertex2d(-600, 40)
    glVertex2d(-300, 40)
    glVertex2d(-300, -300)
    glEnd()
    glPopAttrib()
    glPopMatrix()


def backGround():
    texture = glGenTextures(1)
    back_ground = pygame.image.load("sky.jpg")

    background_raw = pygame.image.tostring(back_ground, "RGBA", 1)

    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, back_ground.get_width(), back_ground.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE,
                 background_raw)
    glEnable(GL_TEXTURE_2D)
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-600, -500, 0)

    glTexCoord(1, 0)
    glVertex(1000000, -500, 0)

    glTexCoord(1, 1)
    glVertex(1000000, 10000, 0)

    glTexCoord(0, 1)
    glVertex(-600, 10000, 0)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glDeleteTextures(1, texture)
    glPopAttrib()
    glPopMatrix()


def drawGround():
    texture = glGenTextures(1)
    back_ground = pygame.image.load("floor.jpg")

    background_raw = pygame.image.tostring(back_ground, "RGBA", 1)

    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, back_ground.get_width(), back_ground.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE,
                 background_raw)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_TEXTURE_2D)

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-600, -300, 0)

    glTexCoord(1, 0)
    glVertex(1000000, -300, 0)

    glTexCoord(1, 1)
    glVertex(1000000, -2000, 0)

    glTexCoord(0, 1)
    glVertex(-600, -2000, 0)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glDeleteTextures(1, texture)
    glPopAttrib()
    glPopMatrix()


