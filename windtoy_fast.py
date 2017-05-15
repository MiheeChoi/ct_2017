import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

oldpos=t1.pos()
size=100

def giyuk(size):
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)
    t1.penup()
    t1.setpos(oldpos)
    oldhead=t1.heading()
    t1.setheading(oldhead+45)
    t1.pendown()


    

giyuk(size)
giyuk(size)
giyuk(size)
giyuk(size)
giyuk(size)
giyuk(size)
giyuk(size)
giyuk(size)

wn.exitonclick()
