a=input("Enter a number: ")
print(f"Multiplication of table {a} is: ")

try:
    for i in range(1,11):
     print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid syntax")

print("Ronit is good")
