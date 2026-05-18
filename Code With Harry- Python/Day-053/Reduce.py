from functools import reduce

l=[1,2,3,4,5,6]

def red_func(x,y):
    return x+y
new=reduce(red_func,l)
print(new)