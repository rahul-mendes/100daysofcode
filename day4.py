
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

play = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

disp = [rock, paper, scissors]
print(disp[play])

resp = random.randint(0, 2)
print(disp[resp])

if play >= 3 or play < 0:
    print("Invalid choice")
elif play == 0 and resp == 2:
    print("You win!")
elif play == 2 and resp == 0:
    print("You lose!")
elif play > resp:
    print("You win!")
elif resp > play:
    print("You lose!")
elif resp == play:
    print("It's a draw!")
