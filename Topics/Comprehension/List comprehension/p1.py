#without list comp

str="hello hi"
word=str.split()
li=[]
for i in word:
    if(len(i)%2==0):
        li.append(i)
print(li)

#with list comp
str="hello hi"
word=str.split()
li=[i for i in word if(len(i)%2==0)]
print(li)

