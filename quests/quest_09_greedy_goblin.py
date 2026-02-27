gold_pieces = 27
friends = 4

# // is floor division (whole numbers), % is the remainder
per_friend = gold_pieces // friends
goblin_remainder = gold_pieces % friends

print(f"Each friend gets {per_friend} pieces. The goblin keeps the remaining {goblin_remainder} pieces.")
