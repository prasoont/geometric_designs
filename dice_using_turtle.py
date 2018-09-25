# Dice roll simulation
# prasoon tripathi 15/6/18

import turtle, random
t = turtle.Turtle()

# draw 1 on screen
def one():
    t.pd()
    t.lt(180)
    t.lt(45)
    t.fd(10)
    t.bk(10)
    t.lt(45)
    t.fd(60)
    t.rt(90)
    t.fd(10)
    t.bk(20)
    t.ht()
    t.pu()
    t.home()

# draw 2 on screen
def two():
    t.pd()
    t.circle(-26.5,180)
    t.circle(-7,240)
    t.fd(40)
    t.ht()
    t.up()
    t.home()

# draw 3 on screen
def three():
    t.pd()
    t.fd(50)
    t.rt(135)
    t.fd(50)
    t.lt(135)
    t.circle(-25,250)
    t.ht()
    t.pu()
    t.home()
    
# draw 4 on screen
def four():
    t.pd()
    t.rt(90)
    t.fd(30)
    t.lt(90)
    t.fd(30)
    t.lt(90)
    t.fd(30)
    t.bk(60)
    t.ht()
    t.pu()
    t.home()

# draw 5 on screen
def five():
    t.pd()
    t.fd(30)
    t.bk(30)
    t.rt(90)
    t.fd(30)
    t.lt(120)
    t.circle(-25,250)
    t.ht()
    t.pu()
    t.home()

# draw 6 on screen
def six():
    t.pd()
    t.lt(180)
    t.circle(40,150)
    t.circle(20)
    t.ht()
    t.up()
    t.home()
    
# main logic
option = "y"
while option == "y" :
    num = random.randrange(2,7)
    print(num)
    if num == 1:
        one()
    elif num == 2:
        two()
    elif num == 3:
        three()
    elif num == 4:
        four()
    elif num == 5:
        five()
    elif num == 6:
        six()
    option = input("Roll Again?(y/n)")
    t.clear()
