from OpenGL.GL import *
from OpenGL.GLU import  *
from OpenGL.GLUT import *
import math
x=1
y=1
angle=45
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1000,1000,-1000,1000)
def ball():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,361,1):
        glVertex2f(100*math.cos(i)+x,100*math.sin(i)+y)
    glEnd()
    
    #spock
    glBegin(GL_LINES)
    glColor(0,1,0)
    glVertex2f(x,y)
    glVertex2f(100*math.cos(math.pi*angle/180)+x,100*math.sin(math.pi*angle/180)+y)
    glEnd()
    
    
    #ground
    glBegin(GL_LINES)
    glColor(1.0,1.0,0)
    glVertex2f(-850,-1000)
    glVertex2f(1150,1000)
    glEnd()
    glutSwapBuffers()
def animate(temp):
    global angle,x,y
    if(angle>=360):
        angle=0
    else:
        angle+=1
    if(x+100>=1000):
        x=-900
    x+=1
    if(y+100>=1000):
        y=-900
    y+=1
        
    glutPostRedisplay()
    glutTimerFunc(10,animate,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(1000,1000)
    glutInitWindowPosition(0,0)
    glutCreateWindow("ball translation")
    glutDisplayFunc(ball)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()
    
    