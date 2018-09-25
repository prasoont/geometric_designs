# import the turtle module
from turtle import *

# turtle setting or function
speed(0)
bgcolor('black')
color('white')
hideturtle()

# star
def star(la,ra,d):
    for  i in range(5):
        lt(la)
        fd(d)
        rt(ra)
        fd(d)
        
# design using satr function
for i in range(89):
    star(58,130,110)
    rt(89)

# to exit
exitonclick()
