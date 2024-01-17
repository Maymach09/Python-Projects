import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

characters = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_char = nr_letters + nr_numbers + nr_symbols

#Create a list of random letters
random_char = ""
random_list = []


for list in characters:
    # if len(random_char) == total_char:
    #     break
    # else:
    ran_no_list = random.randint(0,len(characters)-1)
    ran_no_letters = random.randint(0, len(letters)-1)
    ran_no_numbers = random.randint(0, len(numbers)-1)
    ran_no_symbols = random.randint(0, len(symbols)-1)
    random_list += characters[ran_no_list][ran_no]

print(random_list)
