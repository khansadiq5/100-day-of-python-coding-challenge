import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z' 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '?']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to password generator!")
ks_letters = int(input("How many letters would you like in your password? \n"))
ks_symbols = int(input("How many symbols would you like in your password? \n"))
ks_numbers = int(input("how many number would you like in your password? \n"))

password_list = []

for char in range(1, ks_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, ks_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, ks_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password_list = "".join(password_list)

print(f"Your password is: {password_list}")
# \SAIJFKWNFWORFNWORVNRWKO
# dgornwognroivnrojgnrwvjonrwv



            
     
