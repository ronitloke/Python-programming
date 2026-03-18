words="hello hi welcome to python programming"

d={}

for i in words.split():
    d[i]=len(i)
print(d)

d1={i:len(i) for i in words.split()}
print(d1)
