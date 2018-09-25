
import turtle
my_turtle = turtle.Turtle()
turtle.speed(0)                         # for speed of turtle
turtle.bgcolor('red')                   # for background color behind turtle
turtle.color('yellow')                  # for color of line drawn by turtle



# square
def square():
    # a single straight line
    turtle.right(85)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(100)
    
    turtle.right(90)
    turtle.forward(100)

# circle of square by calling function - square
for i in range(72):
    square()



turtle.exitonclick()                   # When you click, turtle exits.
