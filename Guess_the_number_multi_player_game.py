import random

# a = 5
# b = 10

class guessing_game:
    def __init__(self, n):
        self.n = 0
    @staticmethod
    def player():
        a = int(input("Enter the minimum number : "))
        b = int(input("Enter the maximum number : "))
        fixed_number = random.randint(a, b)

        i = 0
        while True:
            c = int(input(f"Enter a number between {a} and {b} : "))
            i += 1
            if c > fixed_number:
                print("Enter a Lesser number ")

            elif c < fixed_number:
                print("Enter a Greater number ")

            elif c == fixed_number:
                print(f"Correct guess you took {i} guesses to guess the correct number . ")
                break
            else:
                print("Something went Wrong ! ")
                break
        return i


if __name__ == '__main__':
    player_1 = guessing_game
    player_2 = guessing_game
    print("Player 1 Please begin the game\n ")
    a = player_1.player()   # This will run the code and save the the number of guesses to a
    # player_1.player()
    print("\nPlayer 2 Please begin the game\n")
    b = player_2.player()    # This will run the code and save the the number of guesses to b
    # player_2.player()
    if a > b:
        print("\nPlayer 1 wins !")
    elif a == b:
        print("\nIts a tie !")
    else:
        print("\nPlayer 2 wins !")
