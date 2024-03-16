from turtle import *


t = Turtle()
t.speed(30)
t.screen.setup(800, 800)
t.left(90)

for i in range(2):
    t.forward(400)
    t.right(120)

# penup()
t.setheading(0)
for y in range (0, 400, 40):   
    t.setpos(0,y)
    t.pendown()
    t.forward(400)
    t.penup()

t.left(90)
for x in range(0, 400, 40):
    t.setpos(x, 0)
    t.pendown()
    t.forward(400)
    t.penup()




mainloop()


