secret_number = "7"
guess = ""

while guess != secret_number:
    guess = input("Guess the secret number: ")
    if guess != secret_number:
        print("Wrong! Try again.")

print("Correct! The door opens.")
