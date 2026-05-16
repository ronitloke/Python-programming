l=[1,2,3,4,5,6,7,8,9]

def fil_func(x):
    return x>2
new=list(filter(fil_func,l))
new1=list(map(fil_func,l))

print(new)
print(new1)
