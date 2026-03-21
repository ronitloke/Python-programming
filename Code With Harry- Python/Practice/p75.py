word="This is programming language and programming is fun"

d={}
for i in word.split():
    d[i]=word.count(i)
print(d)