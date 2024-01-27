import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
import random


def colour_choice():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_colour = (r, g, b)
    return my_colour


def draw_spirals(degrees):
    for _ in range(int(360/degrees)):
        pointer.color(colour_choice())
        pointer.circle(100)
        pointer.right(degrees)


pointer = Turtle()
pointer.speed(0)

draw_spirals(10)

screen = Screen()
screen.exitonclick()
