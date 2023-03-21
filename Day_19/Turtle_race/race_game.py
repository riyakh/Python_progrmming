from turtle import Turtle,Screen, color
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height =400)
user_bet = screen.textinput("Make a bet", "Which turtle witll win the race? Enter a color:")
colors =['red','orange','yellow','green','blue','purple']
all_turtle = []
y = -100
final_x_coordinate = 230.00


for i in range(0,6):
    y = y+40
    
    turtle_call = Turtle(shape='turtle')
    turtle_call.color(colors[i])
    turtle_call.penup()
    turtle_call.goto(-230,y)
    all_turtle.append(turtle_call)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if round(turtle.xcor(),2) >= final_x_coordinate:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won !! The {winning_color} is the winner")
            else:
                print(f"You've lost. The {winning_color} is the winner")
   


screen.exitonclick()

