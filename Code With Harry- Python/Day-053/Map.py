def xyz(x):
    return x*x*x
print(xyz(3))

l=[1,2,3,4,5,6,7,8]

new=list(map(xyz,l))
new1=tuple(map(xyz,l))
new2=set(map(xyz,l))
print(new)
print(new1)
print(new2)