def factorial(n):
    if isinstance(n,str):
        raise TypeError("Any string value is not allowed")
    if n<0:
        raise ValueError("The num should not be less than zero")
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))