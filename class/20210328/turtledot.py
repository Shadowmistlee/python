import turtle
t=turtle.Turtle()
t.shape("arrow")
t.speed(0)
for n in range(99999999999):
    t.penup
    t.forward(n)
    t.stamp
    t.right(90)