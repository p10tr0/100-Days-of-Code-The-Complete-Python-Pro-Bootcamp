from art import logo
print(logo)

still_bids = True
current_bids = {}

while still_bids:
    # Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: £"))

    # Save data into dictionary {name: price}
    current_bids[name] = bid

    # Check if new bids need to be added
    bidding_question = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if bidding_question == 'yes':
        print("\n" * 100)
        continue
    else:
        still_bids = False

# Compare bids in dictionary
max_bid = 0
for name,value in current_bids.items():
    if value > max_bid:
        max_bid = value
print(f"The winner is {name} with a bid of £{max_bid}")