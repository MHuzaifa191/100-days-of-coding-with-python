import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
global restart
global prompt

restart = 'y'

print(logo)
print("\n\t\t\t\t\t\tWelcome To BlackJack!\n\n\n")

while restart == 'y':

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def deal_card():
        return cards[random.randint(0, len(cards) - 1)]

    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    global user_cards
    global computer_cards
    user_cards = []
    computer_cards = []

    user_cards.append(deal_card())
    user_cards.append(deal_card())

    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    #Hint 6: Create a function called calculate_score() that takes a List of cards as input
    #and returns the score.
    #Look up the sum() function to help you do this.


    def calculate_score(list_of_cards):
        score = 0
        ace = False
        ten = False
        for item in list_of_cards:
            score += item
            if item == 11:
                ace = True
            if item == 10:
                ten = True
        if ace and ten and score == 21:
            return 0
        if list_of_cards[-1] == 11 and score > 21:
            list_of_cards.remove(11)
            list_of_cards.append(10)
        return score

    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

    def let_computer_play():
        comp_score = calculate_score(computer_cards)
        while comp_score < 16:
            computer_cards.append(deal_card())
            comp_score = calculate_score(computer_cards)

    def decide_winner():
        comp_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        if comp_score == 0:
            print(f"Your Cards : {user_cards}, Final Score : {user_score}")
            print(
                f"Computer Cards : {computer_cards}, Computer Final Score :{comp_score}"
            )
            print("Computer Hit BlackJack! Computer Wins!")
        elif comp_score <= 21 and comp_score > user_score:
            print(f"Your Cards : {user_cards}, Final Score : {user_score}")
            print(
                f"Computer Cards : {computer_cards}, Computer Final Score :{comp_score}"
            )
            print("Computer Wins!")
        elif user_score > 21:
            print("You went over! You lost!\n\n")
            print(f"Your Cards : {user_cards}, Final Score : {user_score}")
            print(
                f"Computer Cards : {computer_cards}, Computer Final Score :{comp_score}"
            )
        elif comp_score == user_score:
            print(f"Your Cards : {user_cards}, Final Score : {user_score}")
            print(
                f"Computer Cards : {computer_cards}, Computer Final Score :{comp_score}"
            )
            print("It's a draw!")
        else:
            print(f"Your Cards : {user_cards}, Final Score : {user_score}")
            print(
                f"Computer Cards : {computer_cards}, Computer Final Score :{comp_score}"
            )
            print("You Win!")
        global restart
        restart = input("\n\nRestart Game? (Y or N) : ").lower()
        os.system("cls")

    user_score = calculate_score(user_cards)

    print(f"Your Cards : {user_cards}, Current Score : {user_score}")
    print(f"Computer's First Card : {computer_cards[0]}")

    if user_score == 0:
        let_computer_play()
        decide_winner()
        break
    else:
        prompt = input("Deal another card? (Y or N) : ").lower()
        print("\n\n")

        while prompt == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            comp_score = calculate_score(computer_cards)
            if user_score > 21:
                decide_winner()
                break
            elif user_score == 21:
                let_computer_play()
                print(f"Your Cards : {user_cards}, Final Score : {user_score}")
                print(
                    f"Computer Cards : {computer_cards}, Computer Final Score :{comp_score}"
                )
                decide_winner()
                break
            print(f"Your Cards : {user_cards}, Current Score : {user_score}")
            print(f"Computer's First Card : {computer_cards[0]}")
            prompt = input("Deal another card? (Y or N) : ").lower()
            print("\n\n")

    if prompt != 'y':
        let_computer_play()
        decide_winner()

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
