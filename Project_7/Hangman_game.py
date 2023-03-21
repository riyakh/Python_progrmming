import random
import hangman_art
import hangman_words

print(hangman_art.logo)
stages = hangman_art.stages

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in range(0, len(chosen_word)):
  display.append("_")
while (display.count("_") > 0):
  guess = input("Guess a letter: ").lower()
  
  #Check guessed letter
  flag = 0
  if(guess in display):
      print(f"You have already guessed{guess}")
  for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter
          flag = 1
   
  print(f"{' '.join(display)}")
  if flag == 1:
      print(stages[lives])
  if flag == 0:
      print(f"You guessed {guess}, that's not in the word. You Loose a life ")
      lives -= 1  
      print(stages[lives])
  if(lives == 0):
      print("You Loose")
      break
  if display.count("_") == 0:
    print("You win")
    break


