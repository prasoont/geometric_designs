# importing module TURTLE
import turtle
turtle = turtle.Turtle()
turtle.speed(0)

# function for square
def square(lenght,angle):
    for i in range(4):
        turtle.forward(lenght)
        turtle.right(angle)


# calling function
for i in range(95):
    square(200,90)
    turtle.right(11)




# to hold the screen
input("Press ENTER key to exit!")
