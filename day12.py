from random import randint

EASY = 10
HARD = 5


def check(guess, ans, turn):
    if guess > ans:
        print("TOO HIGH")
        return turn-1
    elif guess < ans:
        print("TOO LOW")
        return turn-1
    else:
        print(f"YOU GOT IT! THE ANSWER IS {ans}")


def diff():
    level = input("HARD OR EASY?")
    if level == "HARD":
        return HARD
    else:
        return EASY


def game():
    print("Welcome to the game!")
    print("Picking a random number between 1 and 100.")
    ans = randint(1, 100)
    print(f"Random number is {ans}")
    turn = diff()
    guess = 0
    while guess != ans:
        print(f"You have {turn} turns to find the answer")
        guess = int(input("Make a guess: "))
        turn = check(guess, ans, turn)
        if turn == 0:
            print("You lose")
        elif guess != ans:
            print("Try again")


game()
