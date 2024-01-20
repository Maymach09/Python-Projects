import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
lives = 6
end_of_game = False

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

for letter in chosen_word:
    display.append('_')
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for rcount,letter in enumerate(chosen_word):
        if letter == guess:
            display[rcount] = letter
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")
    
    #Join all the elements in a list and turn it into a string
    print(f"{' '.join(display)}")
    
    if '_' not in display:
        end_of_game = True
        print("You Won.")

    print(stages[lives])


    


