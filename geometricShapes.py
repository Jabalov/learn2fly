from OpenGL.GL import *
import numpy as np
from math import *
def conicSections(a, b, x, y):
    glBegin(GL_POLYGON)

    for th in np.arange(0, 2 * pi, .001):
        r = (a * b) / sqrt(((b ** 2) * (cos(th) ** 2)) + ((a ** 2) * (sin(th) ** 2)))
        x1 = r * sin(th)
        y1 = r * cos(th)
        glVertex2d(x + x1, y + y1)

    glEnd()


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
    glBegin(GL_POLYGON)
    for th in np.arange(0, 2 * pi, .001):
        x = r * sin(th)
        y = r * cos(th)
        glVertex2d(x + x1, y + y1)

    glEnd()
