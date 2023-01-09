print('''
********************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
********************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You come to a fork in the path. One leads left and the other diverts to the right.\n")
choice1 = input("Choose whether to go to the RIGHT or LEFT.\n")
choice1 = choice1.lower()
if choice1 == "right":
    print("You fall into a hole in the path. You have failed at the first hurdle. You die with regrets. Make better choices.\n")
elif choice1 == "left":
    print("You come to a small stream of water. It is dark and muddy. A small boat is coming slowly to collect you from the other side. You may either wait for it, or you may swim across.\n")
    choice2 = input("Choose whether to WAIT for the boat or SWIM across.\n")
    choice2 = choice2.lower()
    if choice2 == "swim":
        print("The stream is populated by poisonous trout. Go lie with the fishes. You die with regrets. Make better choices.\n")
    elif choice2 == "wait":
        print("You get into the boat. The stream is populated by poisonous trout. You cross safely.\n")
        print("You come to a dark hall with many doors. There are three doors closest to you. You can choose from a red door, green door, blue door, or you can go look for another door.\n")
        choice3 = input(
            "Choose between the doors: RED, BLUE, YELLOW or ANOTHER.\n")
        choice3 = choice3.lower()
        if choice3 == "yellow":
            print("You enter a room of great and grand treasures. You are amazed at your good luck and skill. Congratulations on a successful adventure.\n")
        elif choice3 == "blue":
            print("The door leads you down a steep staircase, and you slip and fall. There is a giant venomous beast which will have you for dinner and dessert. You die with regrets. Make better choices.\n")
        elif choice3 == "red":
            print("The door opens and a huge fire breaks out from behind. This seems to be a trap. You start burning to death. You die with regrets. Make better choices.\n")
        else:
            print("Are sure this is what you wanted? You had better choices, you know. Start finding your way forward. There is no way back.  Make better choices.\n")
