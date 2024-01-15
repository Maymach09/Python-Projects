import random #random number generator module

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

choices = [rock,paper,scissors]

#Fetching and displaying user's input
user_input = int(input("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print("User chose:\n", choices[user_input])

#Fetching and dispaying computer's input
computer_input = random.randint(0,2)
print("Computer chose:\n", choices[computer_input])

#winning logic
if user_input == computer_input:
        print("It's a draw")
elif (user_input == 0 and computer_input == 1) or (user_input == 1 and computer_input == 2) or (user_input == 2 and computer_input == 0):
        print("\nComputer Wins!")
elif (user_input == 2 and computer_input == 1) or (user_input == 1 and computer_input == 0) or (user_input == 0 and computer_input == 2):
        print("\nYou Win!")
else:
    print("\nInvalid input, you lose")