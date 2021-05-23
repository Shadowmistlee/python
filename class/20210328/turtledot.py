import turtle
t=turtle.Turtle()
t.shape("arrow")
t.speed(0)
n = 1
while True:
    t.penup
    t.forward(n)
    t.stamp()
    t.right(90)
    n += 1