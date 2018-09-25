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

# inner square
for i in range(4):
    square(100,90)                                     # calling a function

# outer square
for i in range(4):
    square(200,90)



# just to hold the screen
input("Press Enter Key to exit!")

