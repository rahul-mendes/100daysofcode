complete = False
bids = {}


def find_highest(bids):
    winning_bid = 0
    winner = ""
    for name in bids:
        amount = bids[name]
        if amount > winning_bid:
            winning_bid = amount
            winner = name
    print(f"The winner is {winner} with a bid of ${winning_bid}")


while not complete:
    name = input("Enter name: ")
    bid = int(input("Enter bid: $"))
    bids[name] = bid
    next = input("Any other bids? Enter yes or no: ")
    if next == "no":
        complete = True
        find_highest(bids)
