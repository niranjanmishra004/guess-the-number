import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        try:
            guess = int(input("Hey buddy please Enter your number between (1-100): "))
            attempts += 1

            if guess < number_to_guess:
                print("Naah! The number is lower than the guessed number.")
            elif guess > number_to_guess:
                print("Naah! The number is higher than the guessed number.")
            else:
                print(f"🎉 Booyah....!Correct! The number was {number_to_guess}.")
                print(f"Hey buddy you guessed it in {attempts} attempts!")
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()
