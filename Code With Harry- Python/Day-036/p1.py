try:
    num = int(input("Enter an integer: "))

except NameError :
    print("Number entered is a name.")
except:
    print("Number entered is not an integer.")
