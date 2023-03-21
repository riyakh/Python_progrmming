import turtle
from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
turtle.colormode(255)
tim.shape('turtle')
tim.color('red')
tim.pencolor('blue')

# drawing a square

# for i in range(0, 4):
#     tim.forward(100)
#     tim.right(90)

# dashed line
"""
for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
"""

# different shapes
"""
def draw_shapes(number_of_sides):
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)


for shapes in range(3, 11):
    draw_shapes(shapes)
"""

"""
def random_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    color =(r,g,b)
    return color


direction = [0, 90, 180, 270]
tim.speed('fastest')
tim.pensize(10)

for move in range(200):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(choice(direction))
"""


def random_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    color = (r, g, b)
    return color


tim.speed('fastest')


def draw_spirograph(size_of_graph):
    for i in range(int(360 / size_of_graph)):
        tim.circle(100)
        tim.pencolor(random_color())
        tim.setheading(tim.heading() + size_of_graph)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
