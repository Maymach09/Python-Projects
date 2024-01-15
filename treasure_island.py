print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("A treasure awaits you, tell me the direction you want to take. left or right?\n")

if direction == 'left':
    print("You are a step closer but near a hole!")
    hole = input("Now, tell me if you want to explore the 'hole' or want to 'jump' the hole?\n")
    if hole == 'jump':
        print("Well done! Now, you are near the lake!")
        lake = input("Do you want to 'wait' for the boat or 'swim' across the lake?\n")
        if lake == 'wait':
            print("You have come a long way, with 3 doors in front of you!")
            door = input("Which door you want to open? red or yellow or green?\n")
            if door == 'red':
                print('You dared to open the red door! Room is full of mouse.\nGame Over!')
            elif door == 'yellow':
                print('You were close but not there! Room is empty.\nGame Over!')
            elif door == 'green':
                print('You have hit the jackpot! There is a box full of gold Jewellery.\nCongratulations!, YOU WON')
            else:
                print("Invalid Input")
        elif hole == 'hole':
            print("That was not you were supposed to do, lake is full of Alligators.\nGame Over!")
        else:
            print("Invalid Input! Start Over")
    else:
        print("That was quite adventurous, the hole is full of Snakes.\nGame Over!")
elif direction == 'right':
    print("You are a step closer but near a road.")
    road = input("Do you want to take the 'road' or cross the road to stay in the 'woods'?\n")
    if road == 'woods':
        print("Well done! You are near the lake")
        lake = input("Do you want to 'wait' for the boat or 'swim' across the lake?\n")
        if lake == 'wait':
            print("You have come a long way, with 3 doors in front of you!")
            door = input("Which door you want to open? red or yellow or green?\n")
            if door == 'red':
                print("You dared to open the red door!Room is full of mouse.\nGame Over!")
            elif door == 'yellow':
                print('You were close but not there! Room is empty.\nGame Over!')
            elif door == 'green':
                print("You have hit the jackpot! There is a box full of gold Jewellery.\nCongratulations!, YOU WON")
            else:
                print("Invalid Input! Start Over")
        else:
            print("That was not you were supposed to do, lake is full of Alligators.\nGame Over!")
    elif road == 'road':
        print("Oh! No. You ran over by a speeding car!\nGame Over!")
    else:
        print("Invalid Input! Start Over")
else:
    print("Invalid Input! Start Over!")