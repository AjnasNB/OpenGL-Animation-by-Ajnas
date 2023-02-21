from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
mode=0
scale=3
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1500.0, 1500.0, -1500.0, 1500.0)
def star():
    #1st triangle cordiantes
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(scale*200,scale*100)
    glVertex2f(scale*(-200),scale*100)
    glVertex2f(0,scale*(-250))
    glEnd()
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(scale*200,scale*(-100))
    glVertex2f((-200)*scale,(-100)*scale)
    glVertex2f(0,250*scale)
    glEnd()
    glutSwapBuffers()
def animate(temp):
    global scale,mode
    if scale==0:
        mode=0
    elif scale==3:
        mode=1
    if mode==1:
        scale-=1
    elif mode==0:
        scale+=1
    glutTimerFunc(500, animate, 0)
        
    glutPostRedisplay()
        
        
    
    
def main():
    glutInit(sys.argv)
    glutInitWindowSize(1500, 1500)
    glutInitWindowPosition(100, 100)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Star scaling")
    init()
    glutDisplayFunc(star)
    glutTimerFunc(0, animate, 0)
    glutMainLoop()
main()
        
        