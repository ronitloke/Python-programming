try:
    num = int(input("Enter a integer"))
    5/0        #only one condition is used in try block
except ValueError:
    print("value is not integer")
except ZeroDivisionError as z:
    print(z)