from data import data
import random
from art import logo, vs


def randomchoice():
    return random.choice(data)


def format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, {country}"


def check(guess, a_foll, b_foll):
    if a_foll > b_foll:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    playon = True
    account_a = randomchoice()
    account_b = randomchoice()
    while playon:
        account_a = account_b
        account_b = randomchoice()
        while account_a == account_b:
            account_b = randomchoice()

        print(f"Compare A: {format(account_a)}.")
        print(vs)
        print(f"Against B: {format(account_b)}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check(guess, a_follower_count, b_follower_count)

        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            playon = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
