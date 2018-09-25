# import module
from turtle import *

# turtle features
#hideturtle()
speed(0)
bgcolor('black')
color('white')

# triangle
def triangle():
    lt(60)
    fd(200)
    rt(125)
    fd(190)
    rt(115)
    fd(180)


for i in range(120):
    triangle()
    lt(69)


# for exit
exitonclick()
