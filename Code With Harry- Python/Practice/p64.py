str="welcome home"
li=[]
a=str.split()
for i in a:
    if(len(i)%2==0):
        li.append(i)
print(li)

li=[i for i in a if(len(i)%2==0)]
print(li)