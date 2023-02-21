from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
scale=5
mode=0
x=0
y=0
angle=45
import math
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1000,1000,-1000,1000)
def draw():
    global angle,scale,x,y
    glClear(GL_COLOR_BUFFER_BIT)
    #square
    x1=(scale*50)*(math.cos(math.pi*(angle/180)))
    y1=(scale*50)*(math.sin(math.pi*(angle/180)))
    
    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex2f(x1+x,y1+y)
    glVertex2f(y1+x,-x1+y)
    glVertex2f(-x1+x,-y1+y)
    glVertex2f(-y1+x,x1+y)
    glEnd()
    glutSwapBuffers()
def animate(temp):
    #rotate
    global angle
    
    if(angle>=360):
        angle=0
    angle+=1
    #translate
    global x,y
    
    if(x+300>=1000):
        x=-700
    x+=1
    if(y+300>=1000):
        y=-700
    y+=1
    
    #scale
    global scale,mode
    if scale==5:
        mode=1
    elif scale==0:
        mode=0
    if mode==1:
        scale-=1
    elif mode==0:
        scale+=1
    glutTimerFunc(25,animate,0)
    glutPostRedisplay()
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(1000,1000)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Full transition")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()