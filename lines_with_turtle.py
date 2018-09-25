from turtle import *
speed(0)
bgcolor('black')
color('yellow')

# horizontal line
def line(a):
    fd(200)
    lt(180)
    fd(400)
    rt(180)
    fd(200)
    lt(a+1)
'''
#horizontal line
fd(200)
lt(180)
fd(400)
rt(180)
fd(200)
lt(a+43)
#vertical line
lt(90)
fd(200)
lt(180)
fd(400)
rt(180)
fd(200)
#
lt(45)
fd(200)
lt(180)
fd(400)
rt(180)
fd(200)
#
rt(90)
fd(200)
lt(180)
fd(400)
rt(180)
fd(200)

'''
for i in range(200):
    line(0.05)

# exit
exitonclick()
