import turtle
import figures
import random
# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")
pen = turtle.Turtle()
pen.speed(5)
minimal = 1
maximal =600
for x in range(2):
    figures.draw_rectangle(100,100,pen)
    pen.goto(random.randint(minimal,maximal),random.randint(minimal,maximal))
    figures.draw_square(100,pen)
    pen.goto(random.randint(minimal,maximal),random.randint(minimal,maximal))

    figures.draw_trangle(60,pen)
    pen.goto(random.randint(minimal,maximal),random.randint(minimal,maximal))
