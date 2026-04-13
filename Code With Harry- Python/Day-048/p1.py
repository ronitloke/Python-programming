x=4
print(x)

def msg():
    x=5
    print(f"local variable is {x}")
    print(x)
print(f"global variable is {x}")
print(msg())

print(x)