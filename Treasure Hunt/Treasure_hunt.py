from turtle import right


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_stage = input("You are at the cross road. Where do you want to go? Type \"left\" or \"right\"\n ")
first_stage_lower = first_stage.lower()
if(first_stage_lower == "right"):
    print("Fall into a hole❗❗ Game Over ❌❌")
elif(first_stage_lower == 'left'):
    second_stage = input("You came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n ")
    second_stage_lower = second_stage.lower()
    if(second_stage_lower == 'swim'):
        print("Attacked by trout👺. Game Over ❌❌")
    elif(second_stage_lower == "wait"):
        stage_three = input("You arrived at the island unharmed. There is a 🏠 with three doors. One Red, one yellow and one blue. which color do you choose? \n")
        stage_three_lower = stage_three.lower()
        if(stage_three_lower == "red"):
            print("Burned by 🔥. Game Over ❗❗")
        elif(stage_three_lower == "blue"):
            print("You enter a room . Eaten by 👻. Game Over❗❗")
        elif(stage_three_lower == 'yellow'):
            print("You found the treasure. You are a winner.🤗")
        else:
            print("Game Over❗❗")
    else:
        print("oho incorrect option!! Game Over ")
else:
    print("Game Over")