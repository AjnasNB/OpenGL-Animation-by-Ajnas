from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math,sys
angle=0.0
x=0
y=0
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

def car():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(x+100,y+50)
    glVertex2f(x-100,y+50)
    glVertex2f(x-100,y-50)
    glVertex2f(x+100,y-50)
    glEnd()
    
    
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x-70,y-52)
    for i in range(0,361,1):
        glVertex2f(20*math.cos(math.pi*i/180.0)-70+x,20*math.sin(math.pi*i/180.0)-52+y)
        
    glEnd()
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x+70,y-52)
    for i in range(0,361,1):
        glVertex2f(20*math.cos(math.pi*i/180.0)+70+x,20*math.sin(math.pi*i/180.0)-52+y)    
    glEnd()
    
    glColor3f(.1,.1,.1)
    glBegin(GL_LINES)
    glVertex2f(x-70,y-52)
    glVertex2f(20*math.cos(math.pi*angle/180.0)-70+x,20*math.sin(math.pi*angle/180.0)-52+y)
    glEnd()
    
    glColor3f(.1,.1,.1)
    glBegin(GL_LINES)
    glVertex2f(x+70,y-52)
    glVertex2f(20*math.cos(math.pi*angle/180.0)+70+x,20*math.sin(math.pi*angle/180.0)-52+y)
    glEnd()
    
    
    glutSwapBuffers()
def animate(temp):
    global angle,x,y
    if((x+100)>=500):
        x=-400
    else:
        x+=1
    glutPostRedisplay()
    glutTimerFunc(10,animate,0)
    # if(angle)
    if(angle<=0):
        angle=360
    angle-=10
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Car")
    glutDisplayFunc(car)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(car)
    init()
    glutMainLoop()
main()