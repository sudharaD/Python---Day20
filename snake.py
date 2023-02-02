from turtle import Turtle, Screen
// test

class Snake:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My snake game")

    POSITION_LIST = [(0, 0), (-20, 0), (-40, 0)]
    SNAKE_BODY_PARTS = []

    for position in POSITION_LIST:
        turtle = Turtle()
        turtle.penup()
        turtle.goto(position)
        turtle.shape("square")
        turtle.color("white")
        SNAKE_BODY_PARTS.append(turtle)
        turtle.forward(10)

    def move(self, body_parts_list):
        while True:
            for body_part in body_parts_list:

    screen.exitonclick()



