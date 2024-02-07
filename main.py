import colorgram
import random
from turtle import Turtle, Screen
import turtle

colours = colorgram.extract("image.jpg",30)

rgb = []

for colour in colours:
    red = colour.rgb.r
    green = colour.rgb.g
    blue = colour.rgb.b
    new_colour = (red, green, blue)
    new_colour = list(new_colour)
    if new_colour[0] and new_colour[1] and new_colour[2] > 170:
        continue
    else:
        rgb.append(new_colour)



turtle.colormode(255)


def starting_position(blob, x, y):
    blob.speed(0)
    blob.hideturtle()
    blob.penup()
    blob.goto(x, y)
    blob.showturtle()
    blob.shape("circle")


def move_pointer(mover):
    mover.speed(0)
    mover.color(random.choice(rgb))
    mover.pendown()
    mover.dot(40)
    mover.penup()
    mover.forward(100)


pointer = Turtle()
start_x = -350
start_y = 300

for lines in range(8):
    starting_position(pointer, start_x, start_y)
    start_y -= 80
    for dots in range(7):
        move_pointer(pointer)
        pointer.dot(40)

screen = Screen()
screen.exitonclick()
