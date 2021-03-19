from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
bids = {}

def add_bid(name,bid):
    bids[name] = bid

def auction():
    name_given = input("What is your name?: ")
    bid_offered = int(input("What is your bid?: "))
    add_bid(name_given,bid_offered)

print('Welcome the secret auction program')

answer = 'yes'

while answer == 'yes':
    auction()
    answer = input('Are there any other bidders?: ').lower()
    clear()

highest_bidder = 0
winner = ''


for bidder in bids:
    if bids[bidder] > highest_bidder:
        highest_bidder = bids[bidder]
        winner = bidder
    else:
        pass

print(f'the winner is {winner} with a bid of ${highest_bidder}')
    

    

