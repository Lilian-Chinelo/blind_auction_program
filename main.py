from replit import clear
from art import logo
print(logo)

print("Welcome to the blind auction!")

bids = {}
bidding_finished = False

def auction(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    amounts = bidding_record[bidder]
    if amounts > highest_bid:
      highest_bid = amounts
      winner = bidder
  print(f" The winner is {winner} with a bid of ${highest_bid} ")
    
while not bidding_finished:
  name = input("Please enter your name: ")
  bid_amount = int(input("Please enter your bid amount: "))
  bids[name] = bid_amount
    
  bid_again = input("Is there another bidder? type yes or no: ").lower()
  if bid_again == "no":
    bidding_finished = True
    auction(bids)
  elif bid_again == "yes":
    clear()



  

  