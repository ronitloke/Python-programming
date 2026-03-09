try:
    5/5
except ZeroDivisionError as z:
    print(z)
else:
    print("No error")
finally:
    print("i dont care abt errors")