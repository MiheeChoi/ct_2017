import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def giyuk(size):
    t1.fd(size)
    t1.right(90)
    t1.fd(size)

def nien(size):
    t1.fd(size)
    t1.left(90)
    t1.fd(size)

def giyukAT(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    giyuk(size)
giyukAT(-100,100,100)

def nienAT(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    nien(size)
nienAT(-100,0,100)

def miemAT(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    giyuk(size)
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    nien(size)
miemAT(-100,-150,100)

wn.exitonclick()
