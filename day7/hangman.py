import random
from hangman_logo import stages, logo
from hangman_list import word_list

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
display = []
for ch in chosen_word:
    display += "_"

endcondition = False
while not endcondition:
    guess = input("Please enter a letter: ").lower()

    if guess in display:
        print(f"You have already entered {guess}")

    for p in range(len(chosen_word)):
        ch = chosen_word[p]
        if guess == ch:
            display[p] = ch
    print(f"{''.join(display)}")

    if "_" not in display:
        endcondition = True
        print("Winner!")

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            endcondition = True
            print("Game over! ")
