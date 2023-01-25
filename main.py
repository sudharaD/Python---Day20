# create a snake body
# move the snake
# control the snake
# detect collision with food
# create a scoreboard
# detect collision with wall
# detect collision with tail
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

turtle1 = Turtle()
turtle1.penup()
turtle1.shape("square")
turtle1.color("white")
turtle2 = Turtle()
turtle2.penup()
turtle2.shape("square")
turtle2.color("white")
turtle2.goto(-20, 0)
turtle3 = Turtle()
turtle3.penup()
turtle3.shape("square")
turtle3.color("white")
turtle3.goto(-40, 0)
print(turtle2.pos())

# screen.register_shape("snake", ((10, -50), (10, 10), (-10, 10), (-10, -50)))
# turtle.shape("snake")


screen.exitonclick()


