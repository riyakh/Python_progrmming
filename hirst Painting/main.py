# import colorgram
#
# colors = colorgram.extract('image.jpg', 40)
# rgb_colors =[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
from turtle import Turtle, Screen

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40), (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112), (16, 54, 243), (240, 16, 16)]
tim = Turtle()
Screen().colormode(255)
rand_num = random.randrange(0,36)
color_tup = color_list[rand_num]


for xaxis in range(0,10):
    tim.dot(20, color_tup)
    tim.penup()
    tim.forward(50)
tim.left(50)


screen = Screen()
screen.exitonclick()