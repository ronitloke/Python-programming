x=10
print(x)

def func():
    global x
    x=4
    print(f"inside func{x}")
print(f"lets try{x}")
print(func())

print(x) #value of global variable was overriden as we declare "Global" variable in func