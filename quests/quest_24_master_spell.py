def ask_for_age():
    age = int(input("What is your age? "))
    return age

def can_they_vote(age):
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are not old enough to vote yet.")

# Nesting the logic
current_age = ask_for_age()
can_they_vote(current_age)
