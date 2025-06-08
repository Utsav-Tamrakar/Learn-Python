import random
#Defining a function 
def number_guess_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 6.")

    # Generate a random number between 1 and 6
    secret_number = random.randint(1, 6)

    # Ask the user to guess
    guess = int(input("Enter your guess (1-6): "))

    # Check the guess
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
    else:
        print(f"Sorry, the correct number was {secret_number}.")

# Run the game
number_guess_game()
