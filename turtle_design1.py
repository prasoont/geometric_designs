# imports the module turtle
from turtle import *                # * for all,make things easier
speed(0)
pencolor('white')
bgcolor('Black')

x=0
up()                            # lifts up the pen, so no lines are drawn

rt(45)                          
fd(90) 
rt(135)

down()                          # sets down the pen, so that turtle can draw

while x < 120:                  # while the value of x is lesser than 120,
                                #continuously do this:
    for i in range(6):
        fd(200)     
        rt(61)
    
    rt(11.1111) 
    x = x+1                     # adds 1 to the value of x,
                               # so that it is closer to 120 after every loop

exitonclick()                   # When you click, turtle exits.
