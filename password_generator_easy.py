import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Create a list of random letters
random_letters = ""
for letter in letters:
    if len(random_letters) == nr_letters:
        break
    else:
        ran_no = random.randint(0,len(letters)-1)
        random_letters += letters[ran_no]

#Create a list of random numbers
random_numbers = ""
for number in numbers:
    if len(random_numbers) == nr_numbers:
        break
    else:
        ran_no = random.randint(0,len(numbers)-1)
        random_numbers += numbers[ran_no]

#Create a list of random symbols
random_symbols = ""
for symbol in symbols:
    if len(random_symbols) == nr_symbols:
        break
    else:
        ran_no = random.randint(0,len(symbols)-1)
        random_symbols += symbols[ran_no]

password = random_letters + random_numbers + random_symbols

print(f"Here is your password: {password}")