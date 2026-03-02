def ascii(value):
    if ord(value)%2==0:
        return "It is even"
    else:
        return "It is odd"
print(ascii("B"))