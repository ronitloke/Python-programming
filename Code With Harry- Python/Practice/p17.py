word="This is programming language and programming is fun"

d={}

for i in word:
    d[i]=word.count(i)
print(d)

# d={i:word.count(i) for i in word}
# print(d)