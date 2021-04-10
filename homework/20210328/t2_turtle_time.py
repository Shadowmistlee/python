"""
Topic:請使用turtle及loop及time.sleep(1)印出秒針動畫

e.g.
import time
time.sleep(1)
"""
import turtle
import time
t=turtle.Turtle()
t.speed(0)
for n in range(99999999999999999999999999999999999999):
    t.forward(150)
    t.right(180)
    t.forward(150)
    t.right(180)
    t.right(6)
    time.sleep(1)
    t.clear()