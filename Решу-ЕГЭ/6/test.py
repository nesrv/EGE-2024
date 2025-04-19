from turtle import Screen, Turtle
from random import random

WIDTH, HEIGHT = 800, 800
DIAMETER = 200


def chameleon(x, y):
    turtle.ondrag(None)
    overlapping = canvas.find_overlapping(
        x, -y, x, -y)  # adjust to tkinter coordinates

    if overlapping:
        color = canvas.itemcget(overlapping[0], "fill")

        if color:
            turtle.fillcolor(color)

    turtle.goto(x, y)
    turtle.ondrag(chameleon)


screen = Screen()
screen.setup(WIDTH, HEIGHT)
canvas = screen.getcanvas()

turtle = Turtle()
turtle.hideturtle()
turtle.speed('fastest')
turtle.penup()

for x in range(-WIDTH//2, WIDTH//2, DIAMETER):
    for y in range(-HEIGHT//2, HEIGHT//2, DIAMETER):
        turtle.goto(x + DIAMETER/2, y + DIAMETER/2)
        color = random(), random(), random()
        turtle.dot(DIAMETER - 1, color)

turtle.home()
turtle.shape('turtle')
turtle.shapesize(2)
turtle.showturtle()
turtle.ondrag(chameleon)

screen.mainloop()
