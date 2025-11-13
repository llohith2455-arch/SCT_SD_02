import random

def guess_the_number():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    print("🎯 I'm thinking of a number between 1 and 100. Can you guess it?")

    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        if guess < secret_number:
            print("🔼 Too low! Try again.")
        elif guess > secret_number:
            print("🔽 Too high! Try again.")
        else:
            print(f"✅ Correct! You guessed it in {attempts} attempts.")
            break

# Run the game
guess_the_number()