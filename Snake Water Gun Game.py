# Snake Water Gun
import random

n = 0

while True:

    user = input("User's object : ")
    choice = ["Snake", "Water", "Gun"]
    computer = random.choice(choice)
    print("Computer's object : ", computer)
    n += 1

    if user == "Snake" and computer == "Snake":
        print("Draw")
        if n == 3:
            break

    elif user == "Water" and computer == "Water":
        print("Draw")
        if n == 3:
            break

    elif user == "Gun" and computer == "Gun":
        print("Draw")
        if n == 3:
            break

    elif user == "Snake" and computer == "Water":
        print("Snake drinks the water hence wins")
        if n == 3:
            break

    elif user == "Water" and computer == "Snake":
        print("Snake drinks the water hence wins")
        if n == 3:
            break

    elif user == "Water" and computer == "Gun":
        print("The Gun will drown in the water")
        if n == 3:
            break

    elif user == "Gun" and computer == "Water":
        print("The Gun will drown in the water")
        if n == 3:
            break

    elif user == "Snake" and computer == "Gun":
        print("Gun will kill the Snake and win")
        if n == 3:
            break

    elif user == "Gun" and computer == "Snake":
        print("Gun will kill the Snake and win")
        if n == 3:
            break

    else:
        print("No other inputs")
        break
