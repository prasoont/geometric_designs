import turtle
my_turtle = turtle.Turtle()

# square function
def square(lenght,angle):                           # defining a function
    my_turtle.forward(lenght)
    my_turtle.left(angle)
    my_turtle.forward(lenght)
    my_turtle.left(angle)
    my_turtle.forward(lenght)
    my_turtle.left(angle)
    my_turtle.forward(lenght)

square(100,90)                                     # calling a function
square(100,90)
square(100,90)
square(100,90)



# just to hold the screen
input("Press Enter Key to exit!")
