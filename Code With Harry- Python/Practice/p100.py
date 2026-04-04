li=[1,3,5,7,9]
i=int(input("Enter a number: "))

try:
    print(li[i])
except IndexError:
    print("index value not present")
