def personalized_greeting(name, quest):
    print(f"Hero {name}, your quest to {quest} is noble!")

user_name = input("Enter your name: ")
user_quest = input("Enter your quest: ")

# Passing arguments to the function
personalized_greeting(user_name, user_quest)
