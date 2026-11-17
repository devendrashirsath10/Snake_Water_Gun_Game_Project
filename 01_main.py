
'''

 1 for Snake
-1 for Water 
 0 for Gun


'''
import random

computer = random.choice([-1, 0, 1])

youstr = input("Enter Your Choice Player (s/w/g): ").lower()

youDict = {'s': 1, 'w': -1, 'g': 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

Player = youDict[youstr]

print(f"You Chose = {reverseDict[Player]}")
print(f"Computer Chose = {reverseDict[computer]}")

if computer == Player:
    print("It is a Draw!")

else:
    if computer == -1 and Player == 1:
        print("You Win!")

    elif computer == -1 and Player == 0:
        print("You Lose!")

    elif computer == 1 and Player == -1:
        print("You Lose!")

    elif computer == 1 and Player == 0:
        print("You Win!")

    elif computer == 0 and Player == -1:
        print("You Win!")

    elif computer == 0 and Player == 1:
        print("You Lose!")

    else:
        print("Something Went Wrong!")