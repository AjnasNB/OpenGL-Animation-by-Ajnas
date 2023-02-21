from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

WINDOW_SIZE =500
gx =0.0
gy =0.0
mode =1



def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-500,500,-500,500)
def drawball():
	glClear(GL_COLOR_BUFFER_BIT)
	global gx
	global gy

	glBegin(GL_TRIANGLE_FAN)
	glColor3f(0.0,0.0,1.0)
	glVertex2f(gx,gy)
	for i in range(0,361,1):
		glVertex2f(100*math.cos(math.pi*i/180.0)+gx,100*math.sin(math.pi*i/180.0)+gy)
	glEnd()
	glutSwapBuffers()

def animate(temp):
	global gx,gy,mode 

	if mode ==1:
		gy=gy-1
		if gy==-50:
			mode=0
	elif mode==0:
		gy=gy+1
		if gy==50:
			mode=1
	glutTimerFunc(int(1000/100),animate,0)
	glutPostRedisplay()
		



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("ball")
    glutDisplayFunc(drawball)
    glutIdleFunc(drawball)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()