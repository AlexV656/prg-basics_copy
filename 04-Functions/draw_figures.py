import turtle
import figures
import random
# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")
pen = turtle.Turtle()
pen.speed(5)
minimal = 10
height =40
for x in range(1,3):
    pen.penup()
    pen.goto(minimal*x,height)

    figures.draw_rectangle(100,50,pen)
    pen.goto(minimal*x*2,height)
    figures.draw_square(100,pen)
    pen.goto(minimal*x*3,height)
    height+=50

    figures.draw_trangle(60,pen)
pen.hideturtle()
window.mainloop()