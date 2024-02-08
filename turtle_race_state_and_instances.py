from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: "
                                                          "red, gold, magenta, green, indigo, blue: ")


def make_turtle(colour, start_x, start_y):
    turtle_name = Turtle()
    turtle_name.color(colour)
    turtle_name.shape("turtle")
    turtle_name.penup()
    turtle_name.goto(start_x, start_y)
    return turtle_name

is_race_on = False
andy = make_turtle("red", -200, 125)
benny = make_turtle("gold", -200, 75)
carly = make_turtle("magenta", -200, 25)
denny = make_turtle("green", -200, -25)
early = make_turtle("indigo", -200, -75)
franny = make_turtle("cyan", -200, -125)

all_turtles = andy, benny, carly, denny, early, franny

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            winner = turtles.pencolor()
            if winner == user_bet:
                print(f"You won! The winner was {winner}")
            else:
                print(f"You lost. The winner was {winner}")
            is_race_on = False
        else:
            how_far = random.randint(0,10)
            turtles.forward(how_far)

screen.exitonclick()
