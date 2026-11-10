words= "hello hi welcome to python programming"

#without dict comp
b=words.split()
d={}

for i in b:
    d[i]=len(i)
print(d)


#with dict comp
dic={i:len(i) for i in b}
print(dic)
