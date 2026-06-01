print("Lets begin the game")
print("Comp's turn: ")

comp=str(input()).strip().lower()
print("player's turn: ")
player=str(input()).strip().lower()

c="comp wins"
p="player wins"
d="Match is draw"

def game():
    if comp=="snake" and player=="water":
        return c
    elif comp=="snake" and player=="gun":
        return p
    elif comp=="water" and player=="snake":
        return p
    elif comp == "water" and player == "gun":
        return c
    elif comp=="gun" and player=="snake":
        return c
    elif comp == "gun" and player == "water":
        return p
    elif comp=="snake" and player=="snake":
        return d
    elif comp == "water" and player == "water":
        return d
    elif comp=="gun" and player=="gun":
        return d
    else:
        return("String entered is invalid")
print(game())






