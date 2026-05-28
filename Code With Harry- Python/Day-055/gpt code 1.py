print("Lets begin the game")

VALID = {"snake", "water", "gun"}

def read_choice(prompt):
    choice = input(prompt).strip().lower()   # allow CAPS/small + extra spaces
    if choice not in VALID:
        return None
    return choice

comp = read_choice("Comp's turn: ")
player = read_choice("Player's turn: ")

def game(comp, player):
    if comp is None or player is None:
        return "Invalid input! Only: snake, water, gun"

    if comp == player:
        return "Draw"

    # winning pairs for player (player beats comp)
    wins = {("snake", "water"), ("water", "gun"), ("gun", "snake")}
    if (player, comp) in wins:
        return "Player wins"
    else:
        return "Comp wins"

print(game(comp, player))