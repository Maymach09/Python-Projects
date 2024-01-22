from art import logo
import os

print("Welcome to the secret auction program.")
bid_item = {}

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def bid_winner(bid_data):
    max_bid = 0
    bidder = ""
    for person in bid_data.keys():
        if int(bid_data[person]) > int(max_bid):
            bidder = person
            max_bid = bid_data[person]
    print(f"Winner is {person} with a bid of {max_bid}.")

should_continue = True
while should_continue:
    person_name = input("What is your name?: ")
    person_bid = input("What's your bid: $")
    bid_item[person_name] = person_bid
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.")
    if continue_bidding == 'yes':
        should_continue = True
        clear_screen()
    else:
        should_continue = False
        clear_screen()

bid_winner(bid_item)
# print("Winning bid is: ", result)



    
