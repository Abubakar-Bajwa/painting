import turtle as t
import random
from colors import extract_colours


def move(colour):
    for dots in range(1, 101):
        tim.dot(40, random.choice(colour))
        tim.forward(50)
        if dots % 10 == 0:
            tim.setheading(90)
            tim.forward(65)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


colour_list = []

extract_colours(colour_list)
t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(235)
tim.forward(350)
tim.setheading(0)
tim.speed(0)


move(colour_list)


screen = t.Screen()
screen.exitonclick()


