import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

characters = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

total_char = nr_letters + nr_numbers + nr_symbols

#Create a string of random letters
random_char = ""
letter_count = 0
num_count = 0
sym_count = 0

for out_num in range(1, total_char+1):
    for in_num in range(1, nr_letters+1):
        ran_no_outer_list = random.randint(0, len(characters)-1)
        ran_no_inner_list = random.randint(0, len(letters)-1)
        print(ran_no_outer_list, ran_no_inner_list)
        letter_count += 1
        random_char += characters[1][34]

print(f"Here is the  password: {random_char}")
    