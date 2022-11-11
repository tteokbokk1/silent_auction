import os
from art import logo

print(logo)
print("Welcome to the silent audtion")

bidder = ""
amount = 0
addition_bidders = ""

bids = []

def add_bid(name, bid):
    entry = {}
    entry["Person"] = name
    entry["Amount"] = bid
    bids.append(entry)

while True:
    bidder = input("What is your name? ")
    amount = int(input("What is your bid? "))
    additional_bidders = input("Is there another bidder? y/n ").lower()
    add_bid(bidder, amount)
    if additional_bidders == "n":
        break
    os.system("clear")

sorted_bids = sorted(bids, key=lambda bids: bids["Amount"], reverse=True)

winner_name = sorted_bids[0]["Person"]
winning_amount = sorted_bids[0]["Amount"]

print(f"The winner of the auction is {winner_name} with a bid of ${winning_amount}")