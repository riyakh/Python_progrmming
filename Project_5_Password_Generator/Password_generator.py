from itertools import count
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
complete_list = [*letters,*numbers,*symbols]
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_length = nr_letters+nr_numbers+nr_symbols
count_letters = 0
count_numbers = 0
count_symbols = 0
password = []
for passw in range(0, len(letters)):
    generated_number = random.choice(complete_list)
    if(generated_number in letters and count_letters < nr_letters):
        count_letters += 1
        password.append(generated_number)
    elif(generated_number in numbers and count_numbers < nr_numbers):
        count_numbers += 1
        password.append(generated_number)
    elif(generated_number in symbols and count_symbols < nr_symbols):
        count_symbols += 1
        password.append(generated_number)
    if( len(password) == password_length):
        break
print(''.join(str(i) for i in password))
