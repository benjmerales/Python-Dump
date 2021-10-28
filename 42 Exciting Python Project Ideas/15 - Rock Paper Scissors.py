import random

choices = ("Rock", "Paper", "Scissors")

while True:
    computer = random.choice(choices)

    you = input("Rock, Paper or Scissors?    : ")

    print("Computer picked: " + computer)
    if you == "Rock":
        if computer == "Rock":
            print("Draw!")
        elif computer == "Paper":
            print("You Lose!")
        elif computer == "Scissors":
            print("You Win!")
    elif you == "Paper":
        if computer == "Rock":
            print("You Win!")
        elif computer == "Paper":
            print("Draw!")
        elif computer == "Scissors":
            print("You Lose!")
    elif you == "Scissors":
        if computer == "Rock":
            print("You Lose!")
        elif computer == "Paper":
            print("You Win!")
        elif computer == "Scissors":
            print("Draw!")
    elif you == "End":
        break
    else:
        print("Please enter a valid string!")
    