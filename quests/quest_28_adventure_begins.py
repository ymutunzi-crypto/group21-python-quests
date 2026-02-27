def forest():
    print("You are in a dark forest. You see a light.")

def cave():
    print("You are in a damp cave. You hear a growl.")

choice = input("Go to 'forest' or 'cave'? ")
if choice == "forest":
    forest()
else:
    cave()
