li=["app","goo","meta","netflix"]
d={}

for i in li:
    try:
        d[i]+=1
    except KeyError:
        d[i]=0
print("Exception keyerror is handled")
print(d)