import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
width=wn.window_width()
w1 = (width - 60) / 3
x1 = 0.0 - w1
x2 = 0.0
x3 = 0.0 + w1  

def drawSquareAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for i in range(0,4):
        t1.write(t1.pos())
        t1.fd(size)
        t1.right(90)
def drawTrangleAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for u in range(0,3):
        t1.write(t1.pos())
        t1.fd(size)
        t1.right(120)
def drawStarAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for y in range(0,5):
        t1.write(t1.pos())
        t1.fd(size)
        t1.right(144)

drawSquareAt(x1,0,100)
drawTrangleAt(x2,0,100)
drawStarAt(x3,0,100)

wn.exitonclick()
