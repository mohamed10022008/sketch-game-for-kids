from turtle import *

s = Screen()
t = Turtle("arrow")
t.color("green3")
s.listen()
s.bgcolor("black")
t.pencolor("white")


def pnup():
    t.penup()


def pndwn():
    t.pendown()

def fd():
    t.forward(5)


def bd():
    t.backward(5)


def rt():
    t.right(10)


def lt():
    t.left(10)


def c():
    t.penup()
    t.clear()
    t.goto(0, 0)
    t.pendown()
    t.setheading(0)

def finish():
    s.bye()

s.onkey(fd, "Up")
s.onkey(bd, "Down")
s.onkey(rt, "Right")
s.onkey(lt, "Left")
s.onkey(c, "c")
s.onkey(pnup, "u")
s.onkey(pndwn, "d")
s.onkey(finish, "b")

s.exitonclick()
