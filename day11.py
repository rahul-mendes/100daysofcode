import random


def deal():
    """Return a card from main deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calc_score(cards):
    """Calculate the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, comp_score):
    if user_score > 21 and comp_score > 21:
        return "You went over. Lose"

    if user_score == comp_score:
        return "Draw"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose "
    elif comp_score > 21:
        return "Opponent went over. You win"
    elif user_score > comp_score:
        return "You win "
    else:
        return "You lose "


def game():

    user_cards = []
    comp_cards = []
    is_over = False
    for _ in range(2):
        user_cards.append(deal())
        comp_cards.append(deal())

    while not is_over:
        user_score = calc_score(user_cards)
        comp_score = calc_score(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card:  {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_over = True
        else:
            user_schould_deal = input("Type 'y' to get another card: ")
            if user_schould_deal == "y":
                user_cards.append(deal())
            else:
                is_over = True

        while comp_score != 0 and comp_score < 17:
            comp_cards.append(deal())
            comp_score = calc_score(comp_cards)
            print(
                f"Your final hand : {user_cards}, final score:  {user_score}")
            print(
                f"Computer's final hand : {comp_cards}, final score:  {comp_score}")
            print(compare(user_score, comp_score))


while input("Type 'y' to play: ") == "y":
    game()
