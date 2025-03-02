# Import dependencies
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")

# Generate random number between 0-100
random_number = random.randint(0, 100)
print(f"Random number is {random_number}")

def guess_the_number():
    print("I'm thinking of a number between 1 and 100.")
    # Ask user to choose between 'easy' or 'hard' difficulty, answer dictates number of lives (10 = easy, 5 = hard)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    # Condition to check if easy or hard difficulty selected
    if difficulty == "easy":
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif difficulty == "hard":
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number.")

    # While loop to check status of number of remaining attempts
    while attempts != 0:
        # Ask user to enter a number to guess
        guess = int(input("Make a guess: "))

        # Check if guess is too high
        if guess > random_number:
            attempts -= 1
            print("Too high.")
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
        # Check if guess is too low
        if guess < random_number:
            attempts -= 1
            print("Too low.")
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
        # Check if guess equals the random number, if so exit the loop
        if guess == random_number:
            print(f"You got it! The answer was {random_number}")
            break
    # Check if attempts remaining equals zero
    if attempts == 0:
        print("You've run out of guesses. Refresh the program to run again.")

guess_the_number()
