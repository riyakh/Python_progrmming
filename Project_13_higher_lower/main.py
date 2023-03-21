from random import sample
from art import logo
from art import vs
from data import data


def game_start_person():
  rand_number = sample(data, k =2)
  return rand_number

def high_followers_count(person_list,user_input):

  followe_a = int(f"{person_list[0]['follower_count']} ")
  followe_b = int( f"{person_list[1]['follower_count']} ")
  if followe_a > followe_b:
      high_followers = "a"
  elif followe_a < followe_b:
      high_followers = "b"
  if high_followers == user_input:
     return True
  else:
     return False

def higher_lower():
  wins = 0
  should_continue = True
  person_list = game_start_person()
  while(should_continue):
    print(f"Compare A: {person_list[0]['name']}, a {person_list[0]['description']}, from {person_list[0]['country']}. ")
    
    print(vs)
    
    print(f"Compare B: {person_list[1]['name']}, a {person_list[1]['description']}, from {person_list[1]['country']}. ")
    high_follower_user_input = (input("Who has more followers? Type 'A' or 'B': ")).lower()
    guess = high_followers_count(person_list,high_follower_user_input)
    if guess:
      wins +=1
      print(f"You're right! Current Score : {wins}")
      person_list[0] = person_list[1]
      new_person = sample(data, k =1)
      person_list[1] = new_person[0]
      
    else:
     
      print(f"Incorrect answer. Your Final Score: {wins}")
      should_continue = False
    
  
  

  
print(logo)
higher_lower()



