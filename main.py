#Import os in order to use the screen clear functionality (line 41)
import os

#Show logo from art.py
from art import logo
print(logo)

#Define function to check the dictionary of bids to find the highest bidder and their bid.
def check_winner(user_bids):
    highest_bid = 0
    winner = ""
    for name in user_bids:
        bid_amount = user_bids[name]
        if bid_amount >= highest_bid:
            highest_bid = bid_amount
            winner = name
    print(f"The winner is {winner} with a bid of ${highest_bid}!")



while True:

    #Ask for name input
    bidder_name = input(f"What is your name? ")

    #Ask for bid amount
    bid = int(input(f"How much do you want to bid?  $"))


    #Add inputs to dictionary
    bidders = {}
    bidders[bidder_name] = bid

    #Ask if there are any more bidders.
    more_bids = input(f"Are there any more bids? ").lower()
    if more_bids != "yes": #If no, break out of loop. If yes, clear screen then repeat loop.
        check_winner(bidders)
        break
    else:
        #Clear screen
        os.system('cls||clear')
        continue





