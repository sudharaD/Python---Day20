class Snake:
    from turtle import Turtle, Screen

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My snake game")

    POSITION_LIST = [(0, 0), (-20, 0), (-40, 0)]

    for position in POSITION_LIST:
        turtle = Turtle()
        turtle.penup()
        turtle.goto(position)
        turtle.shape("square")
        turtle.color("white")

    def __init__(self):
        pass

    screen.exitonclick()
