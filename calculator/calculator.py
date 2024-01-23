from art import logo
import os

print(logo)

#To clear the screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')

#Adding the numbers
def add_numbers(n1, n2):
    return n1 + n2

#Subtracting the numbers
def sub_numbers(n1, n2):
    return n1 - n2

#Multiplying the numbers
def mult_numbers(n1, n2):
    return n1 * n2

#Dividing the numbers
def div_numbers(n1, n2):
    return n1 / n2

operations = {
    '+': add_numbers,
    '-': sub_numbers,
    '*': mult_numbers,
    '/': div_numbers
}

def calculator():
    number1 = int(input("What's the first number? "))
        
    for op in operations:
        print(op)

    should_continue = True
    while should_continue:
        symbol = input("\nSelect operator: ")
        calc = operations[symbol]
        number2 = int(input("\nWhat's the next number? "))
        print("\nPick up an operation from the list below:")
        result = calc(number1, number2)
        print(f"\n{number1} {symbol} {number2} = {result}\n")

        to_continue = input("Do you want to perform more opeartions? Type 'Y' for yes or 'N' for No: ")
        if to_continue == 'Y':
            number1 = result
        else:
            should_continue = False
            clear_screen()
            calculator()

calculator()
