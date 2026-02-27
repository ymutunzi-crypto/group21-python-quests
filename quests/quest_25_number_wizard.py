secret = 42
guess = 0

while guess != secret:
    guess = int(input("Guess the secret number: "))
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")

print("Correct! You are a Number Wizard.")
