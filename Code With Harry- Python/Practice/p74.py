d={"a":1,"b":2,"c":3,"d":4}

d1={}
for i in d.items():
    key,value=i
    d1[value]=key
print(d1)