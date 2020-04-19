
# Jean Joubert 18 April 2020
# Simple program to rotate cube in 3D space
# Breakout using simple 3d block rotation

import turtle
from math import sin,cos
import time


win = turtle.Screen()
win.setup(600,600)
win.tracer(0)
counter = 0
win.listen()

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c

ball = turtle.Turtle()
ball.color('red')
ball.shape('circle')
ball.up()
ball.dx = 3
ball.dy = 4

paddle = turtle.Turtle()
paddle.shape('square')
paddle.color('blue')
paddle.shapesize(1,5)
paddle.up()
paddle.goto(0,-250)

def paddle_right():
    if paddle.xcor()<250:
        paddle.goto(paddle.xcor()+40, paddle.ycor())

def paddle_left():
    if paddle.xcor()>-250:
        paddle.goto(paddle.xcor()-40, paddle.ycor())

 
class Cube:
    EDGES = (0,1), (1,2), (2,3), (3,0),(4,5), (5,6), (6,7), (7,4),(0,4), (1,5), (2,6), (3,7)
    VERTICES = [(-1,-1,-1),(1,-1,-1), (1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),( 1,1,1),(-1,1,1)]

    def __init__(self, xpos, ypos,axes, color, ball):
        self.xpos = xpos
        self.ypos = ypos
        self.counter = counter
        self.axes = axes
        self.c = color
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color(self.c)
        self.ball = ball
        self.fall = False


    def draw(self):

        for edge in self.EDGES:
            points = []
            
            for vertex in edge:
                x,y,z = self.VERTICES[vertex]

                if self.axes == '3' and self.fall==True:
                    x,z = rotate(x,z,self.counter) # Only this one to rotate around y
                    y,z = rotate(y,z,self.counter) # Only this for x
                    x,y = rotate(x,y,self.counter) # This for z
                    
                elif self.axes == 'x':
                    y,z = rotate(y,z,self.counter) # Only this for x
                elif self.axes == 'y':
                    x,z = rotate(x,z,self.counter)
                elif self.axes == 'z':
                    x,y = rotate(x,y,self.counter)
            
                z += 5
                if z != 0:
                    f = 100/(z)
               
                sx, sy = x*f,y*f
                points.append((sx,sy))

            self.t.up()
            self.t.goto(points[0][0]+self.xpos, points[0][1]+self.ypos)
            self.t.down()
            self.t.goto(points[1][0]+self.xpos, points[1][1]+self.ypos)
            self.t.goto(points[0][0]+self.xpos, points[0][1]+self.ypos)
            self.t.up()


# Cube( where on x, where on y, choose axis x,y,z or all 3)
x_pos = [-250,-200,-150,-100,-50,0,50,100,150,200,250]
y_pos = [250, 200, 150]

cube_list = []

for i in x_pos:
    for j in y_pos:
        cube = Cube(i,j,'3','black', ball)
        cube_list.append(cube)
        cube.draw()


win.onkey(paddle_right,'Right')
win.onkey(paddle_left, 'Left')

while True:
    win.update()
    time.sleep(0.01)
    
    for i in cube_list:
        # Only render the cube if falling
        if i.fall == True:
            i.t.clear()
            i.draw()
        if i.xpos-25<=ball.xcor()<= i.xpos+25:
            if i.ypos-20<= ball.ycor()<=i.ypos+25 and i.fall==False:
                i.counter = 0.01
                i.fall = True
                ball.dy*= -1

        if i.fall == True:
            i.ypos-= 3
            i.counter += 0.05
            if i.ypos<-350:
                cube_list.remove(i)
 
    

    ball.goto(ball.xcor()+ball.dx,ball.ycor()+ball.dy)
    
    if (ball.xcor()<=-280 and ball.dx<0) or (ball.xcor()>=280 and ball.dx>0):
        ball.dx *= -1
    if ball.ycor()>280 and ball.dy>0:
        ball.dy *= -1

    if ball.xcor()-10<=paddle.xcor()+50 and ball.xcor()+10>=paddle.xcor()-50:
        if ball.ycor()<=paddle.ycor()+10 and ball.dy<0:
            ball.dy *= -1

    if ball.ycor()<-320:
        ball.goto(0,100)
    
    
