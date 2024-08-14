import random
import os
from words import word_list


def clear():
    os.system('cls')

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

              

stages = [
    '''
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
'''
]

print(logo)
print("\n\n")

chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

blank_list = list(chosen_word)

for i in range(len(blank_list)):
    blank_list[i] = '_'

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

life = int(len(stages) - 1)
found = bool(0)

while '_' in blank_list:
    guess = input("\nGuess a letter: ").lower()
    clear()
    if guess in blank_list:
        print("\nYou have already guessed {guess}!\n")
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            blank_list[i] = guess
            found = 1
        else:
            pass

    if not found:
        life -= 1
        if life == -1:
            print("\n\nYOU LOST!")
            break
        print("\nWrong answer! You loose a life!")
    print(stages[life])
    print(blank_list)
    for i in blank_list:
        print(i, end = "")
        print(" ", end = "")
    print("\n \t <---------> \n")
    found = 0

if '_' not in blank_list:
    print("\n------> Congrats! You Won! <------")


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
