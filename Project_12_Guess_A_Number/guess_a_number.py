#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from time import process_time
import logo




def number_guess(level):
  should_continue = True
  attempts = 0
  number = random.randint(0,101)
  if level == 'hard':
    attempts = 5
  elif level == 'easy':
    attempts = 10
  while should_continue:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess:"))
    if number == guess:
      print(f"You got it ! Answer is {number}")
      should_continue = False
    elif number < guess:
      print("Too high \nGuess again")
      attempts -= 1
    elif number >guess:
      print("Too Low \nGuess Again")
      attempts -=1
    if attempts == 0:
      print("You have run out of guesses, You Loose")
      should_continue = False
    
    
      
print(logo.logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 to 100")
difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
number_guess(difficulty_level)

