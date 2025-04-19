from turtle import *
lt(90)
# screensize(600,600)
# tracer(0)
speed(20)
down()
for i in range(7):
    fd(300)
    rt(120)
# up()
for x in range(0,300, 30 ):
    for y in range(0,300, 30):
        setpos(x,y)
        dot(4,'red')
        up()
done()