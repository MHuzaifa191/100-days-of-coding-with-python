import os
from art import logo

print(logo)
bidders = 'yes'
print("Welcome to the secret auction program!")
bidders_dictionary = {}

while bidders == 'yes' or bidders == 'y':
    name = input("What is your name? : ")
    bid = input("What's your bid? : $")
    bidders_dictionary[name] = bid
    bidders = input("Are there other secret bidders? (Y or N) : ").lower()
    os.system('cls')

max_bid = int(0)
for bidder in bidders_dictionary:
    if int(bidders_dictionary[bidder]) > max_bid:
        max_bid = int(bidders_dictionary[bidder])

for bidder in bidders_dictionary:
    if max_bid == int(bidders_dictionary[bidder]):
        print(f"The winner is {bidder} with a bid of ${bidders_dictionary[bidder]}")
        break