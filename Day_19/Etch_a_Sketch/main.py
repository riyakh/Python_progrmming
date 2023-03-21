# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = turtle.heading() + 10
    tim.setheading(new_heading)

def trun_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()

screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_left, 'a')
screen.onkey(trun_right, 'd')
screen.onkey(clear_screen, 'c')
screen.exitonclick()
