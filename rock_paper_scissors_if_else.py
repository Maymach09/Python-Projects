rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random #random number generator module

#Fetching user's input
user_input = int(input("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

#Fetching computer's input
computer_input = random.randint(0,2)

#display user's selection
if user_input == 0:
    print("You chose:\n\n", rock)
elif user_input == 1:
    print("You chose:\n\n", paper)
else:
    print("You chose:\n\n", scissors)

#display computer's selection
if computer_input == 0:
    print("Computer chose:\n\n", rock)
elif computer_input == 1:
    print("Computer chose:\n\n", paper)
else:
    print("Computer chose:\n\n", scissors)

#winning logic
if user_input == 0:
    if computer_input == 0:
        print("It's a draw")
    elif computer_input == 1:
        print("You lose")
    else:
        print("You win")

elif user_input == 1:
    if computer_input == 1:
        print("It's a draw")
    elif computer_input == 2:
        print("You lose")
    else:
        print("You win")

elif user_input == 2:
    if computer_input == 2:
        print("It's a draw")
    elif computer_input == 0:
        print("You lose")
    else:
        print("You win")  

else:
    print("Invalid Input")      
    