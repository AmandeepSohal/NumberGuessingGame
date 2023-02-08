# make a program where the user has to guess the number that the computer picks

# Need to use a random int to make the computer pick a number
# Need to get the user input
# Need to validate the user's input
# Need to have the computer tell the user if the guess was too high or too low
# If user's input is not in the range, make user input a new number
# When input is correct, output Win statement

import random 

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        while (guess < 1 or guess > 10):
            guess = int(input(f"\nThat is not between 1 and {x}, please try again.\nInput a number between 1 and {x}: "))
        if guess < random_number:
            print("\nToo low ")
        elif guess > random_number:
            print("\nToo high")

    print(f"\nYou Win. The answer was {random_number}")

guess(10)