print("         Number Guessing Game        ")

number = 50
i = 5
print("Total number of guesses : 5  ")

while True:

    num1 = int(input("Enter your number : "))
    i = i - 1
    print("Number of guesses left : ", i)

    if i == 0:
        print("Game Over  you lose")
        break

    elif num1 > number:
        print("Enter a lesser number ")

    elif num1 < number:
        print("Enter a greater number ")

    else:
        print("Congrats !! You Won ")
        break
