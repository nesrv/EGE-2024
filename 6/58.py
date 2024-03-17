from turtle import *
from collections import deque
import time
t = Turtle()

t.screen.setup(1000, 900)
t.speed(30)


t.setpos(0, 0)
t.penup()

for y in range(-100, 300, 20):
    t.setpos(-300, y)
    t.pendown()
    t.forward(400)
    t.penup()

t.left(90)
for x in range(-300, 100, 20):
    t.setpos(x, -100)
    t.pendown()
    t.forward(400)
    t.penup()

t.speed(5)




t.setpos(0, 0)
t.left(90)
t.pensize(3)

t.pendown()

for x in range(4):  
    t.pencolor((1,0,0))
    for y in range(4):        
        t.forward(120)
        t.right(90)
    t.pencolor((0, 0, 1))
    t.forward(120)
    t.pencolor((1, 0, 0))
    t.forward(80)
    t.right(90)   
    t.forward(60)




mainloop()
