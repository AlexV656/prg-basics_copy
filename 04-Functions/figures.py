import turtle

def draw_trangle(length,pen):

    # Side length
    length = 100
    pen.pendown()
    # Draw a square
    for i in range(3):
        pen.forward(length)
        pen.right(120)

    # Hide the turtle and finish
    pen.penup()

#draw_trangle(1000)
def draw_rectangle(lenght_a, lenght_b,pen):
    # Create the turtle
    pen.pendown()

    for i in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)
    pen.penup()
def draw_square(length,pen):
    # Create the turtle
    pen.pendown()

    # Side length
    length = 100

    # Draw a square
    for i in range(4):
        pen.forward(length)
        pen.right(90)
    pen.penup()

    # Hide the turtle and finish 