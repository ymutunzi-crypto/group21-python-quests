choice1 = input("Do you go 'left' or 'right'? ").lower()

if choice1 == "left":
    choice2 = input("You hit a river. Do you 'swim' or 'wait'? ").lower()
    if choice2 == "swim":
        print("You braved the currents and found a treasure!")
    else:
        print("You waited too long and a goblin stole your boots.")
else:
    print("You walked into a wall. Ouch.")
