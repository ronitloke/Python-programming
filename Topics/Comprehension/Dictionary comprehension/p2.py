d={"a":1,"b":2,"c":3,"d":4}

#without dict comp
dic={}
for key,value in d.items():
    dic[value]=key
print(dic)

#with dict comp
d={"a":1,"b":2,"c":3,"d":4}

dic={value:key for key,value in d.items()}
print(dic)