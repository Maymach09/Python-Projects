from art import logo
import os

print(logo)

print("Welcome to the secret auction program.\n")
bid_items = {}

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

def bid_winner(bid_data):
    max_bid = 0
    bidder = ""
    for person, bid in bid_data.items():
        if bid > max_bid:
            bidder = person
            max_bid = bid
    print(f"The winner is {bidder} with a bid of {max_bid}")

should_continue = True
while should_continue:
    person_name = input("What is your name?: ")
    person_bid = int(input("What's your bid: $"))
    bid_items[person_name] = person_bid

    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if continue_bidding.lower() == 'yes':
        should_continue = True
        clear_screen()
    else:
        should_continue = False
        clear_screen()

print(bid_items)
bid_winner(bid_items)



    
