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

for out_num in range(1, total_char):
    ran_no_outer_list = random.randint(0, len(characters)-1)
    
    print(f"Loop: {out_num}")

    if ran_no_outer_list == 0:
        if letter_count > nr_letters:
            continue
        else:
            ran_no_inner_list = random.randint(0, len(letters)-1)
            random_char += characters[ran_no_outer_list][ran_no_inner_list]
            letter_count += 1
            print("letter: ", random_char)

    elif ran_no_outer_list == 1:
        if num_count > nr_numbers:
            continue
        else:
            ran_no_inner_list = random.randint(0, len(numbers)-1)
            random_char += characters[ran_no_outer_list][ran_no_inner_list]
            num_count += 1
            print("number: ", random_char)
        
    elif ran_no_outer_list == 2:
        if sym_count > nr_symbols:
            continue
        else:
            ran_no_inner_list = random.randint(0, len(symbols)-1)
            random_char += characters[ran_no_outer_list][ran_no_inner_list]
            sym_count += 1
            print("symbol: ", random_char)


print(f"Here is the  password: {random_char}")
    