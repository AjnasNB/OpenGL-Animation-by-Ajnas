from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math,sys
x=0
y=0
angle=45
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1000.0, 1000.0, -1000.0, 1000.0)
    
def circle():
    global x,y,angle
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    #circle
    for i in range(0,361,1):
        glVertex2f(200*math.cos(math.pi*i/180.0)+x,200*math.sin(math.pi*i/180.0)+y)
    glEnd() 
    
    
    
    #spock
    glColor3f(0,1,0)
    glBegin(GL_LINES)
    glVertex2f(x,y)
    glVertex2f(200*math.cos(math.pi*angle/180.0)+x,200*math.sin(math.pi*angle/180.0)+y)
    
    glEnd()
    
    glutSwapBuffers()
def animate(temp):
    global x,angle
    if x+200>=1000:
        x=-800
    x+=1 
    
    if angle<=0:
        angle=360
    angle-=1
    glutTimerFunc(10,animate,0)
    glutPostRedisplay()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0,0)
    glutCreateWindow("circle")
    glutDisplayFunc(circle)
    glutTimerFunc(0,animate,0)

    #
    
    init()
    glutMainLoop()
main()