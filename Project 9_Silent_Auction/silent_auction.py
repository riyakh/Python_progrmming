from turtle import clear
import art
print(art.logo)
print("Welcome to secret Auction Program")
user_input = True
members ={}
while(user_input):
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  members[name] = bid
  more_bidders = input("Are there any other bidders? Type 'Yes' or 'No'. ").lower()
  if more_bidders == "no":
    clear()
    user_input = False
  else:
    clear()
max_bid =0
bidder_name =''
for key in members:
  if members[key] > max_bid:
    max_bid = members[key]
    bidder_name = key
print(f"The winner is {key} with a bid of ${max_bid}.")