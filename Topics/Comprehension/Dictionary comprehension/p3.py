word="This is programming language and programming is fun"
#without dict comp
d={}
for i in word.split():
    d[i]=word.count(i)
print(d)


#with dict comp
d={i:word.count(i) for i in word.split()}
print(d)