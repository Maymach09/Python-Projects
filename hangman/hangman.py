import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
display = []
lives = 6
end_of_game = False

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

for letter in chosen_word:
    display.append('_')
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You have already entered this letter, please chose a different letter")
    
    #Check guessed letter
    for rcount,letter in enumerate(chosen_word):
        if letter == guess:
            display[rcount] = letter
    
    #Check if user is wrong.
    if guess not in chosen_word:
        print("Sorry! you have guessed the wrong letter, please chose another letter.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou Lose")
    
    #Join all the elements in a list and turn it into a string
    print(f"{' '.join(display)}")
    
    #check if user has got all letters
    if '_' not in display:
        end_of_game = True
        print("You Won.")

    #Print hangman after every guess
    print(hangman_art.stages[lives])


    


