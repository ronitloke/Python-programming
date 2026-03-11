a=int(input("Enter an integer between 5 and 9: "))

if(a<5 or a>9):
    raise ValueError("Invalid input")
